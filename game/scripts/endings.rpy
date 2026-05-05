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

    narrator_voice "Edward Snowden sits in a modest apartment in Moscow, watching the world he set in motion."

    narrator_voice "He is wanted by the most powerful nation on Earth. He may never go home again."

    narrator_voice "But the truth is out. And it can never be taken back."

    narrator_voice "In boardrooms and bedrooms, in parliaments and classrooms, people are asking the question he wanted them to ask: {i}Who is watching the watchers?{/i}"

    call screen ending_screen(
        title="// ENDING 1: THE HERO //",
        color="#00FFD1",
        description="Snowden successfully leaked all documents, escaped to safety, and his disclosures sparked global privacy reform. Companies adopted end-to-end encryption. Governments passed new oversight laws. The world changed.",
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

    narrator_voice "Snowden escapes, barely. His passport is revoked mid-flight. He is stranded in a Moscow airport for 40 days."

    narrator_voice "Russia grants him asylum — not out of kindness, but politics."

    narrator_voice "He becomes a symbol, but an incomplete one. A man trapped between two superpowers."

    narrator_voice "The truth is out there, some of it. But the cost is measured in a life lived in exile."

    narrator_voice "He will never eat at his favorite diner again. Never see his family without a screen between them. The price of partial truth."

    call screen ending_screen(
        title="// ENDING 2: THE FUGITIVE //",
        color="#FFD700",
        description="Snowden leaked crucial files and escaped, but lives in permanent exile. The truth reached the public, but gaps in his operational security meant some evidence was lost. The surveillance debate continues, but reform is slow.",
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

    narrator_voice "The moment Snowden's passport was scanned, the system flagged him. Every camera, every sensor, every algorithm turned its eye toward Gate 14."

    narrator_voice "Men in dark suits. No badges. No names. Just a quiet walk to a windowless room."

    narrator_voice "The charges: espionage, theft of government property, violation of the Espionage Act of 1917."

    narrator_voice "The trial is closed to the public. The evidence is classified. The verdict is predetermined."

    narrator_voice "In a federal supermax facility, Edward Snowden watches the news through a 4-inch window of reinforced glass. The surveillance programs continue unchanged."

    narrator_voice "The truth dies in a cell. And the machine keeps running."

    call screen ending_screen(
        title="// ENDING 3: IMPRISONED //",
        color="#FF2D55",
        description="Snowden's identity was exposed before he could escape. He was arrested, charged under the Espionage Act, and sentenced to decades in federal prison. The surveillance programs continued unchecked. Nothing changed.",
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

    narrator_voice "The internal monitoring system flagged Edward Snowden's access patterns three weeks before he planned to act."

    narrator_voice "Unusual file access. After-hours logins. Queries that didn't match his assigned projects."

    narrator_voice "A quiet reassignment. His clearance revoked overnight. His workstation wiped."

    narrator_voice "No arrest. No trial. No headlines. Just silence."

    narrator_voice "Snowden finds himself working IT support in a suburban Virginia office park. No access. No power. No story."

    narrator_voice "The journalists wait for a contact that never comes. The documents remain locked in NSA servers."

    narrator_voice "The greatest surveillance apparatus in history continues to grow, invisible and unchallenged."

    call screen ending_screen(
        title="// ENDING 4: SILENCED //",
        color="#FF2D55",
        description="NSA internal monitors detected Snowden's suspicious behavior before he could act. His clearance was revoked, access terminated. The files never reached journalists. The programs continue in secret.",
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

    narrator_voice "What Snowden thought was a secure PGP channel was actually a honeypot — a man-in-the-middle operation run by the very agency he was trying to expose."

    narrator_voice "Every document he shared was intercepted. Every plan he made was monitored. Every ally he trusted was catalogued."

    narrator_voice "The co-worker who offered to help? An informant. The encrypted channel? Broken by a zero-day exploit."

    narrator_voice "Edward Snowden disappeared on a Tuesday morning. No announcement. No media coverage."

    narrator_voice "His apartment was cleaned out within 24 hours. His digital footprint scrubbed from every server."

    narrator_voice "It was as if he never existed at all."

    call screen ending_screen(
        title="// ENDING 5: BETRAYED //",
        color="#FF2D55",
        description="Everything collapsed. A trusted contact was an NSA informant. The encrypted channel was compromised. No leaks, no escape, no legacy. Snowden vanished without a trace.",
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
    # Dark terminal background
    add "#050A0F"
    
    # Animated subtle logo
    add "animated_logo":
        xalign 0.5 yalign 0.5
        alpha 0.05

    viewport:
        xfill True yfill True
        scrollbars "vertical"
        mousewheel True

        fixed:
            xfill True
            yfit True

            frame:
                xpos 0.5 xanchor 0.5
                yoffset 60
                xsize 1100
                background Solid("#000000CC")
                padding (40, 40)
                
                vbox:
                    xfill True
                    spacing 30
                    
                    # Header
                    text title:
                        color color
                        size 56
                        bold True
                        xalign 0.5
                        at terminal_glitch

                    null height 5

                    # Description Box
                    frame:
                        xfill True
                        background Solid("#0A121A")
                        padding (30, 25)
                        at slide_up_delay(0.5)

                        text description:
                            color "#E8E8E8"
                            size 22
                            xalign 0.5
                            text_align 0.5

                    null height 10

                    # Score Breakdown
                    frame:
                        xfill True
                        background Solid("#0A121A")
                        padding (30, 25)
                        at slide_up_delay(1.0)

                        vbox:
                            spacing 15

                            text "> root@nsa-surveillance:~# ./mission_debrief.sh" color "#00FF41" size 20
                            null height 5

                            hbox:
                                xfill True
                                text "Knowledge Score:" color "#888888" size 20
                                text "[knowledge_score]/10" color "#00FFD1" size 20 bold True xalign 1.0

                            hbox:
                                xfill True
                                text "Trust Score:" color "#888888" size 20
                                text "[trust_score]" color "#FFD700" size 20 bold True xalign 1.0

                            hbox:
                                xfill True
                                text "Suspicion Level:" color "#888888" size 20
                                text "[suspicion_level]/5" color "#FF2D55" size 20 bold True xalign 1.0

                            hbox:
                                xfill True
                                text "Contacts Secured:" color "#888888" size 20
                                text "[contacts_secured]" color "#00FFD1" size 20 bold True xalign 1.0

                            hbox:
                                xfill True
                                text "Evidence Secured:" color "#888888" size 20
                                if evidence_secured:
                                    text "YES" color "#00FF00" size 20 bold True xalign 1.0
                                else:
                                    text "NO" color "#FF2D55" size 20 bold True xalign 1.0

                            hbox:
                                xfill True
                                text "Escape:" color "#888888" size 20
                                if escape_successful:
                                    text "SUCCESSFUL" color "#00FF00" size 20 bold True xalign 1.0
                                else:
                                    text "FAILED" color "#FF2D55" size 20 bold True xalign 1.0

                    # What did we learn?
                    frame:
                        xfill True
                        background Solid("#0A121A")
                        padding (30, 25)
                        at slide_up_delay(1.5)

                        vbox:
                            spacing 15

                            text "> root@nsa-surveillance:~# cat post_mortem_analysis.log" color "#00FF41" size 20

                            null height 5

                            for i, lesson in enumerate(lessons):
                                hbox:
                                    spacing 15
                                    text ">>" color color size 18 yalign 0.0 bold True
                                    text lesson color "#00FF41" size 18

                    null height 30

                    # Buttons
                    hbox:
                        xalign 0.5
                        spacing 50
                        at slide_up_delay(2.0)

                        textbutton "> [[ EXECUTE: RESTART ]":
                            text_color "#00FFD1"
                            text_hover_color "#FFFFFF"
                            text_size 24
                            text_bold True
                            action [Return("restart")]

                        textbutton "> [[ SYSTEM: EXIT ]":
                            text_color "#FF2D55"
                            text_hover_color "#FFFFFF"
                            text_size 24
                            text_bold True
                            action MainMenu()

                    null height 40

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
