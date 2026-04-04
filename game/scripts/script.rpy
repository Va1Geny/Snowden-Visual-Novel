################################################################################
## SCRIPT.RPY — Main Game Script (All 5 Chapters + Introduction)
## Classified: The Snowden Files
################################################################################

################################################################################
## GAME START
################################################################################

label start:
    $ show_hud = False
    jump intro


################################################################################
## INTRODUCTION SEQUENCE
################################################################################

label intro:
    scene black
    with fade

    $ renpy.pause(0.5)

    centered "{i}\"The greatest fear I have regarding the outcome of these disclosures\nis that nothing will change.\"{/i}\n\n— Edward Snowden"

    $ renpy.pause(3.0)

    scene black with dissolve

    narrator_voice "The year is 2013."

    narrator_voice "The United States government operates the most sophisticated surveillance network in human history."

    narrator_voice "Billions of phone calls, emails, and internet sessions are collected, analyzed, and stored — all in the name of national security."

    narrator_voice "You are Edward Snowden — NSA contractor, former CIA employee, and the man who is about to make the most consequential decision of his life."

    narrator_voice "Your choices in this story mirror the real dilemmas Snowden faced. Some paths lead to freedom. Others lead to ruin."

    narrator_voice "Along the way, your knowledge of network security will be tested. Every correct answer moves you closer to the truth."

    narrator_voice "Pay attention. Think carefully. The skills you learn here are real — and in the digital age, they matter."

    call screen briefing_screen

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
    $ current_chapter = 1
    $ show_hud = True

    call screen chapter_title_screen(1, "INSIDE THE MACHINE", "NSA Facility — Oahu, Hawaii — 2012")

    scene bg_nsa_exterior at parallax with chapter_transition

    # --- Scene: Arriving at the NSA ---

    narrator_voice "The Tunnel. That's what they call it — the underground NSA facility beneath a pineapple field in Oahu, Hawaii."

    scene bg_nsa_checkpoint at parallax with dissolve
    narrator_voice "Edward Snowden walks through layers of biometric security. Badge. Fingerprint. Retinal scan. The door hisses open."

    scene bg_nsa_main at parallax with dissolve
    show edward neutral at enter_center
    with dissolve

    im "Another day inside the machine. Rows of monitors tracking billions of data points. Every packet, every connection, every digital breath."

    show supervisor neutral at enter_right
    with dissolve

    supervisor "Morning, Snowden. We've got a batch of flagged selectors to process. XKeyscore caught some interesting traffic overnight."

    e "Yes sir. I'll pull up the queue."


    supervisor "And don't overthink the 'why.' If the system flags a packet, it's because the math says they're a threat. Your job is to verify the handshake, not question the person."

    show colleague neutral at enter_left
    with dissolve

    colleague "Hey Ed. Check this out — I can watch this guy's webcam feed in real time. He's just eating cereal. It's wild what we can access without even a targeted request."

    e "That's... that's a lot of access for an unflagged individual."

    colleague "Welcome to the NSA, man. Everything is accessible. Everything."

    im "The scale of it is staggering. This isn't targeted surveillance. This is a vacuum cleaner, sucking up everything."

    # --- Choice 1: Follow protocol or explore restricted files? ---
    hide colleague neutral with dissolve
    hide supervisor neutral with dissolve

    menu:
        "Follow protocol. Process the flagged selectors as assigned.":
            e "Alright, let's focus on the assignment. Processing the flagged selectors now."
            $ trust_score += 1
            $ renpy.notify("Trust +1")

            scene bg_nsa_terminal at parallax with dissolve
            show edward neutral at center
            with dissolve

            im "Stay in your lane, Snowden. Do your job. Don't attract attention."

            narrator_voice "Edward processes the assigned selectors. Standard targets. Foreign IP addresses. But among the flagged traffic, domestic addresses keep appearing."

        "Explore the restricted directories. Something doesn't add up.":
            e "I need to check something first..."
            $ suspicion_level += 1
            $ renpy.notify("Suspicion +1")

            scene bg_nsa_terminal at parallax with dissolve
            show edward neutral at center
            with dissolve

            im "These directories shouldn't be this easy to access. Why does a systems administrator have read access to raw intelligence feeds?"

            narrator_voice "Edward navigates deeper into the classified file system. Folders upon folders of surveillance programs he's never been briefed on. The scope is enormous."

    # --- Tutorial Exposition ---

    narrator_voice "On his screen, Edward sees the tools of the trade: network monitoring dashboards tracking millions of connections in real time."

    sys "// SYSTEM NOTE: Network monitoring tools analyze traffic patterns. Firewalls filter incoming and outgoing packets based on predefined rules. Access control determines who can see what. //"

    # --- Minigame 1: Firewall Breach ---

    $ mg_intro = renpy.call_screen("minigame_intro", title="FIREWALL BREACH", description="You must analyze incoming network packets and decide which to ALLOW through the firewall and which to BLOCK. Look for suspicious ports, unknown source IPs, and insecure protocols.")

    if mg_intro:
        $ mg_firewall_score = renpy.call_screen("minigame_firewall")
        if mg_firewall_score >= 6:
            $ knowledge_score += 2
            $ renpy.notify("Knowledge +2")
            sys "// CHALLENGE PASSED. Your firewall analysis was solid. //"
        else:
            $ suspicion_level += 1
            $ renpy.notify("Suspicion +1")
            sys "// CHALLENGE FAILED. Poor packet filtering leaves the network vulnerable. //"
    else:
        $ knowledge_score -= 1
        $ renpy.notify("Knowledge -1 (Skipped)")

    # --- Question Segment 1: MCQ ---

    call screen mcq_question(
        question="What does VPN stand for?",
        answers=["Virtual Private Network", "Verified Protocol Node", "Virtual Program Network", "Variable Packet Node"],
        correct_index=0,
        explanation="A VPN (Virtual Private Network) creates an encrypted tunnel between your device and a VPN server, protecting your traffic from surveillance on the local network."
    )

    # --- Choice 2: Report anomaly or stay silent? ---
    show edward neutral at center
    show supervisor neutral at enter_right
    with dissolve

    narrator_voice "While processing selectors, Edward discovers domestic IP addresses mixed in with foreign intelligence targets."

    e "Sir, I'm seeing domestic addresses in the foreign intelligence queue. These are American citizens."

    if suspicion_level >= 2:
        supervisor "Snowden. I've noticed you've been poking around where you shouldn't. Are you having second thoughts about your oath?"
        e "No sir. Just doing my due diligence."
        supervisor "Your 'due diligence' is noted. Logged and noted."
        $ suspicion_level += 1
        $ renpy.notify("Suspicion +1")
    else:
        supervisor "Those addresses were flagged by the FISA court authorization. Everything is legal, Snowden. Don't make waves."

    menu:
        "Report the anomaly to the Inspector General's office.":
            e "I should file a formal concern with the IG office."
            $ trust_score += 2
            $ renpy.notify("Trust +2")

            supervisor "Do what you have to do. But I'm telling you, this goes nowhere."

            im "I filed the report. I used the proper channels. And nothing happened. Nothing."

            narrator_voice "The report was acknowledged, reviewed, and buried. The system protects itself."

        "Stay silent. Keep working. Gather more information.":
            im "Not yet. I need to understand the full scope before I act. If I report one anomaly, they'll lock me out. I need to see the whole picture."
            $ trust_score -= 1
            $ renpy.notify("Trust -1")

            narrator_voice "Edward continues working in silence, but his eyes are open. Every day reveals more."

    hide supervisor neutral with dissolve
    hide edward neutral with dissolve

    # --- Chapter 1 Summary ---

    if knowledge_score >= 2 and trust_score >= 1:
        $ ch1_outcome = "good"
    else:
        $ ch1_outcome = "bad"

    call screen chapter_summary(1, "INSIDE THE MACHINE")

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
    $ current_chapter = 2

    call screen chapter_title_screen(2, "THE PRISM REVELATION", "NSA Servers — Classified Briefings — 2012-2013")

    scene bg_prism at parallax with chapter_transition

    show edward neutral at enter_center
    with dissolve

    # --- Snowden discovers PRISM ---

    im "I found it. The architecture is... infinite. It's not a targeted tap anymore. It's a vacuum."

    im "They call it PRISM — a direct pipeline into the servers of every major tech company. Google. Facebook. Apple. Microsoft. All of them."

    sys "// CLASSIFIED: PRISM — Planning Tool for Resource Integration, Synchronization, and Management. Direct server access to 9 major internet service providers. //"

    im "We aren't looking for needles in haystacks. We're just stealing the whole field."

    narrator_voice "The PRISM program gave the NSA direct access to user data from the world's largest tech companies. Emails, chat logs, file transfers, photos — all accessible without individual warrants."

    sys "// SYSTEM NOTE: PRISM worked by collecting data 'upstream' — directly from fiber-optic cables and company servers, bypassing traditional warrant requirements through the FISA Amendments Act. //"

    # --- Internal conflict with colleague ---
    show colleague neutral at enter_left
    with dissolve

    colleague "Ed, you look like you've seen a ghost. What's wrong?"

    e "Have you ever looked at what we're actually collecting? Not the reports. The raw feeds."

    colleague "I try not to think about it too much. We've got clearance, we've got authorization. That's enough for me."

    e "Is it? Because what I'm seeing goes way beyond foreign intelligence. This is domestic surveillance on a massive scale."

    colleague "Ed... be very careful what you say next. The walls have ears. Literally."

    # --- Choice 1: Trust colleague or work alone? ---

    menu:
        "Trust the colleague. Share what you've found.":
            e "Look, I need someone I can trust. What I've found... it's bigger than both of us."
            $ trust_score += 1
            $ renpy.notify("Trust +1")

            colleague "I... I've had my own doubts. But Ed, if you're thinking what I think you're thinking, you need to be incredibly careful."

            colleague "Whatever you do, don't use the internal network. They monitor everything. Every keystroke."

            im "At least I'm not completely alone in this."

        "Work alone. Trust no one inside the NSA.":
            e "Never mind. Forget I said anything. Just tired."
            $ suspicion_level += 0
            $ trust_score -= 1
            $ renpy.notify("Trust -1")

            colleague "Sure, man. Get some rest."

            im "I can't trust anyone here. One wrong word and I'm done. I need to do this alone."

    hide colleague neutral with dissolve

    # --- Question Segment 2: Text Input ---

    call screen text_input_question_screen(
        question="Type the name of the NSA surveillance program Snowden exposed:",
        correct_answer="PRISM",
        hint="It's named after a glass object that splits light into a spectrum...",
        explanation="PRISM was a clandestine mass electronic surveillance data mining program launched in 2007 by the NSA, with participation from major tech companies."
    )

    # --- Minigame 2: Decrypt the Message ---

    $ mg_intro2 = renpy.call_screen("minigame_intro", title="DECRYPT THE MESSAGE", description="A classified document name has been encrypted using a Caesar cipher (ROT-3). Decode the message by shifting each letter back by 3 positions in the alphabet.")

    if mg_intro2:
        $ mg_decrypt_solved = renpy.call_screen("minigame_decrypt")
        if mg_decrypt_solved:
            $ knowledge_score += 2
            $ evidence_secured = True
            $ renpy.notify("Knowledge +2 | Evidence Secured!")
        else:
            $ renpy.notify("Decryption failed.")
    else:
        $ knowledge_score -= 1
        $ renpy.notify("Knowledge -1 (Skipped)")

    # --- Choice 2: Copy the files or take notes only? ---
    scene bg_nsa_servers at parallax with dissolve
    show edward neutral at center
    with dissolve

    im "I have access to everything. The question is: what do I do with it?"

    narrator_voice "Edward stares at his screen. The classified documents are right there. Proof of mass surveillance. Proof of constitutional violations."

    menu:
        "Copy the files to an encrypted drive. This evidence needs to survive.":
            im "I need the original documents. Notes won't be enough. Journalists need primary sources."
            $ evidence_secured = True
            $ suspicion_level += 1
            $ renpy.notify("Evidence Secured! | Suspicion +1")

            narrator_voice "Edward carefully copies selected documents to a micro SD card hidden inside a Rubik's Cube. Every file transfer is a risk."

            sys "// DATA TRANSFER INITIATED. ENCRYPTION: AES-256. CONTAINER: VERACRYPT HIDDEN VOLUME. //"

        "Take detailed notes only. Digital evidence is too risky.":
            im "If they catch me with files, it's espionage. Notes are deniable."
            $ trust_score -= 1
            $ renpy.notify("Trust -1")

            narrator_voice "Edward writes down key details from memory. It's safer, but journalists may question the credibility without primary documents."

    hide edward neutral with dissolve

    # --- MCQ Question ---
    call screen mcq_question(
        question="Which protocol encrypts web traffic?",
        answers=["HTTP", "FTP", "HTTPS", "SMTP"],
        correct_index=2,
        explanation="HTTPS (HyperText Transfer Protocol Secure) uses SSL/TLS encryption to secure data transmitted between your browser and a web server. Regular HTTP sends everything in plain text."
    )

    # --- Chapter 2 Summary ---

    if evidence_secured and knowledge_score >= 4:
        $ ch2_outcome = "good"
    else:
        $ ch2_outcome = "bad"

    call screen chapter_summary(2, "THE PRISM REVELATION")

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
    $ current_chapter = 3

    call screen chapter_title_screen(3, "THE CONTACT", "Encrypted Communications — January 2013")

    scene bg_hong_kong at parallax with chapter_transition

    show edward neutral at enter_left
    with dissolve

    # --- Snowden must contact journalists ---

    im "I have the evidence. Now I need someone to publish it. But one wrong email, one unencrypted message, and the NSA will know before the ink is dry."

    narrator_voice "Edward needs to contact journalists who can responsibly publish the classified documents. But the NSA monitors virtually all electronic communication."

    sys "// SYSTEM NOTE: OpSec (Operational Security) is the practice of protecting critical information from adversaries. Every digital action leaves traces. //"

    im "I can't use my work email. I can't use my personal email. I need a completely new identity, on a completely separate network."

    # --- Snowball Effect Check ---
    if suspicion_level >= 3:
        narrator_voice "Edward's unusual access patterns have already triggered internal alerts. His options are narrowing."

        sys "// WARNING: INTERNAL SECURITY MONITORING HAS FLAGGED YOUR ACTIVITY //"

        menu:
            "Try to bluff your way through the security review.":
                $ suspicion_level += 1
                $ renpy.notify("Suspicion +1")

                im "I told them I was running diagnostic tests on the archival system. They seemed to buy it... for now."

                narrator_voice "The security team notes the explanation but doesn't close the file. The clock is ticking."

            "Accelerate the timeline. Contact journalists immediately.":
                $ trust_score -= 1
                $ renpy.notify("Trust -1")

                im "No more waiting. If I don't move now, I won't get another chance."

                jump ch3_contact_unsafe

    # --- Choice 1: Secure channel or personal email? ---

    menu:
        "Set up a PGP-encrypted email channel using Tor (requires knowledge).":
            if knowledge_score >= 3:
                jump ch3_secure_success
            else:
                jump ch3_secure_fail

        "Contact Glenn Greenwald directly through his public email.":
            $ contacts_secured += 1
            $ renpy.notify("Contacts +1")
            jump ch3_greenwald_contact

        "Wait for a safer moment to make contact.":
            $ trust_score -= 1
            $ renpy.notify("Trust -1")
            jump ch3_wait

label ch3_secure_success:
    im "I know how PGP works. Public key, private key. I generate a key pair, publish my public key, and any message encrypted with it can only be read by me."

    sys "// PGP KEY PAIR GENERATED. RSA-4096. FINGERPRINT VERIFIED THROUGH SEPARATE CHANNEL. //"

    $ contacts_secured += 1
    $ knowledge_score += 1
    $ renpy.notify("Contacts +1 | Knowledge +1")

    narrator_voice "Edward creates an anonymous email account, accessed only through Tor, and uses PGP encryption to contact documentary filmmaker Laura Poitras."

    show journalist neutral at enter_right
    with dissolve

    greenwald "I received your encrypted message. The fingerprint checks out. Who are you?"

    e "I'm a senior member of the intelligence community. I have evidence of massive, unconstitutional surveillance by the NSA."

    greenwald "Can you prove it?"

    e "I can prove everything. But we need to meet in person. And you need to learn to use encryption. Your current security is... inadequate."

    jump ch3_continue

label ch3_secure_fail:
    im "I know I need to use PGP, but I'm not confident in the setup. If I make a mistake with the key exchange..."

    sys "// WARNING: INSUFFICIENT KNOWLEDGE TO ESTABLISH SECURE CHANNEL. PROCEEDING WITH PARTIAL ENCRYPTION. //"

    $ suspicion_level += 1
    $ renpy.notify("Suspicion +1")

    narrator_voice "Edward attempts to set up encrypted communications, but makes errors in the key exchange process. The channel may not be fully secure."

    jump ch3_continue

label ch3_greenwald_contact:
    show journalist neutral at enter_right
    with dissolve

    narrator_voice "Edward reaches out to Glenn Greenwald through his public contact information. It's faster, but less secure."

    e "Mr. Greenwald, I have information of extreme importance regarding US government surveillance. We need to talk on a secure channel."

    greenwald "I get messages like this every week. Can you give me more details?"

    e "Not over this channel. You need to set up PGP encryption. I'll send you instructions."

    greenwald "PGP? I've never used it. Can't we just talk on the phone?"

    im "This is the problem. The people who need to publish this information don't know the first thing about security."

    $ suspicion_level += 1
    $ renpy.notify("Suspicion +1")

    jump ch3_continue

label ch3_wait:
    narrator_voice "Edward decides to wait for a safer window. But there may not be one."

    im "Every day I wait is another day they could catch me. But rushing makes mistakes. Mistakes get you caught."

    $ suspicion_level += 1
    $ renpy.notify("Suspicion +1")

    narrator_voice "Weeks pass. Edward's access patterns grow more suspicious. The window is closing."

    jump ch3_continue

label ch3_contact_unsafe:
    narrator_voice "With time running out, Edward takes risks he normally wouldn't."

    $ suspicion_level += 1
    $ contacts_secured += 1
    $ renpy.notify("Suspicion +1 | Contacts +1")

    im "No time for perfect OpSec. I just need to get the message out."

    jump ch3_continue

label ch3_continue:
    # --- Question Segment 3: MCQ on Encryption ---
    hide journalist neutral with dissolve
    hide edward neutral with dissolve

    call screen mcq_question(
        question="What does TOR stand for?",
        answers=["Transfer Over Router", "The Onion Router", "Terminal Output Relay", "Timed Output Router"],
        correct_index=1,
        explanation="TOR (The Onion Router) anonymizes internet traffic by encrypting it in multiple layers and routing it through a series of volunteer-operated nodes around the world, like layers of an onion."
    )

    # --- Minigame 3: OpSec Challenge ---
    $ mg_intro3 = renpy.call_screen("minigame_intro", title="OPSEC CHALLENGE", description="Review a series of actions taken by 'Agent X' who is trying to contact a journalist. Identify which actions are SAFE and which are MISTAKES that could blow their cover.")

    if mg_intro3:
        $ mg_opsec_score = renpy.call_screen("minigame_opsec")
        if mg_opsec_score >= 4:
            $ contacts_secured += 1
            $ knowledge_score += 1
            $ renpy.notify("Contacts +1 | Knowledge +1")
        else:
            $ suspicion_level += 1
            $ renpy.notify("Suspicion +1")
    else:
        $ knowledge_score -= 1
        $ renpy.notify("Knowledge -1 (Skipped)")

    # --- Choice 2: How much to reveal? ---
    show edward neutral at center
    show journalist neutral at enter_right
    with dissolve

    narrator_voice "The journalist asks for more details about the scope of the leaks."

    greenwald "I need to know what we're dealing with. How big is this?"

    menu:
        "Tell everything. Full transparency builds trust.":
            e "It's everything. PRISM, XKeyscore, Boundless Informant, upstream collection — the NSA is collecting data on hundreds of millions of people. American citizens included."
            $ trust_score += 2
            $ contacts_secured += 1
            $ renpy.notify("Trust +2 | Contacts +1")

            greenwald "My God. If this is true... this is the biggest intelligence leak in history."

        "Share only what's necessary. Protect sources and methods.":
            e "I can confirm the NSA is conducting mass domestic surveillance. I'll share the details when we meet in person."
            $ trust_score += 1
            $ renpy.notify("Trust +1")

            greenwald "Fair enough. Where do we meet?"

        "Be vague. Don't reveal the scope until you're safe.":
            e "It's significant. That's all I can say right now."
            $ trust_score -= 1
            $ renpy.notify("Trust -1")

            greenwald "You're asking me to fly halfway around the world on a vague tip?"

    hide journalist neutral with dissolve
    hide edward neutral with dissolve

    # --- Chapter 3 Summary ---

    if contacts_secured >= 2:
        $ ch3_outcome = "good"
    else:
        $ ch3_outcome = "bad"

    call screen chapter_summary(3, "THE CONTACT")

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
    $ current_chapter = 4

    call screen chapter_title_screen(4, "THE ESCAPE", "Hong Kong — May 2013")

    scene bg_hong_kong at parallax with chapter_transition

    show edward neutral at enter_left
    with dissolve

    # --- Snowden in Hong Kong ---

    narrator_voice "Edward Snowden arrives in Hong Kong with a laptop full of classified documents and a plan that's already falling apart."

    im "I told my employer I needed medical leave for epilepsy treatment. They didn't question it. That bought me a few weeks."

    im "Now I'm in a hotel room in Hong Kong, waiting for journalists who might not come, hunted by an agency that can find anyone."

    sys "// LOCATION: MIRA HOTEL, HONG KONG. STATUS: UNDETECTED — FOR NOW. //"

    # --- Tense dialogue with pressure ---

    show journalist neutral at enter_right
    with dissolve

    greenwald "You do realize what you're asking me to do? If we publish this, both our lives change forever."

    e "My life changed the moment I read those documents. I can't unread them. I can't unknow what the government is doing to its own people."

    if suspicion_level >= 3:
        sys "// WARNING: NSA INTERNAL AUDIT HAS FLAGGED YOUR ACCESS ANOMALIES. INVESTIGATION IN PROGRESS. //"

        im "They know something is wrong. I can feel it. The clock is ticking."

    greenwald "The documents check out. Laura and I have verified them. We're ready to publish."

    e "Publish everything. The world needs to see this."

    hide journalist neutral with dissolve

    # --- Choice 1: Hotel Wi-Fi or mobile hotspot? ---

    narrator_voice "Edward needs to send final instructions to the publication team, but the hotel network is compromised."

    menu:
        "Use the hotel Wi-Fi with a VPN (dangerous — hotel networks are easily monitored).":
            $ suspicion_level += 1
            $ renpy.notify("Suspicion +1")

            im "The VPN encrypts my traffic, but the hotel's network logs will show my room connected to a VPN. That alone is a red flag for anyone watching."

            sys "// WARNING: VPN CONNECTION DETECTED ON LOCAL NETWORK. COMMERCIAL VPN IPs ARE CATALOGUED BY INTELLIGENCE AGENCIES. //"

        "Use a personal mobile hotspot with Tor (safer — direct cellular connection).":
            $ trust_score += 1
            $ renpy.notify("Trust +1")

            im "A mobile hotspot bypasses the hotel network entirely. With Tor on top of it, my traffic is encrypted and anonymized through multiple relay nodes."

            sys "// SECURE CONNECTION ESTABLISHED. TRAFFIC ROUTED THROUGH 3 TOR RELAY NODES. //"

    # --- Question Segment 4: Text Input ---

    call screen text_input_question_screen(
        question="What network anonymization tool uses 'onion routing'?",
        correct_answer="TOR",
        hint="It's named after a vegetable with many layers...",
        explanation="TOR (The Onion Router) encrypts your data in multiple layers, each peeled away at successive relay nodes, making it extremely difficult to trace traffic back to its source."
    )

    # --- Minigame 4: Trace the Route ---

    $ mg_intro4 = renpy.call_screen("minigame_intro", title="TRACE THE ROUTE", description="Route your network connection from your laptop to the journalist's secure server. Avoid the Government Monitor node! Choose safe routing through VPN and Tor nodes.")

    if mg_intro4:
        $ mg_trace_solved = renpy.call_screen("minigame_trace")
        if mg_trace_solved:
            $ escape_successful = True
            $ knowledge_score += 2
            $ renpy.notify("Knowledge +2 | Escape route secured!")
        else:
            $ identity_exposed = True
            $ renpy.notify("Identity Exposed!")
    else:
        $ knowledge_score -= 1
        $ renpy.notify("Knowledge -1 (Skipped)")

    # --- Choice 2: Fly to Russia or seek another country? ---

    scene bg_leak at parallax with dissolve
    show edward neutral at center
    with dissolve

    narrator_voice "The first stories are published. The world erupts. And now, Edward Snowden is the most wanted man on Earth."

    im "The US government has revoked my passport. I need to move. Now."

    if suspicion_level >= 4:
        narrator_voice "With his cover blown, Snowden's options have narrowed to almost nothing."

        menu:
            "Head to the airport immediately. Every minute counts.":
                $ escape_successful = True
                $ renpy.notify("Escape initiated!")

                im "No time to plan. The passport might still work for a few hours before the revocation hits every system."

            "Go to the Russian consulate. They're the only ones who might help.":
                $ escape_successful = True
                $ trust_score -= 1
                $ renpy.notify("Escape to Russia | Trust -1")

                im "Russia isn't ideal, but beggars can't be choosers. They have their own reasons for helping me."

    else:
        menu:
            "Fly to Ecuador via Moscow. Multiple stops make tracking harder.":
                $ escape_successful = True
                $ renpy.notify("Escape route planned!")

                im "Ecuador has a history of granting asylum to people the US wants. WikiLeaks arranged the route through Moscow."

                narrator_voice "But Edward will never make it past Moscow. His passport will be revoked mid-flight."

            "Seek asylum at a European embassy in Hong Kong.":
                $ trust_score += 1
                $ renpy.notify("Trust +1")

                if identity_exposed:
                    narrator_voice "With his identity already exposed, no embassy will risk the diplomatic fallout of harboring him."
                    $ escape_successful = False
                else:
                    narrator_voice "The European embassies politely decline. No one wants to challenge the United States."
                    $ escape_successful = False

                im "No one will help. Not officially. Moscow may be my only option."
                $ escape_successful = True

            "Stay in Hong Kong and face the legal system.":
                $ escape_successful = False
                $ renpy.notify("Escape abandoned.")

                im "If I stay, Hong Kong will extradite me. The US legal system won't give me a fair trial under the Espionage Act."

    hide edward neutral with dissolve

    # --- Chapter 4 Summary ---

    if escape_successful and not identity_exposed:
        $ ch4_outcome = "good"
    else:
        $ ch4_outcome = "bad"

    call screen chapter_summary(4, "THE ESCAPE")

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
    $ current_chapter = 5

    call screen chapter_title_screen(5, "PERMANENT RECORD", "Moscow, Russia — 2013 to Present")

    scene bg_russia at parallax with chapter_transition

    show edward neutral at enter_left
    with dissolve

    # --- Snowden in Russia ---

    narrator_voice "The Sheremetyevo International Airport transit zone. Edward Snowden has been trapped here for 40 days."

    narrator_voice "His passport is cancelled. No country will grant him asylum without risking the wrath of the United States. Russia is his last option."

    show russian_official neutral at enter_right
    with dissolve

    russian_official "Mr. Snowden. The transit zone is a strange place, yes? You are not in Russia, but you are certainly not in America."

    russian_official "You are... nowhere. We can offer you 'somewhere.' Russia can grant you temporary asylum."

    e "I don't want to be a pawn in anyone's geopolitical chess game."

    russian_official "You became a pawn the moment you took those files, Mr. Snowden. The only question is which board you want to play on."

    # --- Reflection Dialogue ---

    hide russian_official neutral with dissolve

    im "I'm an exile in the physical world, but I've never been more active in the digital one."

    im "From this small apartment in Moscow, I can still connect to the world. The irony of a surveillance whistleblower living in the surveillance capital of the East is not lost on me."

    narrator_voice "From Moscow, Snowden continues to advocate for digital privacy through encrypted video calls, secure messaging, and speaking engagements."

    # --- Dialogue based on accumulated flags ---

    if trust_score >= 4:
        im "I trusted the right people. Greenwald, Poitras, the editors — they did what journalists are supposed to do. They told the truth."
    elif trust_score >= 1:
        im "Trust is a calculation, not a feeling. I chose carefully, but not perfectly. Some bridges burned that didn't need to."
    else:
        im "I trusted no one fully, and it cost me. Some stories never got published. Some evidence was lost. Half-measures half-worked."

    if knowledge_score >= 7:
        im "My technical knowledge kept me alive. Every encryption key, every secure channel, every OpSec decision mattered."
    elif knowledge_score >= 4:
        im "I knew enough to be dangerous, but not enough to be safe. There were gaps in my knowledge that almost got me caught."
    else:
        im "Looking back, there's so much I didn't know. So many security mistakes I made. I survived on luck as much as skill."

    # --- Question Segment 5: Final Knowledge Test ---

    # MCQ
    call screen mcq_question(
        question="What is metadata in the context of surveillance?",
        answers=["The content of a message", "Data about data (who, when, where — not what)", "Encrypted file headers", "User passwords"],
        correct_index=1,
        explanation="Metadata is 'data about data.' In surveillance terms, it includes who you communicated with, when, for how long, and from where — but not the content of the communication. The NSA argued metadata collection wasn't as invasive as content collection, but metadata can reveal intimate patterns of life."
    )

    # Text Input
    call screen text_input_question_screen(
        question="Type the encryption software Snowden used to communicate securely with journalists:",
        correct_answer="PGP",
        hint="It stands for 'Pretty Good' something...",
        explanation="PGP (Pretty Good Privacy) uses asymmetric encryption — a public key to encrypt messages and a private key to decrypt them. Snowden insisted journalists learn to use PGP before he would communicate with them."
    )

    # MCQ
    call screen mcq_question(
        question="What is a 'man-in-the-middle' attack?",
        answers=["Physical server theft", "Intercepting communication between two parties", "Overloading a server", "Guessing a password"],
        correct_index=1,
        explanation="A man-in-the-middle (MITM) attack occurs when an attacker secretly intercepts and possibly alters communication between two parties who believe they are communicating directly. This is why verifying encryption keys through a separate channel is critical."
    )

    # --- Final Choice: Culminating Moral Decision ---

    show edward neutral at center
    with dissolve

    narrator_voice "Years have passed. The world has changed — partly because of what Edward Snowden did, and partly in spite of it."

    narrator_voice "A journalist contacts Snowden with a new trove of classified documents from a different whistleblower. The cycle could begin again."

    im "Another person on the inside, seeing what I saw, feeling what I felt. They're asking me what to do."

    menu:
        "Encourage them to leak. The public deserves to know.":
            e "The public's right to know outweighs the government's desire for secrecy. If the system won't reform itself, people of conscience have to act."
            $ trust_score += 2
            $ renpy.notify("Trust +2")

            narrator_voice "Snowden helps the new whistleblower establish secure communications, passing on the hard lessons of his own experience."

        "Advise caution. Use official channels first.":
            e "Try the Inspector General first. Document everything. If the system fails you — and it probably will — then you'll have a record proving you tried."
            $ trust_score += 1
            $ knowledge_score += 1
            $ renpy.notify("Trust +1 | Knowledge +1")

            narrator_voice "Snowden advises a measured approach, hoping the system has improved since his time. Knowing it probably hasn't."

        "Tell them not to do it. The personal cost is too high.":
            e "I lost my country, my family, my freedom. I'd do it again, but I won't ask anyone else to pay that price."
            $ trust_score -= 1
            $ renpy.notify("Trust -1")

            narrator_voice "Snowden's honesty about the personal cost weighs heavily on the would-be whistleblower."

    hide edward neutral with dissolve

    # --- Final scene ---

    scene black with fade

    narrator_voice "Edward Snowden remains in Russia. He was granted permanent residency in 2020 and Russian citizenship in 2022."

    narrator_voice "His disclosures led to the USA FREEDOM Act, which reformed some surveillance practices. Major tech companies adopted end-to-end encryption."

    narrator_voice "But mass surveillance continues in new forms. The debate between security and privacy is far from over."

    narrator_voice "The tools Snowden used — encryption, Tor, secure communication — are the same tools available to you."

    narrator_voice "The question is: will you use them?"

    # --- Determine Ending ---
    jump determine_ending