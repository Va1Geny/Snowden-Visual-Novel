################################################################################
# MINIGAMES.RPY â€” All Minigame Logic and Screens
# Classified: The Snowden Files
################################################################################

################################################################################
# MINIGAME INTRO / RESULT SCREENS
################################################################################

# === Minigame Intro Splash ===
screen block_shortcuts_and_skip(return_value="SKIP", show_skip_button=True):
    zorder 100
    
    key "rollback" action NullAction()
    key "rollforward" action NullAction()
    key "ctrl_K_i" action NullAction()
    key "ctrl_K_n" action NullAction()

    if show_skip_button:
        textbutton t("SKIP MINIGAME"):
            xalign 0.98
            yalign 0.02
            text_size 16
            text_color "#ff4444"
            text_hover_color "#ff0000"
            background Solid("#00000088")
            padding (10, 5)
            action Return(return_value)

screen minigame_intro(title, description):
    modal True
    key "rollback" action NullAction()
    key "K_BACKSPACE" action NullAction()
    add "#0A0E1ACC"

    frame:
        xalign 0.5 yalign 0.5
        xsize 900 ysize 500
        background "#0A0E1A"
        padding(40, 40)

        vbox:
            xalign 0.5 yalign 0.5
            spacing 30

            text t("// SYSTEM CHALLENGE INITIATED //") style "sys_text"
            text title style "minigame_title"
            text description style "minigame_instruction"

            null height 20

            textbutton t("> BEGIN CHALLENGE"):
                xalign 0.5
                text_style "menu_btn_text"
                action Return(True)

            textbutton t("> SKIP (Knowledge -1)"):
                xalign 0.5
                text_color "#FF2D55"
                text_size 18
                action Return(False)


# === Minigame Result ===
screen minigame_result(passed, title, explanation):
    modal True
    key "rollback" action NullAction()
    key "K_BACKSPACE" action NullAction()
    add "#0A0E1ACC"

    frame:
        xalign 0.5 yalign 0.5
        xsize 900 ysize 500
        background "#0A0E1A"
        padding(40, 40)

        vbox:
            xalign 0.5 yalign 0.5
            spacing 20

            if passed:
                text t("// CHALLENGE PASSED //") color "#00FFD1" size 28 bold True xalign 0.5
                text title color "#00FFD1" size 36 bold True xalign 0.5
            else:
                text t("// CHALLENGE FAILED //") color "#FF2D55" size 28 bold True xalign 0.5
                text title color "#FF2D55" size 36 bold True xalign 0.5

            null height 10
            text explanation color "#CCCCCC" size 20 xalign 0.5 text_align 0.5

            null height 20

            textbutton t("> CONTINUE MISSION"):
                xalign 0.5
                text_style "menu_btn_text"
                action Return()


################################################################################
# MINIGAME 1: FIREWALL BREACH (Chapter 1) â€” REDESIGNED
# Cinematic NSA Workstation-style packet analysis minigame
################################################################################

init python:
    import time as _time

    # â”€â”€ Packet Data â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    def get_fw_packets():
        return [
            {
                "source_ip": "192.168.1.10", "port": 80, "protocol": "HTTP",
                "description": "Web Browser Request", "correct": "ALLOW",
                "risk_level": "LOW",
                "explanation": "Port 80 is standard HTTP web traffic from an internal IP. This is normal network activity â€” safe to allow."
            },
            {
                "source_ip": "10.0.0.5", "port": 443, "protocol": "HTTPS",
                "description": "Encrypted Web Traffic", "correct": "ALLOW",
                "risk_level": "LOW",
                "explanation": "Port 443 is HTTPS â€” secure, encrypted web traffic. Standard and safe."
            },
            {
                "source_ip": "45.33.32.1", "port": 31337, "protocol": "TCP",
                "description": "Unknown Connection", "correct": "BLOCK",
                "risk_level": "CRITICAL",
                "explanation": "Port 31337 is infamous in hacking culture (pronounced 'elite'). Used historically by Back Orifice malware. Always block unknown external IPs on this port."
            },
            {
                "source_ip": "172.16.0.1", "port": 22, "protocol": "SSH",
                "description": "Remote Login â€” Internal", "correct": "ALLOW",
                "risk_level": "MEDIUM",
                "explanation": "SSH on port 22 from a known internal IP (172.16.x.x is a private range) is a legitimate remote administration session."
            },
            {
                "source_ip": "89.248.174.5", "port": 4444, "protocol": "TCP",
                "description": "Suspicious Inbound", "correct": "BLOCK",
                "risk_level": "CRITICAL",
                "explanation": "Port 4444 is the default listener port for Metasploit â€” a common hacking framework. Foreign IP + port 4444 = almost certainly a reverse shell attempt. Block immediately."
            },
            {
                "source_ip": "10.0.0.12", "port": 53, "protocol": "DNS",
                "description": "Domain Name Lookup", "correct": "ALLOW",
                "risk_level": "LOW",
                "explanation": "DNS on port 53 from an internal IP is completely normal â€” computers need DNS to look up domain names and connect to websites."
            },
            {
                "source_ip": "203.0.113.99", "port": 23, "protocol": "Telnet",
                "description": "Legacy Protocol Connection", "correct": "BLOCK",
                "risk_level": "HIGH",
                "explanation": "Telnet sends ALL data in plain text â€” no encryption at all. It's outdated and dangerous. From a foreign IP, this is a clear intrusion attempt. Use SSH instead."
            },
            {
                "source_ip": "192.168.1.1", "port": 3389, "protocol": "RDP",
                "description": "Remote Desktop â€” Router", "correct": "ALLOW",
                "risk_level": "MEDIUM",
                "explanation": "RDP on port 3389 from the internal router IP (192.168.1.1) is internal remote desktop. Acceptable from a trusted internal source."
            },
        ]

    # â”€â”€ Timer Class â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    class PacketTimer(object):
        def __init__(self, max_time=15.0):
            self.max_time = max_time
            self.start_time = None
            self.active = False

        def start(self, max_time=None):
            if max_time is not None:
                self.max_time = max_time
            self.start_time = _time.time()
            self.active = True

        def stop(self):
            self.active = False

        def get_remaining(self):
            if not self.active or self.start_time is None:
                return self.max_time
            elapsed = _time.time() - self.start_time
            return max(0.0, self.max_time - elapsed)

        def get_fraction(self):
            return self.get_remaining() / self.max_time

        def is_expired(self):
            return self.active and self.get_remaining() <= 0

    packet_timer = PacketTimer()

    # â”€â”€ Game State â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    fw_state = {
        "phase": "incoming",
        "current_index": 0,
        "score": 0,
        "streak": 0,
        "allowed_count": 0,
        "blocked_count": 0,
        "answers": [],
        "last_correct": False,
        "timed_out": False,
        "show_continue": False,
    }

    def fw_reset():
        fw_state["phase"] = "incoming"
        fw_state["current_index"] = 0
        fw_state["score"] = 0
        fw_state["streak"] = 0
        fw_state["allowed_count"] = 0
        fw_state["blocked_count"] = 0
        fw_state["answers"] = []
        fw_state["last_correct"] = False
        fw_state["timed_out"] = False
        fw_state["show_continue"] = False
        packet_timer.start(fw_current_time_limit())

    def fw_evaluate(choice):
        pkts = get_fw_packets()
        idx = fw_state["current_index"]
        pkt = pkts[idx]
        is_correct = (choice == pkt["correct"])
        fw_state["answers"].append({
            "choice": choice,
            "correct_answer": pkt["correct"],
            "is_correct": is_correct,
        })
        if is_correct:
            fw_state["score"] += 1
            fw_state["streak"] += 1
        else:
            fw_state["streak"] = 0
        if choice == "ALLOW":
            fw_state["allowed_count"] += 1
        else:
            fw_state["blocked_count"] += 1
        fw_state["last_correct"] = is_correct
        fw_state["phase"] = "feedback"
        fw_state["show_continue"] = False
        packet_timer.stop()
        renpy.restart_interaction()

    def fw_handle_timeout():
        if fw_state["phase"] != "incoming":
            return
        fw_state["timed_out"] = True
        pkts = get_fw_packets()
        idx = fw_state["current_index"]
        pkt = pkts[idx]
        is_correct = ("BLOCK" == pkt["correct"])
        fw_state["answers"].append({
            "choice": "BLOCK",
            "correct_answer": pkt["correct"],
            "is_correct": is_correct,
        })
        if is_correct:
            fw_state["score"] += 1
            fw_state["streak"] += 1
        else:
            fw_state["streak"] = 0
        fw_state["blocked_count"] += 1
        fw_state["last_correct"] = is_correct
        fw_state["phase"] = "feedback"
        fw_state["show_continue"] = False
        packet_timer.stop()
        renpy.restart_interaction()

    def fw_next_packet():
        fw_state["current_index"] += 1
        fw_state["timed_out"] = False
        fw_state["show_continue"] = False
        if fw_state["current_index"] >= 8:
            fw_state["phase"] = "complete"
        else:
            fw_state["phase"] = "incoming"
            packet_timer.start(fw_current_time_limit())
        renpy.restart_interaction()

    def fw_show_continue():
        fw_state["show_continue"] = True
        renpy.restart_interaction()

    def fw_risk_color(level):
        if level == "LOW":
            return "#00FF88"
        elif level == "MEDIUM":
            return "#FFD700"
        elif level == "HIGH":
            return "#FF8C00"
        elif level == "CRITICAL":
            return "#FF2D55"
        return "#888888"

    def fw_get_grade(score):
        if score >= 7:
            return ("EXPERT ANALYST", 3)
        elif score >= 5:
            return ("ANALYST", 2)
        elif score >= 3:
            return ("TRAINEE", 1)
        else:
            return ("COMPROMISED", 0)

    def fw_timer_color():
        f = packet_timer.get_fraction()
        if f > 0.5:
            return "#00FFD1"
        elif f > 0.25:
            return "#FFD700"
        else:
            return "#FF2D55"

    def fw_current_time_limit():
        limits = [20.0, 19.0, 18.0, 17.0, 16.0, 15.0, 14.0, 14.0]
        idx = max(0, min(fw_state["current_index"], len(limits) - 1))
        return limits[idx]

    def fw_packet_tag(packet):
        protocol_tags = {
            "HTTP": "WEB REQUEST",
            "HTTPS": "ENCRYPTED SESSION",
            "TCP": "RAW TCP HANDSHAKE",
            "SSH": "REMOTE ACCESS",
            "DNS": "NAME RESOLUTION",
            "Telnet": "LEGACY TERMINAL",
            "RDP": "REMOTE DESKTOP",
        }
        return protocol_tags.get(packet["protocol"], "UNCLASSIFIED FLOW")

# â”€â”€ ATL Transforms â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

transform fw_packet_enter:
    xoffset 600 alpha 0.0
    ease 0.45 xoffset 0 alpha 1.0

transform fw_packet_exit_allow:
    ease 0.35 xoffset - 700 alpha 0.0 zoom 0.92

transform fw_packet_exit_block:
    linear 0.06 xoffset 14
    linear 0.06 xoffset - 14
    linear 0.06 xoffset 10
    linear 0.06 xoffset - 10
    linear 0.04 xoffset 0
    ease 0.3 alpha 0.0 zoom 0.88

transform fw_threat_blink:
    alpha 1.0
    linear 0.5 alpha 0.4
    linear 0.5 alpha 1.0
    repeat

transform fw_cursor_blink:
    alpha 1.0
    linear 0.4 alpha 0.0
    linear 0.4 alpha 1.0
    repeat

transform fw_fade_in:
    alpha 0.0
    ease 0.5 alpha 1.0

transform fw_feedback_enter:
    yoffset 30 alpha 0.0
    ease 0.35 yoffset 0 alpha 1.0

transform fw_result_enter:
    alpha 0.0 zoom 0.95
    ease 0.6 alpha 1.0 zoom 1.0

transform fw_title_enter:
    alpha 0.0 yoffset - 20
    pause 0.2
    ease 0.5 alpha 1.0 yoffset 0

transform fw_subtitle_enter:
    alpha 0.0
    pause 0.7
    ease 0.4 alpha 1.0

transform fw_tagline_enter:
    alpha 0.0
    pause 1.1
    ease 0.4 alpha 1.0

transform fw_btn_enter:
    alpha 0.0
    pause 1.5
    ease 0.3 alpha 1.0


# â”€â”€ Main Firewall Minigame Screen â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

screen minigame_firewall():
    modal True
    key "rollback" action NullAction()
    key "K_BACKSPACE" action NullAction()

    # Reset state on first show
    on "show" action Function(fw_reset)

    add "#0A0E1A"

    add "images/logo.png":
        xalign 0.5
        yalign 0.5
        alpha 0.15
        fit "contain"
        xsize 900
        ysize 900

    # â”€â”€ Scanline overlay (subtle) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    for _sl_y in range(0, 720, 4):
        add Solid("#00000010"):
            xsize 1280 ysize 1
            xpos 0 ypos _sl_y

    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    #  PHASE: INCOMING / FEEDBACK (main gameplay)
    #  (Intro/skip is handled by the existing minigame_intro screen)
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    if fw_state["phase"] in ("incoming", "feedback"):

        # Timer tick â€” refresh display for timer bar
        if fw_state["phase"] == "incoming":
            timer 0.1 repeat True action Function(renpy.restart_interaction)
            timer fw_current_time_limit() action Function(fw_handle_timeout)

        # Feedback continue delay
        if fw_state["phase"] == "feedback" and not fw_state["show_continue"]:
            timer 1.5 action Function(fw_show_continue)

        $ _fw_pkts = get_fw_packets()
        $ _fw_idx = fw_state["current_index"]
        $ _fw_pkt = _fw_pkts[_fw_idx]
        $ _fw_ip = _fw_pkt["source_ip"]
        $ _fw_port = str(_fw_pkt["port"])
        $ _fw_proto = _fw_pkt["protocol"]
        $ _fw_desc = _fw_pkt["description"]
        $ _fw_explanation = _fw_pkt["explanation"]
        $ _fw_correct = _fw_pkt["correct"]
        $ _fw_remaining = packet_timer.get_remaining()
        $ _fw_frac = packet_timer.get_fraction()
        $ _fw_timer_col = fw_timer_color()
        $ _fw_num = _fw_idx + 1
        $ _fw_score = fw_state["score"]
        $ _fw_streak = fw_state["streak"]
        $ _fw_tag = fw_packet_tag(_fw_pkt)

        # â”€â”€ TOP HUD BAR â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
        frame:
            xfill True ysize 100
            xpos 0 ypos 0
            background "#0D1220EE"
            padding(30, 12)

            vbox:
                spacing 6

                # Title row
                hbox:
                    xfill True
                    text t("// NSA NETWORK MONITOR //") color "#00FFD180" size 14 bold True yalign 0.5

                    hbox:
                        xalign 1.0
                        spacing 20
                        text t("STREAK: [_fw_streak]") color "#FFD700" size 14 bold True yalign 0.5
                        text t("AUTHORIZED: [fw_state['allowed_count']]") color "#00FFD1" size 14 bold True yalign 0.5
                        text t("BLOCKED: [fw_state['blocked_count']]") color "#FF2D55" size 14 bold True yalign 0.5
                        text t("SCORE: [_fw_score]") color "#E8E8E8" size 14 bold True yalign 0.5

                # Progress dots
                hbox:
                    spacing 8
                    for _dot_i in range(8):
                        if _dot_i < _fw_idx:
                            # Completed
                            $ _dot_ans = fw_state["answers"][_dot_i] if _dot_i < len(fw_state["answers"]) else None
                            if _dot_ans and _dot_ans["is_correct"]:
                                text t("â—") color "#00FFD1" size 18
                            else:
                                text t("â—") color "#FF2D55" size 18
                        elif _dot_i == _fw_idx:
                            text t("â—†") color "#FFD700" size 18
                        else:
                            text t("â—‹") color "#555555" size 18

                    null width 20
                    text t("PACKET [_fw_num] / 8") color "#888888" size 14 yalign 0.5

                # Timer bar
                if fw_state["phase"] == "incoming":
                    frame:
                        xfill True ysize 6
                        background "#1A1A2E"
                        padding(0, 0)

                        frame:
                            xsize int(1220 * _fw_frac)
                            ysize 6
                            background _fw_timer_col
                            xpos 0

                    $ _fw_secs = int(_fw_remaining)
                    text t("[_fw_secs]s") color _fw_timer_col size 12 xalign 1.0
                else:
                    frame:
                        xfill True ysize 6
                        background "#1A1A2E"
                        padding(0, 0)

        # â”€â”€ PACKET CARD â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
        # Use showif per packet index to trigger enter animation on change
        for _pc_i in range(8):
            showif fw_state["current_index"] == _pc_i and fw_state["phase"] in ("incoming", "feedback"):
                frame at fw_packet_enter:
                    xalign 0.5 yalign 0.42
                    xsize 820 ysize 280
                    background "#131928"
                    padding(0, 0)

                    # Outer border
                    add Solid("#00FFD120"):
                        xsize 820 ysize 1 xpos 0 ypos 0
                    add Solid("#00FFD120"):
                        xsize 820 ysize 1 xpos 0 ypos 279
                    add Solid("#00FFD120"):
                        xsize 1 ysize 280 xpos 0 ypos 0
                    add Solid("#00FFD120"):
                        xsize 1 ysize 280 xpos 819 ypos 0

                    # Corner brackets
                    text t("â—¢") color "#00FFD140" size 14 xpos 6 ypos 2
                    text t("â—£") color "#00FFD140" size 14 xpos 798 ypos 2
                    text t("â—¤") color "#00FFD140" size 14 xpos 6 ypos 258
                    text t("â—¥") color "#00FFD140" size 14 xpos 798 ypos 258

                    vbox:
                        pos(0, 0)
                        xsize 820

                        # Signature bar at top
                        $ _pc_pkts = get_fw_packets()
                        $ _pc_pkt = _pc_pkts[_pc_i]
                        $ _pc_tag = fw_packet_tag(_pc_pkt)

                        hbox:
                            xfill True ysize 32
                            spacing 0

                            frame:
                                xsize 240 ysize 32
                                background "#1A2440"
                                padding(10, 4)
                                text t("SIGNATURE") color "#C9D0F3" size 13 bold True yalign 0.5

                            frame:
                                xfill True ysize 32
                                background "#0D1220"
                                padding(15, 4)
                                text t("[_pc_tag]") color "#8B8FCC" size 14 bold True yalign 0.5

                        null height 20

                        # Data fields
                        hbox:
                            xfill True
                            spacing 0

                            # Source IP column
                            vbox:
                                xsize 320
                                xalign 0.0
                                spacing 4
                                xoffset 30
                                text t("SOURCE IP") color "#888888" size 12 bold True
                                $ _pc_ip = _pc_pkt["source_ip"]
                                text t("[_pc_ip]") color "#00FFD1" size 26 bold True

                            # Port column
                            vbox:
                                xsize 200
                                spacing 4
                                text t("PORT") color "#888888" size 12 bold True
                                $ _pc_port = str(_pc_pkt["port"])
                                text t("[_pc_port]") color "#FFD700" size 30 bold True

                            # Protocol column
                            vbox:
                                xsize 250
                                spacing 4
                                text t("PROTOCOL") color "#888888" size 12 bold True
                                $ _pc_proto = _pc_pkt["protocol"]
                                text t("[_pc_proto]") color "#E8E8E8" size 26 bold True

                        null height 20

                        # Description line
                        hbox:
                            xoffset 30
                            text t("CLASSIFICATION: ") color "#555555" size 14
                            $ _pc_desc2 = _pc_pkt["description"]
                            text t("[_pc_desc2]") color "#888888" size 14 italic True

                        # Feedback overlay on card
                        if fw_state["phase"] == "feedback" and fw_state["current_index"] == _pc_i:
                            null height 15
                            hbox:
                                xoffset 30
                                if fw_state["last_correct"]:
                                    text t("âœ“ CORRECT ANALYSIS") color "#00FF88" size 16 bold True
                                else:
                                    text t("âœ— INCORRECT ANALYSIS") color "#FF2D55" size 16 bold True

        # â”€â”€ ACTION BUTTONS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
        if fw_state["phase"] == "incoming":
            hbox at fw_fade_in:
                xalign 0.5 yalign 0.72
                spacing 60

                # ALLOW button
                frame:
                    xsize 220 ysize 70
                    background "#0D1220"
                    padding(0, 0)

                    # Border
                    add Solid("#00FFD140"):
                        xsize 220 ysize 1 xpos 0 ypos 0
                    add Solid("#00FFD140"):
                        xsize 220 ysize 1 xpos 0 ypos 69
                    add Solid("#00FFD140"):
                        xsize 1 ysize 70 xpos 0 ypos 0
                    add Solid("#00FFD140"):
                        xsize 1 ysize 70 xpos 219 ypos 0

                    textbutton t("âœ“  ALLOW"):
                        xalign 0.5 yalign 0.5
                        text_color "#00FFD1"
                        text_hover_color "#FFFFFF"
                        text_size 22
                        text_bold True
                        action Function(fw_evaluate, "ALLOW")

                # BLOCK button
                frame:
                    xsize 220 ysize 70
                    background "#0D1220"
                    padding(0, 0)

                    add Solid("#FF2D5540"):
                        xsize 220 ysize 1 xpos 0 ypos 0
                    add Solid("#FF2D5540"):
                        xsize 220 ysize 1 xpos 0 ypos 69
                    add Solid("#FF2D5540"):
                        xsize 1 ysize 70 xpos 0 ypos 0
                    add Solid("#FF2D5540"):
                        xsize 1 ysize 70 xpos 219 ypos 0

                    textbutton t("âœ—  BLOCK"):
                        xalign 0.5 yalign 0.5
                        text_color "#FF2D55"
                        text_hover_color "#FFFFFF"
                        text_size 22
                        text_bold True
                        action Function(fw_evaluate, "BLOCK")

        # â”€â”€ ANALYSIS TERMINAL (feedback) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
        if fw_state["phase"] == "feedback":
            frame at fw_feedback_enter:
                xalign 0.5 yalign 0.5
                xsize 642 ysize 282
                background "#00FFD130"
                padding(1, 1)

                frame:
                    xsize 640 ysize 280
                    background "#0A0A14E6"
                    padding(29, 19)

                    vbox:
                        spacing 10
                        xalign 0.5

                        # Terminal header
                        text t("> ANALYSIS TERMINAL <") color "#00FFD180" size 14 bold True xalign 0.5

                        if fw_state["timed_out"]:
                            text t("{cps=40}âš  TIME OUT â€” Packet auto-blocked{/cps}") color "#FFD700" size 16 bold True xalign 0.5
                        elif fw_state["last_correct"]:
                            $ _fb_choice = fw_state["answers"][-1]["choice"]
                            if _fb_choice == "ALLOW":
                                text t("{cps=40}âœ“ AUTHORIZATION GRANTED{/cps}") color "#00FF88" size 18 bold True xalign 0.5
                            else:
                                text t("{cps=40}âœ— PACKET REJECTED{/cps}") color "#00FFD1" size 18 bold True xalign 0.5
                        else:
                            text t("{cps=40}âš  INCORRECT ANALYSIS{/cps}") color "#FF2D55" size 18 bold True xalign 0.5

                        # Explanation
                        text t("{cps=30}[_fw_explanation]{/cps}") color "#AAAAAA" size 15 text_align 0.5 xalign 0.5 justify True

                        if fw_state["last_correct"] and not fw_state["timed_out"]:
                            text t("knowledge_score +1 | streak [_fw_streak]") color "#00FF8880" size 13 xalign 0.5

                        null height 5

                        # Continue button (delayed)
                        if fw_state["show_continue"]:
                            textbutton t("> CONTINUE â†’"):
                                xalign 0.5
                                text_color "#00FFD1"
                                text_hover_color "#FFFFFF"
                                text_size 16
                                text_bold True
                                action Function(fw_next_packet)
                        else:
                            hbox:
                                xalign 0.5
                                text t("> Processing") color "#00FFD180" size 14
                                text t(" _") at fw_cursor_blink color "#00FFD1" size 14

        # â”€â”€ Waiting prompt (incoming phase) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
        if fw_state["phase"] == "incoming":
            frame:
                xalign 0.5 yalign 0.82
                xsize 820 ysize 50
                background "#0A0A14"
                padding(20, 12)

                add Solid("#00FFD120"):
                    xsize 820 ysize 1 xpos 0 ypos 0

                hbox:
                    text t("> Scanning packet... Awaiting your authorization") color "#00FFD160" size 14
                    text t(" _") at fw_cursor_blink color "#00FFD1" size 14

<<<<<<< HEAD
    use block_shortcuts_and_skip("SKIP")

    # ══════════════════════════════════════════════════════════════════════
=======
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
>>>>>>> b487fec (added the proper UI for the input menu, fixed some visual bugs that were occuring before)
    #  PHASE: COMPLETE (Result / Mission Debrief)
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    if fw_state["phase"] == "complete":
        $ _r_score = fw_state["score"]
        $ _r_allowed = fw_state["allowed_count"]
        $ _r_blocked = fw_state["blocked_count"]
        $ _r_grade, _r_bonus = fw_get_grade(_r_score)
        $ _r_answers = fw_state["answers"]

        frame at fw_result_enter:
            xfill True yfill True
            background "#0A0E1A"
            padding(40, 20)

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 10

                text t("// FIREWALL ANALYSIS COMPLETE //") color "#00FFD1" size 28 bold True xalign 0.5 text_align 0.5

                # Mission outcome panel (compact)
                frame:
                    xalign 0.5 xsize 700
                    background "#131928"
                    padding(25, 15)

                    vbox:
                        spacing 6

                        text t("MISSION OUTCOME") color "#E8E8E8" size 18 bold True xalign 0.5

                        hbox:
                            xfill True
                            text t("Correctly Handled:") color "#AAAAAA" size 15
                            text t("[_r_score] / 8") color "#00FFD1" size 15 bold True xalign 1.0

                        hbox:
                            xfill True
                            text t("Allowed: [_r_allowed]   |   Blocked: [_r_blocked]") color "#888888" size 14

                        hbox:
                            xfill True
                            text t("Knowledge Bonus:") color "#888888" size 15
                            text t("+[_r_bonus]") color "#FFD700" size 15 bold True xalign 1.0

                # Grade display
                text t("GRADE:") color "#888888" size 14 xalign 0.5

                if _r_score >= 7:
                    text t("[_r_grade]") color "#00FF88" size 32 bold True xalign 0.5
                elif _r_score >= 5:
                    text t("[_r_grade]") color "#00FFD1" size 32 bold True xalign 0.5
                elif _r_score >= 3:
                    text t("[_r_grade]") color "#FFD700" size 32 bold True xalign 0.5
                else:
                    text t("[_r_grade]") color "#FF2D55" size 32 bold True xalign 0.5

                # Per-packet breakdown (scrollable)
                frame:
                    xalign 0.5 xsize 700
                    background "#0D1220"
                    padding(15, 10)

                    viewport:
                        xfill True ysize 200
                        mousewheel True
                        scrollbars "vertical"

                        vbox:
                            spacing 4
                            text t("â”€â”€â”€ PACKET LOG â”€â”€â”€") color "#00FFD160" size 12 bold True

                            $ _r_pkts = get_fw_packets()
                            for _ri in range(8):
                                $ _rpkt = _r_pkts[_ri]
                                $ _rans = _r_answers[_ri] if _ri < len(_r_answers) else None

                                hbox:
                                    spacing 8
                                    if _rans and _rans["is_correct"]:
                                        text t("âœ“") color "#00FF88" size 13 yalign 0.5
                                    else:
                                        text t("âœ—") color "#FF2D55" size 13 yalign 0.5

                                    $ _r_ip = _rpkt["source_ip"]
                                    $ _r_pt = str(_rpkt["port"])
                                    $ _r_pr = _rpkt["protocol"]
                                    text t("[_r_ip]:[_r_pt]") color "#00FFD1" size 12 yalign 0.5 xsize 180
                                    text t("[_r_pr]") color "#E8E8E8" size 12 yalign 0.5 xsize 70

                                    if _rans:
                                        $ _r_ch = _rans["choice"]
                                        $ _r_co = _rans["correct_answer"]
                                        if _rans["is_correct"]:
                                            text t("[_r_ch]") color "#00FF88" size 12 yalign 0.5
                                        else:
                                            text t("[_r_ch] (should: [_r_co])") color "#FF2D55" size 12 yalign 0.5

                # Key takeaway (compact)
                frame:
                    xalign 0.5 xsize 700
                    background "#131928"
                    padding(15, 10)

                    vbox:
                        spacing 4
                        text t("Dangerous ports: 31337, 4444, 23 (Telnet)") color "#FF2D55" size 13
                        text t("Safe: HTTP(80), HTTPS(443), DNS(53), SSH/RDP from internal IPs") color "#00FF88" size 13

                null height 5

                # CONTINUE button â€” always visible at bottom
                textbutton t("> CONTINUE MISSION"):
                    xalign 0.5
                    text_color "#00FFD1"
                    text_hover_color "#FFFFFF"
                    text_size 22
                    text_bold True
                    action Return(_r_score)
    key "K_BACKSPACE" action NullAction()
    key "mouseup_3" action NullAction()


################################################################################
# MINIGAME 2: DECRYPT THE MESSAGE (Chapter 2)
################################################################################

init python:
    import random
    import time

    caesar_map = {
        "A": "X", "B": "Y", "C": "Z",
        "D": "A", "E": "B", "F": "C",
        "G": "D", "H": "E", "I": "F",
        "J": "G", "K": "H", "L": "I",
        "M": "J", "N": "K", "O": "L",
        "P": "M", "Q": "N", "R": "O",
        "S": "P", "T": "Q", "U": "R",
        "V": "S", "W": "T", "X": "U",
        "Y": "V", "Z": "W"
    }

    decrypt_puzzles = [
        {
            "word": "PRISM",
            "encrypted": "SULVP",
            "difficulty": "EASY",
            "headline": "NSA PRISM INTERCEPT",
            "context": [
                "> PRISM was the codename for the NSA's secret",
                "  surveillance program that collected data from",
                "  internet companies including Google, Facebook,",
                "  and Apple. You revealed it in 2013."
            ],
            "hint": "This is the name of the surveillance program you risked everything to expose."
        },
        {
            "word": "ENCRYPTED",
            "encrypted": "HQFUBSWHG",
            "difficulty": "MEDIUM",
            "headline": "PGP CHANNEL ANALYSIS",
            "context": [
                "> To protect your communications, you used",
                "  ENCRYPTION â€” the process of scrambling data",
                "  so only the intended recipient can read it.",
                "  PGP encryption was his primary tool."
            ],
            "hint": "When data is scrambled to prevent unauthorized reading, it is ."
        },
        {
            "word": "SURVEILLANCE",
            "encrypted": "VXUYHLOODQFH",
            "difficulty": "HARD",
            "headline": "BULK COLLECTION DOSSIER",
            "context": [
                "> The NSA's mass program monitored the",
                "  phone calls, emails, and internet activity",
                "  of millions of people â€” most of whom were",
                "  never suspected of any crime."
            ],
            "hint": "Watching, monitoring, and tracking people's activities â€” what the NSA was doing."
        }
    ]

    decrypt_state = {
        "current_stage": 0,
        "total_score": 0,
        "stage_scores": [0, 0, 0],
        "stage_times": [0, 0, 0],
        "hints_used": [0, 0, 0],
        "stars_earned": [0, 0, 0],
        "letters_placed": [],
        "phase": "intro"
    }

    def decrypt_build_bg_streams():
        streams = []
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for _i in range(6):
            rows = []
            for _j in range(20):
                rows.append(" ".join(random.choice(letters)
                            for _k in range(14)))
            streams.append("\n".join(rows))
        return streams

    def decrypt_score_stars(score):
        return {
            3: u"â˜…â˜…â˜…",
            2: u"â˜…â˜…â˜†",
            1: u"â˜…â˜†â˜†",
            0: u"â˜†â˜†â˜†"
        }.get(score, u"â˜†â˜†â˜†")

    def decrypt_stage_rating(score):
        return {
            3: "Perfect",
            2: "Good",
            1: "Passed",
            0: "Assisted"
        }.get(score, "Incomplete")

    def decrypt_clearance_title(total):
        if total >= 8:
            return "LEVEL 3 â€” MASTER CRYPTOGRAPHER"
        elif total >= 6:
            return "LEVEL 2 â€” CRYPTOGRAPHER"
        elif total >= 4:
            return "LEVEL 1 â€” CIPHER ANALYST"
        return "UNCLEARED â€” Further training required"

    def decrypt_log(message, reset=False):
        if reset:
            decrypt_state["log_lines"] = []
        decrypt_state.setdefault("log_lines", []).append(message)
        decrypt_state["log_lines"] = decrypt_state["log_lines"][-8:]

    def decrypt_get_selected_position():
        letters = decrypt_state.get("letters_placed", [])
        puzzle = decrypt_puzzles[decrypt_state["current_stage"]]
        selected = decrypt_state.get("selected_position", None)

        if selected is not None and 0 <= selected < len(letters):
            return selected

        for idx, value in enumerate(letters):
            if value != puzzle["word"][idx]:
                return idx

        return 0

    def decrypt_record_activity():
        decrypt_state["last_input_at"] = time.time()
        decrypt_state["hint_flash_letter"] = None

    def decrypt_reset_stage(stage_index):
        puzzle = decrypt_puzzles[stage_index]
        decrypt_state["current_stage"] = stage_index
        decrypt_state["phase"] = "playing"
        decrypt_state["letters_placed"] = [""] * len(puzzle["word"])
        decrypt_state["revealed_positions"] = []
        decrypt_state["selected_position"] = 0
        decrypt_state["hover_letter"] = None
        decrypt_state["wrong_position"] = None
        decrypt_state["wrong_flash_serial"] = 0
        decrypt_state["word_complete_serial"] = 0
        decrypt_state["cursor_visible"] = True
        decrypt_state["wheel_angle"] = 0.0
        decrypt_state["bg_streams"] = decrypt_build_bg_streams()
        decrypt_state["stage_started_at"] = time.time()
        decrypt_state["last_input_at"] = time.time()
        decrypt_state["hint_flash_letter"] = None
        decrypt_state["attempts"] = decrypt_state.get("attempts", [0, 0, 0])
        decrypt_log(reset=True, message="")
        for line in puzzle["context"]:
            decrypt_log(line)
        decrypt_log("> Awaiting decryption input...")
        renpy.restart_interaction()

    def decrypt_reset_game():
        decrypt_state["current_stage"] = 0
        decrypt_state["total_score"] = 0
        decrypt_state["stage_scores"] = [0, 0, 0]
        decrypt_state["stage_times"] = [0, 0, 0]
        decrypt_state["hints_used"] = [0, 0, 0]
        decrypt_state["stars_earned"] = [0, 0, 0]
        decrypt_state["attempts"] = [0, 0, 0]
        decrypt_state["phase"] = "intro"
        decrypt_reset_stage(0)

    def decrypt_elapsed(stage_index=None):
        if stage_index is None:
            stage_index = decrypt_state["current_stage"]
        if decrypt_state["stage_times"][stage_index]:
            return int(decrypt_state["stage_times"][stage_index])
        started_at = decrypt_state.get("stage_started_at", time.time())
        return max(0, int(time.time() - started_at))

    def decrypt_set_hover_letter(letter):
        decrypt_state["hover_letter"] = letter
        decrypt_state["wheel_angle"] = - \
            (ord(letter) - ord("A")) * (360.0 / 26.0)
        renpy.restart_interaction()

    def decrypt_clear_hover_letter():
        decrypt_state["hover_letter"] = None
        renpy.restart_interaction()

    def decrypt_select_position(position):
        if decrypt_state["phase"] != "playing":
            return
        decrypt_state["selected_position"] = position
        puzzle = decrypt_puzzles[decrypt_state["current_stage"]]
        decrypt_state["wheel_angle"] = - \
            (ord(puzzle["encrypted"][position]) - ord("A")) * (360.0 / 26.0)
        decrypt_record_activity()
        renpy.restart_interaction()

    def decrypt_mark_wrong(position, message="> Incorrect. Try again."):
        decrypt_state["wrong_position"] = position
        decrypt_state["wrong_flash_serial"] += 1
        decrypt_state["selected_position"] = position
        decrypt_state["letters_placed"][position] = ""
        decrypt_log(message)
        renpy.restart_interaction()

    def decrypt_advance_selection():
        puzzle = decrypt_puzzles[decrypt_state["current_stage"]]
        for idx, value in enumerate(decrypt_state["letters_placed"]):
            if value != puzzle["word"][idx]:
                decrypt_state["selected_position"] = idx
                return
        decrypt_state["selected_position"] = len(puzzle["word"]) - 1

    def decrypt_place_letter(position, letter, source="keyboard"):
        if decrypt_state["phase"] != "playing":
            return

        puzzle = decrypt_puzzles[decrypt_state["current_stage"]]
        if position is None:
            position = decrypt_get_selected_position()

        if position < 0 or position >= len(puzzle["word"]):
            return

        decrypt_record_activity()

        if letter == puzzle["word"][position]:
            decrypt_state["letters_placed"][position] = letter
            decrypt_state["wrong_position"] = None
            decrypt_log("> " + puzzle["encrypted"]
                        [position] + " -> " + letter + " mapped.")
            decrypt_advance_selection()
            renpy.restart_interaction()
            decrypt_check_word()
            return

        decrypt_state["attempts"][decrypt_state["current_stage"]] += 1
        decrypt_mark_wrong(position)

    def decrypt_type_letter(letter):
        if decrypt_state["phase"] != "playing":
            return

        decrypt_place_letter(decrypt_get_selected_position(),
                             letter.upper(), source="hardware")

    def decrypt_use_cipher_letter(cipher_letter):
        if decrypt_state["phase"] != "playing":
            return

        puzzle = decrypt_puzzles[decrypt_state["current_stage"]]
        decrypt_set_hover_letter(cipher_letter)
        decrypt_record_activity()
        for idx, encrypted_letter in enumerate(puzzle["encrypted"]):
            if encrypted_letter == cipher_letter and decrypt_state["letters_placed"][idx] != puzzle["word"][idx]:
                decrypt_state["selected_position"] = idx
                decrypt_log("> Reference focus: " + cipher_letter +
                            " -> " + caesar_map[cipher_letter])
                renpy.restart_interaction()
                return

        decrypt_log("> Reference focus: " + cipher_letter +
                    " -> " + caesar_map[cipher_letter])
        renpy.restart_interaction()

    def decrypt_delete_letter():
        if decrypt_state["phase"] != "playing":
            return

        position = decrypt_state.get("selected_position", None)
        if position is not None and position not in decrypt_state.get("revealed_positions", []) and decrypt_state["letters_placed"][position]:
            decrypt_state["letters_placed"][position] = ""
            decrypt_log("> Entry cleared.")
        else:
            for idx in range(len(decrypt_state["letters_placed"]) - 1, -1, -1):
                if idx not in decrypt_state.get("revealed_positions", []) and decrypt_state["letters_placed"][idx]:
                    decrypt_state["letters_placed"][idx] = ""
                    decrypt_state["selected_position"] = idx
                    decrypt_log("> Entry cleared.")
                    break

        decrypt_record_activity()
        decrypt_state["wrong_position"] = None
        renpy.restart_interaction()

    def decrypt_give_hint():
        if decrypt_state["phase"] != "playing":
            return

        stage_index = decrypt_state["current_stage"]
        if decrypt_state["hints_used"][stage_index] >= 2:
            return

        if time.time() - decrypt_state.get("last_input_at", time.time()) < 10.0:
            return

        puzzle = decrypt_puzzles[stage_index]
        candidates = [idx for idx, value in enumerate(
            decrypt_state["letters_placed"]) if value != puzzle["word"][idx]]
        if not candidates:
            return

        hint_index = random.choice(candidates)
        decrypt_state["letters_placed"][hint_index] = puzzle["word"][hint_index]
        if hint_index not in decrypt_state["revealed_positions"]:
            decrypt_state["revealed_positions"].append(hint_index)
        decrypt_state["hints_used"][stage_index] += 1
        decrypt_state["hint_flash_letter"] = puzzle["encrypted"][hint_index]
        decrypt_state["selected_position"] = hint_index
        decrypt_state["wrong_position"] = None
        decrypt_state["last_input_at"] = time.time()
        decrypt_log("> Hint activated â€” one letter revealed")
        renpy.notify(t("Hint activated"))
        renpy.restart_interaction()
        decrypt_check_word()

    def decrypt_confirm_word():
        if decrypt_state["phase"] != "playing":
            return

        puzzle = decrypt_puzzles[decrypt_state["current_stage"]]
        for idx, letter in enumerate(decrypt_state["letters_placed"]):
            if letter != puzzle["word"][idx]:
                decrypt_state["attempts"][decrypt_state["current_stage"]] += 1
                decrypt_mark_wrong(idx)
                return

        decrypt_check_word()

    def decrypt_calculate_stage_score(word_index):
        hints = decrypt_state["hints_used"][word_index]
        stage_time = decrypt_state["stage_times"][word_index]

        if hints == 0 and stage_time <= 30:
            return 3
        elif hints <= 1 and stage_time <= 60:
            return 2
        elif hints <= 2:
            return 1
        return 0

    def decrypt_check_word():
        stage_index = decrypt_state["current_stage"]
        puzzle = decrypt_puzzles[stage_index]

        if decrypt_state["letters_placed"] != list(puzzle["word"]):
            return False

        decrypt_state["stage_times"][stage_index] = decrypt_elapsed(
            stage_index)
        score = decrypt_calculate_stage_score(stage_index)
        decrypt_state["stage_scores"][stage_index] = score
        decrypt_state["stars_earned"][stage_index] = score
        decrypt_state["total_score"] = sum(decrypt_state["stage_scores"])
        decrypt_state["phase"] = "word_complete"
        decrypt_state["wrong_position"] = None
        decrypt_state["word_complete_serial"] += 1
        decrypt_log("> " + puzzle["word"] + " â€” DECRYPTION SUCCESSFUL")
        renpy.notify(t("Encryption cracked! +1"))
        renpy.restart_interaction()
        return True

    def decrypt_next_stage():
        stage_index = decrypt_state["current_stage"] + 1
        if stage_index >= len(decrypt_puzzles):
            decrypt_state["phase"] = "complete"
            renpy.restart_interaction()
            return False

        decrypt_reset_stage(stage_index)
        return True

    def decrypt_calculate_score():
        decrypt_state["total_score"] = sum(decrypt_state["stage_scores"])
        return decrypt_state["total_score"]

    def decrypt_tick_cursor():
        if decrypt_state.get("phase") == "playing":
            decrypt_state["cursor_visible"] = not decrypt_state.get(
                "cursor_visible", True)
            renpy.restart_interaction()


transform letter_reveal:
    alpha 0.0
    zoom 0.5
    yoffset - 10
    ease 0.25 alpha 1.0 zoom 1.0 yoffset 0

transform letter_wrong_shake:
    xoffset 0
    ease 0.05 xoffset - 12
    ease 0.05 xoffset 12
    ease 0.05 xoffset - 8
    ease 0.05 xoffset 8
    ease 0.05 xoffset 0

transform word_complete_pulse:
    zoom 1.0
    ease 0.15 zoom 1.06
    ease 0.15 zoom 1.0
    ease 0.15 zoom 1.04
    ease 0.15 zoom 1.0

transform star_earn:
    alpha 0.0
    zoom 0.3
    rotate - 20
    ease 0.4 alpha 1.0 zoom 1.0 rotate 0

transform wheel_spin:
    rotate 0
    linear 20.0 rotate 360
    repeat

transform wheel_snap_to(angle):
    rotate angle
    ease 0.3 rotate angle

transform bg_scroll_down(delay=0.0):
    yoffset - 720
    pause delay
    linear 30.0 yoffset 720
    repeat

transform stage_transition_in:
    alpha 0.0
    zoom 0.96
    ease 0.3 alpha 1.0 zoom 1.0

transform stage_transition_out:
    alpha 1.0
    zoom 1.0
    ease 0.25 alpha 0.0 zoom 1.03


screen decrypt_alphabet_panel():
    $ puzzle = decrypt_puzzles[decrypt_state["current_stage"]]
    $ alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    frame:
        xfill True
        background Solid("#0C1018EE")
        padding(20, 16)

        vbox:
            spacing 10

            text t("â¬¡  CAESAR CIPHER REFERENCE â€” SHIFT: 3  â¬¡"):
                color "#00FFD1"
                size 20
                bold True
                font "fonts/ShareTechMono-Regular.ttf"

            for row_start in (0, 13):
                hbox:
                    spacing 6

                    vbox:
                        spacing 18
                        yalign 0.5

                        text("CIPHER â†’" if row_start == 0 else ""):
                            color "#607080"
                            size 14
                            font "fonts/ShareTechMono-Regular.ttf"

                        text("PLAIN  â†’" if row_start == 0 else ""):
                            color "#607080"
                            size 14
                            font "fonts/ShareTechMono-Regular.ttf"

                    for idx in range(row_start, row_start + 13):
                        $ cipher_letter = alphabet[idx]
                        $ plain_letter = caesar_map[cipher_letter]
                        $ is_focus = decrypt_state.get("hover_letter") == cipher_letter or decrypt_state.get("hint_flash_letter") == cipher_letter
                        $ appears_here = cipher_letter in puzzle["encrypted"]
                        $ cipher_color = "#FFD700" if is_focus else "#B9C7CF" if appears_here else "#8B98A6"
                        $ connector_color = "#00FFD1" if is_focus else "#2A3A4A"
                        $ plain_color = "#00FFD1" if is_focus else "#A4B8C5"

                        vbox:
                            spacing 1
                            xalign 0.5

                            button:
                                style(
                                    "alphabet_cell_highlighted_cipher" if is_focus else "alphabet_cell")
                                background Solid("#3A2912" if is_focus else "#18212B" if appears_here else "#111820")
                                hovered Function(decrypt_set_hover_letter, cipher_letter)
                                unhovered Function(decrypt_clear_hover_letter)
                                action Function(decrypt_use_cipher_letter, cipher_letter)

                                text t("[cipher_letter]"):
                                    font "fonts/ShareTechMono-Regular.ttf"
                                    size 20
                                    bold True
                                    color cipher_color
                                    xalign 0.5
                                    yalign 0.5

                            text t("â”‚"):
                                xalign 0.5
                                color connector_color
                                size 16
                                font "fonts/ShareTechMono-Regular.ttf"

                            frame:
                                xsize 50
                                ysize 42
                                background Solid("#003E38" if is_focus else "#111820")
                                padding(0, 0)

                                text t("[plain_letter]"):
                                    font "fonts/ShareTechMono-Regular.ttf"
                                    size 20
                                    bold True
                                    color plain_color
                                    xalign 0.5
                                    yalign 0.5


screen decrypt_word_display():
    $ puzzle = decrypt_puzzles[decrypt_state["current_stage"]]
    $ selected = decrypt_get_selected_position()
    $ focus_letter = decrypt_state.get("hover_letter") or puzzle["encrypted"][selected]
    frame:
        xfill True
        background Solid("#0C1018EE")
        padding(28, 22)

        vbox:
            spacing 18
            xalign 0.5

            text t("â¬¡  INTERCEPTED TRANSMISSION  â¬¡"):
                color "#00FFD1"
                size 24
                bold True
                font "fonts/ShareTechMono-Regular.ttf"
                xalign 0.5
                text_align 0.5

            text t("âš¡ ENCRYPTED MESSAGE DETECTED â€” [puzzle['headline']]"):
                color "#E8E8E8"
                size 18
                font "fonts/ShareTechMono-Regular.ttf"
                xalign 0.5
                text_align 0.5

            if decrypt_state["phase"] == "word_complete":
                vbox at word_complete_pulse:
                    spacing 12
                    xalign 0.5

                    hbox:
                        xalign 0.5
                        spacing 14

                        for idx, letter in enumerate(puzzle["encrypted"]):
                            $ tile_focus = letter == focus_letter or decrypt_state.get("hint_flash_letter") == letter
                            button:
                                style "cipher_tile"
                                background Solid("#2B2312" if tile_focus else "#161E2A")
                                hovered Function(decrypt_set_hover_letter, letter)
                                unhovered Function(decrypt_clear_hover_letter)
                                action Function(decrypt_select_position, idx)

                                text t("[letter]"):
                                    font "fonts/ShareTechMono-Regular.ttf"
                                    size 38
                                    bold True
                                    color "#FFD700"
                                    xalign 0.5
                                    yalign 0.5

                    hbox:
                        xalign 0.5
                        spacing 14

                        for idx, letter in enumerate(decrypt_state["letters_placed"]):
                            frame:
                                style "decoded_tile_correct"
                                at letter_reveal

                                text t("[letter]"):
                                    font "fonts/ShareTechMono-Regular.ttf"
                                    size 34
                                    bold True
                                    color "#39FF14"
                                    xalign 0.5
                                    yalign 0.5
            else:
                hbox:
                    xalign 0.5
                    spacing 14

                    for idx, letter in enumerate(puzzle["encrypted"]):
                        $ tile_focus = letter == focus_letter or decrypt_state.get("hint_flash_letter") == letter
                        button:
                            style "cipher_tile"
                            background Solid("#2B2312" if tile_focus else "#161E2A")
                            hovered Function(decrypt_set_hover_letter, letter)
                            unhovered Function(decrypt_clear_hover_letter)
                            action Function(decrypt_select_position, idx)

                            text t("[letter]"):
                                font "fonts/ShareTechMono-Regular.ttf"
                                size 38
                                bold True
                                color "#FFD700"
                                xalign 0.5
                                yalign 0.5

                hbox:
                    xalign 0.5
                    spacing 14

                    for idx, letter in enumerate(decrypt_state["letters_placed"]):
                        $ is_selected = idx == selected
                        $ is_revealed = idx in decrypt_state.get("revealed_positions", [])
                        $ is_wrong = idx == decrypt_state.get("wrong_position")
                        $ decoded_style = "decoded_tile_correct" if is_revealed else "decoded_tile_active" if is_selected else "decoded_tile"
                        $ decoded_background = "#12331A" if is_revealed else "#132330" if is_selected else "#0F1520"
                        $ decoded_color = "#39FF14" if is_revealed else "#E8E8E8"
                        $ empty_color = "#00FFD1" if is_selected else "#607080"
                        if is_wrong:
                            button:
                                style decoded_style
                                background Solid(decoded_background)
                                action Function(decrypt_select_position, idx)
                                at letter_wrong_shake

                                if letter:
                                    text t("[letter]"):
                                        font "fonts/ShareTechMono-Regular.ttf"
                                        size 34
                                        bold True
                                        color decoded_color
                                        xalign 0.5
                                        yalign 0.5
                                        at letter_reveal
                                else:
                                    text("_" if is_selected and decrypt_state.get("cursor_visible", True) else ""):
                                        font "fonts/ShareTechMono-Regular.ttf"
                                        size 30
                                        color empty_color
                                        xalign 0.5
                                        yalign 0.72
                        else:
                            button:
                                style decoded_style
                                background Solid(decoded_background)
                                action Function(decrypt_select_position, idx)

                                if letter:
                                    text t("[letter]"):
                                        font "fonts/ShareTechMono-Regular.ttf"
                                        size 34
                                        bold True
                                        color decoded_color
                                        xalign 0.5
                                        yalign 0.5
                                        at letter_reveal
                                else:
                                    text("_" if is_selected and decrypt_state.get("cursor_visible", True) else ""):
                                        font "fonts/ShareTechMono-Regular.ttf"
                                        size 30
                                        color empty_color
                                        xalign 0.5
                                        yalign 0.72

            text t("Select a tile, inspect the cipher map, then type the decoded letter on your keyboard."):
                color "#607080"
                size 16
                xalign 0.5
                text_align 0.5

            if decrypt_state["phase"] == "word_complete":
                text t("ðŸ”’ WORD LOCKED â€” READY FOR NEXT TRANSMISSION"):
                    color "#39FF14"
                    size 18
                    bold True
                    xalign 0.5
                    font "fonts/ShareTechMono-Regular.ttf"


screen decrypt_keyboard():
    $ selected = decrypt_get_selected_position()
    $ mapped_hint = caesar_map[decrypt_puzzles[decrypt_state["current_stage"]]["encrypted"][selected]]
    frame:
        xfill True
        background Solid("#0C1018EE")
        padding(24, 20)

        vbox:
            spacing 16

            text t("â¬¡  KEYBOARD INPUT  â¬¡"):
                color "#00FFD1"
                size 22
                bold True
                font "fonts/ShareTechMono-Regular.ttf"

            text t("Type A-Z on your physical keyboard. Use Backspace to clear and Enter to confirm."):
                color "#E8E8E8"
                size 20
                xalign 0.5
                text_align 0.5

            hbox:
                xalign 0.5
                spacing 20

                text t("Selected cell: [selected + 1] / [len(decrypt_state['letters_placed'])]"):
                    color "#607080"
                    size 18
                    font "fonts/ShareTechMono-Regular.ttf"
                    yalign 0.5

                text t("Cipher hint: [decrypt_puzzles[decrypt_state['current_stage']]['encrypted'][selected]] -> [mapped_hint]"):
                    color "#FFD700"
                    size 18
                    font "fonts/ShareTechMono-Regular.ttf"
                    yalign 0.5

                textbutton t("âŒ« DELETE"):
                    style "keyboard_key"
                    text_style "keyboard_key_text"
                    action Function(decrypt_delete_letter)

                if "" not in decrypt_state["letters_placed"]:
                    textbutton t("âœ“ CONFIRM"):
                        style "keyboard_key"
                        text_style "keyboard_key_text"
                        action Function(decrypt_confirm_word)


screen decrypt_cipher_wheel():
    vbox:
        xalign 0.5
        spacing 6

        fixed:
            xsize 190
            ysize 190
            xalign 0.5

            text t("â—Œ"):
                xalign 0.5
                yalign 0.5
                size 180
                color "#00FFD140"
                font "fonts/ShareTechMono-Regular.ttf"

            text t("â—Œ"):
                xalign 0.5
                yalign 0.5
                size 134
                color "#39FF1440"
                font "fonts/ShareTechMono-Regular.ttf"

            fixed at wheel_spin:
                xalign 0.5
                yalign 0.5
                xsize 160
                ysize 160

                text t("A B C D E F G"):
                    xpos 34
                    ypos 12
                    size 11
                    color "#FFD700"
                    font "fonts/ShareTechMono-Regular.ttf"

                text t("H I J K L M"):
                    xpos 88
                    ypos 46
                    size 11
                    color "#FFD700"
                    font "fonts/ShareTechMono-Regular.ttf"

                text t("N O P Q R"):
                    xpos 96
                    ypos 88
                    size 11
                    color "#FFD700"
                    font "fonts/ShareTechMono-Regular.ttf"

                text t("S T U V W"):
                    xpos 18
                    ypos 126
                    size 11
                    color "#FFD700"
                    font "fonts/ShareTechMono-Regular.ttf"

                text t("X Y Z"):
                    xpos 12
                    ypos 66
                    size 11
                    color "#FFD700"
                    font "fonts/ShareTechMono-Regular.ttf"

            fixed at wheel_snap_to(decrypt_state.get("wheel_angle", 0.0)):
                xalign 0.5
                yalign 0.5
                xsize 126
                ysize 126

                text t("X Y Z A B C"):
                    xpos 22
                    ypos 15
                    size 10
                    color "#00FFD1"
                    font "fonts/ShareTechMono-Regular.ttf"

                text t("D E F G H"):
                    xpos 70
                    ypos 42
                    size 10
                    color "#00FFD1"
                    font "fonts/ShareTechMono-Regular.ttf"

                text t("I J K L M"):
                    xpos 76
                    ypos 78
                    size 10
                    color "#00FFD1"
                    font "fonts/ShareTechMono-Regular.ttf"

                text t("N O P Q R"):
                    xpos 14
                    ypos 94
                    size 10
                    color "#00FFD1"
                    font "fonts/ShareTechMono-Regular.ttf"

                text t("S T U V W"):
                    xpos 4
                    ypos 58
                    size 10
                    color "#00FFD1"
                    font "fonts/ShareTechMono-Regular.ttf"

            # Small dot in center instead of text
            add Solid("#00FFD160"):
                xsize 6
                ysize 6
                xalign 0.5
                yalign 0.5

        text t("ROT-3  â—†  SHIFT 3"):
            xalign 0.5
            size 13
            bold True
            color "#8B8FCC"
            font "fonts/ShareTechMono-Regular.ttf"


screen decrypt_game():
    modal True
    tag decrypt_game
    $ puzzle = decrypt_puzzles[decrypt_state["current_stage"]]
    $ stage_index = decrypt_state["current_stage"]

    if decrypt_state["phase"] == "playing":
        timer 25.0 repeat True action Function(decrypt_give_hint)
        timer 0.5 repeat True action Function(decrypt_tick_cursor)
        for _letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            key("K_" + _letter.lower()) action Function(decrypt_type_letter, _letter)
        key "K_BACKSPACE" action Function(decrypt_delete_letter)
        key "K_DELETE" action Function(decrypt_delete_letter)
        key "K_RETURN" action Function(decrypt_confirm_word)
        key "K_KP_ENTER" action Function(decrypt_confirm_word)

    add "#080C10"

    add "images/logo.png":
        xalign 0.5
        yalign 0.5
        alpha 0.15
        fit "contain"
        xsize 900
        ysize 900

    fixed:
        for idx, stream in enumerate(decrypt_state.get("bg_streams", [])):
            text t("[stream]"):
                xpos 30 + (idx * 310)
                ypos - 620 + (idx * 80)
                color "#2A3A4A10"
                size 18
                line_spacing 2
                font "fonts/ShareTechMono-Regular.ttf"
                at bg_scroll_down(idx * 0.25)

    # â”€â”€ TOP HEADER BAR â”€â”€
    # xsize capped at 1540 so it does not collide with the quick-menu / HUD in the top-right corner
    frame:
        xpos 52
        ypos 20
        xsize 1540
        ysize 72
        background Solid("#0C1018F0")
        padding(24, 14)

        hbox:
            xfill True

            text t("// DECRYPTION TERMINAL //  Stage: [stage_index + 1]/3  [puzzle['difficulty']]"):
                color "#E8E8E8"
                size 20
                bold True
                font "fonts/ShareTechMono-Regular.ttf"
                yalign 0.5

            text t("[decrypt_score_stars(decrypt_state['stage_scores'][0])] [decrypt_score_stars(decrypt_state['stage_scores'][1])] [decrypt_score_stars(decrypt_state['stage_scores'][2])]  Score: [decrypt_state['total_score']]/9"):
                color "#00FFD1"
                size 18
                bold True
                font "fonts/ShareTechMono-Regular.ttf"
                xalign 1.0
                yalign 0.5

    # â”€â”€ CIPHER DISPLAY (CENTERED) â”€â”€
    frame:
        xpos 52
        ypos 106
        xsize 1816
        ysize 340
        background Solid("#0C1018EE")
        padding(0, 0)

        fixed:
            xfill True
            yfill True
            text t("â¬¡"):
                xpos 12
                ypos 8
                color "#607080"
                size 18
            text t("â¬¡"):
                xpos 1786
                ypos 8
                color "#607080"
                size 18
            text t("â¬¡"):
                xpos 12
                ypos 310
                color "#607080"
                size 18
            text t("â¬¡"):
                xpos 1786
                ypos 310
                color "#607080"
                size 18
            use decrypt_word_display

    # â”€â”€ BOTTOM ROW: Score/Stars + Cipher Wheel + Analysis Log â”€â”€
    # Score stars panel
    frame:
        xpos 52
        ypos 460
        xsize 600
        ysize 270
        background Solid("#0C1018EE")
        padding(22, 18)

        vbox:
            spacing 8
            xalign 0.5

            text t("â¬¡  STAGE PROGRESS  â¬¡"):
                color "#00FFD1"
                size 20
                bold True
                xalign 0.5
                font "fonts/ShareTechMono-Regular.ttf"

            null height 6

            for _si in range(3):
                $ _sp = decrypt_puzzles[_si]
                $ _ss = decrypt_state["stage_scores"][_si]
                $ _st = decrypt_score_stars(_ss)
                $ _sr = decrypt_stage_rating(_ss)
                $ _sw = _sp["word"]
                $ _sd = _sp["difficulty"]
                $ _done = decrypt_state["stage_times"][_si] > 0
                $ _active = _si == stage_index and decrypt_state["phase"] == "playing"

                hbox:
                    xfill True
                    spacing 12

                    text t("Stage [_si + 1]"):
                        color("#FFD700" if _active else "#607080")
                        size 16
                        bold _active
                        font "fonts/ShareTechMono-Regular.ttf"
                        yalign 0.5

                    text t("[_sd]"):
                        color("#8B8FCC" if _active else "#4D5186")
                        size 14
                        font "fonts/ShareTechMono-Regular.ttf"
                        yalign 0.5

                    if _done:
                        text t("[_sw]"):
                            color "#39FF14"
                            size 16
                            bold True
                            font "fonts/ShareTechMono-Regular.ttf"
                            yalign 0.5

                        text t("[_st]"):
                            color "#FFD700"
                            size 16
                            font "fonts/ShareTechMono-Regular.ttf"
                            xalign 1.0
                            yalign 0.5

                        text t("[_sr]"):
                            color "#00FFD1"
                            size 14
                            font "fonts/ShareTechMono-Regular.ttf"
                            xalign 1.0
                            yalign 0.5
                    elif _active:
                        text t("IN PROGRESS..."):
                            color "#FFD700"
                            size 14
                            italic True
                            font "fonts/ShareTechMono-Regular.ttf"
                            yalign 0.5
                    else:
                        text t("LOCKED"):
                            color "#333840"
                            size 14
                            font "fonts/ShareTechMono-Regular.ttf"
                            yalign 0.5

            null height 4

            hbox:
                xfill True
                text t("Total Score:"):
                    color "#888888"
                    size 16
                    font "fonts/ShareTechMono-Regular.ttf"
                    yalign 0.5
                text t("[decrypt_state['total_score']] / 9"):
                    color "#00FFD1"
                    size 18
                    bold True
                    font "fonts/ShareTechMono-Regular.ttf"
                    xalign 1.0
                    yalign 0.5

    # Cipher wheel panel
    frame:
        xpos 668
        ypos 460
        xsize 430
        ysize 270
        background Solid("#0C1018EE")
        padding(22, 18)

        vbox:
            spacing 6
            xalign 0.5
            $ hint_color = "#FFD700" if decrypt_state["hints_used"][stage_index] else "#607080"

            text t("â¬¡  CIPHER WHEEL  â¬¡"):
                color "#00FFD1"
                size 20
                bold True
                xalign 0.5
                font "fonts/ShareTechMono-Regular.ttf"

            use decrypt_cipher_wheel

            hbox:
                xalign 0.5
                spacing 18

                text t("Elapsed: [decrypt_elapsed()]s"):
                    color "#E8E8E8"
                    size 15
                    font "fonts/ShareTechMono-Regular.ttf"
                    yalign 0.5

                text t("Hints: [decrypt_state['hints_used'][stage_index]] / 2"):
                    color hint_color
                    size 15
                    font "fonts/ShareTechMono-Regular.ttf"
                    yalign 0.5

    # Analysis log panel
    frame:
        xpos 1114
        ypos 460
        xsize 754
        ysize 270
        style "decrypt_terminal"
        padding(22, 18)

        vbox:
            spacing 10

            text t("â¬¡  ANALYSIS LOG  â¬¡"):
                color "#00FFD1"
                size 20
                bold True
                font "fonts/ShareTechMono-Regular.ttf"

            text t("[puzzle['hint']]"):
                color "#FFD700"
                size 15
                italic True
                text_align 0.0

            $ log_text = "\n".join([line for line in decrypt_state.get("log_lines", [])[-6:] if line])
            text t("[log_text]"):
                color "#E8E8E8"
                size 14
                font "fonts/ShareTechMono-Regular.ttf"
                text_align 0.0
                line_spacing 2

    # â”€â”€ CAESAR CIPHER REFERENCE (BOTTOM LEFT) â”€â”€
    frame:
        xpos 52
        ypos 744
        xsize 1430
        ysize 274
        background Solid("#0C1018EE")
        padding(0, 0)

        fixed:
            xfill True
            yfill True
            text t("â¬¡"):
                xpos 12
                ypos 8
                color "#607080"
                size 18
            text t("â¬¡"):
                xpos 1400
                ypos 8
                color "#607080"
                size 18
            use decrypt_alphabet_panel

    # â”€â”€ DECRYPTION CONTROLS (BOTTOM RIGHT) â”€â”€
    frame:
        xpos 1498
        ypos 744
        xsize 370
        ysize 274
        background Solid("#0C1018EE")
        padding(22, 18)

        vbox:
            spacing 10

            text t("â¬¡  CONTROLS  â¬¡"):
                color "#00FFD1"
                size 18
                bold True
                font "fonts/ShareTechMono-Regular.ttf"
                xalign 0.5

            null height 4

            hbox:
                spacing 8
                text t("A-Z"):
                    color "#FFD700"
                    size 14
                    bold True
                    font "fonts/ShareTechMono-Regular.ttf"
                    yalign 0.5
                text t("Type decoded letter"):
                    color "#AAB0D6"
                    size 13
                    font "fonts/ShareTechMono-Regular.ttf"
                    yalign 0.5

            hbox:
                spacing 8
                text t("âŒ«"):
                    color "#FFD700"
                    size 14
                    bold True
                    font "fonts/ShareTechMono-Regular.ttf"
                    yalign 0.5
                text t("Clear selected cell"):
                    color "#AAB0D6"
                    size 13
                    font "fonts/ShareTechMono-Regular.ttf"
                    yalign 0.5

            hbox:
                spacing 8
                text t("Enter"):
                    color "#FFD700"
                    size 14
                    bold True
                    font "fonts/ShareTechMono-Regular.ttf"
                    yalign 0.5
                text t("Confirm full word"):
                    color "#AAB0D6"
                    size 13
                    font "fonts/ShareTechMono-Regular.ttf"
                    yalign 0.5

            hbox:
                spacing 8
                text t("Click"):
                    color "#FFD700"
                    size 14
                    bold True
                    font "fonts/ShareTechMono-Regular.ttf"
                    yalign 0.5
                text t("Select cipher tile"):
                    color "#AAB0D6"
                    size 13
                    font "fonts/ShareTechMono-Regular.ttf"
                    yalign 0.5

            null height 4

            add Solid("#00FFD120"):
                xsize 326
                ysize 1

            null height 2

            text t("ðŸ’¡ Hints auto-reveal after 25s of inactivity"):
                color "#607080"
                size 12
                font "fonts/ShareTechMono-Regular.ttf"
                text_align 0.5
                xalign 0.5

    if decrypt_state["phase"] == "word_complete":
        $ next_cta = "> LOAD NEXT TRANSMISSION" if stage_index < 2 else "> OPEN DEBRIEF"
        frame:
            xalign 0.5
            yalign 0.5
            xsize 760
            ysize 240
            background Solid("#08130DDC")
            padding(28, 22)
            at stage_transition_in

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 14

                text t("// DECRYPTION SUCCESSFUL //"):
                    color "#39FF14"
                    size 30
                    bold True
                    xalign 0.5
                    font "fonts/ShareTechMono-Regular.ttf"

                text t("[puzzle['word']]  [decrypt_score_stars(decrypt_state['stage_scores'][stage_index])]"):
                    color "#E8E8E8"
                    size 28
                    bold True
                    xalign 0.5
                    font "fonts/ShareTechMono-Regular.ttf"
                    at star_earn

                text t("Time: [decrypt_state['stage_times'][stage_index]]s   Rating: [decrypt_stage_rating(decrypt_state['stage_scores'][stage_index])]"):
                    color "#00FFD1"
                    size 18
                    xalign 0.5
                    font "fonts/ShareTechMono-Regular.ttf"

                textbutton t("[next_cta]"):
                    style "modal_action_button"
                    text_style "modal_action_button_text"
                    xalign 0.5
                    action Return("next")
    key "K_BACKSPACE" action NullAction()
    key "mouseup_3" action NullAction()
    
    use block_shortcuts_and_skip("SKIP")

screen decrypt_stage_transition(word, score, stars):
    modal True
    tag decrypt_transition

    add "#080C10EE"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 360
        background Solid("#0C1018F4")
        padding(40, 34)
        at stage_transition_in

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 16

            text t("// STAGE [decrypt_state['current_stage'] + 1] COMPLETE //"):
                color "#39FF14"
                size 30
                bold True
                xalign 0.5
                font "fonts/ShareTechMono-Regular.ttf"

            text t("Word: [word]"):
                color "#E8E8E8"
                size 28
                xalign 0.5
                font "fonts/ShareTechMono-Regular.ttf"

            text t("Time: [decrypt_state['stage_times'][decrypt_state['current_stage']]]s"):
                color "#00FFD1"
                size 20
                xalign 0.5
                font "fonts/ShareTechMono-Regular.ttf"

            text t("Stars: [stars]   Rating: [decrypt_stage_rating(score)]"):
                color "#FFD700"
                size 22
                xalign 0.5
                font "fonts/ShareTechMono-Regular.ttf"

            text t("Loading next transmission..."):
                color "#607080"
                size 18
                xalign 0.5
                font "fonts/ShareTechMono-Regular.ttf"

            bar:
                value AnimatedValue(0.0, 1.0, 1.7)
                xmaximum 640
                ymaximum 18
                xalign 0.5

    timer 1.9 action Return(True)


screen decrypt_result():
    modal True
    tag decrypt_result
    $ total = decrypt_calculate_score()
    $ clearance_color = "#39FF14" if total >= 6 else "#00FFD1" if total >= 4 else "#FF2D55"

    add "#080C10"

    fixed:
        for idx, stream in enumerate(decrypt_build_bg_streams()):
            text t("[stream]"):
                xpos 24 + (idx * 320)
                ypos - 580 + (idx * 90)
                color "#2A3A4A0F"
                size 18
                line_spacing 2
                font "fonts/ShareTechMono-Regular.ttf"
                at bg_scroll_down(idx * 0.25)

    frame:
        xalign 0.5
        ypos 86
        xsize 1240
        ysize 360
        background Solid("#0C1018EE")
        padding(34, 28)

        vbox:
            spacing 18

            text t("// DECRYPTION MISSION: COMPLETE //"):
                color "#00FFD1"
                size 34
                bold True
                xalign 0.5
                font "fonts/ShareTechMono-Regular.ttf"

            for idx, puzzle in enumerate(decrypt_puzzles):
                hbox:
                    xfill True

                    text t("[puzzle['word']] [decrypt_score_stars(decrypt_state['stage_scores'][idx])]"):
                        color "#E8E8E8"
                        size 25
                        font "fonts/ShareTechMono-Regular.ttf"

                    text t("Decoded in [decrypt_state['stage_times'][idx]]s ([decrypt_stage_rating(decrypt_state['stage_scores'][idx])])"):
                        color "#607080"
                        size 21
                        xalign 1.0

            null height 8

            text t("TOTAL SCORE: [total] / 9"):
                color "#FFD700"
                size 30
                bold True
                xalign 0.5
                font "fonts/ShareTechMono-Regular.ttf"

            text t("CLEARANCE: [decrypt_clearance_title(total)]"):
                color clearance_color
                size 26
                bold True
                xalign 0.5
                font "fonts/ShareTechMono-Regular.ttf"

    frame:
        xalign 0.5
        ypos 484
        xsize 1240
        ysize 300
        background Solid("#0C1018EE")
        padding(34, 28)

        vbox:
            spacing 18

            text t("â¬¡  WHAT YOU LEARNED  â¬¡"):
                color "#00FFD1"
                size 28
                bold True
                font "fonts/ShareTechMono-Regular.ttf"

            text t("A Caesar cipher is one of the oldest encryption methods â€” used by Julius Caesar in 58 BC."):
                color "#E8E8E8"
                size 22

            text t("Modern encryption like AES-256 or PGP follows the same idea of protecting meaning, but uses mathematics so advanced that the message stays unreadable without the right key."):
                color "#E8E8E8"
                size 22

            text t("You used PGP encryption to contact journalists. Without encryption, your communications could have been intercepted long before the files reached the public."):
                color "#E8E8E8"
                size 22

    textbutton t("> CONTINUE MISSION"):
        style "modal_action_button"
        text_style "modal_action_button_text"
        xalign 0.5
        ypos 828
        action Return(True)


label minigame_2_decrypt:
    window hide
    $ mg_intro2 = renpy.call_screen("minigame_briefing", challenge_title="DECRYPT THE MESSAGE", subtitle="Basic encryption relies on keys.\nFind the key, break the cipher.", mission_id="OPS-02-05-2013", classification="TOP SECRET // EYES ONLY", challenge_type="CRYPTOGRAPHY", estimated_time="45 SECONDS", difficulty=1, difficulty_label="TRAINEE", succeed_reward="knowledge_score +1", fail_penalty="suspicion_level +1", learn_concept="Caesar Ciphers shift letters by a fixed amount.\nModern encryption uses the same core principle.", briefing_text="A classified NSA transmission has been encrypted with a Caesar cipher.\n\nCrack three intercepted words by shifting each cipher letter back by 3.\n\nExample: 'D' shifted back by 3 is 'A'.", controls=[("CLICK", "Select letter to input"),("ENTER", "Submit decrypted word")])
    if not mg_intro2:
        $ knowledge_score -= 1
        $ mg_decrypt_solved = False
        $ renpy.notify(t("Knowledge -1 (Skipped)"))
        return

    $ decrypt_reset_game()
    $ quick_menu = False
    $ show_hud = False

    while True:
        $ _decrypt_step = renpy.call_screen("decrypt_game")
        if _decrypt_step == "SKIP":
            jump decrypt_game_results

        if decrypt_state["phase"] == "word_complete":
            if decrypt_state["current_stage"] < len(decrypt_puzzles) - 1:
                $ _stage_index = decrypt_state["current_stage"]
                $ _stage_word = decrypt_puzzles[_stage_index]["word"]
                $ _stage_score = decrypt_state["stage_scores"][_stage_index]
                $ _stage_stars = decrypt_score_stars(_stage_score)
                call screen decrypt_stage_transition(_stage_word, _stage_score, _stage_stars)
                $ decrypt_next_stage()
            else:
                $ decrypt_state["phase"] = "complete"
                jump decrypt_game_results

label decrypt_game_results:
    call screen decrypt_result
    $ total = decrypt_calculate_score()
    if total >= 7:
        $ knowledge_score += 3
        $ evidence_secured = True
    elif total >= 5:
        $ knowledge_score += 2
        $ evidence_secured = True
    elif total >= 3:
        $ knowledge_score += 1
        $ evidence_secured = True
    else:
        $ suspicion_level += 1

    $ mg_decrypt_solved = total >= 3
    $ renpy.notify(t("Decryption score: {}/9").format(total))

    $ quick_menu = True
    $ show_hud = True
    return


################################################################################
# MINIGAME 3: CLEAN THE MESSAGE (Chapter 3)
# -> Implemented in minigame_ctm.rpy
################################################################################


################################################################################
# MINIGAME 4: TRACE THE ROUTE (Chapter 4)
################################################################################

init python:
    def get_trace_nodes():
        return {
            "home":     {"name": "YOUR LAPTOP",      "x": 0.1,  "y": 0.5, "type": "start"},
            "isp":      {"name": "ISP ROUTER",       "x": 0.28, "y": 0.3, "type": "normal"},
            "vpn":      {"name": "VPN SERVER",        "x": 0.28, "y": 0.7, "type": "safe"},
            "tor1":     {"name": "TOR NODE 1",        "x": 0.46, "y": 0.25, "type": "safe"},
            "tor2":     {"name": "TOR NODE 2",        "x": 0.46, "y": 0.75, "type": "safe"},
            "gov":      {"name": "GOV MONITOR",       "x": 0.46, "y": 0.5, "type": "danger"},
            "cdn":      {"name": "CDN SERVER",         "x": 0.64, "y": 0.3, "type": "normal"},
            "secure":   {"name": "SECURE RELAY",       "x": 0.64, "y": 0.7, "type": "safe"},
            "target":   {"name": "JOURNALIST SERVER", "x": 0.85, "y": 0.5, "type": "end"},
        }

    # Valid safe paths (avoiding gov monitor)
    safe_connections = {
        "home": ["isp", "vpn"],
        "isp": ["tor1", "gov"],
        "vpn": ["tor2", "tor1"],
        "tor1": ["cdn", "gov"],
        "tor2": ["secure", "gov"],
        "gov": ["cdn", "secure"],
        "cdn": ["target"],
        "secure": ["target"],
    }

    def trace_node_color(node_type, active=False, visited=False):
        if node_type == "danger":
            return "#FF2D55" if active else "#6B1F31"
        if node_type in ("safe", "end"):
            return "#00FFD1" if active else "#004D45"
        if node_type == "start":
            return "#FFD700" if active else "#594700"
        return "#8B8FCC" if active else "#232843"

    def trace_hint(current_node):
        hints = {
            "home": "The hotel path is noisier. The VPN route is the safer opening move.",
            "isp": "ISP gear is a chokepoint. One branch keeps you moving, the other gets you watched.",
            "vpn": "Nice start. Stack more privacy-friendly hops instead of cutting back toward surveillance.",
            "tor1": "Tor helps, but one wrong turn can still expose the route.",
            "tor2": "You're deep in the safer path now. Finish through the protected relay.",
            "gov": "The monitor has your traffic. That route is burned.",
            "cdn": "You're close, but delivery infrastructure is less private than a secure relay.",
            "secure": "One more clean hop gets the instructions home.",
        }
        return hints.get(current_node, "Keep the route tight and avoid the red monitor.")


screen minigame_trace():
    modal True
    key "rollback" action NullAction()
    key "K_BACKSPACE" action NullAction()
    default nodes = get_trace_nodes()
    default current_node = "home"
    default path = ["home"]
    default moves = 0
    default max_moves = 5
    default time_left = 32
    default hit_gov = False
    default reached_end = False

    if not reached_end and not hit_gov and moves < max_moves and time_left > 0:
        timer 1.0 repeat True action SetScreenVariable("time_left", max(0, time_left - 1))

    add "#0A0E1A"

    add "images/logo.png":
        xalign 0.5
        yalign 0.5
        alpha 0.15
        fit "contain"
        xsize 900
        ysize 900

    frame:
        xfill True yfill True
        background "#0A0E1A"
        padding(40, 30)

        if not reached_end and not hit_gov and moves < max_moves and time_left > 0:
            vbox:
                spacing 16

                text t("// TRACE THE ROUTE //") style "minigame_title"
                text t("Build a clean route to the journalist server. One bad hop sends everything through government eyes.") style "minigame_instruction"

                hbox:
                    xfill True
                    spacing 16

                    frame:
                        xsize 330
                        background "#111827"
                        padding(20, 16)

                        vbox:
                            spacing 8
                            text t("LIVE STATUS") color "#8B8FCC" size 16 bold True
                            text t("[nodes[current_node]['name']]") color "#EAF4F1" size 28 bold True
                            text t("Moves remaining: [max_moves - moves]/[max_moves]") color "#FFD700" size 18
                            text t("Time left: [time_left]s") color("#FF2D55" if time_left <= 8 else "#00FFD1") size 18 bold True
                            text t("Path: ") + " -> ".join([nodes[n]["name"] for n in path]) color "#AAB0D6" size 15

                    frame:
                        xfill True
                        background "#111827"
                        padding(20, 16)

                        text trace_hint(current_node):
                            color "#EAF4F1"
                            size 19
                            xalign 0.5
                            text_align 0.5

                frame:
                    xfill True
                    ysize 420
                    background "#0D1220"
                    padding(24, 20)

                    fixed:
                        xfill True
                        yfill True

                        for node_id, node in nodes.items():
                            $ visited = node_id in path
                            $ active = current_node == node_id
                            $ node_color = trace_node_color(node["type"], active, visited)
                            $ x_pos = int(node["x"] * 1420)
                            $ y_pos = int(node["y"] * 320)

                            frame:
                                xpos x_pos
                                ypos y_pos
                                xsize 220
                                ysize 78
                                background node_color
                                padding(14, 10)

                                vbox:
                                    spacing 2
                                    text node["name"]:
                                        color("#0A0E1A" if active else "#EAF4F1")
                                        size 18
                                        bold True
                                        xalign 0.5
                                        text_align 0.5

                                    text("CURRENT" if active else "VISITED" if visited else node["type"].upper()):
                                        color("#0A0E1A" if active else "#C8D8D0")
                                        size 13
                                        xalign 0.5

                frame:
                    xfill True
                    background "#111827"
                    padding(20, 18)

                    vbox:
                        spacing 12
                        text t("AVAILABLE HOPS") color "#8B8FCC" size 17 bold True

                        hbox:
                            spacing 16

                            for next_node in safe_connections.get(current_node, []):
                                $ nn = nodes[next_node]
                                $ btn_bg = "#241926" if nn["type"] == "danger" else "#002922" if nn["type"] in ("safe", "end") else "#171C30"

                                textbutton nn["name"]:
                                    style "modal_action_button"
                                    background Solid(btn_bg)
                                    hover_background Solid("#006654" if nn["type"] != "danger" else "#7A203A")
                                    xsize 430
                                    action[
                                        SetScreenVariable(
                                            "current_node", next_node),
                                        SetScreenVariable(
                                            "path", path + [next_node]),
                                        SetScreenVariable("moves", moves + 1),
                                        SetScreenVariable(
                                            "hit_gov", next_node == "gov"),
                                        SetScreenVariable(
                                            "reached_end", next_node == "target"),
                                    ]

        else:
            frame:
                xalign 0.5
                yalign 0.5
                xsize 940
                background "#111827"
                padding(32, 28)

                vbox:
                    spacing 14
                    xalign 0.5

                    if reached_end and not hit_gov:
                        text t("// ROUTE SECURED //") color "#00FF88" size 38 bold True xalign 0.5
                        text t("Path: ") + " -> ".join([nodes[n]["name"] for n in path]) color "#00FFD1" size 18 xalign 0.5 text_align 0.5
                        text t("You chained together the safer hops and kept the instructions away from the monitor.") color "#C8D8D0" size 19 xalign 0.5 text_align 0.5
                    elif hit_gov:
                        text t("// ROUTE COMPROMISED //") color "#FF2D55" size 38 bold True xalign 0.5
                        text t("The route hit the Government Monitor node, so the mission is blown.") color "#FF2D55" size 20 xalign 0.5 text_align 0.5
                        text t("Even strong tools fail if one hop routes through a known surveillance point.") color "#C8D8D0" size 19 xalign 0.5 text_align 0.5
                    elif time_left <= 0:
                        text t("// TIME EXPIRED //") color "#FF2D55" size 38 bold True xalign 0.5
                        text t("You ran out of time before finishing the route.") color "#FF2D55" size 20 xalign 0.5 text_align 0.5
                        text t("Good opsec also depends on moving quickly before the surveillance window closes.") color "#C8D8D0" size 19 xalign 0.5 text_align 0.5
                    else:
                        text t("// OUT OF MOVES //") color "#FF2D55" size 38 bold True xalign 0.5
                        text t("You ran out of time before reaching the journalist server.") color "#FF2D55" size 20 xalign 0.5 text_align 0.5
                        text t("Tight, efficient routing matters. Extra hops create delay and more chances to get exposed.") color "#C8D8D0" size 19 xalign 0.5 text_align 0.5

                    textbutton t("> CONTINUE MISSION"):
                        xalign 0.5
                        text_style "menu_btn_text"
                        action Return(reached_end and not hit_gov)
