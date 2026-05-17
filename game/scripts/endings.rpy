################################################################################
## ENDINGS.RPY — All 5 Ending Sequences
## Classified: The Snowden Files
################################################################################

################################################################################
## ENDING DETERMINATION LOGIC
################################################################################

label max_suspicion_game_over:
    $ stop_ambient(0.6)
    $ show_hud = False
    $ quick_menu = True
    $ ending_type = "silenced"
    $ tree_record_ending("silenced")
    jump ending_silenced


label determine_ending:
    $ stop_ambient(0.6)
    # Calculate the ending based on accumulated flags
    if knowledge_score >= 8 and escape_successful and contacts_secured >= 2 and not identity_exposed:
        $ ending_type = "hero"
        $ tree_record_ending("hero")
        jump ending_hero

    elif escape_successful and contacts_secured >= 1 and knowledge_score >= 5:
        $ ending_type = "fugitive"
        $ tree_record_ending("fugitive")
        jump ending_fugitive

    elif identity_exposed and not escape_successful:
        $ ending_type = "imprisoned"
        $ tree_record_ending("imprisoned")
        jump ending_imprisoned

    elif suspicion_level >= 4 and not evidence_secured:
        $ ending_type = "silenced"
        $ tree_record_ending("silenced")
        jump ending_silenced

    else:
        $ ending_type = "betrayed"
        $ tree_record_ending("betrayed")
        jump ending_betrayed


################################################################################
## ENDING 1: THE HERO (Best Ending)
################################################################################

label ending_hero:
    scene black with chapter_transition
    $ renpy.pause(1.0, hard=True)
    $ show_hud = False

    show logo_watermark

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0057_narrator_voice_eb5c85c0b4.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The documents are out. Every major newspaper in the world carries the story."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0059_narrator_voice_1b96c4ca9e.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "PRISM. XKeyscore. Boundless Informant. The names of the programs become household words."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0061_narrator_voice_18b05159ff.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "Governments scramble to explain. Citizens demand answers. The conversation about privacy changes forever."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0063_narrator_voice_a78a11feab.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You sit in a modest apartment in Moscow, watching the world you set in motion."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0065_narrator_voice_5db6799d79.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You are wanted by the most powerful nation on Earth. You may never go home again."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0067_narrator_voice_40b142ca57.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "But the truth is out. And it can never be taken back."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0069_narrator_voice_eaba96f8cc.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "In boardrooms and bedrooms, in parliaments and classrooms, people are asking the question he wanted them to ask: {i}Who is watching the watchers?{/i}"

    call screen ending_screen(
        title=t("// ENDING 1: THE HERO //"),
        color="#00FFD1",
        description=t("You successfully leaked all documents, escaped to safety, and your disclosures sparked global privacy reform. Companies adopted end-to-end encryption. Governments passed new oversight laws. The world changed."),
        lessons=[
            "Strong encryption (AES-256, PGP) is the foundation of digital privacy. Without it, no communication is truly private.",
            "Operational Security (OpSec) is not optional — every step in the chain must be secured, from encrypted channels to physical device security.",
            "Whistleblowing platforms like SecureDrop exist to protect sources. Technology can be a shield for truth."
        ],
        bg_image="images/endings/thehero.png"
    )
    if _return == "restart":
        jump start
    return


################################################################################
## ENDING 2: THE FUGITIVE (Neutral Good)
################################################################################

label ending_fugitive:
    scene black with chapter_transition
    $ renpy.pause(1.0, hard=True)
    $ show_hud = False

    show logo_watermark

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0097_narrator_voice_9831448d21.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The documents reach the journalists. The stories are published."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0099_narrator_voice_1fc0a784eb.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "But the coverage is incomplete. Some of the most damning evidence never makes it to print."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0101_narrator_voice_e2354b03d5.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You escape, barely. Your passport is revoked mid-flight. You are stranded in a Moscow airport for 40 days."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0103_narrator_voice_a306110d65.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "Russia grants you asylum — not out of kindness, but politics."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0105_narrator_voice_0bf3a1bd1c.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You become a symbol, but an incomplete one. A person trapped between two superpowers."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0107_narrator_voice_6788bdfba3.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The truth is out there, some of it. But the cost is measured in a life lived in exile."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0109_narrator_voice_f143930b2f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You will never eat at your favorite diner again. Never see your family without a screen between you. The price of partial truth."

    call screen ending_screen(
        title=t("// ENDING 2: THE FUGITIVE //"),
        color="#FFD700",
        description=t("You leaked crucial files and escaped, but live in permanent exile. The truth reached the public, but gaps in your operational security meant some evidence was lost. The surveillance debate continues, but reform is slow."),
        lessons=[
            "VPNs encrypt your traffic, but they don't make you invisible. Your VPN provider can still see your activity — trust matters.",
            "Metadata (who you contacted, when, from where) can be as revealing as message content. Stripping metadata from files before sharing is essential.",
            "Digital security requires constant vigilance — one mistake can compromise months of careful planning."
        ],
        bg_image="images/endings/fugitive.png"
    )
    if _return == "restart":
        jump start
    return


################################################################################
## ENDING 3: IMPRISONED (Bad Ending)
################################################################################

label ending_imprisoned:
    scene black with chapter_transition
    $ renpy.pause(1.0, hard=True)
    $ show_hud = False

    show logo_watermark

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0137_narrator_voice_ec85050cf2.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "They were waiting for him at the airport."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0139_narrator_voice_540b4abcaf.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The moment your passport was scanned, the system flagged you. Every camera, every sensor, every algorithm turned its eye toward Gate 14."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0141_narrator_voice_87a93064d0.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "Men in dark suits. No badges. No names. Just a quiet walk to a windowless room."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0143_narrator_voice_afd37c1eb1.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The charges: espionage, theft of government property, violation of the Espionage Act of 1917."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0145_narrator_voice_58862349a7.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The trial is closed to the public. The evidence is classified. The verdict is predetermined."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0147_narrator_voice_8c733adaa6.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "In a federal supermax facility, you watch the news through a 4-inch window of reinforced glass. The surveillance programs continue unchanged."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0149_narrator_voice_1b352eea14.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The truth dies in a cell. And the machine keeps running."

    call screen ending_screen(
        title=t("// ENDING 3: IMPRISONED //"),
        color="#FF2D55",
        description=t("Your identity was exposed before you could escape. You were arrested, charged under the Espionage Act, and sentenced to decades in federal prison. The surveillance programs continued unchecked. Nothing changed."),
        lessons=[
            "IP tracking and digital forensics can identify you in minutes if you leave traces. Always use Tor and VPNs together on untrusted networks.",
            "The Espionage Act of 1917 doesn't distinguish between whistleblowers and spies — legal protections for digital whistleblowers remain weak.",
            "Physical security is as important as digital security. Cameras, keyloggers, and 'evil maid' attacks can bypass the strongest encryption."
        ],
        bg_image="images/endings/imprissioned.png"
    )
    if _return == "restart":
        jump start
    return


################################################################################
## ENDING 4: SILENCED (Bad Ending)
################################################################################

label ending_silenced:
    scene black with chapter_transition
    $ renpy.pause(1.0, hard=True)
    $ show_hud = False

    show logo_watermark

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0177_narrator_voice_132068f71e.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The internal monitoring system flagged your access patterns three weeks before you planned to act."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0179_narrator_voice_72bc1b56af.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "Unusual file access. After-hours logins. Queries that didn't match your assigned projects."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0181_narrator_voice_250b25329f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "A quiet reassignment. Your clearance revoked overnight. Your workstation wiped."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0183_narrator_voice_5fbdee97e5.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "No arrest. No trial. No headlines. Just silence."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0185_narrator_voice_ca6ba452d0.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You find yourself working IT support in a suburban Virginia office park. No access. No power. No story."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0187_narrator_voice_7e01c18a47.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The journalists wait for a contact that never comes. The documents remain locked in NSA servers."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0189_narrator_voice_a1a530c9af.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The greatest surveillance apparatus in history continues to grow, invisible and unchallenged."

    call screen ending_screen(
        title=t("// ENDING 4: SILENCED //"),
        color="#FF2D55",
        description=t("NSA internal monitors detected your suspicious behavior before you could act. Your clearance was revoked, access terminated. The files never reached journalists. The programs continue in secret."),
        lessons=[
            "Network monitoring tools like intrusion detection systems (IDS) track access patterns. Unusual behavior triggers automated alerts.",
            "Insider threat programs use behavioral analytics to detect anomalies — accessing files outside your clearance level is immediately flagged.",
            "Firewalls work both ways: they keep threats out, but they also monitor what goes out. Data Loss Prevention (DLP) systems watch for unauthorized transfers."
        ],
        bg_image="images/endings/silenced.png"
    )
    if _return == "restart":
        jump start
    return


################################################################################
## ENDING 5: BETRAYED (Worst Ending)
################################################################################

label ending_betrayed:
    scene black with chapter_transition
    $ renpy.pause(1.0, hard=True)
    $ show_hud = False

    show logo_watermark

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0217_narrator_voice_d9291690bf.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The journalist's email was compromised from the start."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0219_narrator_voice_4d6ea8bc9f.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "What you thought was a secure PGP channel was actually a honeypot — a man-in-the-middle operation run by the very agency you were trying to expose."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0221_narrator_voice_59ed008334.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "Every document you shared was intercepted. Every plan you made was monitored. Every ally you trusted was catalogued."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0223_narrator_voice_60535234d5.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "The co-worker who offered to help? An informant. The encrypted channel? Broken by a zero-day exploit."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0225_narrator_voice_715b6fcba8.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "You disappeared on a Tuesday morning. No announcement. No media coverage."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0227_narrator_voice_09854d3a44.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "Your apartment was cleaned out within 24 hours. Your digital footprint scrubbed from every server."

    $ localized_voice = voice_for_current_language("audio/voice/en/endings_0229_narrator_voice_df310931cc.mp3")  # edge-tts-auto
    if localized_voice:  # edge-tts-auto
        voice localized_voice  # edge-tts-auto
    narrator_voice "It was as if you never existed at all."

    call screen ending_screen(
        title=t("// ENDING 5: BETRAYED //"),
        color="#FF2D55",
        description=t("Everything collapsed. A trusted contact was an NSA informant. The encrypted channel was compromised. No leaks, no escape, no legacy. You vanished without a trace."),
        lessons=[
            "Man-in-the-middle attacks can compromise even encrypted channels if you don't verify the other party's identity through key fingerprints.",
            "Trust verification is critical — in cryptography, you must independently verify public keys through a separate channel, not just accept them.",
            "Zero-day exploits can break any system. Defense in depth (multiple layers of security) is the only way to mitigate unknown vulnerabilities."
        ],
        bg_image="images/endings/betrayed.png"
    )
    if _return == "restart":
        jump start
    return


################################################################################
## ENDING SCREEN (Shared UI - Hacker/Terminal Aesthetic)
################################################################################

transform terminal_glitch:
    alpha 0.0 yoffset 20
    easein 0.8 alpha 1.0 yoffset 0
    block:
        linear 0.05 alpha 0.9
        linear 0.05 alpha 1.0
        pause 3.0
        repeat

transform slide_up_delay(d):
    alpha 0.0 yoffset 50
    pause d
    easein 1.0 alpha 1.0 yoffset 0

screen ending_screen(title, color, description, lessons, bg_image=None):
    modal True
    on "show" action Play("sound", "audio/sfx/transition.wav")
    # ── Background Layer ──────────────────────────────────────────────
    if bg_image:
        add bg_image:
            xsize 1920 ysize 1080
            fit "cover"
            align (0.5, 0.5)
        add Solid("#080C1040") # ~25% opacity overlay so the background is very bright and clear
    else:
        add "#080C10"
    
    add Solid("#00FFD105")
    
    # Subtle logo watermark
    add "images/logo.png":
        xalign 0.5 yalign 0.5
        alpha 0.03
        fit "contain"
        xsize 1000 ysize 1000

    # ── Main Content Viewport ──────────────────────────────────────────
    # NOTE: scrollbars on a viewport steal width from the inner content area,
    # which shifts xalign 0.5 off-center on a 1920px stage. We pin the column
    # at xpos 360 (= (1920 - 1200) / 2) so it sits at true visual center.
    viewport:
        xfill True yfill True
        scrollbars "vertical"
        mousewheel True
        draggable True

        vbox:
            xfill True
            
            vbox:
                xalign 0.5
                xsize 1200
                spacing 40

            null height 80
            
            # ── HEADER: ENDING TITLE ──
            vbox:
                xalign 0.5
                spacing 10
                text t("// MISSION COMPLETE //") color "#7A8A99" size 16 bold True font "fonts/DejaVuSans.ttf" xalign 0.5
                text t(title):
                    color color
                    size 72
                    bold True
                    xalign 0.5
                    font "fonts/DejaVuSans.ttf"
                    at terminal_glitch
                frame:
                    xalign 0.5 xsize 400 ysize 2
                    background color
            
            # ── DESCRIPTION CARD ──
            frame:
                xalign 0.5 xsize 1190
                background "#0D1117E6"
                padding (50, 36)
                at slide_up_delay(0.4)
                
                text description:
                    color "#E8E8E8"
                    size 24
                    text_align 0.5
                    line_spacing 6
                    font "fonts/DejaVuSans.ttf"
            
            # ── METRICS & LOGS ──
            hbox:
                xalign 0.5
                spacing 30
                
                # Left Side: Mission Metrics
                frame:
                    xsize 580 ysize 440
                    background "#0D1117E6"
                    padding (30, 26)
                    at slide_up_delay(0.8)
                    
                    vbox:
                        spacing 15
                        hbox:
                            xfill True
                            text t("MISSION METRICS") color "#00FFD1" size 14 bold True font "fonts/DejaVuSans.ttf"
                            text t("[config.version]") color "#3A4A55" size 12 font "fonts/DejaVuSans.ttf" xalign 1.0
                        
                        null height 10
                        
                        # Knowledge Bar
                        vbox:
                            spacing 4
                            hbox:
                                xfill True
                                text t("OPERATIONAL KNOWLEDGE") color "#7A8A99" size 12 font "fonts/DejaVuSans.ttf"
                                text t("[knowledge_score]/10") color "#00FFD1" size 12 bold True xalign 1.0 font "fonts/DejaVuSans.ttf"
                            frame:
                                xfill True ysize 8
                                background "#1A2530"
                                frame:
                                    xsize int(520 * (knowledge_score / 10.0)) ysize 8
                                    background "#00FFD1"
                        
                        # Suspicion Bar (Inverted Color)
                        vbox:
                            spacing 4
                            hbox:
                                xfill True
                                text t("NSA SUSPICION LEVEL") color "#7A8A99" size 12 font "fonts/DejaVuSans.ttf"
                                text t("[suspicion_level]/5") color "#FF2D55" size 12 bold True xalign 1.0 font "fonts/DejaVuSans.ttf"
                            frame:
                                xfill True ysize 8
                                background "#1A2530"
                                frame:
                                    xsize int(520 * (suspicion_level / 5.0)) ysize 8
                                    background "#FF2D55"

                        null height 10
                        frame:
                            xfill True ysize 1
                            background "#2A3540"
                        null height 5

                        # Toggle Stats
                        hbox:
                            xfill True
                            text t("IDENTITY STATUS:") color "#7A8A99" size 14 font "fonts/DejaVuSans.ttf"
                            if identity_exposed:
                                text t("EXPOSED") color "#FF2D55" size 14 bold True xalign 1.0 font "fonts/DejaVuSans.ttf"
                            else:
                                text t("SECURE") color "#00FF88" size 14 bold True xalign 1.0 font "fonts/DejaVuSans.ttf"
                        
                        hbox:
                            xfill True
                            text t("EVIDENCE STATUS:") color "#7A8A99" size 14 font "fonts/DejaVuSans.ttf"
                            if evidence_secured:
                                text t("ENCRYPTED & SENT") color "#00FFD1" size 14 bold True xalign 1.0 font "fonts/DejaVuSans.ttf"
                            else:
                                text t("LOST/RECOVERED") color "#FF2D55" size 14 bold True xalign 1.0 font "fonts/DejaVuSans.ttf"

                        hbox:
                            xfill True
                            text t("ESCAPE ROUTE:") color "#7A8A99" size 14 font "fonts/DejaVuSans.ttf"
                            if escape_successful:
                                text t("SUCCESSFUL") color "#00FF88" size 14 bold True xalign 1.0 font "fonts/DejaVuSans.ttf"
                            else:
                                text t("COMPROMISED") color "#FF2D55" size 14 bold True xalign 1.0 font "fonts/DejaVuSans.ttf"

                        hbox:
                            xfill True
                            text t("CONTACTS SECURED:") color "#7A8A99" size 14 font "fonts/DejaVuSans.ttf"
                            text t("[contacts_secured]") color "#FFD700" size 14 bold True xalign 1.0 font "fonts/DejaVuSans.ttf"

                # Right Side: Post-Mortem Analysis
                frame:
                    xsize 580 ysize 440
                    background "#0D1117E6"
                    padding (30, 26)
                    at slide_up_delay(1.2)
                    
                    vbox:
                        spacing 15
                        text t("POST-MORTEM ANALYSIS") color "#FFD700" size 14 bold True font "fonts/DejaVuSans.ttf"
                        
                        null height 5
                        
                        viewport:
                            xfill True yfill True
                            scrollbars "vertical"
                            mousewheel True
                            vbox:
                                spacing 12
                                for i, lesson in enumerate(lessons):
                                    hbox:
                                        spacing 12
                                        text str(i+1) color "#FFD700" size 14 bold True font "fonts/DejaVuSans.ttf" xsize 20
                                        text lesson color "#B8C8D8" size 14 font "fonts/DejaVuSans.ttf" line_spacing 4

            # ── ACTION BUTTONS ──
            hbox:
                xalign 0.5
                spacing 60
                at slide_up_delay(1.6)
                
                textbutton t("> REBOOT SYSTEM (RESTART)"):
                    background "#1A2530"
                    hover_background "#00FFD1"
                    text_color "#00FFD1"
                    text_hover_color "#080C10"
                    text_size 23
                    text_bold True
                    text_font "fonts/DejaVuSans.ttf"
                    padding (40, 16)
                    action [Return("restart")]

                textbutton t("> TERMINATE SESSION (EXIT)"):
                    background "#251A20"
                    hover_background "#FF2D55"
                    text_color "#FF2D55"
                    text_hover_color "#FFFFFF"
                    text_size 23
                    text_bold True
                    text_font "fonts/DejaVuSans.ttf"
                    padding (40, 16)
                    action MainMenu()

            null height 100

    # Scanline Overlay
    add Solid("#00000020")
    for _y in range(0, 1080, 4):
        add Solid("#00000040"):
            xsize 1920 ysize 1
            xpos 0 ypos _y


################################################################################
## DEV SHORTCUT: ENDING SELECTOR
################################################################################

label dev_ending_selector:
    scene black with dissolve
    
    menu:
        "Ending 1: The Hero":
            # Set minimum requirements for the UI breakdown to not look weird
            $ knowledge_score = 10
            $ trust_score = 5
            $ suspicion_level = 0
            $ contacts_secured = 3
            $ evidence_secured = True
            $ escape_successful = True
            $ identity_exposed = False
            jump ending_hero
            
        "Ending 2: The Fugitive":
            $ knowledge_score = 6
            $ trust_score = 3
            $ suspicion_level = 2
            $ contacts_secured = 1
            $ evidence_secured = True
            $ escape_successful = True
            $ identity_exposed = True
            jump ending_fugitive
            
        "Ending 3: Imprisoned":
            $ knowledge_score = 3
            $ trust_score = 2
            $ suspicion_level = 4
            $ contacts_secured = 1
            $ evidence_secured = False
            $ escape_successful = False
            $ identity_exposed = True
            jump ending_imprisoned
            
        "Ending 4: Silenced":
            $ knowledge_score = 4
            $ trust_score = 1
            $ suspicion_level = 5
            $ contacts_secured = 0
            $ evidence_secured = False
            $ escape_successful = False
            $ identity_exposed = False
            jump ending_silenced
            
        "Ending 5: Betrayed":
            $ knowledge_score = 2
            $ trust_score = -2
            $ suspicion_level = 5
            $ contacts_secured = 0
            $ evidence_secured = False
            $ escape_successful = False
            $ identity_exposed = True
            jump ending_betrayed
            
        "Cancel":
            return

screen secret_ending_shortcut():
    key "shift_K_0" action Jump("dev_ending_selector")
    key "shift_0" action Jump("dev_ending_selector")

