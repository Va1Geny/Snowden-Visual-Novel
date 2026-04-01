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
## MINIGAME 1: FIREWALL BREACH (Chapter 1)
################################################################################

init python:
    import random

    # Packet data for firewall minigame
    def get_firewall_packets():
        packets = [
            {"src": "192.168.1.10", "port": "80", "proto": "HTTP",  "legit": True,  "reason": "Standard web traffic on port 80"},
            {"src": "10.0.0.5",     "port": "443", "proto": "HTTPS", "legit": True,  "reason": "Encrypted web traffic on port 443"},
            {"src": "45.33.32.1",   "port": "31337", "proto": "TCP", "legit": False, "reason": "Port 31337 is associated with Back Orifice trojan"},
            {"src": "172.16.0.1",   "port": "22",  "proto": "SSH",   "legit": True,  "reason": "SSH remote admin from internal network"},
            {"src": "89.248.174.5", "port": "4444", "proto": "TCP",  "legit": False, "reason": "Port 4444 is commonly used by Metasploit/malware"},
            {"src": "10.0.0.12",    "port": "53",  "proto": "DNS",   "legit": True,  "reason": "DNS resolution from internal server"},
            {"src": "203.0.113.99", "port": "23",  "proto": "Telnet","legit": False, "reason": "Telnet from external IP — unencrypted remote access"},
            {"src": "192.168.1.1",  "port": "3389","proto": "RDP",   "legit": True,  "reason": "Internal Remote Desktop within the LAN"},
        ]
        return packets


screen minigame_firewall():
    modal True
    default packets = get_firewall_packets()
    default answers = {}
    default submitted = False
    default score = 0

    add "#0A0E1A"

    frame:
        xfill True yfill True
        background "#0A0E1A"
        padding (40, 30)

        vbox:
            spacing 10

            # Header
            text "// FIREWALL BREACH CHALLENGE //" style "minigame_title"
            text "Analyze each incoming packet. ALLOW legitimate traffic. BLOCK suspicious packets." style "minigame_instruction"

            null height 10

            # Column headers
            hbox:
                xfill True
                spacing 10
                text "SOURCE IP" color "#888888" size 16 bold True xsize 200
                text "PORT" color "#888888" size 16 bold True xsize 100
                text "PROTOCOL" color "#888888" size 16 bold True xsize 120
                text "ACTION" color "#888888" size 16 bold True xsize 300

            null height 5

            # Packet rows
            for i, pkt in enumerate(packets):
                hbox:
                    xfill True
                    spacing 10
                    ysize 50

                    $ src_ip = pkt["src"]
                    $ port_num = pkt["port"]
                    $ proto_name = pkt["proto"]
                    text "[src_ip]" color "#00FFD1" size 16 yalign 0.5 xsize 200
                    text "[port_num]" color "#FFD700" size 16 yalign 0.5 xsize 100
                    text "[proto_name]" color "#E8E8E8" size 16 yalign 0.5 xsize 120

                    if not submitted:
                        hbox:
                            spacing 10
                            yalign 0.5
                            xsize 300

                            textbutton "ALLOW":
                                text_size 16
                                text_color ("#00FF00" if answers.get(i) == "allow" else "#555555")
                                text_hover_color "#00FF00"
                                action SetScreenVariable("answers", dict(list(answers.items()) + [(i, "allow")]))

                            textbutton "BLOCK":
                                text_size 16
                                text_color ("#FF2D55" if answers.get(i) == "block" else "#555555")
                                text_hover_color "#FF2D55"
                                action SetScreenVariable("answers", dict(list(answers.items()) + [(i, "block")]))
                    else:
                        hbox:
                            spacing 10
                            yalign 0.5
                            xsize 300

                            $ user_ans = answers.get(i, "")
                            $ correct = "allow" if pkt["legit"] else "block"
                            $ is_correct = (user_ans == correct)

                            if is_correct:
                                text "✓ CORRECT" color "#00FF00" size 16
                            else:
                                text "✗ WRONG" color "#FF2D55" size 16

            null height 15

            if not submitted:
                if len(answers) == len(packets):
                    textbutton "> SUBMIT ANALYSIS":
                        xalign 0.5
                        text_style "menu_btn_text"
                        action [SetScreenVariable("submitted", True)]
                else:
                    text "Select ALLOW or BLOCK for all [len(packets)] packets to submit." color "#888888" size 18 xalign 0.5

            else:
                # Calculate score
                python:
                    fw_score = 0
                    for idx, pkt in enumerate(packets):
                        correct_action = "allow" if pkt["legit"] else "block"
                        if answers.get(idx) == correct_action:
                            fw_score += 1

                text "Score: [fw_score]/[len(packets)]" style "minigame_score"

                null height 5

                # Show explanations
                viewport:
                    ysize 200
                    scrollbars "vertical"
                    mousewheel True

                    vbox:
                        spacing 5
                        for i, pkt in enumerate(packets):
                            $ correct = "ALLOW" if pkt["legit"] else "BLOCK"
                            $ p_port = pkt["port"]
                            $ p_proto = pkt["proto"]
                            $ p_reason = pkt["reason"]
                            text "Port [p_port] ([p_proto]): [correct] — [p_reason]" color "#AAAAAA" size 14

                null height 10

                textbutton "> CONTINUE MISSION":
                    xalign 0.5
                    text_style "menu_btn_text"
                    action Return(fw_score)


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


screen minigame_trace():
    modal True
    default nodes = get_trace_nodes()
    default current_node = "home"
    default path = ["home"]
    default moves = 0
    default max_moves = 4
    default hit_gov = False
    default reached_end = False

    add "#0A0E1A"

    frame:
        xfill True yfill True
        background "#0A0E1A"
        padding (40, 30)

        vbox:
            spacing 10

            text "// TRACE THE ROUTE //" style "minigame_title"
            text "Route your connection to the Journalist Server. Avoid the Government Monitor node!" style "minigame_instruction"
            text "Moves remaining: [max_moves - moves]/[max_moves]" color "#FFD700" size 18 xalign 0.5

            null height 5

            if not reached_end and not hit_gov and moves < max_moves:
                # Show current position and options
                frame:
                    xfill True
                    background "#111827"
                    padding (20, 15)

                    vbox:
                        spacing 10
                        $ cn = nodes[current_node]
                        $ cn_name = cn["name"]
                        text "Current Location: [cn_name]" color "#00FFD1" size 22 bold True

                        text "Path taken: " + " → ".join([nodes[n]["name"] for n in path]) color "#888888" size 16

                        null height 10
                        text "Available Routes:" color "#E8E8E8" size 20

                        if current_node in safe_connections:
                            for next_node in safe_connections[current_node]:
                                $ nn = nodes[next_node]
                                $ nn_name = nn["name"]
                                $ node_color = "#FF2D55" if nn["type"] == "danger" else ("#00FFD1" if nn["type"] == "safe" else ("#FFD700" if nn["type"] == "end" else "#E8E8E8"))

                                textbutton "> [nn_name]":
                                    text_size 20
                                    text_color node_color
                                    text_hover_color "#FFFFFF"
                                    action [
                                        SetScreenVariable("current_node", next_node),
                                        SetScreenVariable("path", path + [next_node]),
                                        SetScreenVariable("moves", moves + 1),
                                        SetScreenVariable("hit_gov", next_node == "gov"),
                                        SetScreenVariable("reached_end", next_node == "target"),
                                    ]

            elif reached_end and not hit_gov:
                # Success!
                text "// ROUTE SECURED //" color "#00FF00" size 36 bold True xalign 0.5

                null height 10

                text "Path: " + " → ".join([nodes[n]["name"] for n in path]) color "#00FFD1" size 18 xalign 0.5
                text "You successfully routed through secure nodes, avoiding government surveillance!" color "#AAAAAA" size 18 xalign 0.5 text_align 0.5

                null height 15

                textbutton "> CONTINUE MISSION":
                    xalign 0.5
                    text_style "menu_btn_text"
                    action Return(True)

            elif hit_gov:
                # Hit government monitor
                text "// ROUTE COMPROMISED //" color "#FF2D55" size 36 bold True xalign 0.5

                null height 10

                text "Your traffic passed through the Government Monitor node!" color "#FF2D55" size 20 xalign 0.5
                text "In real networks, government surveillance nodes can inspect unencrypted traffic. Always use VPN and Tor to route around known monitoring points." color "#AAAAAA" size 18 xalign 0.5 text_align 0.5

                null height 15

                textbutton "> CONTINUE MISSION":
                    xalign 0.5
                    text_style "menu_btn_text"
                    action Return(False)

            else:
                # Out of moves
                text "// OUT OF MOVES //" color "#FF2D55" size 36 bold True xalign 0.5

                null height 10

                text "You ran out of routing moves before reaching the target." color "#FF2D55" size 20 xalign 0.5
                text "Efficient routing is critical in network security. Every extra hop increases latency and detection risk." color "#AAAAAA" size 18 xalign 0.5 text_align 0.5

                null height 15

                textbutton "> CONTINUE MISSION":
                    xalign 0.5
                    text_style "menu_btn_text"
                    action Return(False)
