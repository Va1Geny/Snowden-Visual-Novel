################################################################################
## ENDINGS.RPY — All 5 Ending Sequences
## Classified: The Snowden Files
################################################################################

################################################################################
## ENDING DETERMINATION LOGIC
################################################################################

label max_suspicion_game_over:
    $ show_hud = False
    $ quick_menu = True
    $ ending_type = "silenced"
    $ tree_record_ending("silenced")
    jump ending_silenced


label determine_ending:
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

    narrator_voice "The documents are out. Every major newspaper in the world carries the story."

    narrator_voice "PRISM. XKeyscore. Boundless Informant. The names of the programs become household words."

    narrator_voice "Governments scramble to explain. Citizens demand answers. The conversation about privacy changes forever."

    narrator_voice "You sit in a modest apartment in Moscow, watching the world you set in motion."

    narrator_voice "You are wanted by the most powerful nation on Earth. You may never go home again."

    narrator_voice "But the truth is out. And it can never be taken back."

    narrator_voice "In boardrooms and bedrooms, in parliaments and classrooms, people are asking the question he wanted them to ask: {i}Who is watching the watchers?{/i}"

    call screen ending_screen(
        title="// ENDING 1: THE HERO //",
        color="#00FFD1",
        description="You successfully leaked all documents, escaped to safety, and your disclosures sparked global privacy reform. Companies adopted end-to-end encryption. Governments passed new oversight laws. The world changed.",
        lessons=[
            "Strong encryption (AES-256, PGP) is the foundation of digital privacy. Without it, no communication is truly private.",
            "Operational Security (OpSec) is not optional — every step in the chain must be secured, from encrypted channels to physical device security.",
            "Whistleblowing platforms like SecureDrop exist to protect sources. Technology can be a shield for truth."
        ]
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

    narrator_voice "The documents reach the journalists. The stories are published."

    narrator_voice "But the coverage is incomplete. Some of the most damning evidence never makes it to print."

    narrator_voice "You escape, barely. Your passport is revoked mid-flight. You are stranded in a Moscow airport for 40 days."

    narrator_voice "Russia grants you asylum — not out of kindness, but politics."

    narrator_voice "You become a symbol, but an incomplete one. A person trapped between two superpowers."

    narrator_voice "The truth is out there, some of it. But the cost is measured in a life lived in exile."

    narrator_voice "You will never eat at your favorite diner again. Never see your family without a screen between you. The price of partial truth."

    call screen ending_screen(
        title="// ENDING 2: THE FUGITIVE //",
        color="#FFD700",
        description="You leaked crucial files and escaped, but live in permanent exile. The truth reached the public, but gaps in your operational security meant some evidence was lost. The surveillance debate continues, but reform is slow.",
        lessons=[
            "VPNs encrypt your traffic, but they don't make you invisible. Your VPN provider can still see your activity — trust matters.",
            "Metadata (who you contacted, when, from where) can be as revealing as message content. Stripping metadata from files before sharing is essential.",
            "Digital security requires constant vigilance — one mistake can compromise months of careful planning."
        ]
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

    narrator_voice "They were waiting for him at the airport."

    narrator_voice "The moment your passport was scanned, the system flagged you. Every camera, every sensor, every algorithm turned its eye toward Gate 14."

    narrator_voice "Men in dark suits. No badges. No names. Just a quiet walk to a windowless room."

    narrator_voice "The charges: espionage, theft of government property, violation of the Espionage Act of 1917."

    narrator_voice "The trial is closed to the public. The evidence is classified. The verdict is predetermined."

    narrator_voice "In a federal supermax facility, you watch the news through a 4-inch window of reinforced glass. The surveillance programs continue unchanged."

    narrator_voice "The truth dies in a cell. And the machine keeps running."

    call screen ending_screen(
        title="// ENDING 3: IMPRISONED //",
        color="#FF2D55",
        description="Your identity was exposed before you could escape. You were arrested, charged under the Espionage Act, and sentenced to decades in federal prison. The surveillance programs continued unchecked. Nothing changed.",
        lessons=[
            "IP tracking and digital forensics can identify you in minutes if you leave traces. Always use Tor and VPNs together on untrusted networks.",
            "The Espionage Act of 1917 doesn't distinguish between whistleblowers and spies — legal protections for digital whistleblowers remain weak.",
            "Physical security is as important as digital security. Cameras, keyloggers, and 'evil maid' attacks can bypass the strongest encryption."
        ]
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

    narrator_voice "The internal monitoring system flagged your access patterns three weeks before you planned to act."

    narrator_voice "Unusual file access. After-hours logins. Queries that didn't match your assigned projects."

    narrator_voice "A quiet reassignment. Your clearance revoked overnight. Your workstation wiped."

    narrator_voice "No arrest. No trial. No headlines. Just silence."

    narrator_voice "You find yourself working IT support in a suburban Virginia office park. No access. No power. No story."

    narrator_voice "The journalists wait for a contact that never comes. The documents remain locked in NSA servers."

    narrator_voice "The greatest surveillance apparatus in history continues to grow, invisible and unchallenged."

    call screen ending_screen(
        title="// ENDING 4: SILENCED //",
        color="#FF2D55",
        description="NSA internal monitors detected your suspicious behavior before you could act. Your clearance was revoked, access terminated. The files never reached journalists. The programs continue in secret.",
        lessons=[
            "Network monitoring tools like intrusion detection systems (IDS) track access patterns. Unusual behavior triggers automated alerts.",
            "Insider threat programs use behavioral analytics to detect anomalies — accessing files outside your clearance level is immediately flagged.",
            "Firewalls work both ways: they keep threats out, but they also monitor what goes out. Data Loss Prevention (DLP) systems watch for unauthorized transfers."
        ]
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

    narrator_voice "The journalist's email was compromised from the start."

    narrator_voice "What you thought was a secure PGP channel was actually a honeypot — a man-in-the-middle operation run by the very agency you were trying to expose."

    narrator_voice "Every document you shared was intercepted. Every plan you made was monitored. Every ally you trusted was catalogued."

    narrator_voice "The co-worker who offered to help? An informant. The encrypted channel? Broken by a zero-day exploit."

    narrator_voice "You disappeared on a Tuesday morning. No announcement. No media coverage."

    narrator_voice "Your apartment was cleaned out within 24 hours. Your digital footprint scrubbed from every server."

    narrator_voice "It was as if you never existed at all."

    call screen ending_screen(
        title="// ENDING 5: BETRAYED //",
        color="#FF2D55",
        description="Everything collapsed. A trusted contact was an NSA informant. The encrypted channel was compromised. No leaks, no escape, no legacy. You vanished without a trace.",
        lessons=[
            "Man-in-the-middle attacks can compromise even encrypted channels if you don't verify the other party's identity through key fingerprints.",
            "Trust verification is critical — in cryptography, you must independently verify public keys through a separate channel, not just accept them.",
            "Zero-day exploits can break any system. Defense in depth (multiple layers of security) is the only way to mitigate unknown vulnerabilities."
        ]
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

screen ending_screen(title, color, description, lessons):
    modal True
    
    # ── Background Layer ──────────────────────────────────────────────
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
                text "// MISSION COMPLETE //" color "#7A8A99" size 16 bold True font "DejaVuSans.ttf" xalign 0.5
                text title:
                    color color
                    size 72
                    bold True
                    xalign 0.5
                    font "DejaVuSans.ttf"
                    at terminal_glitch
                frame:
                    xalign 0.5 xsize 400 ysize 2
                    background color
            
            # ── DESCRIPTION CARD ──
            frame:
                xalign 0.5 xsize 1000
                background "#0D1117F0"
                padding (40, 30)
                at slide_up_delay(0.4)
                
                text description:
                    color "#E8E8E8"
                    size 24
                    text_align 0.5
                    line_spacing 6
                    font "DejaVuSans.ttf"
            
            # ── METRICS & LOGS ──
            hbox:
                xalign 0.5
                spacing 30
                
                # Left Side: Mission Metrics
                frame:
                    xsize 580 ysize 420
                    background "#0D1117F0"
                    padding (24, 20)
                    at slide_up_delay(0.8)
                    
                    vbox:
                        spacing 15
                        hbox:
                            xfill True
                            text "MISSION METRICS" color "#00FFD1" size 14 bold True font "DejaVuSans.ttf"
                            text "[config.version]" color "#3A4A55" size 12 font "DejaVuSans.ttf" xalign 1.0
                        
                        null height 10
                        
                        # Knowledge Bar
                        vbox:
                            spacing 4
                            hbox:
                                xfill True
                                text "OPERATIONAL KNOWLEDGE" color "#7A8A99" size 12 font "DejaVuSans.ttf"
                                text "[knowledge_score]/10" color "#00FFD1" size 12 bold True xalign 1.0 font "DejaVuSans.ttf"
                            frame:
                                xfill True ysize 8
                                background "#1A2530"
                                frame:
                                    xsize int(532 * (knowledge_score / 10.0)) ysize 8
                                    background "#00FFD1"
                        
                        # Suspicion Bar (Inverted Color)
                        vbox:
                            spacing 4
                            hbox:
                                xfill True
                                text "NSA SUSPICION LEVEL" color "#7A8A99" size 12 font "DejaVuSans.ttf"
                                text "[suspicion_level]/5" color "#FF2D55" size 12 bold True xalign 1.0 font "DejaVuSans.ttf"
                            frame:
                                xfill True ysize 8
                                background "#1A2530"
                                frame:
                                    xsize int(532 * (suspicion_level / 5.0)) ysize 8
                                    background "#FF2D55"

                        null height 10
                        frame:
                            xfill True ysize 1
                            background "#2A3540"
                        null height 5

                        # Toggle Stats
                        hbox:
                            xfill True
                            text "IDENTITY STATUS:" color "#7A8A99" size 14 font "DejaVuSans.ttf"
                            if identity_exposed:
                                text "EXPOSED" color "#FF2D55" size 14 bold True xalign 1.0 font "DejaVuSans.ttf"
                            else:
                                text "SECURE" color "#00FF88" size 14 bold True xalign 1.0 font "DejaVuSans.ttf"
                        
                        hbox:
                            xfill True
                            text "EVIDENCE STATUS:" color "#7A8A99" size 14 font "DejaVuSans.ttf"
                            if evidence_secured:
                                text "ENCRYPTED & SENT" color "#00FFD1" size 14 bold True xalign 1.0 font "DejaVuSans.ttf"
                            else:
                                text "LOST/RECOVERED" color "#FF2D55" size 14 bold True xalign 1.0 font "DejaVuSans.ttf"

                        hbox:
                            xfill True
                            text "ESCAPE ROUTE:" color "#7A8A99" size 14 font "DejaVuSans.ttf"
                            if escape_successful:
                                text "SUCCESSFUL" color "#00FF88" size 14 bold True xalign 1.0 font "DejaVuSans.ttf"
                            else:
                                text "COMPROMISED" color "#FF2D55" size 14 bold True xalign 1.0 font "DejaVuSans.ttf"

                        hbox:
                            xfill True
                            text "CONTACTS SECURED:" color "#7A8A99" size 14 font "DejaVuSans.ttf"
                            text "[contacts_secured]" color "#FFD700" size 14 bold True xalign 1.0 font "DejaVuSans.ttf"

                # Right Side: Post-Mortem Analysis
                frame:
                    xsize 580 ysize 420
                    background "#0D1117F0"
                    padding (24, 20)
                    at slide_up_delay(1.2)
                    
                    vbox:
                        spacing 15
                        text "POST-MORTEM ANALYSIS" color "#FFD700" size 14 bold True font "DejaVuSans.ttf"
                        
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
                                        text str(i+1) color "#FFD700" size 14 bold True font "DejaVuSans.ttf" xsize 20
                                        text lesson color "#B8C8D8" size 14 font "DejaVuSans.ttf" line_spacing 4

            # ── ACTION BUTTONS ──
            hbox:
                xalign 0.5
                spacing 60
                at slide_up_delay(1.6)
                
                textbutton "> REBOOT SYSTEM (RESTART)":
                    background "#1A2530"
                    hover_background "#00FFD1"
                    text_color "#00FFD1"
                    text_hover_color "#080C10"
                    text_size 20
                    text_bold True
                    text_font "DejaVuSans.ttf"
                    padding (40, 16)
                    action [Return("restart")]

                textbutton "> TERMINATE SESSION (EXIT)":
                    background "#251A20"
                    hover_background "#FF2D55"
                    text_color "#FF2D55"
                    text_hover_color "#FFFFFF"
                    text_size 20
                    text_bold True
                    text_font "DejaVuSans.ttf"
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
        "Select Ending to View (Dev Tool):"
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
