init python:
    import time

    class TerminalLine:
        def __init__(self, text, color="#ffffff"):
            self.text = text
            self.color = color
            self.timestamp = time.time()
            self.expired = False

    class TerminalInputValue(InputValue):
        @property
        def default(self):
            return True

        def get_text(self):
            return pw_game_state["current_input"]

        def set_text(self, s):
            pw_game_state["current_input"] = s
            renpy.restart_interaction()

        def enter(self):
            res = pw_check_command()
            if res == "EXIT":
                return True
            renpy.restart_interaction()
            raise renpy.IgnoreEvent()

    pw_game_state = {
        "lines": [],
        "current_input": "",
        "round": 0,
        "wrong_attempts": 0,
        "score": 0,
        "tab_hint_used": False,
        "status": "intro",
        "queued_output": [],
    }

    rounds_data = [

        {
            "intro": [
                "[*] NSA internal system hash intercepted.",
                "[*] Hash algorithm identified: MD5",
                "[*] Salt: NONE",
                "[*] Hash value: 5f4dcc3b5aa765d61d8327deb882cf99",
                "",
                "Your task: run a dictionary attack against this hash.",
                "The rockyou wordlist is available at /usr/share/wordlists/rockyou.txt",
                "The hash is saved at /tmp/hash1.txt",
                "",
                "Use the correct john the ripper command to crack it."
            ],
            "correct_command": "john --wordlist=/usr/share/wordlists/rockyou.txt /tmp/hash1.txt",
            "acceptable_variants": [
                "john --wordlist=rockyou.txt /tmp/hash1.txt",
                "john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-md5 /tmp/hash1.txt",
                "john --wordlist=rockyou.txt --format=raw-md5 /tmp/hash1.txt"
            ],
            "success_output": [
                "Using default input encoding: UTF-8",
                "Loaded 1 password hash (Raw-MD5 [MD5 128/128 AVX 4x3])",
                "Press 'q' or Ctrl-C to abort, almost any other key for status",
                "",
                "Testing: 123456           NO",
                "Testing: password         CRACKED",
                "",
                "password         (nsa_admin)",
                "",
                "1g 0:00:00:00 DONE (2026-06-13 09:47) 33.33g/s 341200p/s",
                "Session completed.",
                "",
                "[+] Hash cracked in 0.003 seconds.",
                "[+] Password: password"
            ],
            "learn_text": [
                "# RESULT ANALYSIS:",
                "# The hash 5f4dcc3b... is MD5(\"password\").",
                "# rockyou.txt contains 14 million real leaked passwords.",
                "# John the Ripper tested each one against the hash.",
                "# \"password\" was found in 0.003 seconds.",
                "# MD5 with no salt provides zero protection for weak passwords.",
                "# Any password found in a dictionary is compromised instantly.",
                "",
                "[press ENTER to continue]"
            ]
        },

        {
            "intro": [
                "[*] Second hash obtained from same database.",
                "[*] Algorithm: MD5",
                "[*] Hash value: ab56b4d92b40713acc5af89985d4b786",
                "[*] Dictionary attack: FAILED (0 results)",
                "",
                "The basic wordlist failed. This password uses",
                "character substitutions: letters replaced with",
                "numbers or symbols (a->@, e->3, o->0, etc.)",
                "",
                "John the Ripper supports rule-based mutations.",
                "Add rules to your previous command to crack this hash.",
                "Hash saved at /tmp/hash2.txt"
            ],
            "correct_command": "john --wordlist=/usr/share/wordlists/rockyou.txt --rules=best64 /tmp/hash2.txt",
            "acceptable_variants": [
                "john --wordlist=rockyou.txt --rules /tmp/hash2.txt",
                "john --wordlist=rockyou.txt --rules=best64 /tmp/hash2.txt",
                "john --wordlist=/usr/share/wordlists/rockyou.txt --rules /tmp/hash2.txt"
            ],
            "success_output": [
                "Using default input encoding: UTF-8",
                "Loaded 1 password hash (Raw-MD5)",
                "Applying best64 rules...",
                "",
                "Testing: password         NO",
                "Testing: P@ssword         NO",
                "Testing: monkey           NO",
                "Testing: M0nk3y           NO",
                "Testing: M0nk3y!          CRACKED",
                "",
                "M0nk3y!          (nsa_agent_07)",
                "",
                "1g 0:00:00:02 DONE 2.4 seconds",
                "Session completed.",
                "",
                "[+] Hash cracked in 2.4 seconds.",
                "[+] Password: M0nk3y!"
            ],
            "learn_text": [
                "# RESULT ANALYSIS:",
                "# \"M0nk3y!\" feels strong — but it is \"monkey\" with",
                "# substitutions that every cracking ruleset includes.",
                "# --rules=best64 applies 64 common transformation rules",
                "# to every word in the dictionary automatically.",
                "# o->0, e->3, a->@, appending ! or 123 — all standard rules.",
                "# Substitution tricks on weak base words provide no security.",
                "# Password length with random characters is the only solution.",
                "",
                "[press ENTER to continue]"
            ]
        },

        {
            "intro": [
                "[*] Third hash obtained. This one is different.",
                "[*] Hash value:",
                "    $2b$12$LQv3c1yqBWVHxkd0LQ4YCOuuQ0InOuelmEMkQmbw.s18GLSJ4MTO2",
                "",
                "[*] Analyzing hash format...",
                "[*] Prefix $2b$ detected: bcrypt",
                "[*] Cost factor: 12 (2^12 = 4096 iterations per guess)",
                "[*] Salt: embedded in hash (unique per user)",
                "",
                "Estimated crack time on modern GPU (RTX 4090):",
                "  - Dictionary attack:        still milliseconds for weak passwords",
                "  - 8-character random:       approximately 3 hours",
                "  - 16-character mixed:       over 400 years",
                "",
                "This hash belongs to user: laura_poitras",
                "The password is 18 characters, mixed case, symbols, numbers.",
                "",
                "Your task: confirm this hash CANNOT be cracked in",
                "reasonable time by running john and observing the result.",
                "Hash saved at /tmp/hash3.txt"
            ],
            "correct_command": "john --format=bcrypt /tmp/hash3.txt",
            "acceptable_variants": [
                "john /tmp/hash3.txt",
                "john --format=bcrypt --wordlist=rockyou.txt /tmp/hash3.txt",
                "john --wordlist=rockyou.txt --format=bcrypt /tmp/hash3.txt",
                "john --wordlist=/usr/share/wordlists/rockyou.txt --format=bcrypt /tmp/hash3.txt"
            ],
            "success_output": [
                "Using default input encoding: UTF-8",
                "Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])",
                "Cost 1 (iteration count) is 4096 for all loaded hashes",
                "Press 'q' or Ctrl-C to abort",
                "",
                "0g 0:00:00:30 0.00% (ETA: 2051-03-14 06:00) 0g/s 12.33p/s",
                "0g 0:00:01:02 0.00% (ETA: 2051-03-14 06:00) 0g/s 12.31p/s",
                "",
                "^C",
                "Session aborted.",
                "",
                "[!] Estimated completion: year 2051.",
                "[!] This hash cannot be cracked in reasonable time.",
                "[!] bcrypt + strong password = computationally infeasible."
            ],
            "learn_text": [
                "# RESULT ANALYSIS:",
                "# bcrypt is intentionally slow — designed to resist brute force.",
                "# Cost factor 12 means 4096 hash computations per guess.",
                "# With salt, identical passwords produce different hashes.",
                "# Rainbow table attacks are completely defeated by salting.",
                "# A 18-character random password with bcrypt:",
                "#   GPU speed: ~12 guesses/second (vs millions for MD5)",
                "#   Time to crack: centuries",
                "# Use a password manager. Generate random 16+ char passwords.",
                "# bcrypt, scrypt, and Argon2 are the only acceptable",
                "# algorithms for storing passwords in 2024.",
                "",
                "[press ENTER to continue]"
            ]
        }
    ]

    def pw_backspace():
        if len(pw_game_state["current_input"]) > 0:
            pw_game_state["current_input"] = pw_game_state["current_input"][:-1]
            renpy.restart_interaction()
    def pw_add_line(text, color="#ffffff"):
        pw_game_state["lines"].append(TerminalLine(text, color=color))

    def pw_add_line_queued():
        if pw_game_state["queued_output"]:
            pw_add_line(pw_game_state["queued_output"].pop(0))

    def pw_add_learning_lines():
        pw_add_line("")
        for l in rounds_data[pw_game_state["round"]]["learn_text"]:
            pw_add_line(l)

    def pw_add_prompt():
        pw_add_line("┌──(snowden㉿nsa-laptop)-[~]", color="#ffffff")

    def pw_reset():
        pw_game_state["lines"] = []
        pw_game_state["current_input"] = ""
        pw_game_state["round"] = 0
        pw_game_state["wrong_attempts"] = 0
        pw_game_state["score"] = 0
        pw_game_state["tab_hint_used"] = False
        pw_game_state["status"] = "playing"
        pw_game_state["queued_output"] = []

        pw_add_line("Initializing hash analysis environment...")
        pw_add_line("Loading wordlists... done.")
        pw_add_line("Loading john the ripper... done.")
        pw_add_line("Session started. Good luck, Snowden.")
        pw_add_line("")

        pw_next_round()

    def pw_next_round():
        r = pw_game_state["round"]
        if r < 3:
            rd = rounds_data[r]
            for line in rd["intro"]:
                pw_add_line(line)
            pw_add_line("")
            pw_add_prompt()
            pw_game_state["wrong_attempts"] = 0
        else:
            pw_game_state["status"] = "report"
            pw_add_prompt()
            pw_add_line("└─$ cat session_report.txt")
            pw_add_line("")
            pw_add_line("SESSION REPORT — HASH CRACKING EXERCISE")
            pw_add_line("========================================")
            pw_add_line("Round 1: MD5 dictionary attack    [ COMPLETED ]")
            pw_add_line("Round 2: MD5 rules-based attack   [ COMPLETED ]")
            pw_add_line("Round 3: bcrypt analysis          [ COMPLETED ]")
            pw_add_line("")
            pw_add_line(f"Score: {pw_game_state['score']}/3 rounds completed correctly.")
            pw_add_line("")
            pw_add_line("KEY TAKEAWAYS:")
            pw_add_line("1. MD5 with no salt is broken. Never use it for passwords.")
            pw_add_line("2. Character substitutions on weak words offer no protection.")
            pw_add_line("3. bcrypt + long random password = practically uncrackable.")
            pw_add_line("4. Use a password manager: Bitwarden, KeePassXC.")
            pw_add_line("")
            pw_add_prompt()
            pw_add_line("> type 'exit' to continue mission")

    def pw_check_command():
        inp = pw_game_state["current_input"].strip()
        pw_game_state["current_input"] = ""

        if pw_game_state["status"] == "report":
            if inp.lower() == "exit" or inp == "":
                return "EXIT"
            else:
                pw_add_line("└─$ " + inp)
                if inp:
                    pw_add_line("command not found: " + inp, color="#ff0000")
                pw_add_line("> type 'exit' to continue mission")
                pw_add_prompt()
            return

        if pw_game_state["status"] == "learning":
            pw_game_state["round"] += 1
            pw_game_state["status"] = "playing"
            pw_add_line("")
            pw_next_round()
            return

        if pw_game_state["status"] != "playing":
            return

        r = pw_game_state["round"]
        if r >= 3:
            return

        if inp == "":
            pw_add_line("└─$ ")
            pw_add_prompt()
            return

        rd = rounds_data[r]
        variants = rd["acceptable_variants"] + [rd["correct_command"]]

        norm_inp = " ".join(inp.split())

        is_correct = False
        for var in variants:
            if norm_inp == " ".join(var.split()):
                is_correct = True
                break

        pw_add_line("└─$ " + inp, color="#00ff00" if is_correct else "#ffffff")

        if is_correct:
            if pw_game_state["wrong_attempts"] < 3:
                pw_game_state["score"] += 1

            pw_game_state["status"] = "outputting"
            pw_game_state["queued_output"] = list(rd["success_output"])
        else:
            pw_game_state["wrong_attempts"] += 1
            cmd_base = norm_inp.split()[0] if norm_inp else ""

            if cmd_base == "hashcat":
                pw_add_line("hashcat: command not found. Try john the ripper.", color="#ff0000")
            elif cmd_base == "crack":
                pw_add_line("crack: command not found.", color="#ff0000")
            else:
                pw_add_line(f"command not found: {inp}", color="#ff0000")

            wa = pw_game_state["wrong_attempts"]

            if wa == 2:
                correct_first_word = rd["correct_command"].split()[0]
                pw_add_line(f"HINT: try '{correct_first_word} ...'")
            elif wa >= 3:
                pw_add_line(f"# suggested: {rd['correct_command']}")

            pw_add_line("")
            pw_add_prompt()

    def pw_autocomplete():
        if pw_game_state["status"] not in ["playing", "report"]:
            return

        inp = pw_game_state["current_input"]
        if pw_game_state["status"] == "report":
            if "exit".startswith(inp.lower()) and len(inp) >= 1:
                pw_game_state["current_input"] = "exit"
            renpy.restart_interaction()
            return

        r = pw_game_state["round"]
        if r >= 3: return

        target = rounds_data[r]["correct_command"]

        if target.startswith(inp) and len(inp) >= 3:
            pw_game_state["current_input"] = target
            pw_game_state["tab_hint_used"] = True
            renpy.restart_interaction()

    def pw_apply_results():
        global knowledge_score, suspicion_level, evidence_secured
        score = pw_game_state["score"]
        if score >= 2:
            knowledge_score += 2
            evidence_secured = True
            renpy.notify("knowledge +2")
        elif score == 1:
            knowledge_score += 1
        else:
            suspicion_level += 1

    def pw_refresh_if_needed():
        now = time.time()
        needs_refresh = False
        for l in pw_game_state["lines"]:
            if l.color in ["#ff0000", "#00ff00"] and not l.expired:
                if now - l.timestamp > 1.5:
                    l.expired = True
                    needs_refresh = True
        if needs_refresh:
            renpy.restart_interaction()

image terminal_caret:
    Text("_", font=FONT_MONO, size=17, color="#ffffff")
    pause 0.5
    Text(" ", font=FONT_MONO, size=17, color="#ffffff")
    pause 0.5
    repeat

transform blink_underscore:
    alpha 1.0
    linear 0.0
    pause 0.5
    alpha 0.0
    linear 0.0
    pause 0.5
    repeat

screen minigame_3_main():
    style_prefix "terminal"

    frame:
        style "terminal_screen_bg"
        xfill True
        yfill True

        add "gui/logo.png" alpha 0.07 xalign 0.5 yalign 0.5 zoom 1.0

        if pw_game_state["status"] == "outputting":
            timer 0.08 repeat True action If(
                len(pw_game_state["queued_output"]) > 0,
                true=[Function(pw_add_line_queued)],
                false=[
                    SetDict(pw_game_state, "status", "learning"),
                    Function(pw_add_learning_lines)
                ]
            )

        timer 0.1 repeat True action Function(pw_refresh_if_needed)

        vbox:
            xfill True
            yfill True

            viewport id "terminal_vp":
                yfill True
                xfill True
                yinitial 1.0
                mousewheel True

                vbox:
                    xfill True
                    yalign 1.0

                    for line in pw_game_state["lines"]:
                        if line.color == "#00ff00" and not line.expired:
                            text line.text style "terminal_correct_line" substitute False
                        elif line.color == "#ff0000" and not line.expired:
                            text line.text style "terminal_error_line" substitute False
                        else:
                            text line.text style "terminal_text" substitute False

                    if pw_game_state["status"] in ["playing", "report"]:
                        hbox:
                            text "└─$ " style "terminal_text"
                            input value TerminalInputValue() style "terminal_input_text" caret "terminal_caret"
                    elif pw_game_state["status"] == "learning":
                        hbox:
                            text "└─$ " style "terminal_text"
                            add "terminal_caret" yalign 1.0
                    elif pw_game_state["status"] == "outputting":
                        hbox:
                            text "└─$ " style "terminal_text"

        if pw_game_state["status"] in ["playing", "report"]:
            key "K_TAB" action Function(pw_autocomplete)
            key "K_BACKSPACE" action Function(pw_backspace)

            if pw_game_state["current_input"] and len(pw_game_state["current_input"]) >= 3 and not pw_game_state["tab_hint_used"]:
                text "Press TAB to autocomplete" xalign 0.5 yalign 0.95 color "#888888" size 14 font FONT_MONO

        if pw_game_state["status"] == "learning":
            key "K_RETURN" action Function(pw_check_command)
            key "K_KP_ENTER" action Function(pw_check_command)

    use block_shortcuts_and_skip("SKIP")

label minigame_3_brute_force:
    python:
        pw_reset()

    call screen minigame_3_main

    if _return == "SKIP":
        return "SKIP"

    return pw_game_state["score"]
