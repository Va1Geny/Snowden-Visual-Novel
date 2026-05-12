init python:
    import time as _time

    class CoverTracksTimer(object):
        def __init__(self, total=90):
            self.start_time = None
            self.total = total
            self._penalty = 0
        def start(self):
            self.start_time = _time.time()
            self._penalty = 0
        def add_penalty(self, seconds):
            self._penalty += seconds
        def get_remaining(self):
            if self.start_time is None:
                return float(self.total)
            elapsed = (_time.time() - self.start_time) + self._penalty
            return max(0.0, self.total - elapsed)
        def get_progress(self):
            if self.start_time is None:
                return 0.0
            elapsed = (_time.time() - self.start_time) + self._penalty
            return min(1.0, elapsed / self.total)
        def is_expired(self):
            return self.get_remaining() <= 0
        def get_threat_level(self):
            p = self.get_progress()
            if p < 0.25: return "LOW"
            elif p < 0.50: return "MEDIUM"
            elif p < 0.75: return "HIGH"
            else: return "CRITICAL"
        def get_threat_color(self):
            return {"LOW":"#00FF88","MEDIUM":"#FFD700","HIGH":"#FF8C00","CRITICAL":"#FF2D55"}[self.get_threat_level()]
        def get_eta_string(self):
            r = int(self.get_remaining())
            return "{:02d}:{:02d}".format(r // 60, r % 60)

    import math as _math
    import random as _random

    class WaveformGraph(renpy.Displayable):
        def __init__(self, w, h, color_hex, speed=1.5, amp=0.35, **kw):
            super(WaveformGraph, self).__init__(**kw)
            self.w = w
            self.h = h
            self.col = color_hex
            self.speed = speed
            self.amp = amp
            self._n = [_random.uniform(-1, 1) for _ in range(w)]
        def _rgb(self, hx):
            hx = hx.lstrip('#')
            return (int(hx[0:2],16), int(hx[2:4],16), int(hx[4:6],16))
        def render(self, width, height, st, at):
            r = renpy.Render(self.w, self.h)
            c = r.canvas()
            rgb = self._rgb(self.col)
            mid = self.h * 0.5
            a = self.h * self.amp
            for gy in range(0, self.h, max(1, self.h // 4)):
                c.line((26, 36, 46, 180), (0, gy), (self.w, gy))
            pts = []
            for x in range(0, self.w, 2):
                ph = (x / float(self.w)) * _math.pi * 6.0
                wv = _math.sin(ph - st * self.speed)
                ns = self._n[x % len(self._n)] * 0.15
                y = int(max(2, min(self.h - 2, mid + (wv + ns) * a)))
                pts.append((x, y))
            for i in range(len(pts) - 1):
                c.line(rgb + (220,), pts[i], pts[i+1])
            renpy.redraw(self, 0.033)
            return r
        def event(self, ev, x, y, st):
            pass
        def visit(self):
            return []

    class NSAThreatBar(renpy.Displayable):
        def __init__(self, w, h, **kw):
            super(NSAThreatBar, self).__init__(**kw)
            self.w = w
            self.h = h
        def render(self, width, height, st, at):
            r = renpy.Render(self.w, self.h)
            c = r.canvas()
            p = cover_timer.get_progress()
            fh = int(self.h * p)
            sy = self.h - fh
            if p < 0.25:
                col = (0, 255, 136, 220)
            elif p < 0.50:
                col = (255, 215, 0, 220)
            elif p < 0.75:
                col = (255, 140, 0, 220)
            else:
                col = (255, 45, 85, 255) if int(_math.sin(st * 8) > 0) else (180, 20, 50, 200)
            c.rect((13, 17, 23, 255), (0, 0, self.w, self.h))
            if fh > 0:
                c.rect(col, (0, sy, self.w, fh))
            sh = max(1, self.h // 10)
            for i in range(10):
                c.line((8, 12, 18, 255), (0, i * sh), (self.w, i * sh))
            bc = (0, 255, 209, 120)
            c.rect(bc, (0, 0, self.w, 2))
            c.rect(bc, (0, self.h - 2, self.w, 2))
            c.rect(bc, (0, 0, 2, self.h))
            c.rect(bc, (self.w - 2, 0, 2, self.h))
            renpy.redraw(self, 0.05)
            return r
        def event(self, ev, x, y, st):
            pass
        def visit(self):
            return []

    class ScanlineOverlay(renpy.Displayable):
        def __init__(self, width=1920, height=1080, line_spacing=3, line_width=2, **kw):
            super(ScanlineOverlay, self).__init__(**kw)
            self.s_width = int(width)
            self.s_height = int(height)
            self.line_spacing = line_spacing
            self.line_width = line_width
        def render(self, width, height, st, at):
            r = renpy.Render(self.s_width, self.s_height)
            c = r.canvas()
            for y in range(0, self.s_height, self.line_spacing):
                c.line((0, 0, 0, 10), (0, y), (self.s_width, y), self.line_width)
            return r
        def event(self, ev, x, y, st):
            pass
        def visit(self):
            return []

    cover_timer = CoverTracksTimer(total=90)
    ct_wave_cpu = WaveformGraph(280, 40, "#00FFD1", speed=1.5)
    ct_wave_net = WaveformGraph(280, 40, "#00FF88", speed=2.0)
    ct_wave_up = WaveformGraph(280, 35, "#FF2D55", speed=1.8, amp=0.25)
    ct_wave_dn = WaveformGraph(280, 35, "#00FFD1", speed=1.2)
    ct_threat_bar = NSAThreatBar(260, 200)
    ct_scanlines = ScanlineOverlay()

    ct_traces = [
        {
            "id": 1, "name": "Browser History", "icon": "ðŸŒ", "phase": 1,
            "danger_title": "YOUR BROWSING PROVES INTENT",
            "danger_text": "Every URL you visited is stored locally with timestamps. NSA forensics will find your searches for WikiLeaks and journalist contacts.",
            "file_type": "SQLite Database", "file_size": "4.2 MB", "risk_level": "CRITICAL",
            "forensic_note": "Recoverable with Autopsy or DB Browser",
            "correct_command": "rm -rf ~/.config/chromium/Default/History",
            "command_breakdown": [
                ("rm", "remove â€” deletes a file or directory"),
                ("-r", "recursive â€” removes all contents inside"),
                ("-f", "force â€” no confirmation prompts"),
                ("~/.config/chromium/Default/History", "exact path to Chromium browser history database"),
            ],
            "tokens": [], "options": [],
            "wrong_commands": [],
            "success_output": [
                "root@snowden:~$ rm -rf ~/.config/chromium/Default/History",
                "[[  OK  ] Locating history database...",
                "[[  OK  ] File found: History (SQLite, 4.2MB)",
                "[[  OK  ] Removing file...",
                "[[  OK  ] Browser history: PERMANENTLY DELETED",
                "[[  OK  ] Trace 1/8 eliminated.",
            ],
            "success_feedback": "Browser history destroyed. Forensic tools like Autopsy can no longer recover your search history. Normal deletion (Recycle Bin) only hides the file â€” rm -rf removes it from the filesystem entirely.",
            "learn_text": "Browsers store every URL in a local database file called History. Forensics investigators always look here first. Even incognito mode only hides history from other users, not from investigators with physical access.",
        },
        {
            "id": 2, "name": "Session Tokens", "icon": "ðŸ”‘", "phase": 1,
            "danger_title": "SAVED LOGINS REVEAL YOUR IDENTITY",
            "danger_text": "Your browser stored authentication tokens for 3 classified NSA systems. These tokens prove you had active sessions during document exfiltration.",
            "file_type": "JSON / SQLite cookies", "file_size": "892 KB", "risk_level": "CRITICAL",
            "forensic_note": "Session tokens valid for up to 30 days",
            "correct_command": "rm -rf ~/.config/chromium/Default/Cookies && rm -rf ~/.config/chromium/Default/Local\\ Storage/",
            "command_breakdown": [
                ("rm -rf", "remove recursively and forcefully"),
                ("Cookies", "browser cookie database (stores login tokens)"),
                ("&&", "run second command only if first succeeded"),
                ("Local\\\\ Storage/", "folder storing web app session data"),
            ],
            "tokens": [], "options": [],
            "wrong_commands": [],
            "success_output": [
                "root@snowden:~$ rm -rf ~/.config/chromium/Default/Cookies",
                "[[  OK  ] Cookie database located (892KB)...",
                "[[  OK  ] Deleting session tokens...",
                "[[  OK  ] Cookies: WIPED",
                "root@snowden:~$ rm -rf ~/.config/chromium/Default/Local Storage/",
                "[[  OK  ] Local Storage: WIPED",
                "[[  OK  ] All authentication tokens destroyed.",
                "[[  OK  ] Trace 2/8 eliminated.",
            ],
            "success_feedback": "Session tokens eliminated. Without these, investigators cannot prove which accounts you were logged into. The && operator chains commands so the second only runs if the first succeeds.",
            "learn_text": "When you log into a website, the server sends a session token stored in Cookies. This token acts like a temporary ID card. Investigators use tokens to prove you were logged into specific systems at specific times.",
        },
        {
            "id": 3, "name": "GPS Photo Metadata", "icon": "ðŸ“¸", "phase": 2,
            "danger_title": "YOUR PHOTOS CONTAIN HIDDEN LOCATION DATA",
            "danger_text": "3 photos contain EXIF metadata with GPS coordinates placing you at NSA HQ during the exfiltration window.",
            "file_type": "JPEG EXIF Metadata", "file_size": "3 x embedded GPS", "risk_level": "CRITICAL",
            "forensic_note": "EXIF GPS accurate to 3 meters",
            "correct_command": "exiftool -all= ~/pictures/*.jpg",
            "command_breakdown": [
                ("exiftool", "industry-standard metadata reader/editor"),
                ("-all=", "set ALL metadata fields to empty (strip them)"),
                ("~/pictures/*.jpg", "all JPEG files in pictures folder"),
            ],
            "tokens": ["exiftool", "-all=", "~/pictures/*.jpg"],
            "distractor_tokens": ["rm", "-rf", "chmod", "000"],
            "options": [],
            "wrong_commands": [],
            "success_output": [
                "root@snowden:~$ exiftool -all= ~/pictures/*.jpg",
                "[[  OK  ] Scanning JPEG files for EXIF data...",
                "[[  OK  ] DSC_0847.jpg: GPS 38.951N 77.147W > STRIPPED",
                "[[  OK  ] DSC_0923.jpg: GPS 38.951N 77.147W > STRIPPED",
                "[[  OK  ] DSC_1102.jpg: GPS 38.951N 77.147W > STRIPPED",
                "[[  OK  ] Camera model data > STRIPPED",
                "[[  OK  ] Trace 3/8 eliminated.",
            ],
            "success_feedback": "EXIF metadata stripped from all photos. GPS coordinates, camera model, and timestamps are gone. The photos remain intact but carry no identifying data.",
            "learn_text": "Every photo contains hidden EXIF metadata: GPS coordinates (accurate to meters), time/date, camera model and serial number. Journalists and whistleblowers ALWAYS strip EXIF data. Tools: exiftool, MAT2, ExifCleaner.",
        },
        {
            "id": 4, "name": "Downloaded PRISM Files", "icon": "ðŸ“", "phase": 2,
            "danger_title": "56,000 CLASSIFIED DOCUMENTS ON DISK",
            "danger_text": "The NSA files are still on your hard drive. Standard DELETE will not work â€” forensic tools recover deleted files in seconds. You need secure overwrite.",
            "file_type": "Classified PDF / DOCX", "file_size": "2.3 GB", "risk_level": "CRITICAL",
            "forensic_note": "Standard rm recoverable with Recuva/PhotoRec",
            "correct_command": "shred -vzu -n 7 ~/documents/nsa_files/*",
            "command_breakdown": [
                ("shred", "overwrites file with random data before deleting"),
                ("-v", "verbose: shows progress for each file"),
                ("-z", "final overwrite pass with zeros (hides shredding)"),
                ("-u", "unlink: delete file after shredding"),
                ("-n 7", "overwrite 7 times (DoD 5220.22-M standard)"),
                ("~/documents/nsa_files/*", "all files in that directory"),
            ],
            "tokens": ["shred", "-vzu", "-n 7", "~/documents/nsa_files/*"],
            "distractor_tokens": ["rm", "-rf"],
            "options": [],
            "wrong_commands": [],
            "success_output": [
                "root@snowden:~$ shred -vzu -n 7 ~/documents/nsa_files/*",
                "[[  OK  ] shred: PRISM_slides_v3.pdf: pass 1/7 (random)...",
                "[[  OK  ] shred: PRISM_slides_v3.pdf: pass 7/7 (000000)...",
                "[[  OK  ] shred: PRISM_slides_v3.pdf: removed",
                "[[  OK  ] shred: All 2.3GB of NSA files: PERMANENTLY WIPED",
                "[[  OK  ] Data unrecoverable. Trace 4/8 eliminated.",
            ],
            "success_feedback": "Files securely overwritten 7 times then deleted. Unlike rm, shred overwrites the actual disk sectors with random data, making forensic recovery impossible.",
            "learn_text": "Normal deletion only removes the file's address from the index â€” the data stays on disk. shred overwrites actual disk sectors multiple times. The DoD 5220.22-M standard requires 7 passes.",
        },
        {
            "id": 5, "name": "Hotel WiFi Record", "icon": "ðŸ“¡", "phase": 2,
            "danger_title": "YOUR DEVICE IS FINGERPRINTED ON THIS NETWORK",
            "danger_text": "The Mira Hotel router logged your MAC address â€” a unique hardware ID identifying your specific laptop at this location.",
            "file_type": "Network Interface ID", "file_size": "Hardware level", "risk_level": "HIGH",
            "forensic_note": "MAC logged by hotel for 90 days minimum",
            "correct_command": "sudo macchanger -r wlan0",
            "command_breakdown": [
                ("sudo", "superuser do â€” run with admin privileges"),
                ("macchanger", "tool for changing MAC address"),
                ("-r", "random: assign a completely random MAC"),
                ("wlan0", "your wireless network interface name"),
            ],
            "tokens": ["sudo", "macchanger", "-r", "wlan0"],
            "distractor_tokens": ["ip", "link", "set", "down"],
            "options": [],
            "wrong_commands": [],
            "success_output": [
                "root@snowden:~$ sudo macchanger -r wlan0",
                "[[sudo] password for snowden: ********",
                "[[  OK  ] Current MAC:   dc:a6:32:44:f1:09 (Intel Corp)",
                "[[  OK  ] New MAC:       3a:f7:12:b9:2e:55 (Unknown)",
                "[[  OK  ] MAC address randomized successfully.",
                "[[  OK  ] Trace 5/8 eliminated.",
            ],
            "success_feedback": "MAC address randomized. The hotel log now points to a hardware ID that no longer exists on any device. Future connections use a different fingerprint.",
            "learn_text": "Every network device has a MAC address â€” a unique hardware ID. Hotels and public WiFi log MACs to track devices. MAC spoofing broadcasts a fake ID, breaking the link between your device and the log.",
        },
        {
            "id": 6, "name": "USB Device History", "icon": "ðŸ’¾", "phase": 3,
            "danger_title": "LINUX LOGGED EVERY USB DEVICE YOU CONNECTED",
            "danger_text": "The kernel logged the serial number, model, and connection time of the USB drive used to copy PRISM files.",
            "file_type": "Kernel syslog / udev journal", "file_size": "Log entries", "risk_level": "HIGH",
            "forensic_note": "journalctl logs persist across reboots",
            "correct_command": "sudo journalctl --rotate && sudo journalctl --vacuum-time=1s",
            "command_breakdown": [
                ("journalctl --rotate", "force journal to create new log file"),
                ("&&", "then run next command only if first succeeded"),
                ("--vacuum-time=1s", "delete all journal files older than 1 second"),
            ],
            "tokens": [],
            "options": [
                "sudo journalctl --rotate && sudo journalctl --vacuum-time=1s",
                "sudo rm /var/log/syslog",
                "sudo dmesg -c",
            ],
            "wrong_commands": [
                {"cmd": "sudo rm /var/log/syslog", "feedback": "Wrong. This removes only the legacy syslog file, but systemd journals store USB logs separately in /var/log/journal/ as binary files. The USB record stays intact."},
                {"cmd": "sudo dmesg -c", "feedback": "Wrong. dmesg -c clears the kernel ring buffer (temporary memory). Persistent journal logs on disk are completely unaffected. After reboot, the USB record is still there."},
            ],
            "success_output": [
                "root@snowden:~$ sudo journalctl --rotate",
                "[[  OK  ] Journal rotated. Old entries archived.",
                "root@snowden:~$ sudo journalctl --vacuum-time=1s",
                "[[  OK  ] Vacuuming done, freed 48.0M of archived journals",
                "[[  OK  ] USB device serial SK8F-4429-X: LOG DESTROYED",
                "[[  OK  ] Trace 6/8 eliminated.",
            ],
            "success_feedback": "Journal logs destroyed. The rotate + vacuum-time trick seals the old log then immediately deletes it. No record of USB connections remains.",
            "learn_text": "Linux keeps detailed logs of every USB device connected. The systemd journal stores device model, serial number, and timestamp. journalctl manages these logs. The rotate + vacuum trick is a real anti-forensics technique.",
        },
        {
            "id": 7, "name": "Bash Command History", "icon": "âŒ¨", "phase": 3,
            "danger_title": "EVERY COMMAND YOU TYPED IS RECORDED",
            "danger_text": "Your terminal history contains the exact commands used to copy PRISM files to USB. Timestamped evidence of exfiltration.",
            "file_type": ".bash_history plaintext", "file_size": "12 KB", "risk_level": "CRITICAL",
            "forensic_note": "Readable with any text editor",
            "correct_command": "cat /dev/null > ~/.bash_history && history -c && exit",
            "command_breakdown": [
                ("cat /dev/null", "reads from /dev/null â€” always empty"),
                (">", "redirect output INTO the file (overwrites)"),
                ("~/.bash_history", "your terminal history file"),
                ("history -c", "clear current session's in-memory history"),
                ("exit", "close terminal â€” writes empty history to disk"),
            ],
            "tokens": [],
            "options": [
                "cat /dev/null > ~/.bash_history && history -c && exit",
                "rm ~/.bash_history",
                "history --clear",
            ],
            "wrong_commands": [
                {"cmd": "rm ~/.bash_history", "feedback": "Wrong. Removing the file is suspicious AND the current session's history is still in memory. When you exit, bash recreates the file from memory. You need to empty it AND clear memory AND exit."},
                {"cmd": "history --clear", "feedback": "Wrong syntax (correct flag is history -c). Even history -c alone only clears in-memory history, not the .bash_history FILE on disk. You need both steps plus exit."},
            ],
            "success_output": [
                "root@snowden:~$ cat /dev/null > ~/.bash_history",
                "[[  OK  ] ~/.bash_history: overwritten with null content",
                "root@snowden:~$ history -c",
                "[[  OK  ] In-memory command history: CLEARED",
                "root@snowden:~$ exit",
                "[[  OK  ] Session closed. History written: 0 entries.",
                "[[  OK  ] Trace 7/8 eliminated.",
            ],
            "success_feedback": "Command history destroyed using the 3-step technique: overwrite file, clear memory, exit. Missing any step leaves recoverable evidence.",
            "learn_text": "Every command typed in a Linux terminal is saved to ~/.bash_history. The correct technique requires THREE steps: (1) overwrite file with /dev/null, (2) clear in-memory history, (3) exit so bash writes empty history.",
        },
        {
            "id": 8, "name": "Cloud Backup Sync", "icon": "â˜", "phase": 3,
            "danger_title": "YOUR FILES ARE ON A REMOTE SERVER",
            "danger_text": "A background sync process uploaded copies of your documents to a cloud server. The NSA can subpoena those files in minutes.",
            "file_type": "Cloud sync daemon", "file_size": "Remote â€” 2.3 GB", "risk_level": "CRITICAL",
            "forensic_note": "Subpoena to provider takes < 2 hours",
            "correct_command": "pkill -f dropbox && rm -rf ~/.dropbox && rm -rf ~/Dropbox",
            "command_breakdown": [
                ("pkill -f dropbox", "kill all processes matching 'dropbox'"),
                ("&&", "then..."),
                ("rm -rf ~/.dropbox", "remove hidden config folder (credentials + sync log)"),
                ("rm -rf ~/Dropbox", "remove local synced files folder"),
            ],
            "tokens": [],
            "options": [
                "pkill -f dropbox && rm -rf ~/.dropbox && rm -rf ~/Dropbox",
                "sudo service dropbox stop",
                "rm -rf ~/Dropbox",
            ],
            "wrong_commands": [
                {"cmd": "sudo service dropbox stop", "feedback": "Wrong. Stopping the service does NOT delete local files or the config folder with credentials and sync history. The data remains fully intact."},
                {"cmd": "rm -rf ~/Dropbox", "feedback": "Incomplete. This removes synced files but leaves ~/.dropbox with account credentials, device token, and full sync history log. Investigators use this to prove what was synced."},
            ],
            "success_output": [
                "root@snowden:~$ pkill -f dropbox",
                "[[  OK  ] Dropbox daemon: TERMINATED (PID 3847)",
                "root@snowden:~$ rm -rf ~/.dropbox",
                "[[  OK  ] Config + credentials: REMOVED",
                "root@snowden:~$ rm -rf ~/Dropbox",
                "[[  OK  ] Synced files folder: REMOVED",
                "[[  OK  ] Cloud sync evidence: ELIMINATED",
                "[[  OK  ] Trace 8/8 eliminated. ALL TRACES WIPED.",
            ],
            "success_feedback": "Cloud sync fully neutralized: process killed, credentials destroyed, local files removed. Three-part cleanup is essential for any sync daemon.",
            "learn_text": "Cloud sync software runs silently and uploads files to remote servers. Even destroying your device leaves files on corporate servers. The hidden config folder stores credentials and a complete sync log.",
        },
    ]

    ct_state = {
        "phase": "playing",
        "current_index": 0,
        "wiped": 0,
        "failed": 0,
        "statuses": [],
        "terminal_log": [],
        "assembled_tokens": [],
        "typed_input": "",
        "show_breakdown": False,
        "show_learn": False,
        "show_result": False,
        "feedback_text": "",
        "feedback_ok": False,
        "hint_used": False,
    }

    def ct_reset():
        ct_state["phase"] = "playing"
        ct_state["current_index"] = 0
        ct_state["wiped"] = 0
        ct_state["failed"] = 0
        ct_state["statuses"] = ["PENDING"] * 8
        ct_state["terminal_log"] = [
            "> COVER YOUR TRACKS v2.1 initialized",
            "> Scanning system for forensic traces...",
            "> 8 digital traces detected",
            "> WARNING: NSA response team dispatched",
            "> Begin elimination sequence",
        ]
        ct_state["assembled_tokens"] = []
        ct_state["typed_input"] = ""
        ct_state["show_breakdown"] = False
        ct_state["show_learn"] = False
        ct_state["show_result"] = False
        ct_state["feedback_text"] = ""
        ct_state["feedback_ok"] = False
        ct_state["hint_used"] = False
        cover_timer.start()

    def ct_current():
        idx = ct_state["current_index"]
        if idx < 8:
            return ct_traces[idx]
        return None

    def ct_get_input_command():
        trace = ct_current()
        if trace is None:
            return ""
        if trace["phase"] == 1:
            return trace["correct_command"]
        elif trace["phase"] == 2:
            return " ".join(ct_state["assembled_tokens"])
        else:
            return ct_state["typed_input"]

    def ct_add_token(token):
        ct_state["assembled_tokens"].append(token)
        renpy.restart_interaction()

    def ct_remove_last_token():
        if ct_state["assembled_tokens"]:
            ct_state["assembled_tokens"].pop()
        renpy.restart_interaction()

    def ct_select_option(cmd):
        ct_state["typed_input"] = cmd
        renpy.restart_interaction()

    def ct_use_hint():
        trace = ct_current()
        if trace is None:
            return
        if trace["phase"] >= 2:
            cover_timer.add_penalty(5)
        ct_state["hint_used"] = True
        ct_state["terminal_log"].append("> HINT USED (-5 sec penalty)")
        correct = trace["correct_command"]
        hint_text = "> HINT: The command starts with: " + correct.split()[0]
        ct_state["terminal_log"].append(hint_text)
        renpy.restart_interaction()

    def ct_execute():
        trace = ct_current()
        if trace is None:
            return
        idx = ct_state["current_index"]
        cmd = ct_get_input_command().strip()
        correct = trace["correct_command"].strip()

        if cmd == correct:
            ct_state["statuses"][idx] = "WIPED"
            ct_state["wiped"] += 1
            ct_state["feedback_ok"] = True
            ct_state["feedback_text"] = trace["success_feedback"]
            for line in trace["success_output"]:
                ct_state["terminal_log"].append(line)
        else:
            wrong_fb = ""
            if trace["phase"] == 3:
                for wc in trace.get("wrong_commands", []):
                    if cmd == wc["cmd"]:
                        wrong_fb = wc["feedback"]
                        break
            if not wrong_fb:
                wrong_fb = "Incorrect command. The correct command was: " + correct
            ct_state["statuses"][idx] = "FAILED"
            ct_state["failed"] += 1
            ct_state["feedback_ok"] = False
            ct_state["feedback_text"] = wrong_fb
            ct_state["terminal_log"].append("> FAILED: " + trace["name"])
            if trace["phase"] >= 2:
                cover_timer.add_penalty(5)
                ct_state["terminal_log"].append("> PENALTY: +5 seconds")

        ct_state["show_breakdown"] = True
        ct_state["assembled_tokens"] = []
        ct_state["typed_input"] = ""
        ct_state["hint_used"] = False
        renpy.restart_interaction()

    def ct_show_learn():
        ct_state["show_breakdown"] = False
        ct_state["show_learn"] = True
        renpy.restart_interaction()

    def ct_advance():
        ct_state["show_breakdown"] = False
        ct_state["show_learn"] = False
        ct_state["hint_used"] = False
        idx = ct_state["current_index"] + 1
        ct_state["current_index"] = idx
        if idx >= 8:
            ct_state["show_result"] = True
        else:
            st = "IN PROGRESS"
            ct_state["statuses"][idx] = st
            ct_state["terminal_log"].append("> Analyzing trace " + str(idx + 1) + "/8: " + ct_traces[idx]["name"])
        renpy.restart_interaction()

    def ct_status_color(status):
        if status == "WIPED": return "#00FF88"
        if status == "FAILED": return "#FF2D55"
        if status == "IN PROGRESS": return "#FFD700"
        if status == "DETECTED": return "#FF2D55"
        return "#3A4A55"

    def ct_get_all_tokens(trace):
        correct = list(trace.get("tokens", []))
        distractors = list(trace.get("distractor_tokens", []))
        import random
        all_t = correct + distractors
        random.shuffle(all_t)
        return all_t

    ct_shuffled_tokens_cache = {}

    def ct_get_shuffled_tokens(trace_id):
        if trace_id not in ct_shuffled_tokens_cache:
            for t in ct_traces:
                if t["id"] == trace_id:
                    ct_shuffled_tokens_cache[trace_id] = ct_get_all_tokens(t)
                    break
        return ct_shuffled_tokens_cache.get(trace_id, [])

    def ct_reset_token_cache():
        ct_shuffled_tokens_cache.clear()

transform ct_cursor_blink:
    alpha 1.0
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0
    repeat

transform ct_glow_pulse:
    alpha 0.6
    linear 1.5 alpha 1.0
    linear 1.5 alpha 0.6
    repeat

transform ct_threat_flash:
    alpha 0.7
    linear 0.4 alpha 1.0
    linear 0.4 alpha 0.7
    repeat

transform ct_panel_enter:
    yoffset 30 alpha 0.0
    ease 0.3 yoffset 0 alpha 1.0

screen screen_cover_tracks():
    modal True
    on "show" action Function(ct_reset)
    timer 0.1 repeat True action Function(renpy.restart_interaction)

    if cover_timer.is_expired() and not ct_state["show_result"] and not ct_state["show_breakdown"] and not ct_state["show_learn"]:
        timer 0.01 action [SetDict(ct_state, "show_result", True), Function(renpy.restart_interaction)]

    $ _ct = ct_current()
    $ _ct_idx = ct_state["current_index"]
    $ _ct_eta = cover_timer.get_eta_string()
    $ _ct_tlvl = cover_timer.get_threat_level()
    $ _ct_tcol = cover_timer.get_threat_color()
    $ _ct_prog = cover_timer.get_progress()
    $ _ct_wiped = ct_state["wiped"]
    $ _ct_rem = cover_timer.get_remaining()

    add "#080C10"
    add "images/logo.png":
        xalign 0.5 yalign 0.5 alpha 0.04
        fit "contain" xsize 900 ysize 900

    frame:
        xpos 0 ypos 0 xsize 1920 ysize 52
        background "#0D1117F0"
        padding (20, 0)
        hbox:
            xfill True yalign 0.5
            hbox:
                spacing 20 yalign 0.5
                text t("CLASSIFIED") color "#FF2D55" size 11 bold True font "fonts/ShareTechMono-Regular.ttf"
                text t("CH.4: THE ESCAPE") color "#7A8A99" size 11 font "fonts/ShareTechMono-Regular.ttf"
                text t("// COVER YOUR TRACKS //") color "#00FFD1" size 16 bold True font "fonts/ShareTechMono-Regular.ttf"
            hbox:
                spacing 24 xalign 1.0 yalign 0.5
                text t("TRACES: [_ct_wiped]/8") color "#E8E8E8" size 14 bold True font "fonts/ShareTechMono-Regular.ttf"
                text t("[_ct_eta]") color (_ct_tcol if _ct_rem > 0 else "#FF2D55") size 22 bold True font "fonts/ShareTechMono-Regular.ttf"
                text t("THREAT: [_ct_tlvl]") color _ct_tcol size 14 bold True font "fonts/ShareTechMono-Regular.ttf"

    frame:
        xpos 0 ypos 52 xsize 330 ysize 924
        background "#0D1117"
        padding (10, 10)
        vbox:
            spacing 6

            text t("--- SYS MONITOR ---") color "#00FFD1" size 11 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
            null height 4
            hbox:
                xfill True
                text t("CPU") color "#7A8A99" size 11 bold True font "fonts/ShareTechMono-Regular.ttf" yalign 0.5 xsize 30
                add ct_wave_cpu
            hbox:
                xfill True
                text t("RAM") color "#7A8A99" size 11 bold True font "fonts/ShareTechMono-Regular.ttf" yalign 0.5 xsize 30
                frame:
                    xsize 280 ysize 14 yalign 0.5
                    background "#111720"
                    frame:
                        xsize max(4, int(280 * 61 / 100)) ysize 14
                        background "#FFD700"
            hbox:
                xfill True
                text t("NET") color "#7A8A99" size 11 bold True font "fonts/ShareTechMono-Regular.ttf" yalign 0.5 xsize 30
                add ct_wave_net

            null height 6
            frame:
                xfill True ysize 1
                background "#3A4A55"

            text t("--- PROCESSES ---") color "#00FFD1" size 11 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
            null height 2
            text t("PID   NAME              CPU   MEM") color "#3A4A55" size 10 font "fonts/ShareTechMono-Regular.ttf"
            text t("1024  snowden-os        2.1%%  4.8%%") color "#7A8A99" size 10 font "fonts/ShareTechMono-Regular.ttf"
            text t("3847  dropbox-daemon   12.4%%  8.2%%") color "#7A8A99" size 10 font "fonts/ShareTechMono-Regular.ttf"
            text t("4401  ssh-agent         0.3%%  0.1%%") color "#7A8A99" size 10 font "fonts/ShareTechMono-Regular.ttf"
            text t("5102  chrome-render    43.8%% 19.6%%") color "#7A8A99" size 10 font "fonts/ShareTechMono-Regular.ttf"
            text t("7788  wpa_supplicant    1.1%%  0.3%%") color "#7A8A99" size 10 font "fonts/ShareTechMono-Regular.ttf"

            null height 6
            frame:
                xfill True ysize 1
                background "#3A4A55"

            text t("--- TRACES DETECTED ---") color "#00FFD1" size 11 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
            null height 4
            for _i in range(8):
                $ _tr = ct_traces[_i]
                $ _st = ct_state["statuses"][_i] if _i < len(ct_state["statuses"]) else "PENDING"
                $ _stcol = ct_status_color(_st)
                $ _is_cur = (_i == _ct_idx and not ct_state["show_result"])
                frame:
                    xfill True ysize 38
                    background ("#111720" if _is_cur else "#0D1117")
                    left_padding 6
                    right_padding 6
                    top_padding 2
                    bottom_padding 2
                    if _is_cur:
                        left_padding 4
                    hbox:
                        xfill True yalign 0.5
                        hbox:
                            spacing 6 yalign 0.5
                            text _tr["icon"] size 14 font "fonts/ShareTechMono-Regular.ttf" yalign 0.5
                            text _tr["name"] color ("#E8E8E8" if _is_cur else "#7A8A99") size 12 font "fonts/ShareTechMono-Regular.ttf" yalign 0.5
                        text _st color _stcol size 10 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 1.0 yalign 0.5

    frame:
        xpos 1590 ypos 52 xsize 330 ysize 924
        background "#0D1117"
        padding (10, 10)
        vbox:
            spacing 8

            text t("--- NSA MONITOR ---") color "#FF2D55" size 11 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
            null height 4
            add ct_threat_bar xalign 0.5
            $ _pct_text = "{:.0f}%%".format(_ct_prog * 100)
            text _pct_text color _ct_tcol size 24 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
            text t("NSA CLOSING IN") color "#7A8A99" size 11 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
            text t("AGENT ETA: [_ct_eta]") color _ct_tcol size 18 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5

            null height 6
            frame:
                xfill True ysize 1
                background "#3A4A55"

            text t("--- NET TRAFFIC ---") color "#00FFD1" size 11 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
            null height 2
            add ct_wave_up xalign 0.5
            add ct_wave_dn xalign 0.5
            text t("UP: 2.4 KB/s   DOWN: 14.8 KB/s") color "#7A8A99" size 10 font "fonts/ShareTechMono-Regular.ttf" xalign 0.5

            null height 6
            frame:
                xfill True ysize 1
                background "#3A4A55"

            if _ct is not None:
                text t("--- EVIDENCE SCAN ---") color "#00FFD1" size 11 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
                null height 4
                $ _rl = _ct["risk_level"]
                $ _rlcol = "#FF2D55" if _rl == "CRITICAL" else "#FF8C00" if _rl == "HIGH" else "#FFD700"
                hbox:
                    xfill True
                    text t("FILE TYPE:") color "#7A8A99" size 11 font "fonts/ShareTechMono-Regular.ttf"
                    text _ct["file_type"] color "#E8E8E8" size 11 font "fonts/ShareTechMono-Regular.ttf" xalign 1.0
                hbox:
                    xfill True
                    text t("SIZE:") color "#7A8A99" size 11 font "fonts/ShareTechMono-Regular.ttf"
                    text _ct["file_size"] color "#E8E8E8" size 11 font "fonts/ShareTechMono-Regular.ttf" xalign 1.0
                hbox:
                    xfill True
                    text t("RISK:") color "#7A8A99" size 11 font "fonts/ShareTechMono-Regular.ttf"
                    text t("[_rl]") color _rlcol size 11 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 1.0
                text _ct["forensic_note"] color "#3A4A55" size 10 font "fonts/ShareTechMono-Regular.ttf"

            null height 6
            frame:
                xfill True ysize 1
                background "#3A4A55"

            text t("--- LOCATION ---") color "#00FFD1" size 11 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
            null height 4
            text t("IP:     172.16.4.22") color "#7A8A99" size 10 font "fonts/ShareTechMono-Regular.ttf"
            text t("VPN:    ACTIVE (ProtonVPN)") color "#00FF88" size 10 font "fonts/ShareTechMono-Regular.ttf"
            text t("LOC:    Hong Kong, CN") color "#7A8A99" size 10 font "fonts/ShareTechMono-Regular.ttf"
            text t("UPTIME: 00:01:23") color "#7A8A99" size 10 font "fonts/ShareTechMono-Regular.ttf"
            text t("CRYPTO: AES-256-GCM") color "#00FFD1" size 10 font "fonts/ShareTechMono-Regular.ttf"

    if _ct is not None and not ct_state["show_result"]:
        frame:
            xpos 330 ypos 52 xsize 1260 ysize 924
            background "#0A0E14"
            padding (20, 14)
            vbox:
                spacing 8

                frame:
                    xfill True ysize 90
                    background "#0D1117"
                    padding (16, 10)
                    vbox:
                        spacing 4
                        $ _phase_label = "GUIDED" if _ct["phase"] == 1 else "ASSEMBLY" if _ct["phase"] == 2 else "SELECT"
                        $ _trace_id = _ct["id"]
                        $ _trace_name = _ct["name"]
                        hbox:
                            spacing 12
                            text t("TARGET: TRACE [_trace_id]/8 — [_trace_name]") color "#00FFD1" size 15 bold True font "fonts/ShareTechMono-Regular.ttf" yalign 0.5
                            text t("MODE: [_phase_label]") color "#7A8A99" size 12 font "fonts/ShareTechMono-Regular.ttf" yalign 0.5
                        text _ct["danger_title"] color "#FF2D55" size 13 bold True font "fonts/ShareTechMono-Regular.ttf"
                        text _ct["danger_text"] color "#7A8A99" size 11 font "fonts/ShareTechMono-Regular.ttf"

                frame:
                    xfill True ysize 380
                    background "#080C10"
                    left_padding 2
                    right_padding 12
                    top_padding 8
                    bottom_padding 8

                    hbox:

                        frame:
                            xsize 2 yfill True
                            background "#00FFD1"
                        null width 10
                        viewport:
                            xfill True yfill True
                            scrollbars "vertical"
                            mousewheel True
                            yinitial 1.0
                            vbox:
                                spacing 2
                                for _line in ct_state["terminal_log"][-25:]:
                                    $ _lcol = "#00FF88" if "[[  OK  ]" in _line else "#FF2D55" if "FAILED" in _line or "PENALTY" in _line else "#FFD700" if "WARN" in _line or "HINT" in _line else "#C8E6C9"
                                    text _line color _lcol size 13 font "fonts/ShareTechMono-Regular.ttf"

                                hbox:
                                    spacing 4
                                    text t("root@snowden-laptop:~$") color "#00FFD1" size 13 bold True font "fonts/ShareTechMono-Regular.ttf"
                                    text t("_") color "#00FFD1" size 13 font "fonts/ShareTechMono-Regular.ttf" at ct_cursor_blink

                frame:
                    xfill True ysize 40
                    background "#0D1117"
                    padding (12, 8)
                    hbox:
                        spacing 6 yalign 0.5
                        text t("root@snowden-laptop:~$") color "#00FFD1" size 14 bold True font "fonts/ShareTechMono-Regular.ttf"
                        $ _cmd_display = ct_get_input_command()
                        text t("[_cmd_display]") color "#A8FF78" size 14 font "fonts/ShareTechMono-Regular.ttf"

                null height 4

                if _ct["phase"] == 1:
                    frame:
                        xfill True
                        background "#111720"
                        padding (14, 10)
                        vbox:
                            spacing 6
                            text t("GUIDED MODE — Review the command, then press EXECUTE") color "#FFD700" size 12 bold True font "fonts/ShareTechMono-Regular.ttf"
                            text t("The correct command is pre-filled above. Study each part before executing.") color "#7A8A99" size 11 font "fonts/ShareTechMono-Regular.ttf"

                elif _ct["phase"] == 2:
                    frame:
                        xfill True
                        background "#111720"
                        padding (14, 10)
                        vbox:
                            spacing 8
                            text t("ASSEMBLY MODE — Click tokens in the correct order") color "#FFD700" size 12 bold True font "fonts/ShareTechMono-Regular.ttf"
                            hbox:
                                spacing 8
                                box_wrap True
                                $ _avail = ct_get_shuffled_tokens(_ct["id"])
                                for _tok in _avail:
                                    if _tok not in ct_state["assembled_tokens"]:
                                        textbutton t("[_tok]"):
                                            background "#1A2A2A"
                                            hover_background "#00FFD1"
                                            text_color "#A8FF78"
                                            text_hover_color "#000000"
                                            text_size 21
                                            text_font "fonts/ShareTechMono-Regular.ttf"
                                            padding (12, 8)
                                            action Function(ct_add_token, _tok)
                            if ct_state["assembled_tokens"]:
                                hbox:
                                    spacing 6
                                    text t("Built:") color "#7A8A99" size 12 font "fonts/ShareTechMono-Regular.ttf" yalign 0.5
                                    for _atok in ct_state["assembled_tokens"]:
                                        text t("[_atok]") color "#00FFD1" size 13 font "fonts/ShareTechMono-Regular.ttf" yalign 0.5
                                    textbutton t("UNDO"):
                                        text_color "#FF2D55" text_size 21 text_font "fonts/ShareTechMono-Regular.ttf"
                                        action Function(ct_remove_last_token)

                elif _ct["phase"] == 3:
                    frame:
                        xfill True
                        background "#111720"
                        padding (14, 10)
                        vbox:
                            spacing 8
                            text t("SELECT MODE — Choose the correct command") color "#FFD700" size 12 bold True font "fonts/ShareTechMono-Regular.ttf"
                            for _opt in _ct["options"]:
                                $ _is_sel = (ct_state["typed_input"] == _opt)
                                textbutton t("[_opt]"):
                                    xfill True
                                    background ("#1A2A2A" if _is_sel else "#111720")
                                    hover_background "#00FFD1"
                                    text_color ("#00FFD1" if _is_sel else "#A8FF78")
                                    text_hover_color "#000000"
                                    text_size 17
                                    text_font "fonts/ShareTechMono-Regular.ttf"
                                    padding (12, 8)
                                    action Function(ct_select_option, _opt)

                null height 6
                hbox:
                    xalign 0.5 spacing 20
                    textbutton t("> EXECUTE COMMAND"):
                        background "#003A2A"
                        hover_background "#00FFD1"
                        text_color "#00FFD1"
                        text_hover_color "#000000"
                        text_size 21
                        text_bold True
                        text_font "fonts/ShareTechMono-Regular.ttf"
                        padding (40, 12)
                        action Function(ct_execute)
                    if not ct_state["hint_used"]:
                        textbutton t("? HINT -5s"):
                            background "#2A2000"
                            hover_background "#FFD700"
                            text_color "#FFD700"
                            text_hover_color "#000000"
                            text_size 21
                            text_font "fonts/ShareTechMono-Regular.ttf"
                            padding (15, 8)
                            action Function(ct_use_hint)

    if ct_state["show_breakdown"] and _ct is not None:
        add "#080C10DD"
        frame at ct_panel_enter:
            xalign 0.5 yalign 0.5 xsize 1000
            background "#0D1117F8"
            padding (30, 24)
            vbox:
                spacing 12
                if ct_state["feedback_ok"]:
                    text t("// TRACE WIPED //") color "#00FF88" size 24 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
                else:
                    text t("// TRACE FAILED //") color "#FF2D55" size 24 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
                $ _fb = ct_state["feedback_text"]
                text t("[_fb]") color "#E8E8E8" size 14 font "fonts/ShareTechMono-Regular.ttf"
                null height 6
                text t("--- COMMAND BREAKDOWN ---") color "#00FFD1" size 14 bold True font "fonts/ShareTechMono-Regular.ttf"
                for _bk, _bv in _ct["command_breakdown"]:
                    hbox:
                        spacing 12
                        text t("[_bk]") color "#00FFD1" size 13 bold True font "fonts/ShareTechMono-Regular.ttf" xsize 220
                        text t("[_bv]") color "#7A8A99" size 13 font "fonts/ShareTechMono-Regular.ttf"
                null height 10
                hbox:
                    xalign 0.5 spacing 16
                    textbutton t("> WHAT I LEARNED"):
                        background "#2A2000" hover_background "#FFD700"
                        text_color "#FFD700" text_hover_color "#000000"
                        text_size 17 text_bold True text_font "fonts/ShareTechMono-Regular.ttf"
                        padding (20, 10)
                        action Function(ct_show_learn)
                    textbutton t("> NEXT TRACE"):
                        background "#003A2A" hover_background "#00FFD1"
                        text_color "#00FFD1" text_hover_color "#000000"
                        text_size 17 text_bold True text_font "fonts/ShareTechMono-Regular.ttf"
                        padding (20, 10)
                        action Function(ct_advance)

    if ct_state["show_learn"] and _ct is not None:
        add "#080C10DD"
        frame at ct_panel_enter:
            xalign 0.5 yalign 0.5 xsize 900
            background "#0D1117F8"
            padding (30, 24)
            vbox:
                spacing 14
                text t("--- WHAT YOU LEARNED ---") color "#FFD700" size 16 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
                $ _lt = _ct["learn_text"]
                text t("[_lt]") color "#CCCCCC" size 15 font "fonts/ShareTechMono-Regular.ttf" line_spacing 4
                null height 10
                textbutton t("> NEXT TRACE"):
                    background "#003A2A" hover_background "#00FFD1"
                    text_color "#00FFD1" text_hover_color "#000000"
                    text_size 21 text_bold True text_font "fonts/ShareTechMono-Regular.ttf"
                    padding (30, 12)
                    xalign 0.5
                    action Function(ct_advance)

    if ct_state["show_result"]:
        add "#080C10EE"
        frame:
            xalign 0.5 yalign 0.5 xsize 1100
            background "#0D1117F8"
            padding (36, 30)
            viewport:
                xfill True ysize 900
                scrollbars "vertical"
                mousewheel True
                vbox:
                    spacing 14 xalign 0.5
                    if _ct_wiped >= 8:
                        text t("// MISSION ACCOMPLISHED //") color "#00FF88" size 28 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
                        text t("All 8 digital traces destroyed. NSA agents found nothing.") color "#E8E8E8" size 18 font "fonts/ShareTechMono-Regular.ttf" xalign 0.5 text_align 0.5
                        text t("DIGITAL FORENSICS EXPERT") color "#00FFD1" size 16 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
                    elif _ct_wiped >= 6:
                        text t("// MISSION PARTIAL //") color "#FFD700" size 28 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
                        text t("Most traces destroyed. Some evidence may be recoverable.") color "#E8E8E8" size 18 font "fonts/ShareTechMono-Regular.ttf" xalign 0.5 text_align 0.5
                    else:
                        text t("// MISSION FAILED //") color "#FF2D55" size 28 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
                        text t("NSA agents reached the room. Forensic evidence recovered.") color "#E8E8E8" size 18 font "fonts/ShareTechMono-Regular.ttf" xalign 0.5 text_align 0.5
                    null height 6
                    text t("WIPED: [_ct_wiped] / 8") color "#00FFD1" size 22 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
                    null height 10
                    text t("--- 8 THINGS YOU LEARNED TODAY ---") color "#FFD700" size 15 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
                    for _si in range(8):
                        $ _str = ct_traces[_si]
                        $ _sst = ct_state["statuses"][_si]
                        $ _ssc = ct_status_color(_sst)
                        frame:
                            xfill True
                            background "#111720"
                            padding (14, 8)
                            hbox:
                                spacing 10
                                text str(_si + 1) + "." color "#7A8A99" size 14 font "fonts/ShareTechMono-Regular.ttf" yalign 0.0 xsize 24
                                vbox:
                                    spacing 2
                                    hbox:
                                        spacing 8
                                        text _str["name"] color "#E8E8E8" size 14 bold True font "fonts/ShareTechMono-Regular.ttf"
                                        text t("[_sst]") color _ssc size 12 bold True font "fonts/ShareTechMono-Regular.ttf"
                                    text _str["learn_text"][:80] + "..." color "#7A8A99" size 12 font "fonts/ShareTechMono-Regular.ttf"
                    null height 16
                    textbutton t("> CONTINUE MISSION"):
                        background "#003A2A" hover_background "#00FFD1"
                        text_color "#00FFD1" text_hover_color "#000000"
                        text_size 23 text_bold True text_font "fonts/ShareTechMono-Regular.ttf"
                        padding (40, 14) xalign 0.5
                        action Return(_ct_wiped)

    if not ct_state["show_result"] and not ct_state["show_breakdown"] and not ct_state["show_learn"]:
        frame:
            xpos 0 ypos 976 xsize 1920 ysize 104
            background "#0D1117F0"
            padding (24, 0)
            hbox:
                xfill True yalign 0.5
                hbox:
                    spacing 30
                    text t("ESC: ABORT") color "#3A4A55" size 12 font "fonts/ShareTechMono-Regular.ttf"
                    text t("ENTER: EXECUTE") color "#3A4A55" size 12 font "fonts/ShareTechMono-Regular.ttf"
                    text t("HINT: -5 SEC") color "#3A4A55" size 12 font "fonts/ShareTechMono-Regular.ttf"
                text t("Leave no trace. Destroy all evidence.") color "#7A8A99" size 14 font "fonts/ShareTechMono-Regular.ttf" xalign 0.5
                text t("AGENT ETA: [_ct_eta]") color _ct_tcol size 16 bold True font "fonts/ShareTechMono-Regular.ttf" xalign 1.0

    add ct_scanlines

    key "K_RETURN" action Function(ct_execute)
    key "K_KP_ENTER" action Function(ct_execute)
    key "K_BACKSPACE" action NullAction()
    key "mouseup_3" action NullAction()

    use block_shortcuts_and_skip("SKIP")

label minigame_4_cover_tracks:
    $ cover_wiped = 0
    $ cover_failed = 0
    $ ct_reset_token_cache()
    $ cover_timer.start()

    $ quick_menu = False
    $ show_hud = False

    call screen screen_cover_tracks

    if _return == "SKIP":
        $ quick_menu = True
        $ show_hud = True
        $ renpy.notify("Minigame Skipped")
        return

    $ cover_wiped = ct_state["wiped"]
    $ cover_failed = ct_state["failed"]
    $ quick_menu = True
    $ show_hud = True

    if cover_wiped >= 8:
        $ knowledge_score += 3
        $ escape_successful = True
        $ evidence_secured = True
        $ renpy.notify(t("PERFECT â€” Digital Forensics Expert! +3"))
    elif cover_wiped >= 6:
        $ knowledge_score += 2
        $ escape_successful = True
        $ renpy.notify(t("Good work. Most traces wiped. +2"))
    elif cover_wiped >= 4:
        $ knowledge_score += 1
        $ suspicion_level += 1
        $ renpy.notify(t("Partial success. Some evidence remains."))
    else:
        $ suspicion_level += 2
        $ identity_exposed = True
        $ renpy.notify(t("Mission failed. NSA found evidence."))

    return
