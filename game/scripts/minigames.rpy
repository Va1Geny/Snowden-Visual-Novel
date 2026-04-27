################################################################################
## MINIGAMES.RPY — All Minigame Logic and Screens
## Classified: The Snowden Files
################################################################################

################################################################################
## MINIGAME INTRO / RESULT SCREENS
################################################################################

# === Minigame Intro Splash ===
screen minigame_intro(title, description):
    modal True
    add "#0A0E1ACC"

    frame:
        xalign 0.5 yalign 0.5
        xsize 900 ysize 500
        background "#0A0E1A"
        padding (40, 40)

        vbox:
            xalign 0.5 yalign 0.5
            spacing 30

            text "// SYSTEM CHALLENGE INITIATED //" style "sys_text"
            text title style "minigame_title"
            text description style "minigame_instruction"

            null height 20

            textbutton "> BEGIN CHALLENGE":
                xalign 0.5
                text_style "menu_btn_text"
                action Return(True)

            textbutton "> SKIP (Knowledge -1)":
                xalign 0.5
                text_color "#FF2D55"
                text_size 18
                action Return(False)


# === Minigame Result ===
screen minigame_result(passed, title, explanation):
    modal True
    add "#0A0E1ACC"

    frame:
        xalign 0.5 yalign 0.5
        xsize 900 ysize 500
        background "#0A0E1A"
        padding (40, 40)

        vbox:
            xalign 0.5 yalign 0.5
            spacing 20

            if passed:
                text "// CHALLENGE PASSED //" color "#00FFD1" size 28 bold True xalign 0.5
                text title color "#00FFD1" size 36 bold True xalign 0.5
            else:
                text "// CHALLENGE FAILED //" color "#FF2D55" size 28 bold True xalign 0.5
                text title color "#FF2D55" size 36 bold True xalign 0.5

            null height 10
            text explanation color "#CCCCCC" size 20 xalign 0.5 text_align 0.5

            null height 20

            textbutton "> CONTINUE MISSION":
                xalign 0.5
                text_style "menu_btn_text"
                action Return()


################################################################################
## MINIGAME 1: FIREWALL BREACH (Chapter 1) — REDESIGNED
## Cinematic NSA Workstation-style packet analysis minigame
################################################################################

init python:
    import time as _time

    # ── Packet Data ──────────────────────────────────────────────────────────
    def get_fw_packets():
        return [
            {
                "source_ip": "192.168.1.10", "port": 80, "protocol": "HTTP",
                "description": "Web Browser Request", "correct": "ALLOW",
                "risk_level": "LOW",
                "explanation": "Port 80 is standard HTTP web traffic from an internal IP. This is normal network activity — safe to allow."
            },
            {
                "source_ip": "10.0.0.5", "port": 443, "protocol": "HTTPS",
                "description": "Encrypted Web Traffic", "correct": "ALLOW",
                "risk_level": "LOW",
                "explanation": "Port 443 is HTTPS — secure, encrypted web traffic. Standard and safe."
            },
            {
                "source_ip": "45.33.32.1", "port": 31337, "protocol": "TCP",
                "description": "Unknown Connection", "correct": "BLOCK",
                "risk_level": "CRITICAL",
                "explanation": "Port 31337 is infamous in hacking culture (pronounced 'elite'). Used historically by Back Orifice malware. Always block unknown external IPs on this port."
            },
            {
                "source_ip": "172.16.0.1", "port": 22, "protocol": "SSH",
                "description": "Remote Login — Internal", "correct": "ALLOW",
                "risk_level": "MEDIUM",
                "explanation": "SSH on port 22 from a known internal IP (172.16.x.x is a private range) is a legitimate remote administration session."
            },
            {
                "source_ip": "89.248.174.5", "port": 4444, "protocol": "TCP",
                "description": "Suspicious Inbound", "correct": "BLOCK",
                "risk_level": "CRITICAL",
                "explanation": "Port 4444 is the default listener port for Metasploit — a common hacking framework. Foreign IP + port 4444 = almost certainly a reverse shell attempt. Block immediately."
            },
            {
                "source_ip": "10.0.0.12", "port": 53, "protocol": "DNS",
                "description": "Domain Name Lookup", "correct": "ALLOW",
                "risk_level": "LOW",
                "explanation": "DNS on port 53 from an internal IP is completely normal — computers need DNS to look up domain names and connect to websites."
            },
            {
                "source_ip": "203.0.113.99", "port": 23, "protocol": "Telnet",
                "description": "Legacy Protocol Connection", "correct": "BLOCK",
                "risk_level": "HIGH",
                "explanation": "Telnet sends ALL data in plain text — no encryption at all. It's outdated and dangerous. From a foreign IP, this is a clear intrusion attempt. Use SSH instead."
            },
            {
                "source_ip": "192.168.1.1", "port": 3389, "protocol": "RDP",
                "description": "Remote Desktop — Router", "correct": "ALLOW",
                "risk_level": "MEDIUM",
                "explanation": "RDP on port 3389 from the internal router IP (192.168.1.1) is internal remote desktop. Acceptable from a trusted internal source."
            },
        ]

    # ── Timer Class ──────────────────────────────────────────────────────────
    class PacketTimer(object):
        def __init__(self, max_time=15.0):
            self.max_time = max_time
            self.start_time = None
            self.active = False

        def start(self):
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

    # ── Game State ───────────────────────────────────────────────────────────
    fw_state = {
        "phase": "incoming",
        "current_index": 0,
        "score": 0,
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
        fw_state["allowed_count"] = 0
        fw_state["blocked_count"] = 0
        fw_state["answers"] = []
        fw_state["last_correct"] = False
        fw_state["timed_out"] = False
        fw_state["show_continue"] = False
        packet_timer.start()

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
            packet_timer.start()
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

# ── ATL Transforms ───────────────────────────────────────────────────────────

transform fw_packet_enter:
    xoffset 600 alpha 0.0
    ease 0.45 xoffset 0 alpha 1.0

transform fw_packet_exit_allow:
    ease 0.35 xoffset -700 alpha 0.0 zoom 0.92

transform fw_packet_exit_block:
    linear 0.06 xoffset 14
    linear 0.06 xoffset -14
    linear 0.06 xoffset 10
    linear 0.06 xoffset -10
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
    alpha 0.0 yoffset -20
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


# ── Main Firewall Minigame Screen ────────────────────────────────────────────

screen minigame_firewall():
    modal True

    # Reset state on first show
    on "show" action Function(fw_reset)

    add "#0A0E1A"

    # ── Scanline overlay (subtle) ────────────────────────────────────────
    for _sl_y in range(0, 720, 4):
        add Solid("#00000010"):
            xsize 1280 ysize 1
            xpos 0 ypos _sl_y

    # ══════════════════════════════════════════════════════════════════════
    #  PHASE: INCOMING / FEEDBACK (main gameplay)
    #  (Intro/skip is handled by the existing minigame_intro screen)
    # ══════════════════════════════════════════════════════════════════════
    if fw_state["phase"] in ("incoming", "feedback"):

        # Timer tick — refresh display for timer bar
        if fw_state["phase"] == "incoming":
            timer 0.1 repeat True action Function(renpy.restart_interaction)
            timer 15.0 action Function(fw_handle_timeout)

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
        $ _fw_risk = _fw_pkt["risk_level"]
        $ _fw_risk_col = fw_risk_color(_fw_risk)
        $ _fw_explanation = _fw_pkt["explanation"]
        $ _fw_correct = _fw_pkt["correct"]
        $ _fw_remaining = packet_timer.get_remaining()
        $ _fw_frac = packet_timer.get_fraction()
        $ _fw_timer_col = fw_timer_color()
        $ _fw_num = _fw_idx + 1
        $ _fw_score = fw_state["score"]

        # ── TOP HUD BAR ─────────────────────────────────────────────────
        frame:
            xfill True ysize 100
            xpos 0 ypos 0
            background "#0D1220EE"
            padding (30, 12)

            vbox:
                spacing 6

                # Title row
                hbox:
                    xfill True
                    text "// NSA NETWORK MONITOR //" color "#00FFD180" size 14 bold True yalign 0.5

                    hbox:
                        xalign 1.0
                        spacing 20
                        text "AUTHORIZED: [fw_state['allowed_count']]" color "#00FFD1" size 14 bold True yalign 0.5
                        text "BLOCKED: [fw_state['blocked_count']]" color "#FF2D55" size 14 bold True yalign 0.5
                        text "SCORE: [_fw_score]" color "#E8E8E8" size 14 bold True yalign 0.5

                # Progress dots
                hbox:
                    spacing 8
                    for _dot_i in range(8):
                        if _dot_i < _fw_idx:
                            # Completed
                            $ _dot_ans = fw_state["answers"][_dot_i] if _dot_i < len(fw_state["answers"]) else None
                            if _dot_ans and _dot_ans["is_correct"]:
                                text "●" color "#00FFD1" size 18
                            else:
                                text "●" color "#FF2D55" size 18
                        elif _dot_i == _fw_idx:
                            text "◆" color "#FFD700" size 18
                        else:
                            text "○" color "#555555" size 18

                    null width 20
                    text "PACKET [_fw_num] / 8" color "#888888" size 14 yalign 0.5

                # Timer bar
                if fw_state["phase"] == "incoming":
                    frame:
                        xfill True ysize 6
                        background "#1A1A2E"
                        padding (0, 0)

                        frame:
                            xsize int(1220 * _fw_frac)
                            ysize 6
                            background _fw_timer_col
                            xpos 0

                    $ _fw_secs = int(_fw_remaining)
                    text "[_fw_secs]s" color _fw_timer_col size 12 xalign 1.0
                else:
                    frame:
                        xfill True ysize 6
                        background "#1A1A2E"
                        padding (0, 0)

        # ── PACKET CARD ──────────────────────────────────────────────────
        # Use showif per packet index to trigger enter animation on change
        for _pc_i in range(8):
            showif fw_state["current_index"] == _pc_i and fw_state["phase"] in ("incoming", "feedback"):
                frame at fw_packet_enter:
                    xalign 0.5 yalign 0.42
                    xsize 820 ysize 280
                    background "#131928"
                    padding (0, 0)

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
                    text "◢" color "#00FFD140" size 14 xpos 6 ypos 2
                    text "◣" color "#00FFD140" size 14 xpos 798 ypos 2
                    text "◤" color "#00FFD140" size 14 xpos 6 ypos 258
                    text "◥" color "#00FFD140" size 14 xpos 798 ypos 258

                    vbox:
                        pos (0, 0)
                        xsize 820

                        # Threat level bar at top
                        $ _pc_pkts = get_fw_packets()
                        $ _pc_pkt = _pc_pkts[_pc_i]
                        $ _pc_risk = _pc_pkt["risk_level"]
                        $ _pc_rcol = fw_risk_color(_pc_risk)

                        hbox:
                            xfill True ysize 32
                            spacing 0

                            frame:
                                xsize 180 ysize 32
                                background _pc_rcol
                                padding (10, 4)
                                if _pc_risk == "CRITICAL":
                                    at fw_threat_blink
                                text "THREAT: [_pc_risk]" color "#0A0E1A" size 14 bold True yalign 0.5

                            frame:
                                xfill True ysize 32
                                background "#0D1220"
                                padding (15, 4)
                                $ _pc_desc = _pc_pkt["description"]
                                text "[_pc_desc]" color "#888888" size 14 yalign 0.5

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
                                text "SOURCE IP" color "#888888" size 12 bold True
                                $ _pc_ip = _pc_pkt["source_ip"]
                                text "[_pc_ip]" color "#00FFD1" size 26 bold True

                            # Port column
                            vbox:
                                xsize 200
                                spacing 4
                                text "PORT" color "#888888" size 12 bold True
                                $ _pc_port = str(_pc_pkt["port"])
                                text "[_pc_port]" color "#FFD700" size 30 bold True

                            # Protocol column
                            vbox:
                                xsize 250
                                spacing 4
                                text "PROTOCOL" color "#888888" size 12 bold True
                                $ _pc_proto = _pc_pkt["protocol"]
                                text "[_pc_proto]" color "#E8E8E8" size 26 bold True

                        null height 20

                        # Description line
                        hbox:
                            xoffset 30
                            text "CLASSIFICATION: " color "#555555" size 14
                            $ _pc_desc2 = _pc_pkt["description"]
                            text "[_pc_desc2]" color "#888888" size 14 italic True

                        # Feedback overlay on card
                        if fw_state["phase"] == "feedback" and fw_state["current_index"] == _pc_i:
                            null height 15
                            hbox:
                                xoffset 30
                                if fw_state["last_correct"]:
                                    text "✓ CORRECT ANALYSIS" color "#00FF88" size 16 bold True
                                else:
                                    text "✗ INCORRECT ANALYSIS" color "#FF2D55" size 16 bold True

        # ── ACTION BUTTONS ───────────────────────────────────────────────
        if fw_state["phase"] == "incoming":
            hbox at fw_fade_in:
                xalign 0.5 yalign 0.72
                spacing 60

                # ALLOW button
                frame:
                    xsize 220 ysize 70
                    background "#0D1220"
                    padding (0, 0)

                    # Border
                    add Solid("#00FFD140"):
                        xsize 220 ysize 1 xpos 0 ypos 0
                    add Solid("#00FFD140"):
                        xsize 220 ysize 1 xpos 0 ypos 69
                    add Solid("#00FFD140"):
                        xsize 1 ysize 70 xpos 0 ypos 0
                    add Solid("#00FFD140"):
                        xsize 1 ysize 70 xpos 219 ypos 0

                    textbutton "✓  ALLOW":
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
                    padding (0, 0)

                    add Solid("#FF2D5540"):
                        xsize 220 ysize 1 xpos 0 ypos 0
                    add Solid("#FF2D5540"):
                        xsize 220 ysize 1 xpos 0 ypos 69
                    add Solid("#FF2D5540"):
                        xsize 1 ysize 70 xpos 0 ypos 0
                    add Solid("#FF2D5540"):
                        xsize 1 ysize 70 xpos 219 ypos 0

                    textbutton "✗  BLOCK":
                        xalign 0.5 yalign 0.5
                        text_color "#FF2D55"
                        text_hover_color "#FFFFFF"
                        text_size 22
                        text_bold True
                        action Function(fw_evaluate, "BLOCK")

        # ── ANALYSIS TERMINAL (feedback) ─────────────────────────────────
        if fw_state["phase"] == "feedback":
            frame at fw_feedback_enter:
                xalign 0.5 yalign 0.82
                xsize 820 yminimum 120
                background "#0A0A14"
                padding (20, 15)

                # Terminal border
                add Solid("#00FFD130"):
                    xsize 820 ysize 1 xpos 0 ypos 0
                add Solid("#00FFD130"):
                    xsize 1 ysize 120 xpos 0 ypos 0

                vbox:
                    spacing 8

                    # Terminal header
                    text "> ANALYSIS TERMINAL" color "#00FFD180" size 12 bold True

                    if fw_state["timed_out"]:
                        text "{cps=40}⚠ TIME OUT — Packet auto-blocked (safe default){/cps}" color "#FFD700" size 16 bold True
                    elif fw_state["last_correct"]:
                        $ _fb_choice = fw_state["answers"][-1]["choice"]
                        if _fb_choice == "ALLOW":
                            text "{cps=40}✓ AUTHORIZATION GRANTED — Packet forwarded{/cps}" color "#00FF88" size 16 bold True
                        else:
                            text "{cps=40}✗ PACKET REJECTED — Firewall rule applied{/cps}" color "#00FFD1" size 16 bold True
                    else:
                        text "{cps=40}⚠ INCORRECT ANALYSIS — Review required{/cps}" color "#FF2D55" size 16 bold True

                    # Explanation
                    text "{cps=30}[_fw_explanation]{/cps}" color "#AAAAAA" size 15

                    if fw_state["last_correct"] and not fw_state["timed_out"]:
                        text "knowledge_score +1" color "#00FF8880" size 13

                    null height 5

                    # Continue button (delayed)
                    if fw_state["show_continue"]:
                        textbutton "> CONTINUE →":
                            text_color "#00FFD1"
                            text_hover_color "#FFFFFF"
                            text_size 16
                            text_bold True
                            action Function(fw_next_packet)
                    else:
                        hbox:
                            text "> Processing" color "#00FFD180" size 14
                            text " _" at fw_cursor_blink color "#00FFD1" size 14

        # ── Waiting prompt (incoming phase) ──────────────────────────────
        if fw_state["phase"] == "incoming":
            frame:
                xalign 0.5 yalign 0.82
                xsize 820 ysize 50
                background "#0A0A14"
                padding (20, 12)

                add Solid("#00FFD120"):
                    xsize 820 ysize 1 xpos 0 ypos 0

                hbox:
                    text "> Scanning packet... Awaiting your authorization" color "#00FFD160" size 14
                    text " _" at fw_cursor_blink color "#00FFD1" size 14

    # ══════════════════════════════════════════════════════════════════════
    #  PHASE: COMPLETE (Result / Mission Debrief)
    # ══════════════════════════════════════════════════════════════════════
    if fw_state["phase"] == "complete":
        $ _r_score = fw_state["score"]
        $ _r_allowed = fw_state["allowed_count"]
        $ _r_blocked = fw_state["blocked_count"]
        $ _r_grade, _r_bonus = fw_get_grade(_r_score)
        $ _r_answers = fw_state["answers"]

        frame at fw_result_enter:
            xfill True yfill True
            background "#0A0E1A"
            padding (40, 20)

            vbox:
                xalign 0.5
                spacing 10

                text "// FIREWALL ANALYSIS COMPLETE //" color "#00FFD1" size 28 bold True xalign 0.5

                # Mission outcome panel (compact)
                frame:
                    xalign 0.5 xsize 700
                    background "#131928"
                    padding (25, 15)

                    vbox:
                        spacing 6

                        text "MISSION OUTCOME" color "#E8E8E8" size 18 bold True xalign 0.5

                        hbox:
                            xfill True
                            text "Correctly Handled:" color "#AAAAAA" size 15
                            text "[_r_score] / 8" color "#00FFD1" size 15 bold True xalign 1.0

                        hbox:
                            xfill True
                            text "Allowed: [_r_allowed]   |   Blocked: [_r_blocked]" color "#888888" size 14

                        hbox:
                            xfill True
                            text "Knowledge Bonus:" color "#888888" size 15
                            text "+[_r_bonus]" color "#FFD700" size 15 bold True xalign 1.0

                # Grade display
                text "GRADE:" color "#888888" size 14 xalign 0.5

                if _r_score >= 7:
                    text "[_r_grade]" color "#00FF88" size 32 bold True xalign 0.5
                elif _r_score >= 5:
                    text "[_r_grade]" color "#00FFD1" size 32 bold True xalign 0.5
                elif _r_score >= 3:
                    text "[_r_grade]" color "#FFD700" size 32 bold True xalign 0.5
                else:
                    text "[_r_grade]" color "#FF2D55" size 32 bold True xalign 0.5

                # Per-packet breakdown (scrollable)
                frame:
                    xalign 0.5 xsize 700
                    background "#0D1220"
                    padding (15, 10)

                    viewport:
                        xfill True ysize 200
                        mousewheel True
                        scrollbars "vertical"

                        vbox:
                            spacing 4
                            text "─── PACKET LOG ───" color "#00FFD160" size 12 bold True

                            $ _r_pkts = get_fw_packets()
                            for _ri in range(8):
                                $ _rpkt = _r_pkts[_ri]
                                $ _rans = _r_answers[_ri] if _ri < len(_r_answers) else None

                                hbox:
                                    spacing 8
                                    if _rans and _rans["is_correct"]:
                                        text "✓" color "#00FF88" size 13 yalign 0.5
                                    else:
                                        text "✗" color "#FF2D55" size 13 yalign 0.5

                                    $ _r_ip = _rpkt["source_ip"]
                                    $ _r_pt = str(_rpkt["port"])
                                    $ _r_pr = _rpkt["protocol"]
                                    text "[_r_ip]:[_r_pt]" color "#00FFD1" size 12 yalign 0.5 xsize 180
                                    text "[_r_pr]" color "#E8E8E8" size 12 yalign 0.5 xsize 70

                                    if _rans:
                                        $ _r_ch = _rans["choice"]
                                        $ _r_co = _rans["correct_answer"]
                                        if _rans["is_correct"]:
                                            text "[_r_ch]" color "#00FF88" size 12 yalign 0.5
                                        else:
                                            text "[_r_ch] (should: [_r_co])" color "#FF2D55" size 12 yalign 0.5

                # Key takeaway (compact)
                frame:
                    xalign 0.5 xsize 700
                    background "#131928"
                    padding (15, 10)

                    vbox:
                        spacing 4
                        text "Dangerous ports: 31337, 4444, 23 (Telnet)" color "#FF2D55" size 13
                        text "Safe: HTTP(80), HTTPS(443), DNS(53), SSH/RDP from internal IPs" color "#00FF88" size 13

                null height 5

                # CONTINUE button — always visible at bottom
                textbutton "> CONTINUE MISSION":
                    xalign 0.5
                    text_color "#00FFD1"
                    text_hover_color "#FFFFFF"
                    text_size 22
                    text_bold True
                    action Return(_r_score)


################################################################################
## MINIGAME 2: DECRYPT THE MESSAGE (Chapter 2)
################################################################################

init python:
    def caesar_encrypt(text, shift):
        result = ""
        for ch in text:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                result += chr((ord(ch) - base + shift) % 26 + base)
            else:
                result += ch
        return result

    # The secret word to decrypt
    cipher_answer = "PRISM"
    cipher_text = caesar_encrypt(cipher_answer, 3)  # SULVP


screen minigame_decrypt():
    modal True
    default user_input = ""
    default submitted = False
    default is_correct = False
    default hint_shown = False
    default attempts = 0

    add "#0A0E1A"

    frame:
        xfill True yfill True
        background "#0A0E1A"
        padding (60, 60)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            text "// DECRYPT THE MESSAGE //" style "minigame_title"
            text "A classified document name has been encrypted using a Caesar cipher." style "minigame_instruction"

            null height 15

            frame:
                xalign 0.5
                xsize 700
                background "#111827"
                padding (30, 20)

                vbox:
                    spacing 15
                    text "ENCRYPTED TEXT:" color "#FF2D55" size 18 bold True
                    text "[cipher_text]" color "#00FFD1" size 48 bold True xalign 0.5
                    text "Cipher: ROT-3 (Caesar cipher, shift each letter BACK by 3)" color "#FFD700" size 18 xalign 0.5

            null height 10

            if hint_shown:
                text "HINT: This is the name of the NSA's mass surveillance program." color "#FFD700" size 18 xalign 0.5 italic True

            if not submitted:
                hbox:
                    xalign 0.5
                    spacing 10

                    text "> " color "#00FF00" size 24 yalign 0.5

                    input:
                        value ScreenVariableInputValue("user_input")
                        length 10
                        color "#00FFD1"
                        size 28
                        allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

                null height 10

                textbutton "> SUBMIT DECRYPTION":
                    xalign 0.5
                    text_style "menu_btn_text"
                    action [
                        SetScreenVariable("submitted", True),
                        SetScreenVariable("is_correct", (user_input.strip().upper() == cipher_answer)),
                        SetScreenVariable("attempts", attempts + 1)
                    ]

            else:
                if is_correct:
                    text "// DECRYPTION SUCCESSFUL //" color "#00FF00" size 28 bold True xalign 0.5
                    text "The classified program name is: PRISM" color "#00FFD1" size 24 xalign 0.5
                    text "PRISM allowed the NSA to collect data directly from major tech companies' servers, including emails, photos, and file transfers." color "#AAAAAA" size 18 xalign 0.5 text_align 0.5

                    null height 15

                    textbutton "> CONTINUE MISSION":
                        xalign 0.5
                        text_style "menu_btn_text"
                        action Return(True)

                else:
                    text "// DECRYPTION FAILED //" color "#FF2D55" size 28 bold True xalign 0.5
                    text "Your answer: [user_input]" color "#FF2D55" size 20 xalign 0.5

                    if attempts >= 3:
                        text "ANSWER REVEALED: PRISM" color "#FFD700" size 24 bold True xalign 0.5
                        text "The Caesar cipher shifts each letter. S→P, U→R, L→I, V→S, P→M = PRISM" color "#AAAAAA" size 18 xalign 0.5 text_align 0.5

                        null height 10

                        textbutton "> CONTINUE MISSION":
                            xalign 0.5
                            text_style "menu_btn_text"
                            action Return(False)
                    else:
                        if attempts >= 2:
                            $ hint_shown = True

                        textbutton "> TRY AGAIN":
                            xalign 0.5
                            text_style "menu_btn_text"
                            action [
                                SetScreenVariable("submitted", False),
                                SetScreenVariable("user_input", ""),
                                SetScreenVariable("hint_shown", attempts >= 1)
                            ]


################################################################################
## MINIGAME 3: OPSEC CHALLENGE (Chapter 3)
################################################################################

init python:
    def get_opsec_scenarios():
        return [
            {
                "action": "Agent X logged into his secure email from his home IP address without using a VPN.",
                "is_mistake": True,
                "reason": "Home IP can be traced directly to his identity by the ISA."
            },
            {
                "action": "Agent X used the Tor browser to access the journalist's SecureDrop site.",
                "is_mistake": False,
                "reason": "Tor anonymizes your connection through multiple relay nodes."
            },
            {
                "action": "Agent X sent the documents via regular email using his work address.",
                "is_mistake": True,
                "reason": "Work email is monitored and directly tied to his identity."
            },
            {
                "action": "Agent X created a new identity with a burner email, accessed from a public library.",
                "is_mistake": False,
                "reason": "Using a burner email from a public location helps maintain anonymity."
            },
            {
                "action": "Agent X reused his personal Facebook password for the encrypted file container.",
                "is_mistake": True,
                "reason": "Password reuse means if one account is compromised, all are compromised."
            },
        ]


screen minigame_opsec():
    modal True
    default scenarios = get_opsec_scenarios()
    default answers = {}
    default submitted = False

    add "#0A0E1A"

    frame:
        xfill True yfill True
        background "#0A0E1A"
        padding (50, 40)

        vbox:
            spacing 15

            text "// OPSEC CHALLENGE //" style "minigame_title"
            text "Review Agent X's actions. Mark each as SAFE or MISTAKE." style "minigame_instruction"

            null height 10

            viewport:
                ysize 700
                scrollbars "vertical"
                mousewheel True

                vbox:
                    spacing 15

                    for i, scenario in enumerate(scenarios):
                        frame:
                            xfill True
                            background "#111827"
                            padding (20, 15)

                            vbox:
                                spacing 10
                                text "Action [i+1]:" color "#00FFD1" size 16 bold True
                                text scenario["action"] color "#E8E8E8" size 18

                                if not submitted:
                                    hbox:
                                        spacing 15

                                        textbutton "✓ SAFE":
                                            text_size 18
                                            text_color ("#00FF00" if answers.get(i) == "safe" else "#555555")
                                            text_hover_color "#00FF00"
                                            action SetScreenVariable("answers", dict(list(answers.items()) + [(i, "safe")]))

                                        textbutton "✗ MISTAKE":
                                            text_size 18
                                            text_color ("#FF2D55" if answers.get(i) == "mistake" else "#555555")
                                            text_hover_color "#FF2D55"
                                            action SetScreenVariable("answers", dict(list(answers.items()) + [(i, "mistake")]))

                                else:
                                    $ user_ans = answers.get(i, "")
                                    $ correct_ans = "mistake" if scenario["is_mistake"] else "safe"
                                    $ got_it = (user_ans == correct_ans)

                                    if got_it:
                                        text "✓ CORRECT" color "#00FF00" size 16
                                    else:
                                        text "✗ INCORRECT — Should be: [correct_ans.upper()]" color "#FF2D55" size 16

                                    text scenario["reason"] color "#AAAAAA" size 15 italic True

            null height 10

            if not submitted:
                if len(answers) == len(scenarios):
                    textbutton "> SUBMIT ANALYSIS":
                        xalign 0.5
                        text_style "menu_btn_text"
                        action SetScreenVariable("submitted", True)
                else:
                    text "Mark all [len(scenarios)] actions to submit." color "#888888" size 18 xalign 0.5
            else:
                python:
                    opsec_score = 0
                    for idx, sc in enumerate(scenarios):
                        correct_a = "mistake" if sc["is_mistake"] else "safe"
                        if answers.get(idx) == correct_a:
                            opsec_score += 1

                text "Score: [opsec_score]/[len(scenarios)]" style "minigame_score"

                textbutton "> CONTINUE MISSION":
                    xalign 0.5
                    text_style "menu_btn_text"
                    action Return(opsec_score)


################################################################################
## MINIGAME 4: TRACE THE ROUTE (Chapter 4)
################################################################################

init python:
    def get_trace_nodes():
        return {
            "home":     {"name": "YOUR LAPTOP",      "x": 0.1,  "y": 0.5, "type": "start"},
            "isp":      {"name": "ISP ROUTER",       "x": 0.28, "y": 0.3, "type": "normal"},
            "vpn":      {"name": "VPN SERVER",        "x": 0.28, "y": 0.7, "type": "safe"},
            "tor1":     {"name": "TOR NODE 1",        "x": 0.46, "y": 0.25,"type": "safe"},
            "tor2":     {"name": "TOR NODE 2",        "x": 0.46, "y": 0.75,"type": "safe"},
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
    default nodes = get_trace_nodes()
    default current_node = "home"
    default path = ["home"]
    default moves = 0
    default max_moves = 5
    default hit_gov = False
    default reached_end = False

    add "#0A0E1A"

    frame:
        xfill True yfill True
        background "#0A0E1A"
        padding (40, 30)

        if not reached_end and not hit_gov and moves < max_moves:
            vbox:
                spacing 16

                text "// TRACE THE ROUTE //" style "minigame_title"
                text "Build a clean route to the journalist server. One bad hop sends everything through government eyes." style "minigame_instruction"

                hbox:
                    xfill True
                    spacing 16

                    frame:
                        xsize 330
                        background "#111827"
                        padding (20, 16)

                        vbox:
                            spacing 8
                            text "LIVE STATUS" color "#8B8FCC" size 16 bold True
                            text "[nodes[current_node]['name']]" color "#EAF4F1" size 28 bold True
                            text "Moves remaining: [max_moves - moves]/[max_moves]" color "#FFD700" size 18
                            text "Path: " + " -> ".join([nodes[n]["name"] for n in path]) color "#AAB0D6" size 15

                    frame:
                        xfill True
                        background "#111827"
                        padding (20, 16)

                        text trace_hint(current_node):
                            color "#EAF4F1"
                            size 19
                            xalign 0.5
                            text_align 0.5

                frame:
                    xfill True
                    ysize 420
                    background "#0D1220"
                    padding (24, 20)

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
                                padding (14, 10)

                                vbox:
                                    spacing 2
                                    text node["name"]:
                                        color ("#0A0E1A" if active else "#EAF4F1")
                                        size 18
                                        bold True
                                        xalign 0.5
                                        text_align 0.5

                                    text ("CURRENT" if active else "VISITED" if visited else node["type"].upper()):
                                        color ("#0A0E1A" if active else "#C8D8D0")
                                        size 13
                                        xalign 0.5

                frame:
                    xfill True
                    background "#111827"
                    padding (20, 18)

                    vbox:
                        spacing 12
                        text "AVAILABLE HOPS" color "#8B8FCC" size 17 bold True

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
                                    action [
                                        SetScreenVariable("current_node", next_node),
                                        SetScreenVariable("path", path + [next_node]),
                                        SetScreenVariable("moves", moves + 1),
                                        SetScreenVariable("hit_gov", next_node == "gov"),
                                        SetScreenVariable("reached_end", next_node == "target"),
                                    ]

        else:
            frame:
                xalign 0.5
                yalign 0.5
                xsize 940
                background "#111827"
                padding (32, 28)

                vbox:
                    spacing 14
                    xalign 0.5

                    if reached_end and not hit_gov:
                        text "// ROUTE SECURED //" color "#00FF88" size 38 bold True xalign 0.5
                        text "Path: " + " -> ".join([nodes[n]["name"] for n in path]) color "#00FFD1" size 18 xalign 0.5 text_align 0.5
                        text "You chained together the safer hops and kept the instructions away from the monitor." color "#C8D8D0" size 19 xalign 0.5 text_align 0.5
                    elif hit_gov:
                        text "// ROUTE COMPROMISED //" color "#FF2D55" size 38 bold True xalign 0.5
                        text "The route hit the Government Monitor node, so the mission is blown." color "#FF2D55" size 20 xalign 0.5 text_align 0.5
                        text "Even strong tools fail if one hop routes through a known surveillance point." color "#C8D8D0" size 19 xalign 0.5 text_align 0.5
                    else:
                        text "// OUT OF MOVES //" color "#FF2D55" size 38 bold True xalign 0.5
                        text "You ran out of time before reaching the journalist server." color "#FF2D55" size 20 xalign 0.5 text_align 0.5
                        text "Tight, efficient routing matters. Extra hops create delay and more chances to get exposed." color "#C8D8D0" size 19 xalign 0.5 text_align 0.5

                    textbutton "> CONTINUE MISSION":
                        xalign 0.5
                        text_style "menu_btn_text"
                        action Return(reached_end and not hit_gov)
