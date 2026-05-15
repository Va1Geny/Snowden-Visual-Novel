################################################################################
## SCRIPT.RPY — Main Game Script (All 5 Chapters + Introduction)
## Classified: The Snowden Files
################################################################################

################################################################################
## GAME START
################################################################################

label start:
    show screen secret_ending_shortcut
    $ show_hud = False
    $ notebook_entries = []
    $ notebook_draft = ""
    if not english_voice_bootstrap_done:
        $ preferences.set_volume("voice", 1.0)
        $ english_voice_bootstrap_done = True
    $ translation_service.current_language()
    $ suspicion_lockdown_triggered = False
    $ tree_reset_current_run()
    if not preferences.fullscreen:
        call screen intro_fullscreen_prompt
    call screen intro_shortcuts_screen
    jump intro


################################################################################
## INTRODUCTION SEQUENCE
################################################################################

label intro:
    scene black
    show expression "images/ui/headphones_icon.png" as headphones_icon:
        xalign 0.5 yalign 0.5
        zoom 0.5
    show text "{font=fonts/ShareTechMono-Regular.ttf}{size=+5}{color=#00FFD1}Better experience with headphones.{/color}{/size}{/font}" as headphones_text:
        xalign 0.5 yalign 0.85
    with dissolve

    $ renpy.pause()

    hide headphones_icon
    hide headphones_text
    with dissolve

    scene black
    with fade
    $ renpy.pause(1.0, hard=True)

    show logo_watermark

    $ renpy.pause(0.5)

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0040_centered_b2e91c2074.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    centered "{i}\"The greatest fear I have regarding the outcome of these disclosures\nis that nothing will change.\"{/i}\n\n— Edward Snowden"

    $ renpy.pause(3.0)

    scene black with dissolve
    $ renpy.pause(1.0, hard=True)
    show logo_watermark

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0048_narrator_voice_60d854ee2d.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The year is 2013."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0050_narrator_voice_3d785b1c36.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The United States government operates the most sophisticated surveillance network in human history."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0052_narrator_voice_0514bcc733.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "Billions of phone calls, emails, and internet sessions are collected, analyzed, and stored — all in the name of national security."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0054_narrator_voice_e2cd9c5f7e.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You are an NSA contractor, a former CIA employee — and the person about to make the most consequential decision of your life."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0056_narrator_voice_f2819080db.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "Your choices in this story mirror the real dilemmas Snowden faced. Some paths lead to freedom. Others lead to ruin."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0058_narrator_voice_07620b7385.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "Along the way, your knowledge of network security will be tested. Every correct answer moves you closer to the truth."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0060_narrator_voice_280f9cef5e.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "Pay attention. Think carefully. The skills you learn here are real — and in the digital age, they matter."

    jump chapter_1


################################################################################
##  ██████╗██╗  ██╗ ██╗
## ██╔════╝██║  ██║███║
## ██║     ███████║╚██║
## ██║     ██╔══██║ ██║
## ╚██████╗██║  ██║ ██║
##  ╚═════╝╚═╝  ╚═╝ ╚═╝
## CHAPTER 1: INSIDE THE MACHINE
################################################################################

label chapter_1:
    call show_loading_screen
    $ current_chapter = 1
    $ persistent.tree_ch_reached = max(getattr(persistent, 'tree_ch_reached', 0), 1)

    call screen chapter_transition(chapter_num=1, codename="INSIDE THE MACHINE", location="Fort Meade, Maryland, USA", date="June 2013", time_str="09:14 EST", clearance="TOP SECRET // SCI", description="Edward Snowden begins his final day at the NSA.\nThe PRISM surveillance program is fully\noperational. The files are within reach —\nbut so are the eyes of the agency.", status="ACTIVE", bg_image="bg_nsa_exterior")
    $ show_hud = True
    $ quick_menu = True


    scene bg_nsa_exterior at parallax with chapter_transition

    # --- Scene: Arriving at the NSA ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0090_narrator_voice_730bbdeb62.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The Tunnel. That's what they call it — the underground NSA facility beneath a pineapple field in Oahu, Hawaii."

    scene bg_nsa_checkpoint at parallax with dissolve
    $ localized_voice = voice_for_current_language("audio/voice/en/script_0093_narrator_voice_75301c64a2.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You walk through layers of biometric security. Badge. Fingerprint. Retinal scan. The door hisses open."

    scene bg_nsa_main at parallax with dissolve
    show edward neutral at enter_center
    with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0099_im_6b61024b7f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Another day inside the machine. Rows of monitors tracking billions of data points. Every packet, every connection, every digital breath."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0101_im_ebcb5237fc.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "I'm a systems administrator — I keep this infrastructure running. The irony is, the more access I have to maintain the system, the more I see what the system actually does."

    show supervisor neutral at enter_right
    with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0106_supervisor_e79ba05711.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    supervisor "Morning. We've got a batch of flagged selectors to process. XKeyscore caught some interesting traffic overnight."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0108_im_82ac04ca10.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "XKeyscore — the NSA's most powerful search tool. It can search virtually anything a person does on the internet: emails, browsing history, chat sessions, even webcam feeds. All in near real time, all without a warrant."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0110_e_4e0609bf0c.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    e "Yes sir. I'll pull up the queue."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0112_supervisor_f938148bc0.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    supervisor "And don't overthink the 'why.' If the system flags a packet, it's because the math says they're a threat. Your job is to verify the handshake, not question the person."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0114_im_8674c5c462.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Verify the handshake. That's NSA-speak for confirming the network connection is legitimate — checking that the source and destination match the selector criteria. But nobody asks whether the criteria themselves are legitimate."

    show colleague casual at enter_left
    with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0119_colleague_123e1203e7.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    colleague "Hey Ed. Check this out — I can watch this guy's webcam feed in real time. He's just eating cereal. It's wild what we can access without even a targeted request."

    show edward concerned

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0123_e_274a3d437d.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    e "That's... that's a lot of access for an unflagged individual."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0125_colleague_d5cd461592.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    colleague "Welcome to the NSA, man. Everything is accessible. Everything."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0127_im_1b9db96e27.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "The scale of it is staggering. This isn't targeted surveillance. This is a vacuum cleaner, sucking up everything. Emails, phone records, browsing histories — all stored, all searchable, all belonging to ordinary people who've done nothing wrong."

    # --- Choice 1: Follow protocol or explore restricted files? ---
    hide colleague with dissolve
    hide supervisor with dissolve

    menu:
        "Follow protocol. Process the flagged selectors as assigned.":
            $ tree_record_choice("choice_ch1_1", "protocol")
            $ localized_voice = voice_for_current_language("audio/voice/en/script_0136_e_2a2ed285bb.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            e "Alright, let's focus on the assignment. Processing the flagged selectors now."
            $ trust_score += 1
            $ renpy.notify(t("Trust +1"))

            scene bg_nsa_terminal at parallax with dissolve
            with dissolve

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0143_im_b6beac96b3.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            im "Stay in your lane. Do your job. Don't attract attention."

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0145_narrator_voice_7527edd93e.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            narrator_voice "You process the assigned selectors. Standard targets. Foreign IP addresses. But among the flagged traffic, domestic addresses keep appearing."

        "Explore the restricted directories. Something doesn't add up.":
            $ tree_record_choice("choice_ch1_1", "explore")
            $ localized_voice = voice_for_current_language("audio/voice/en/script_0149_e_28ce7bd45d.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            e "I need to check something first..."
            $ suspicion_level += 1
            $ renpy.notify(t("Suspicion +1"))

            scene bg_nsa_terminal at parallax with dissolve
            with dissolve

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0156_im_0d6c45c0a5.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            im "These directories shouldn't be this easy to access. Why does a systems administrator have read access to raw intelligence feeds?"

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0158_narrator_voice_0f4ff8ada0.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            narrator_voice "You navigate deeper into the classified file system. Folders upon folders of surveillance programs you've never been briefed on. The scope is enormous."

    # --- Tutorial Exposition: Firewall Learning Section ---
    # (Structured as a self-contained briefing — can be branched into the story tree later)

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0163_narrator_voice_55e820c9e1.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "On your screen, you see the tools of the trade: network monitoring dashboards tracking millions of connections in real time."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0165_im_88a9681d41.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Every network has a firewall — a security system that monitors all incoming and outgoing traffic and decides what gets through based on predefined rules. Think of it as a barrier between trusted and untrusted networks."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0167_im_c3fd13aeda.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "The firewall inspects each packet for three things: the source IP address, the destination port number, and the protocol. Get those right and you can tell the difference between normal traffic and an intrusion attempt."

    # --- IP Addresses: Internal vs External ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0171_im_2013b1f408.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "First, IP addresses. Every device on a network has one — it's like a street address for computers. But not all addresses are equal."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0173_im_edf8b3a762.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Private IP ranges — 192.168.x.x, 10.0.x.x, and 172.16.x.x — belong to your own internal network. Traffic from these addresses is usually safe because it's coming from inside the building."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0175_im_796675d30e.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "But an IP like 45.33.32.1 or 89.248.174.5? That's an external address — someone on the internet reaching into our network. External IPs demand much more scrutiny."

    sys "// SYSTEM NOTE: Private IPs (192.168.x.x, 10.0.x.x, 172.16.x.x) = internal/trusted. Public IPs = external/unknown — verify before allowing. //"

    # --- Ports: The Doors Into a Network ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0181_im_d3aa9c6d0f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Next, ports. If an IP address is the building's street address, a port is a specific door. Every network service listens on a numbered port, and knowing which port does what is fundamental."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0183_im_0e6a89781b.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Port 80 is HTTP — standard, unencrypted web traffic. Port 443 is HTTPS — the same thing but encrypted with TLS. These are the two most common ports on the internet, and traffic on them is usually legitimate."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0185_im_2d2267f668.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Port 53 is DNS — the Domain Name System. It's how computers translate website names like 'google.com' into IP addresses. Without DNS, nothing works. It's the phone book of the internet."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0187_im_aacc2024d6.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Port 22 is SSH — Secure Shell. It's used for remote administration, letting an authorised user log into a server from another location. From an internal IP, it's normal. From an external IP, it needs careful review."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0189_im_895740dd12.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Port 3389 is RDP — Remote Desktop Protocol. It lets someone control a computer's desktop remotely. Like SSH, it's fine from a trusted internal source, but dangerous if exposed to the outside."

    sys "// SAFE PORTS (common services): 80 = HTTP | 443 = HTTPS | 53 = DNS | 22 = SSH | 3389 = RDP //"

    # --- Dangerous Ports and Protocols ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0195_im_54ee849d2d.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Then there are the ports that should set off alarm bells. Port 23 is Telnet — an ancient protocol that sends everything in plain text, including passwords. It has no encryption at all. Telnet should never be used; SSH replaced it decades ago."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0197_im_9b9f20b60c.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Port 31337 — pronounced 'elite' in hacker culture — is historically associated with the Back Orifice trojan. If you see traffic on port 31337 from an unknown external IP, it's almost certainly malicious."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0199_im_9200dbe497.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "And port 4444 — the default listener for Metasploit, one of the most widely used hacking frameworks. An external IP connecting on port 4444 usually means someone is trying to establish a reverse shell — giving themselves remote control of the target machine."

    sys "// DANGER PORTS: 23 = Telnet (unencrypted!) | 31337 = Known hacker port | 4444 = Metasploit reverse shell //"

    # --- Putting It Together ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0205_im_7d99182ac5.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "So the logic is straightforward: check the IP, check the port, check the protocol. Internal IP on a standard port? Probably safe. External IP on a suspicious port with no encryption? Block it immediately."

    sys "// FIREWALL RULE: ALLOW = internal IPs on standard ports | BLOCK = external IPs on suspicious ports or unencrypted protocols. When in doubt, block. //"

    # --- Minigame 1: Firewall Breach ---

    window hide
    $ mg_intro = renpy.call_screen("minigame_briefing", challenge_title="FIREWALL BREACH", subtitle="Eight packets. Eight decisions.\nOne wrong call exposes the network.", mission_id="OPS-01-01-2013", classification="TOP SECRET // SCI", challenge_type="NETWORK SECURITY", estimated_time="60-90 SECONDS", difficulty=2, difficulty_label="ANALYST", succeed_reward="knowledge_score +2", fail_penalty="suspicion_level +1", learn_concept="Firewalls filter traffic using ports,\nIP addresses, and protocol rules.", briefing_text="You are monitoring the NSA firewall.\nIncoming data packets are attempting to enter the network.\n\nEach packet shows three pieces of information:\n  WHERE it is coming from  (IP address)\n  Which DOOR it is using   (Port number)\n  What TYPE of data it is  (Protocol)\n\nYour job: decide ALLOW or BLOCK for each packet.", controls=[("ALLOW", "Permit the packet through"),("BLOCK", "Reject the packet")])

    if mg_intro:
        $ quick_menu = False
        $ show_hud = False
        $ mg_firewall_score = renpy.call_screen("minigame_firewall")
        $ quick_menu = True
        $ show_hud = True
        if mg_firewall_score == "SKIP":
            $ renpy.notify(t("Minigame Skipped"))
        elif mg_firewall_score >= 6:
            $ knowledge_score += 2
            $ renpy.notify(t("Knowledge +2"))
            sys "// CHALLENGE PASSED. Your firewall analysis was solid. //"
        else:
            $ suspicion_level += 1
            $ renpy.notify(t("Suspicion +1"))
            sys "// CHALLENGE FAILED. Poor packet filtering leaves the network vulnerable. //"
    else:
        $ knowledge_score -= 1
        $ renpy.notify(t("Knowledge -1 (Skipped)"))

    # --- Question Segment 1: MCQ ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0236_im_551dbc9b15.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Working here, I've learned how critical a VPN is. A VPN — Virtual Private Network — creates an encrypted tunnel between your device and a remote server. Anyone watching the local network sees only scrambled data, not what you're actually doing."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0238_im_f19aee1fb7.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "On untrusted networks like public Wi-Fi, a VPN is essential. Without one, your browsing history, login credentials, and private messages are all visible to anyone sniffing the network."

    call screen mcq_question(
        question=t("What does VPN stand for?"),
        answers=[t("Virtual Private Network"), t("Verified Protocol Node"), t("Virtual Program Network"), t("Variable Packet Node")],
        correct_index=0,
        explanation=t("A VPN (Virtual Private Network) creates an encrypted tunnel between your device and a VPN server, protecting your traffic from surveillance on the local network.")
    )

    # --- Choice 2: Report anomaly or stay silent? ---
    show supervisor stern at enter_right
    with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0251_narrator_voice_b4f3cc6714.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "While processing selectors, you discover domestic IP addresses mixed in with foreign intelligence targets."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0253_e_920d6dda17.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    e "Sir, I'm seeing domestic addresses in the foreign intelligence queue. These are American citizens."

    if suspicion_level >= 2:
        $ localized_voice = voice_for_current_language("audio/voice/en/script_0256_supervisor_4f94ab31cb.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        supervisor "I've noticed you've been poking around where you shouldn't. Are you having second thoughts about your oath?"
        $ localized_voice = voice_for_current_language("audio/voice/en/script_0257_e_e164b6aaa5.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        e "No sir. Just doing my due diligence."
        $ localized_voice = voice_for_current_language("audio/voice/en/script_0258_supervisor_eaf33e4822.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        supervisor "Your 'due diligence' is noted. Logged and noted."
        $ suspicion_level += 1
        $ renpy.notify(t("Suspicion +1"))
    else:
        $ localized_voice = voice_for_current_language("audio/voice/en/script_0262_supervisor_fe38e0aa8f.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        supervisor "Those addresses were flagged by the FISA court authorization. Everything is legal. Don't make waves."

    menu:
        "Report the anomaly to the Inspector General's office.":
            $ tree_record_choice("choice_ch1_2", "report")
            $ localized_voice = voice_for_current_language("audio/voice/en/script_0267_e_29b9cdba6a.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            e "I should file a formal concern with the IG office."
            $ trust_score += 2
            $ renpy.notify(t("Trust +2"))

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0271_supervisor_974b128c9d.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            supervisor "Do what you have to do. But I'm telling you, this goes nowhere."

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0273_im_2fa34f15b6.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            im "I filed the report. I used the proper channels. And nothing happened. Nothing."

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0275_narrator_voice_3199460e04.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            narrator_voice "The report was acknowledged, reviewed, and buried. The system protects itself."

        "Stay silent. Keep working. Gather more information.":
            $ tree_record_choice("choice_ch1_2", "silent")
            scene bg_1 at parallax with dissolve
            $ localized_voice = voice_for_current_language("audio/voice/en/script_0280_im_c8fb179fad.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            im "Not yet. I need to understand the full scope before I act. If I report one anomaly, they'll lock me out. I need to see the whole picture."
            $ trust_score -= 1
            $ renpy.notify(t("Trust -1"))

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0284_narrator_voice_6162d06c6d.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            narrator_voice "You continue working in silence, but your eyes are open. Every day reveals more."

    hide supervisor neutral with dissolve
    hide edward neutral with dissolve

    # --- Chapter 1 Summary ---

    if knowledge_score >= 2 and trust_score >= 1:
        $ ch1_outcome = "good"
    else:
        $ ch1_outcome = "bad"

    $ autosave_chapter(1)

    jump chapter_2


################################################################################
##  ██████╗██╗  ██╗██████╗
## ██╔════╝██║  ██║╚════██╗
## ██║     ███████║ █████╔╝
## ██║     ██╔══██║██╔═══╝
## ╚██████╗██║  ██║███████╗
##  ╚═════╝╚═╝  ╚═╝╚══════╝
## CHAPTER 2: THE PRISM REVELATION
################################################################################

label chapter_2:
    call show_loading_screen
    $ current_chapter = 2
    $ persistent.tree_ch_reached = max(getattr(persistent, 'tree_ch_reached', 0), 2)

    call screen chapter_transition(chapter_num=2, codename="THE PRISM REVELATION", location="NSA Data Center, Fort Meade", date="June 5, 2013", time_str="23:47 EST", clearance="TOP SECRET // SCI // PRISM", description="The full scope of the surveillance program\nbecomes clear. Millions of citizens monitored\nwithout warrants. Snowden must decide:\nstay silent, or act.", status="ACTIVE", bg_image="bg_prism")
    $ show_hud = True
    $ quick_menu = True


    scene bg_prism at parallax with chapter_transition

    with dissolve

    # --- Snowden discovers PRISM ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0327_im_467385a3d7.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "I found it. Hidden in the classified briefing materials — a program so vast it makes everything else look like a hobby project."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0329_im_a3ba63fb1d.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "They call it PRISM — a direct pipeline into the servers of every major tech company. Google. Facebook. Apple. Microsoft. Yahoo. All of them. Nine companies in total, handing over user data on demand."

    sys "// CLASSIFIED: PRISM — Planning Tool for Resource Integration, Synchronization, and Management. Direct server access to 9 major internet service providers. //"

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0333_im_96b271d7d3.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "We aren't looking for needles in haystacks. We're just stealing the whole field. Every email, every photo, every chat message — all vacuumed up and stored in data centres the size of small cities."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0335_narrator_voice_fc3d2e8786.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The PRISM program gave the NSA direct access to user data from the world's largest tech companies. Emails, chat logs, file transfers, photos — all accessible without individual warrants. The legal basis? A secret interpretation of the FISA Amendments Act that no court had publicly reviewed."

    sys "// SYSTEM NOTE: PRISM worked by collecting data 'upstream' — directly from fiber-optic cables and company servers, bypassing traditional warrant requirements through the FISA Amendments Act. //"

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0339_im_568527215f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "And there's more. Boundless Informant — a tool that counts and visualises exactly how much data the NSA collects from each country. In one month alone, 97 billion pieces of intelligence were gathered worldwide. The American public has no idea."

    # --- Internal conflict with colleague ---
    show colleague uneasy at enter_left
    with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0345_colleague_5d696f38ce.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    colleague "Ed, you look like you've seen a ghost. What's wrong?"

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0347_e_b847e376d8.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    e "Have you ever looked at what we're actually collecting? Not the reports. The raw feeds."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0349_colleague_ee118b8d6e.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    colleague "I try not to think about it too much. We've got clearance, we've got authorization. That's enough for me."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0351_e_1d3fd0f3e3.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    e "Is it? Because what I'm seeing goes way beyond foreign intelligence. This is domestic surveillance on a massive scale."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0353_colleague_f68db9361d.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    colleague "Ed... be very careful what you say next. The walls have ears. Literally."

    scene bg_prism1 at parallax with dissolve

    # --- Choice 1: Trust colleague or work alone? ---

    menu:
        "Trust the colleague. Share what you've found.":
            $ tree_record_choice("choice_ch2_1", "trust")
            $ localized_voice = voice_for_current_language("audio/voice/en/script_0362_e_da3c043e07.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            e "Look, I need someone I can trust. What I've found... it's bigger than both of us."
            $ trust_score += 1
            $ renpy.notify(t("Trust +1"))

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0366_colleague_dd16107ec9.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            colleague "I... I've had my own doubts. But Ed, if you're thinking what I think you're thinking, you need to be incredibly careful."

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0368_colleague_5298fbaa8d.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            colleague "Whatever you do, don't use the internal network. They monitor everything. Every keystroke."

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0370_im_60f0d439b8.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            im "At least I'm not completely alone in this."

        "Work alone. Trust no one inside the NSA.":
            $ tree_record_choice("choice_ch2_1", "alone")
            $ localized_voice = voice_for_current_language("audio/voice/en/script_0374_e_0d3f8c6717.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            e "Never mind. Forget I said anything. Just tired."
            $ suspicion_level += 0
            $ trust_score -= 1
            $ renpy.notify(t("Trust -1"))

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0379_colleague_f0450ba0a8.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            colleague "Sure, man. Get some rest."

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0381_im_8f40e62992.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            im "I can't trust anyone here. One wrong word and I'm done. I need to do this alone."

    hide colleague neutral with dissolve

    # --- Question Segment 2: Text Input ---

    $ tiq_reset()
    $ tiq_result = renpy.call_screen(
        "text_input_question",
        chapter_num    = "02",
        chapter_name   = t("The PRISM Revelation"),
        question_text  = t("Type the codename of the surveillance\nprogram you found:"),
        hint_text      = t("It's named after a glass object that splits light into a spectrum..."),
        check_type     = "Text Input",
        difficulty     = "Easy",
        reward_label   = "+1 Knowledge",
        reward_color   = "green",
        correct_answer = "PRISM",
        explanation    = t("PRISM was the codename for the NSA program that collected user data from major tech platforms."),
        allow_skip     = True
    )
    if tiq_result == "continue" and tiq_is_correct:
        $ knowledge_score += 1
        $ renpy.notify(t("Knowledge +1"))

    # --- Minigame 2: Decrypt the Message — Learning Section ---
    # (Structured as a self-contained briefing — can be branched into the story tree later)

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0409_im_cb95095d5b.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Some of these classified filenames are encoded with a Caesar cipher — one of the oldest encryption methods in history. It's a simple substitution cipher where each letter is shifted by a fixed number of positions in the alphabet."

    # --- How Caesar Cipher Works ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0413_im_6ab3b8c889.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Here's how it works. The alphabet is a loop: A B C D E F... all the way to Z, and then it wraps back to A. A Caesar cipher shifts every letter forward by a fixed number — the key."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0415_im_31bfb4d9be.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "With ROT-3 — a rotation of 3 — the letter A becomes D, B becomes E, C becomes F. The word 'CAT' encrypts to 'FDW'. Every letter moves exactly three places forward."

    sys "// SYSTEM NOTE: Caesar Cipher encryption with ROT-3: A→D, B→E, C→F, D→G ... X→A, Y→B, Z→C //"

    # --- Decryption: Reversing the Shift ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0421_im_c3de04e0ce.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "To decrypt, you do the reverse — shift each letter back by the same number. So D becomes A, E becomes B, F becomes C. Decryption undoes the encryption."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0423_im_f7c0216c52.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Let me work through an example. If I see the letter 'S', I count back 3: S... R... Q... P. So S decrypts to P. If I see 'U', count back 3: U... T... S... R. So U becomes R."

    sys "// DECRYPTION RULE: Take each letter → count backwards by the key number → that's your plaintext letter. ROT-3 decryption: D→A, E→B, F→C, G→D ... //"

    # --- Why It Matters ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0429_im_4c4c03d967.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "The Caesar cipher is trivially easy to break — there are only 25 possible shifts, so you can try them all in seconds. But it teaches the fundamental principle behind all encryption: transform readable data into unreadable data using a key, and reverse the process with the same key."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0431_im_208e917f23.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Modern encryption like AES-256 uses the same concept — just with keys that are billions of times more complex, making brute-force attacks effectively impossible."

    sys "// CHALLENGE PREP: You'll see an encrypted word. Shift each letter back by 3 to reveal the name of a classified NSA program. //"

    call minigame_2_decrypt

    # --- Choice 2: Copy the files or take notes only? ---
    scene bg_nsa_servers at parallax with dissolve
    show edward tense at stage_center
    with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0442_im_09c3298c5f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "I have access to everything. The question is: what do I do with it?"

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0444_narrator_voice_07e4a37dd7.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You stare at your screen. The classified documents are right there. Proof of mass surveillance. Proof of constitutional violations. But taking them means crossing a line there's no coming back from."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0446_im_dd410947fd.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "If I copy these files, I'm committing espionage under the law. If I don't, no one will ever know this is happening. The proper channels have already failed me — my report to the Inspector General disappeared into a black hole."

    menu:
        "Copy the files to an encrypted drive. This evidence needs to survive.":
            $ tree_record_choice("choice_ch2_2", "copy")
            $ localized_voice = voice_for_current_language("audio/voice/en/script_0451_im_5d1c8c9aa6.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            im "I need the original documents. Notes won't be enough. Journalists need primary sources — verifiable proof that can't be denied or dismissed."
            $ evidence_secured = True
            $ suspicion_level += 1
            $ renpy.notify(t("Evidence Secured! | Suspicion +1"))

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0456_narrator_voice_475a96d3e3.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            narrator_voice "You carefully copy selected documents to a micro SD card hidden inside a Rubik's Cube. Every file transfer is a risk — the NSA logs all data movement, and an unusual transfer could trigger an automated alert."

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0458_im_dcce61426d.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            im "The files are protected with AES-256 encryption — the Advanced Encryption Standard with a 256-bit key. It's the same encryption the US government uses to protect its own top-secret data. Effectively impossible to brute-force with any existing hardware."

            sys "// DATA TRANSFER INITIATED. ENCRYPTION: AES-256. CONTAINER: VERACRYPT HIDDEN VOLUME. //"

        "Take detailed notes only. Digital evidence is too risky.":
            $ tree_record_choice("choice_ch2_2", "notes")
            $ localized_voice = voice_for_current_language("audio/voice/en/script_0464_im_6e0732e0f1.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            im "If they catch me with files, it's espionage. Notes are deniable."
            $ trust_score -= 1
            $ renpy.notify(t("Trust -1"))

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0468_narrator_voice_6f1dede966.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            narrator_voice "You write down key details from memory. It's safer, but journalists may question the credibility without primary documents."

    hide edward neutral with dissolve

    # --- MCQ Question ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0474_im_0cfcfeb477.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "When transferring these documents, the protocol matters. Standard HTTP sends everything in plain text — anyone on the network can read it. But HTTPS adds a layer of TLS/SSL encryption, securing the data between your browser and the web server."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0476_im_e48dbc264f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "That padlock icon in your browser's address bar? That's HTTPS at work. It's the difference between shouting your secrets across a room and whispering them through a sealed envelope."

    call screen mcq_question(
        question=t("Which protocol encrypts web traffic?"),
        answers=[t("HTTP"), t("FTP"), t("HTTPS"), t("SMTP")],
        correct_index=2,
        explanation=t("HTTPS (HyperText Transfer Protocol Secure) uses SSL/TLS encryption to secure data transmitted between your browser and a web server. Regular HTTP sends everything in plain text.")
    )

    # --- Chapter 2 Summary ---

    if evidence_secured and knowledge_score >= 4:
        $ ch2_outcome = "good"
    else:
        $ ch2_outcome = "bad"

    $ autosave_chapter(2)

    jump chapter_3


################################################################################
##  ██████╗██╗  ██╗██████╗
## ██╔════╝██║  ██║╚════██╗
## ██║     ███████║ █████╔╝
## ██║     ██╔══██║ ╚═══██╗
## ╚██████╗██║  ██║██████╔╝
##  ╚═════╝╚═╝  ╚═╝╚═════╝
## CHAPTER 3: THE CONTACT
################################################################################

label chapter_3:
    call show_loading_screen
    $ current_chapter = 3
    $ persistent.tree_ch_reached = max(getattr(persistent, 'tree_ch_reached', 0), 3)

    call screen chapter_transition(chapter_num=3, codename="THE CONTACT", location="Encrypted Channel — Location Unknown", date="June 9, 2013", time_str="02:31 EST", clearance="TOP SECRET // HUMINT", description="First contact with journalists Glenn Greenwald\nand Laura Poitras. Every message could be\nintercepted. Operational security is the\ndifference between freedom and prison.", status="ACTIVE", bg_image="bg_hong_kong")
    $ show_hud = True
    $ quick_menu = True


    scene bg_hong_kong at parallax with chapter_transition

    show edward tense at enter_left
    with dissolve

    # --- Snowden must contact journalists ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0524_im_a1f3b0cd16.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "I have the evidence. Now I need someone to publish it. But one wrong email, one unencrypted message, and the NSA will know before the ink is dry."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0526_narrator_voice_bf90d38e91.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You need to contact journalists who can responsibly publish the classified documents. But the NSA monitors virtually all electronic communication — the very programs you plan to expose are the ones hunting for people like you."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0528_im_907ef704f9.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "The NSA doesn't just collect data in bulk. They have tools that flag specific patterns: a new email address contacting a known journalist, an encrypted connection from a government network, a Tor exit node accessing a news site. Any of these could trigger an alert."

    sys "// SYSTEM NOTE: OpSec (Operational Security) is the practice of protecting critical information from adversaries. Every digital action leaves traces. //"

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0532_im_c4dda3676a.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "I can't use my work email. I can't use my personal email. I need a completely new identity, on a completely separate network. And I need to make contact without anyone inside the NSA knowing I've reached out."

    # --- Snowball Effect Check ---
    if suspicion_level >= 3:
        $ localized_voice = voice_for_current_language("audio/voice/en/script_0536_narrator_voice_e35f399c18.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        narrator_voice "Your unusual access patterns have already triggered internal alerts. Your options are narrowing."

        sys "// WARNING: INTERNAL SECURITY MONITORING HAS FLAGGED YOUR ACTIVITY //"

        menu:
            "Try to bluff your way through the security review.":
                $ tree_record_choice("choice_ch3_0", "bluff")
                $ suspicion_level += 1
                $ renpy.notify(t("Suspicion +1"))

                $ localized_voice = voice_for_current_language("audio/voice/en/script_0546_im_cbda80472a.mp3")  # edge-tts-auto
                if localized_voice:  # edge-tts-auto
                    voice localized_voice  # edge-tts-auto
                im "I told them I was running diagnostic tests on the archival system. They seemed to buy it... for now."

                $ localized_voice = voice_for_current_language("audio/voice/en/script_0548_narrator_voice_d205792db4.mp3")  # edge-tts-auto
                if localized_voice:  # edge-tts-auto
                    voice localized_voice  # edge-tts-auto
                narrator_voice "The security team notes the explanation but doesn't close the file. The clock is ticking."

            "Accelerate the timeline. Contact journalists immediately.":
                $ tree_record_choice("choice_ch3_0", "accelerate")
                $ trust_score -= 1
                $ renpy.notify(t("Trust -1"))

                $ localized_voice = voice_for_current_language("audio/voice/en/script_0555_im_8e4992e8c5.mp3")  # edge-tts-auto
                if localized_voice:  # edge-tts-auto
                    voice localized_voice  # edge-tts-auto
                im "No more waiting. If I don't move now, I won't get another chance."

                jump ch3_contact_unsafe

    # --- Choice 1: Secure channel or personal email? ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0561_im_9b856234a5.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "I've identified two journalists who might have the courage to publish: Leah Portman, a documentary filmmaker who's been investigating NSA surveillance for years, and Grayson Wardell, a constitutional lawyer turned journalist at The Guardian."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0563_im_0976dace9c.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "The challenge is reaching them securely. PGP encryption with Tor would make my messages virtually untraceable — but it requires technical knowledge to set up correctly. One mistake in the key exchange and the whole channel is compromised."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0565_narrator_voice_b6587fb3cb.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You weigh your options. Each method of contact carries its own risks and rewards."

    menu:
        "Set up a PGP-encrypted email channel using Tor (requires knowledge).":
            $ tree_record_choice("choice_ch3_1", "pgp")
            if knowledge_score >= 3:
                jump ch3_secure_success
            else:
                jump ch3_secure_fail

        "Contact Grayson Wardell directly through his public email.":
            $ tree_record_choice("choice_ch3_1", "email")
            $ contacts_secured += 1
            $ renpy.notify(t("Contacts +1"))
            jump ch3_greenwald_contact

        "Wait for a safer moment to make contact.":
            $ tree_record_choice("choice_ch3_1", "wait")
            $ trust_score -= 1
            $ renpy.notify(t("Trust -1"))
            jump ch3_wait

label ch3_secure_success:
    $ localized_voice = voice_for_current_language("audio/voice/en/script_0588_im_87da0b6702.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "I know how PGP works. Public key, private key. I generate a key pair, publish my public key, and any message encrypted with it can only be read by me."

    sys "// PGP KEY PAIR GENERATED. RSA-4096. FINGERPRINT VERIFIED THROUGH SEPARATE CHANNEL. //"

    $ contacts_secured += 1
    $ knowledge_score += 1
    $ renpy.notify(t("Contacts +1 | Knowledge +1"))

    scene bg_hong_kong_terminal at parallax with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0598_narrator_voice_87feb29d1c.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You create an anonymous email account, accessed only through Tor, and use PGP encryption to contact documentary filmmaker Leah Portman."

    show poitras neutral at enter_right
    with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0603_poitras_f96af47c05.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    poitras "I received your encrypted message. The fingerprint checks out. Who are you?"

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0605_e_7b666f57e5.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    e "I'm a senior member of the intelligence community. I have evidence of massive, unconstitutional surveillance by the NSA."

    show poitras cautious
    $ localized_voice = voice_for_current_language("audio/voice/en/script_0608_poitras_48d170a87b.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    poitras "Can you prove it?"

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0610_e_6cd0011cd2.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    e "I can prove everything. But we need to meet in person. I'll also reach out to Grayson Wardell — together, you can publish the full story."

    jump ch3_continue

label ch3_secure_fail:
    $ localized_voice = voice_for_current_language("audio/voice/en/script_0615_im_2f3ed2294a.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "I know I need to use PGP, but I'm not confident in the setup. If I make a mistake with the key exchange..."

    sys "// WARNING: INSUFFICIENT KNOWLEDGE TO ESTABLISH SECURE CHANNEL. PROCEEDING WITH PARTIAL ENCRYPTION. //"

    $ suspicion_level += 1
    $ renpy.notify(t("Suspicion +1"))

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0622_narrator_voice_941572744c.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You attempt to set up encrypted communications, but make errors in the key exchange process. The channel may not be fully secure."

    jump ch3_continue


label ch3_greenwald_contact:
    scene bg_hong_kong_street at parallax with dissolve
    show greenwald neutral at enter_right
    with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0632_narrator_voice_7aaee15875.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You reach out to Grayson Wardell through his public contact information. It's faster, but less secure."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0634_e_a446fe8fb9.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    e "Mr. Wardell, I have information of extreme importance regarding US government surveillance. We need to talk on a secure channel."

    show greenwald skeptical
    $ localized_voice = voice_for_current_language("audio/voice/en/script_0637_greenwald_c70b3f1894.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    greenwald "I get messages like this every week. Can you give me more details?"

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0639_e_3ca18f646e.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    e "Not over this channel. You need to set up PGP encryption. I'll send you instructions."

    show greenwald confused
    $ localized_voice = voice_for_current_language("audio/voice/en/script_0642_greenwald_c2437be411.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    greenwald "PGP? I've never used it. Can't we just talk on the phone?"

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0644_im_b631248db8.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "This is the problem. The people who need to publish this information don't know the first thing about security."

    $ suspicion_level += 1
    $ renpy.notify(t("Suspicion +1"))

    jump ch3_continue

label ch3_wait:
    $ localized_voice = voice_for_current_language("audio/voice/en/script_0652_narrator_voice_223e24c66a.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You decide to wait for a safer window. But there may not be one."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0654_im_0210df48a3.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Every day I wait is another day they could catch me. But rushing makes mistakes. Mistakes get you caught."

    $ suspicion_level += 1
    $ renpy.notify(t("Suspicion +1"))

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0659_narrator_voice_498387062f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "Weeks pass. Your access patterns grow more suspicious. The window is closing."

    jump ch3_continue

label ch3_contact_unsafe:
    $ localized_voice = voice_for_current_language("audio/voice/en/script_0664_narrator_voice_3074d89f5b.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "With time running out, you take risks you normally wouldn't."

    $ suspicion_level += 1
    $ contacts_secured += 1
    $ renpy.notify(t("Suspicion +1 | Contacts +1"))

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0670_im_6aa5038206.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "No time for perfect OpSec. I just need to get the message out."

    jump ch3_continue

label ch3_continue:
    # --- Question Segment 3: MCQ on Encryption ---
    hide journalist
    hide greenwald
    hide poitras
    hide edward
    with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0682_im_aab8cbfb6a.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Everything I've done to contact journalists relies on one tool above all others: Tor — The Onion Router. It's an anonymization network that routes your traffic through multiple relay nodes around the world, each encrypting another layer."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0684_im_c108062c3a.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "By the time your traffic reaches its destination, tracing it back to the source is nearly impossible. That's what makes Tor the tool of choice for anyone who needs to communicate without being tracked."

    call screen mcq_question(
        question=t("What is Tor mainly used for?"),
        answers=[t("To hide where your internet traffic is coming from"), t("To make your laptop charge faster"), t("To delete files forever"), t("To boost a Wi-Fi signal")],
        correct_index=0,
        explanation=t("Tor hides your route by bouncing traffic through several relays, which makes it much harder for observers to trace it back to you."),
        helper_text=t("Think about privacy and staying hard to track, not the full acronym.")
    )

    # --- Minigame 3: OpSec Challenge — Learning Section ---
    # (Structured as a self-contained briefing — can be branched into the story tree later)

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0697_im_3d8d0f8b94.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "But technology alone isn't enough. OpSec — Operational Security — is the practice of thinking like your adversary. What can they learn from your actions? Every digital footprint, every unguarded conversation, every pattern of behaviour is a piece of the puzzle they're assembling."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0699_im_3c26d4cba7.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Good OpSec means denying the adversary those pieces. It means asking yourself before every action: could this reveal my identity, my location, or my intent?"

    # --- IP Address Exposure ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0703_im_43bea91758.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "The most basic OpSec failure is IP exposure. Your home IP address is assigned by your Internet Service Provider and tied directly to your name and physical address. If you log into a secure service from your home IP without a VPN, you've just stamped your real identity on the connection."

    sys "// OPSEC RULE #1: Never access sensitive services from a traceable IP address. Use a VPN or Tor to mask your connection. //"

    # --- Anonymous Communication Tools ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0709_im_f603d0f2ef.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "The right tools make anonymity possible. Tor anonymizes your connection through multiple relay nodes. SecureDrop — an open-source platform used by major newsrooms — lets whistleblowers submit documents anonymously. Burner email accounts, created from public locations like libraries, add another layer of separation between your real identity and your actions."

    sys "// SAFE PRACTICE: Tor + SecureDrop + burner accounts from public locations = maximum anonymity //"

    # --- Work Email and Monitored Channels ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0715_im_27caff8d87.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "The biggest mistake an insider can make is using work infrastructure for anything sensitive. Work email, work Wi-Fi, work devices — all of these are monitored, logged, and directly tied to your employee identity. Sending classified documents via work email is essentially confessing."

    sys "// OPSEC RULE #2: Work infrastructure is monitored. Never use work email, devices, or networks for sensitive communication. //"

    # --- Password Hygiene ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0721_im_15c85c6e8c.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "And then there's password reuse — the silent killer. If you use your personal Facebook password for an encrypted file container, you've created a bridge between your public identity and your secret activity. When one account is compromised, every account sharing that password falls."

    sys "// OPSEC RULE #3: Never reuse passwords. Every service gets a unique, strong password. Use a password manager. //"

    # --- Password Cracking and Cryptanalysis ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0727_im_f73a328ffa.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Now it's time to put that knowledge into practice. I've intercepted an encrypted password hash from the internal NSA directory. Before I can access the PRISM architecture files, I need to crack it."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0729_im_534a1add8b.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "A hash is a one-way mathematical function — you can't just 'decrypt' it. You have to guess the password, hash your guess, and see if it matches. To do this, we use tools like 'John the Ripper' and a massive list of known passwords, like the 'rockyou.txt' wordlist. This is called a dictionary attack."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0731_im_fd1dc944a8.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "But what if the password has substitutions, like 'M0nk3y!' instead of 'monkey'? That's where rule-based mutations come in. By applying rules, the cracking tool automatically tests thousands of variations for every word in the dictionary."

    sys "// SYSTEM NOTE: Passwords are only as strong as their entropy. Fast algorithms like MD5 can be cracked instantly using dictionary attacks. Strong algorithms like bcrypt use a computational cost factor to make guessing intentionally slow. //"
    # --- Hash Functions vs Encryption ---

    im "A hash is fundamentally different from encryption. Encryption is a two-way street — you scramble data with a key, and decrypt it with the same key. A hash is a one-way mathematical meat grinder."
    
    im "When you create a password, the system doesn't save the password itself. It runs it through a hashing algorithm to produce a fixed-length string of characters. You can't reverse the math to 'decrypt' a hash back into the password."
    
    sys "// SYSTEM NOTE: Hashes are one-way cryptographic functions. You cannot decrypt a hash; you must guess the input that produced it. //"

    # --- Dictionary Attacks ---

    im "So how do you crack it? You guess. You take a massive list of known passwords — like the infamous 'rockyou.txt' wordlist, which contains millions of real passwords leaked from previous breaches."
    
    im "You run every word in that dictionary through the hashing algorithm. If the resulting hash matches the one you stole, you've found the password. This is called a dictionary attack, and tools like 'John the Ripper' can test millions of guesses per second."
    
    sys "// SYSTEM NOTE: A Dictionary Attack systematically hashes a list of common passwords to find a match. Fast algorithms like MD5 are highly vulnerable to this. //"

    # --- Rule-Based Mutations ---

    im "But people think they're clever. They substitute letters for numbers — 'M0nk3y!' instead of 'monkey'. That's where rule-based mutations come in."
    
    im "The cracking software doesn't just try the dictionary words. It automatically applies rules: capitalizing letters, adding numbers at the end, swapping 'e' for '3'. It turns one dictionary word into thousands of variations, devastating most 'clever' passwords."
    
    sys "// SYSTEM NOTE: Passwords are only as strong as their entropy. Adding predictable substitutions (like 'a' to '@') does not stop modern cracking tools. //"

    # --- Kali Linux & Terminal Commands ---

    im "To run this attack, we'll use Kali Linux — an operating system built specifically for penetration testing. We'll execute the attack entirely from the command line terminal."
    
    im "When running 'John the Ripper' from the terminal, you need to pass it specific arguments telling it which wordlist to use, and which file contains the hashes you want to crack."
    
    im "The standard syntax looks like this: 'john --wordlist=<path_to_wordlist> <path_to_hash_file>'. In Kali Linux, the famous 'rockyou.txt' dictionary is typically stored at '/usr/share/wordlists/rockyou.txt'."
    
    sys "// COMMAND SYNTAX: john --wordlist=/usr/share/wordlists/rockyou.txt /path/to/hash.txt //"

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0735_im_c407e05342.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "If these hashes use MD5, they'll break in seconds. If they use bcrypt... we might be here for a century. Let's find out."
    im "If these hashes use an outdated algorithm like MD5, they'll break instantly. If they use a slow, modern algorithm like bcrypt... we might be here for a century. Let's find out."

    window hide
    $ mg_intro3 = renpy.call_screen("minigame_briefing", challenge_title="BRUTE FORCE", subtitle="Passwords are only as strong as their entropy.\nTime to crack the hashes.", mission_id="OPS-03-09-2013", classification="TOP SECRET // EYES ONLY", challenge_type="CRYPTANALYSIS", estimated_time="120 SECONDS", difficulty=3, difficulty_label="OPERATIVE", succeed_reward="access_granted +1", fail_penalty="suspicion_level +1", learn_concept="Dictionary attacks and rule-based mutations\ncan break weak passwords instantly.", briefing_text="You intercepted an NSA internal system hash.\nYour task is to run the correct John the Ripper command for each round.\n\nRound 1: use a basic dictionary attack.\nRound 2: add rules so John also tests common substitutions.\nRound 3: prove that bcrypt plus a strong password is too slow to crack.\n\nRead the prompt, type the full command, press Enter to execute it, and use TAB for quick autocomplete when you already know the start of the command.", controls=[("BACKSPACE", "Delete typed text"),("TAB", "Autocomplete command"),("ENTER", "Execute operation")])

    if mg_intro3:
        $ quick_menu = False
        $ show_hud = False
        call minigame_3_brute_force
        $ quick_menu = True
        $ show_hud = True
        
        if mg_opsec_score == "SKIP":
            $ renpy.notify(t("Minigame Skipped"))
        elif mg_opsec_score >= 4:
            $ contacts_secured += 1
            $ knowledge_score += 1
            $ renpy.notify(t("Contacts +1 | Knowledge +1"))
        else:
            $ suspicion_level += 1
            $ renpy.notify(t("Suspicion +1"))
    else:
        $ knowledge_score -= 1
        $ renpy.notify(t("Knowledge -1 (Skipped)"))

    # --- Choice 2: How much to reveal? ---
    show edward neutral at stage_center
    show greenwald serious at enter_right
    with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0765_narrator_voice_d0803e0aea.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The journalist asks for more details about the scope of the leaks."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0767_greenwald_8b32bc7026.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    greenwald "I need to know what we're dealing with. How big is this?"

    menu:
        "Tell everything. Full transparency builds trust.":
            $ tree_record_choice("choice_ch3_2", "full")
            $ localized_voice = voice_for_current_language("audio/voice/en/script_0772_e_d0a24ec501.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            e "It's everything. PRISM, XKeyscore, Boundless Informant, upstream collection — the NSA is collecting data on hundreds of millions of people. American citizens included."
            $ trust_score += 2
            $ contacts_secured += 1
            $ renpy.notify(t("Trust +2 | Contacts +1"))

            show greenwald shocked
            $ localized_voice = voice_for_current_language("audio/voice/en/script_0778_greenwald_0602aec18d.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            greenwald "My God. If this is true... this is the biggest intelligence leak in history."

        "Share only what's necessary. Protect sources and methods.":
            $ tree_record_choice("choice_ch3_2", "partial")
            $ localized_voice = voice_for_current_language("audio/voice/en/script_0782_e_dd5fb197c0.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            e "I can confirm the NSA is conducting mass domestic surveillance. I'll share the details when we meet in person."
            $ trust_score += 1
            $ renpy.notify(t("Trust +1"))

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0786_greenwald_236a5dbfee.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            greenwald "Fair enough. Where do we meet?"

        "Be vague. Don't reveal the scope until you're safe.":
            $ tree_record_choice("choice_ch3_2", "vague")
            $ localized_voice = voice_for_current_language("audio/voice/en/script_0790_e_60a26c0348.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            e "It's significant. That's all I can say right now."
            $ trust_score -= 1
            $ renpy.notify(t("Trust -1"))

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0794_greenwald_475a58f9be.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            greenwald "You're asking me to fly halfway around the world on a vague tip?"

    hide greenwald
    hide edward
    with dissolve

    # --- Chapter 3 Summary ---

    if contacts_secured >= 2:
        $ ch3_outcome = "good"
    else:
        $ ch3_outcome = "bad"

    $ autosave_chapter(3)

    jump chapter_4


################################################################################
##  ██████╗██╗  ██╗██╗  ██╗
## ██╔════╝██║  ██║██║  ██║
## ██║     ███████║███████║
## ██║     ██╔══██║╚════██║
## ╚██████╗██║  ██║     ██║
##  ╚═════╝╚═╝  ╚═╝     ╚═╝
## CHAPTER 4: THE ESCAPE
################################################################################

label chapter_4:
    call show_loading_screen
    $ current_chapter = 4
    $ persistent.tree_ch_reached = max(getattr(persistent, 'tree_ch_reached', 0), 4)

    call screen chapter_transition(chapter_num=4, codename="THE ESCAPE", location="Mira Hotel, Hong Kong", date="June 10, 2013", time_str="14:22 HKT", clearance="TOP SECRET // EYES ONLY", description="NSA agents are closing in. The hotel room\nis the last safe ground. Every digital trace\nmust be destroyed before they arrive.\nNinety seconds. No margin for error.", status="ACTIVE", bg_image="bg_hong_kong_street")
    $ show_hud = True
    $ quick_menu = True


    scene bg_hong_kong_hotel at parallax with chapter_transition

    show edward tired at enter_left
    with dissolve

    # --- Snowden in Hong Kong ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0839_narrator_voice_fe3b65f13f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You arrive in Hong Kong with a laptop full of classified documents and a plan that's already falling apart."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0841_im_f9cb777112.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "I chose Hong Kong deliberately. It has its own legal system, independent from mainland China. Extradition would take time — time I need to get the story published before the government can suppress it."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0843_im_36f6d47aac.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "I told my employer I needed medical leave for epilepsy treatment. They didn't question it. That bought me a few weeks."

    show edward tense
    $ localized_voice = voice_for_current_language("audio/voice/en/script_0846_im_3e19aa6dbc.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Now I'm in a hotel room in Hong Kong, waiting for journalists who might not come, hunted by an agency that can find anyone. I've wedged pillows against the door, piled cushions against the window. Even the smoke detector might have a camera."

    sys "// LOCATION: MIRA HOTEL, HONG KONG. STATUS: UNDETECTED — FOR NOW. //"

    # --- Tense dialogue with pressure ---

    show greenwald neutral at enter_right
    with dissolve

    show greenwald serious
    $ localized_voice = voice_for_current_language("audio/voice/en/script_0856_greenwald_5382c3a548.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    greenwald "You do realize what you're asking me to do? If we publish this, both our lives change forever."

    show edward determined
    $ localized_voice = voice_for_current_language("audio/voice/en/script_0859_e_e8a42759c0.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    e "My life changed the moment I read those documents. I can't unread them. I can't unknow what the government is doing to its own people."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0861_im_ec87f9b69a.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Greenwald flew here from Rio de Janeiro. Poitras from Berlin. They left their lives behind on the strength of encrypted emails from a stranger. That took courage."

    if suspicion_level >= 3:
        sys "// WARNING: NSA INTERNAL AUDIT HAS FLAGGED YOUR ACCESS ANOMALIES. INVESTIGATION IN PROGRESS. //"

        show edward tense
        $ localized_voice = voice_for_current_language("audio/voice/en/script_0867_im_1bb62c6667.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        im "They know something is wrong. I can feel it. The clock is ticking."

    show greenwald resolved
    $ localized_voice = voice_for_current_language("audio/voice/en/script_0870_greenwald_9415e885fe.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    greenwald "The documents check out. Laura and I have verified them. We're ready to publish."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0872_e_13806b9fc0.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    e "Publish everything. The world needs to see this."

    hide greenwald with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0876_im_f87c5e50be.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "What scares me most isn't just the surveillance — it's the NSA's offensive capabilities. They stockpile zero-day exploits — vulnerabilities in software that the vendor doesn't even know about. Called 'zero-day' because there are zero days of notice before they're exploited. No patch exists yet."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0878_im_833e8fb56e.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "If the NSA wants into your laptop, they don't need your password. They use a zero-day to bypass everything — your firewall, your encryption, your operating system. And the vendor can't fix what they don't know is broken."

    sys "// SYSTEM NOTE: A zero-day exploit targets an unknown software vulnerability. Because no patch exists, even fully updated systems are at risk. Intelligence agencies hoard zero-days as offensive weapons. //"

    # --- Choice 1: Hotel Wi-Fi or mobile hotspot? ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0884_narrator_voice_2fc99a4f65.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You need to send final instructions to the publication team, but the hotel network is compromised. Every network connection is a potential leak."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0886_im_2c235d6245.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "The hotel Wi-Fi is managed by the hotel — they can see every device that connects, every connection made. Intelligence agencies routinely request hotel network logs. I need to decide how to send this last message."

    menu:
        "Use the hotel Wi-Fi with a VPN.":
            $ tree_record_choice("choice_ch4_1", "hotel")
            $ suspicion_level += 1
            $ renpy.notify(t("Suspicion +1"))

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0894_im_436f937719.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            im "The VPN encrypts my traffic, but the hotel's network logs will show my room connected to a VPN. That alone is a red flag for anyone watching."

            sys "// WARNING: VPN CONNECTION DETECTED ON LOCAL NETWORK. COMMERCIAL VPN IPs ARE CATALOGUED BY INTELLIGENCE AGENCIES. //"
            sys "// CHOICE REVIEW: Fast and convenient, but the hotel can still log that a protected tunnel came from your room. Good for speed, bad for stealth. //"

        "Use a personal mobile hotspot with Tor.":
            $ tree_record_choice("choice_ch4_1", "mobile")
            $ trust_score += 1
            $ renpy.notify(t("Trust +1"))

            $ localized_voice = voice_for_current_language("audio/voice/en/script_0904_im_c25ed56dd0.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            im "A mobile hotspot bypasses the hotel network entirely. With Tor on top of it, my traffic is encrypted and anonymized through multiple relay nodes."

            sys "// SECURE CONNECTION ESTABLISHED. TRAFFIC ROUTED THROUGH 3 TOR RELAY NODES. //"
            sys "// CHOICE REVIEW: Slower, but it avoids hotel logs and adds extra privacy layers. Good for stealth, bad for speed. //"

    # --- Question Segment 4: Text Input ---

    $ tiq_reset()
    $ tiq_result = renpy.call_screen(
        "text_input_question",
        chapter_num    = "04",
        chapter_name   = t("The Escape"),
        question_text  = t("Type the 3-letter privacy tool that\nhides your route online:"),
        hint_text      = t("It's the same tool mentioned in the safer option above."),
        check_type     = "Text Input",
        difficulty     = "Easy",
        reward_label   = "+1 Knowledge",
        reward_color   = "green",
        correct_answer = "TOR",
        explanation    = t("Tor wraps your traffic in several layers and sends it through relays, which helps hide where it started."),
        allow_skip     = True
    )
    if tiq_result == "continue" and tiq_is_correct:
        $ knowledge_score += 1
        $ renpy.notify(t("Knowledge +1"))

    # --- Minigame 4: Trace the Route — Learning Section ---
    # (Structured as a self-contained briefing — can be branched into the story tree later)

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0933_im_b9bfd3fea0.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "When you route traffic through Tor, you're building a chain of relay nodes. Each node only knows the hop before it and the hop after it — never the full path. Pick the right nodes and your trail goes cold."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0935_im_625d8484b9.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "But if even one node in the chain is compromised — a monitored relay, a hostile exit point — the entire route is exposed and your identity with it. So understanding what each type of node does is critical."

    # --- The Starting Point: Your Device ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0939_im_e48c94ea65.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "It all starts at your device — your laptop, your phone. This is where traffic originates. Right now, it carries your real IP address and your real identity. The goal is to strip that identity away before the traffic reaches its destination."

    # --- ISP Router ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0943_im_35a43a03f9.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "The first hop is usually your ISP router — the Internet Service Provider that connects you to the internet. Your ISP can see every website you visit, every connection you make. They log this data and, in many countries, hand it over to law enforcement on request."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0945_im_f62459a507.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Going through the ISP is unavoidable — it's your on-ramp to the internet. But it's a chokepoint. If someone is watching at this level, they see everything unless you've already encrypted your traffic."

    sys "// NODE TYPE: ISP ROUTER — Your gateway to the internet. Sees all unencrypted traffic. A surveillance chokepoint. //"

    # --- VPN Server ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0951_im_54aebd2657.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "A VPN server is your first line of defence. It creates an encrypted tunnel between your device and the VPN server. Your ISP can see that you've connected to a VPN, but they can't see what you're doing through it."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0953_im_83b66655ee.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Starting your route through a VPN before entering the Tor network is called 'VPN over Tor' — it hides the fact that you're using Tor from your ISP, adding an extra layer of protection."

    sys "// NODE TYPE: VPN SERVER — Encrypts your traffic before it hits the internet. Hides your activity from your ISP. Safe opening move. //"

    # --- Tor Nodes ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0959_im_b1edda6959.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Tor nodes are the backbone of anonymous routing. Each Tor relay adds a layer of encryption — like nesting your message inside multiple sealed envelopes. The first relay knows who you are but not where you're going. The last relay knows where you're going but not who you are."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0961_im_f22a75b396.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "The more Tor nodes you route through, the harder it is to trace the connection back to you. But each hop adds latency — there's a trade-off between anonymity and speed."

    sys "// NODE TYPE: TOR NODE — Adds encryption layers and anonymity. Multiple Tor hops = harder to trace. Safe nodes. //"

    # --- Government Monitor (Danger!) ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0967_im_bc6a5cae97.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "The one node you must avoid at all costs is the government monitoring point. Intelligence agencies like the NSA operate surveillance nodes that intercept and log all traffic passing through them. If your route goes through a government monitor, the entire chain is compromised."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0969_im_a92f31da76.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "It doesn't matter how many Tor nodes you've used — if even one hop routes through a known surveillance point, the adversary can correlate timing data to identify you. This is called a 'traffic correlation attack'."

    sys "// NODE TYPE: GOV MONITOR — Intercepts all traffic. If your route hits this node, your identity is exposed. AVOID AT ALL COSTS. //"

    # --- CDN Server vs Secure Relay ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0975_im_c8683a1aae.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Near the end of the route, you'll see two types of final relay. A CDN — Content Delivery Network — is standard internet infrastructure. It's fast but not designed for privacy. Your traffic is delivered efficiently, but CDN logs can be subpoenaed."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0977_im_62714fef2f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "A secure relay, on the other hand, is specifically designed for private communication. It doesn't log traffic, strips metadata, and forwards your message with minimal exposure. When anonymity matters, always prefer the secure relay."

    sys "// NODE TYPE: CDN SERVER — Fast but logs traffic. SECURE RELAY — Private, no logs. Choose secure relay for maximum anonymity. //"

    # --- Route Strategy ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0983_im_6941e4b3e3.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "So the optimal route is: start with a VPN to hide your Tor usage, chain through Tor nodes for anonymity, avoid the government monitor completely, and exit through a secure relay to reach the destination without leaving a trail."

    sys "// ROUTE STRATEGY: VPN → Tor nodes → Secure relay → Destination. Avoid GOV MONITOR. Fewer hops = less exposure time. //"

    window hide

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0989_im_6e485d9b67.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "But before I can run, I need to wipe everything. Every file, every log, every trace. If I leave even one digital breadcrumb, it's over."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0991_im_e86a8dfd17.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    # --- Digital Forensics and Secure Deletion ---

    im "Digital forensics is relentless. Most people think that when they delete a file, it's gone. It's not. The operating system just deletes the pointer to the file, marking that space on the hard drive as 'available'."
    
    im "The actual 1s and 0s are still sitting on the disk. Forensic agents can easily recover them. To truly destroy digital evidence, you have to use secure deletion tools like 'shred' to physically overwrite those disk sectors with random data."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0993_im_f9bb534562.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    sys "// SYSTEM NOTE: Standard deletion only removes file pointers. Secure deletion (shredding) overwrites the physical disk space to prevent forensic recovery. //"

    # --- Metadata Tracking ---

    im "And it's not just the files themselves. It's the metadata — the data about the data. Take photos, for instance."
    
    im "Every photo taken on a modern smartphone contains hidden EXIF metadata. It records the camera model, the exact time, and the precise GPS coordinates of where you were standing when you took it. If I don't strip that metadata using 'exiftool', the photos themselves will lead them straight to this hotel."

    sys "// SYSTEM NOTE: EXIF Metadata embeds location and device information directly into image files. Always strip metadata before publishing sensitive media. //"

    # --- Network and Hardware Logs ---

    im "My browser history and session tokens prove exactly what I accessed and when. My terminal history recorded every single command I typed. "
    
    im "Even my laptop's physical hardware is a liability. The hotel's Wi-Fi router logged my MAC address — a unique identifier hardcoded into my network card. If they match that MAC address to my machine, it's game over. I have to randomize it using 'macchanger'."

    sys "// FORENSICS ALERT: Digital footprints include browser tokens, terminal logs, and hardware MAC addresses. All must be wiped or randomized. //"

    $ localized_voice = voice_for_current_language("audio/voice/en/script_0995_im_059dc00155.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "I have 90 seconds before NSA agents reach my room. 8 digital traces that prove I copied the PRISM files. Each one needs a different command to destroy."

    sys "// ALERT: NSA RESPONSE TEAM EN ROUTE. ESTIMATED ARRIVAL: 90 SECONDS. BEGIN DIGITAL EVIDENCE ELIMINATION. //"

    $ mg_intro4 = renpy.call_screen("minigame_briefing", challenge_title="COVER YOUR TRACKS", subtitle="NSA forensics are knocking. Destroy the evidence.", mission_id="OPS-04-10-2013", classification="TOP SECRET // BLACK", challenge_type="DIGITAL FORENSICS", estimated_time="90 SECONDS", difficulty=4, difficulty_label="EXPERT", succeed_reward="escape_secured = True", fail_penalty="evidence_compromised = True", learn_concept="Secure deletion requires overwriting data,\nnot just deleting file pointers.", briefing_text="NSA forensic agents are knocking on the hotel door.\nYou have 90 seconds to wipe your digital footprints from the laptop before they image your hard drive.\n\nEach trace uses one of three modes:\n1. GUIDED: study the pre-filled command and execute it.\n2. ASSEMBLY: click tokens in the correct order to build the command.\n3. SELECT: choose the safest command from the list.\n\nHints and mistakes can add time pressure, so move quickly and wipe all 8 traces.", controls=[("CLICK", "Pick tokens or command options"),("ENTER", "Execute operation"),("HINT", "Get help for a 5s penalty")])

    if mg_intro4:
        call minigame_4_cover_tracks
    else:
        $ knowledge_score = max(0, knowledge_score - 1)
        $ escape_successful = False
        $ renpy.notify(t("Challenge skipped. Knowledge -1"))

    if escape_successful and evidence_secured:
        $ localized_voice = voice_for_current_language("audio/voice/en/script_1011_im_28df0547ea.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        im "Clean. Not a single trace left on this machine. When they get here, they'll find nothing but a blank hard drive and an empty hotel room."
        sys "// ALL DIGITAL EVIDENCE ELIMINATED. DEVICE IS FORENSICALLY CLEAN. //"
    elif escape_successful:
        $ localized_voice = voice_for_current_language("audio/voice/en/script_1014_im_829e5d201c.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        im "Most of it is gone, but I'm not sure I got everything. Some fragments might still be recoverable. I need to move — now."
        sys "// PARTIAL EVIDENCE REMAINS. FORENSIC RECOVERY POSSIBLE. //"
    else:
        $ localized_voice = voice_for_current_language("audio/voice/en/script_1017_im_48e4d51bf3.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        im "I ran out of time. They'll find everything — the files, the history, the logs. My identity is compromised."
        sys "// WARNING: FORENSIC EVIDENCE RECOVERED. IDENTITY COMPROMISED. //"

    # --- Choice 2: Fly to Russia or seek another country? ---

    scene bg_leak at parallax with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1024_narrator_voice_c0ed9ef7b0.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The first stories are published. The world erupts. And now, you are the most wanted person on Earth."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1026_im_2e0d97358d.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "The US government has revoked my passport. I need to move. Now."

    if suspicion_level >= 4:
        $ localized_voice = voice_for_current_language("audio/voice/en/script_1029_narrator_voice_1ca019e40c.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        narrator_voice "With your cover blown, your options have narrowed to almost nothing."

        menu:
            "Head to the airport immediately. Every minute counts.":
                $ tree_record_choice("choice_ch4_2", "airport")
                $ escape_successful = True
                $ renpy.notify(t("Escape initiated!"))

                $ localized_voice = voice_for_current_language("audio/voice/en/script_1037_im_71e6faaa30.mp3")  # edge-tts-auto
                if localized_voice:  # edge-tts-auto
                    voice localized_voice  # edge-tts-auto
                im "No time to plan. The passport might still work for a few hours before the revocation hits every system."
                sys "// ROUTE REVIEW: Best for immediate movement, worst for preparation. Good if you need speed more than certainty. //"

            "Go to the Russian consulate. They're the only ones who might help.":
                $ tree_record_choice("choice_ch4_2", "russia")
                $ escape_successful = True
                $ trust_score -= 1
                $ renpy.notify(t("Escape to Russia | Trust -1"))

                $ localized_voice = voice_for_current_language("audio/voice/en/script_1046_im_3630118336.mp3")  # edge-tts-auto
                if localized_voice:  # edge-tts-auto
                    voice localized_voice  # edge-tts-auto
                im "Russia isn't ideal, but beggars can't be choosers. They have their own reasons for helping me."
                sys "// ROUTE REVIEW: Good for immediate shelter, bad for independence. Help comes with political strings attached. //"

    else:
        menu:
            "Fly to Ecuador via Moscow. Multiple stops make tracking harder.":
                $ tree_record_choice("choice_ch4_2", "ecuador")
                $ escape_successful = True
                $ renpy.notify(t("Escape route planned!"))

                $ localized_voice = voice_for_current_language("audio/voice/en/script_1056_im_13f8ccf5d4.mp3")  # edge-tts-auto
                if localized_voice:  # edge-tts-auto
                    voice localized_voice  # edge-tts-auto
                im "Ecuador has a history of granting asylum to people the US wants. WikiLeaks arranged the route through Moscow."

                $ localized_voice = voice_for_current_language("audio/voice/en/script_1058_narrator_voice_63c95dd554.mp3")  # edge-tts-auto
                if localized_voice:  # edge-tts-auto
                    voice localized_voice  # edge-tts-auto
                narrator_voice "But you will never make it past Moscow. Your passport will be revoked mid-flight."
                sys "// ROUTE REVIEW: Strong asylum logic, but the travel chain is fragile. Good long-term idea, risky short-term execution. //"

            "Seek asylum at a European embassy in Hong Kong.":
                $ tree_record_choice("choice_ch4_2", "embassy")
                $ trust_score += 1
                $ renpy.notify(t("Trust +1"))

                if identity_exposed:
                    $ localized_voice = voice_for_current_language("audio/voice/en/script_1067_narrator_voice_eac9e81ce5.mp3")  # edge-tts-auto
                    if localized_voice:  # edge-tts-auto
                        voice localized_voice  # edge-tts-auto
                    narrator_voice "With his identity already exposed, no embassy will risk the diplomatic fallout of harboring him."
                    $ escape_successful = False
                else:
                    $ localized_voice = voice_for_current_language("audio/voice/en/script_1070_narrator_voice_faf752b7c7.mp3")  # edge-tts-auto
                    if localized_voice:  # edge-tts-auto
                        voice localized_voice  # edge-tts-auto
                    narrator_voice "The European embassies politely decline. No one wants to challenge the United States."
                    $ escape_successful = False

                $ localized_voice = voice_for_current_language("audio/voice/en/script_1073_im_affcf3bdba.mp3")  # edge-tts-auto
                if localized_voice:  # edge-tts-auto
                    voice localized_voice  # edge-tts-auto
                im "No one will help. Not officially. Moscow may be my only option."
                sys "// ROUTE REVIEW: Good legal optics, but embassies rarely want the diplomatic fallout. Good principle, poor odds. //"

            "Stay in Hong Kong and face the legal system.":
                $ tree_record_choice("choice_ch4_2", "stay")
                $ escape_successful = False
                $ renpy.notify(t("Escape abandoned."))

                $ localized_voice = voice_for_current_language("audio/voice/en/script_1081_im_fc5a5dc374.mp3")  # edge-tts-auto
                if localized_voice:  # edge-tts-auto
                    voice localized_voice  # edge-tts-auto
                im "If I stay, Hong Kong will extradite me. The US legal system won't give me a fair trial under the Espionage Act."
                sys "// ROUTE REVIEW: Good if you want to make a stand, bad if your goal is to stay free long enough to keep the story alive. //"

    hide edward with dissolve

    if escape_successful and not identity_exposed:
        scene bg_hk_airport at parallax with dissolve
        $ localized_voice = voice_for_current_language("audio/voice/en/script_1088_narrator_voice_bb80e4e123.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        narrator_voice "You board an international flight just hours before your name hits the global no-fly lists."

    # --- Chapter 4 Summary ---

    if escape_successful and not identity_exposed:
        $ ch4_outcome = "good"
    else:
        $ ch4_outcome = "bad"

    $ autosave_chapter(4)

    jump chapter_5


################################################################################
##  ██████╗██╗  ██╗███████╗
## ██╔════╝██║  ██║██╔════╝
## ██║     ███████║███████╗
## ██║     ██╔══██║╚════██║
## ╚██████╗██║  ██║███████║
##  ╚═════╝╚═╝  ╚═╝╚══════╝
## CHAPTER 5: PERMANENT RECORD
################################################################################

label chapter_5:
    call show_loading_screen
    $ current_chapter = 5
    $ persistent.tree_ch_reached = max(getattr(persistent, 'tree_ch_reached', 0), 5)

    call screen chapter_transition(chapter_num=5, codename="NO WAY BACK", location="Sheremetyevo Airport, Moscow", date="June 23, 2013", time_str="18:05 MSK", clearance="DECLASSIFIED // PUBLIC RECORD", description="The documents are published. The world knows.\nSnowden's passport has been revoked mid-flight.\nStranded in transit. The final choice:\nasylum, silence, or surrender.", status="ACTIVE", bg_image="bg_hk_airport")
    $ show_hud = True
    $ quick_menu = True


    scene bg_sheremetyevo at parallax with chapter_transition

    show edward tired at enter_left
    with dissolve

    # --- Snowden in Russia ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1129_narrator_voice_a9b3ec75a2.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The Sheremetyevo International Airport transit zone. You have been trapped here for 40 days. Sleeping on chairs, eating airport food, living in legal limbo."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1131_narrator_voice_90d75eae6e.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "His passport is cancelled. No country will grant him asylum without risking the wrath of the United States. Twenty-one countries rejected his application. Russia is his last option."

    show russian_official neutral at enter_right
    with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1136_russian_official_5de4a348f9.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    russian_official "The transit zone is a strange place, yes? You are not in Russia, but you are certainly not in America."

    show russian_official smug
    $ localized_voice = voice_for_current_language("audio/voice/en/script_1139_russian_official_a53360cbb5.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    russian_official "You are... nowhere. We can offer you 'somewhere.' Russia can grant you temporary asylum."

    show edward defiant
    $ localized_voice = voice_for_current_language("audio/voice/en/script_1142_e_f8262dbd27.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    e "I don't want to be a pawn in anyone's geopolitical chess game."

    show russian_official calculating
    $ localized_voice = voice_for_current_language("audio/voice/en/script_1145_russian_official_1a6014bf55.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    russian_official "You became a pawn the moment you took those files. The only question is which board you want to play on."

    show edward sad
    $ localized_voice = voice_for_current_language("audio/voice/en/script_1148_im_cab42c105f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "He's right. I have no leverage. The US government pressured every ally to refuse me. Bolivia's presidential plane was even forced to land in Austria because they suspected I was on board. That's how far they'll go."

    # --- Reflection Dialogue ---

    hide russian_official with dissolve

    scene bg_moscow_apartment at parallax with dissolve
    show edward thoughtful at stage_center
    with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1158_im_cc807ea41d.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "I'm an exile in the physical world, but I've never been more active in the digital one."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1160_im_d4346e345f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "From this small apartment in Moscow, I can still connect to the world. I use encrypted video calls to speak at conferences, secure messaging to coordinate with press freedom organisations. The irony of a surveillance whistleblower living in the surveillance capital of the East is not lost on me."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1162_narrator_voice_2f99891ff7.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "From Moscow, you continue to advocate for digital privacy. You develop tools to help journalists protect their sources, speak to millions through encrypted channels, and become the face of the global privacy debate."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1164_im_87b75174eb.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "SecureDrop — an open-source whistleblowing platform — was adopted by dozens of major news organizations after the leaks. It allows anonymous document submission, protecting sources the way I wish I had been protected. The tools I helped popularise are now standard practice in investigative journalism."

    # --- Dialogue based on accumulated flags ---

    if trust_score >= 4:
        $ localized_voice = voice_for_current_language("audio/voice/en/script_1169_im_a3aa20ccb1.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        im "I trusted the right people. Greenwald, Poitras, the editors — they did what journalists are supposed to do. They told the truth."
    elif trust_score >= 1:
        $ localized_voice = voice_for_current_language("audio/voice/en/script_1171_im_3effeb54fb.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        im "Trust is a calculation, not a feeling. I chose carefully, but not perfectly. Some bridges burned that didn't need to."
    else:
        $ localized_voice = voice_for_current_language("audio/voice/en/script_1173_im_a0f7c5aa3c.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        im "I trusted no one fully, and it cost me. Some stories never got published. Some evidence was lost. Half-measures half-worked."

    if knowledge_score >= 7:
        $ localized_voice = voice_for_current_language("audio/voice/en/script_1176_im_d3d44d07f6.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        im "My technical knowledge kept me alive. Every encryption key, every secure channel, every OpSec decision mattered."
    elif knowledge_score >= 4:
        $ localized_voice = voice_for_current_language("audio/voice/en/script_1178_im_340634d39d.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        im "I knew enough to be dangerous, but not enough to be safe. There were gaps in my knowledge that almost got me caught."
    else:
        $ localized_voice = voice_for_current_language("audio/voice/en/script_1180_im_c547d1f041.mp3")  # edge-tts-auto
        if localized_voice:  # edge-tts-auto
            voice localized_voice  # edge-tts-auto
        im "Looking back, there's so much I didn't know. So many security mistakes I made. I survived on luck as much as skill."

    # --- Question Segment 5: Final Knowledge Test ---

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1184_im_48b084225f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "People think metadata is harmless — it's just 'data about data.' Who you called, when, for how long, from where. Not the content of the message itself."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1186_im_b92206868f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "But metadata reveals patterns of life. Call a doctor at midnight, a divorce lawyer the next morning, and a locksmith that afternoon — the content doesn't matter. The pattern tells the whole story. Intelligence agencies consider metadata even more valuable than content in many cases."

    # MCQ
    call screen mcq_question(
        question=t("What is metadata in the context of surveillance?"),
        answers=[t("The content of a message"), t("Data about data (who, when, where — not what)"), t("Encrypted file headers"), t("User passwords")],
        correct_index=1,
        explanation=t("Metadata is 'data about data.' In surveillance terms, it includes who you communicated with, when, for how long, and from where — but not the content of the communication. The NSA argued metadata collection wasn't as invasive as content collection, but metadata can reveal intimate patterns of life.")
    )

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1196_im_46c2c7688b.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "PGP — Pretty Good Privacy. It's the asymmetric encryption system that made the whole operation possible. I publish a public key that anyone can use to encrypt a message to me, but only my private key can decrypt it. Without PGP, every email to the journalists would have been an open letter to the NSA."

    # Text Input
    $ tiq_reset()
    $ tiq_result = renpy.call_screen(
        "text_input_question",
        chapter_num    = "05",
        chapter_name   = t("The Aftermath"),
        question_text  = t("Type the 3-letter encryption tool you\nused to message journalists:"),
        hint_text      = t("It stands for 'Pretty Good' something, and the short version is enough."),
        check_type     = "Text Input",
        difficulty     = "Easy",
        reward_label   = "+1 Knowledge",
        reward_color   = "green",
        correct_answer = "PGP",
        explanation    = t("PGP lets one key lock a message and another key unlock it, which is why you pushed journalists to learn it."),
        allow_skip     = True
    )
    if tiq_result == "continue" and tiq_is_correct:
        $ knowledge_score += 1
        $ renpy.notify(t("Knowledge +1"))

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1218_im_39e8e483ff.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "The scariest attack is one you never see — a man-in-the-middle. An attacker secretly positions themselves between you and the person you're talking to, intercepting every message. Both sides think they're communicating directly, but the attacker sees everything."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1220_im_cedff0ede3.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "The only defence is key verification — confirming encryption fingerprints through a separate, trusted channel. If you skip that step, you could be handing your secrets directly to the adversary."

    # MCQ
    call screen mcq_question(
        question=t("What is a 'man-in-the-middle' attack?"),
        answers=[t("Physical server theft"), t("Intercepting communication between two parties"), t("Overloading a server"), t("Guessing a password")],
        correct_index=1,
        explanation=t("A man-in-the-middle (MITM) attack occurs when an attacker secretly intercepts and possibly alters communication between two parties who believe they are communicating directly. This is why verifying encryption keys through a separate channel is critical.")
    )

    # --- Final Choice: Culminating Moral Decision ---

    show edward neutral at stage_center
    with dissolve

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1235_narrator_voice_08a8526fb3.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "Years have passed. The world has changed — partly because of what you did, and partly in spite of it."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1237_narrator_voice_fa6dfd1c1f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "A journalist contacts you with a new trove of classified documents from a different whistleblower. The cycle could begin again."

    show edward thoughtful
    $ localized_voice = voice_for_current_language("audio/voice/en/script_1240_im_6841c8ac3d.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    im "Another person on the inside, seeing what I saw, feeling what I felt. They're asking me what to do."

    menu:
        "Encourage them to leak. The public deserves to know.":
            $ tree_record_choice("choice_ch5_1", "encourage")
            show edward determined
            $ localized_voice = voice_for_current_language("audio/voice/en/script_1246_e_4f4a602c3f.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            e "The public's right to know outweighs the government's desire for secrecy. If the system won't reform itself, people of conscience have to act."
            $ trust_score += 2
            $ renpy.notify(t("Trust +2"))

            $ localized_voice = voice_for_current_language("audio/voice/en/script_1250_narrator_voice_9b7a0efd80.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            narrator_voice "You help the new whistleblower establish secure communications, passing on the hard lessons of your own experience."

        "Advise caution. Use official channels first.":
            $ tree_record_choice("choice_ch5_1", "caution")
            show edward concerned
            $ localized_voice = voice_for_current_language("audio/voice/en/script_1255_e_b72bcc09af.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            e "Try the Inspector General first. Document everything. If the system fails you — and it probably will — then you'll have a record proving you tried."
            $ trust_score += 1
            $ knowledge_score += 1
            $ renpy.notify(t("Trust +1 | Knowledge +1"))

            $ localized_voice = voice_for_current_language("audio/voice/en/script_1260_narrator_voice_bd6fa239ee.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            narrator_voice "You advise a measured approach, hoping the system has improved since your time. Knowing it probably hasn't."

        "Tell them not to do it. The personal cost is too high.":
            $ tree_record_choice("choice_ch5_1", "refuse")
            show edward sad
            $ localized_voice = voice_for_current_language("audio/voice/en/script_1265_e_016930bf79.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            e "I lost my country, my family, my freedom. I'd do it again, but I won't ask anyone else to pay that price."
            $ trust_score -= 1
            $ renpy.notify(t("Trust -1"))

            $ localized_voice = voice_for_current_language("audio/voice/en/script_1269_narrator_voice_f16f66cc19.mp3")  # edge-tts-auto
            if localized_voice:  # edge-tts-auto
                voice localized_voice  # edge-tts-auto
            narrator_voice "Your honesty about the personal cost weighs heavily on the would-be whistleblower."

    hide edward with dissolve

    # --- Final scene ---

    scene bg_moscow_winter_epilogue at parallax with fade

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1277_narrator_voice_8e4ba5b403.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You remain in Russia. You were granted permanent residency in 2020 and Russian citizenship in 2022."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1279_narrator_voice_0e0e34e658.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "Your disclosures led to the USA FREEDOM Act, which reformed some surveillance practices. Major tech companies adopted end-to-end encryption."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1281_narrator_voice_e84ac7fa3a.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "But mass surveillance continues in new forms. The debate between security and privacy is far from over."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1283_narrator_voice_8f7fbf11a4.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The tools you used — encryption, Tor, secure communication — are the same tools available to everyone."

    $ localized_voice = voice_for_current_language("audio/voice/en/script_1285_narrator_voice_5dac7a125e.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The question is: will you use them?"

    # --- Determine Ending ---
    jump determine_ending
