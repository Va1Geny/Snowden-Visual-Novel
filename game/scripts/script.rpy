################################################################################
## SCRIPT.RPY — Main Game Script (All 5 Chapters + Introduction)
## Classified: The Snowden Files
################################################################################

################################################################################
## GAME START
################################################################################

label start:
    $ show_hud = False
    $ notebook_entries = []
    $ notebook_draft = ""
    $ suspicion_lockdown_triggered = False
    $ tree_reset_current_run()
    call screen intro_controls_screen
    jump intro


################################################################################
## INTRODUCTION SEQUENCE
################################################################################

label intro:
    scene black
    with fade

    show logo_watermark

    $ renpy.pause(0.5)

    centered "{i}\"The greatest fear I have regarding the outcome of these disclosures\nis that nothing will change.\"{/i}\n\n— Edward Snowden"

    $ renpy.pause(3.0)

    scene black with dissolve
    show logo_watermark

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
    $ persistent.tree_ch_reached = max(getattr(persistent, 'tree_ch_reached', 0), 1)

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

    im "I'm a systems administrator — I keep this infrastructure running. The irony is, the more access I have to maintain the system, the more I see what the system actually does."

    show supervisor neutral at enter_right
    with dissolve

    supervisor "Morning, Snowden. We've got a batch of flagged selectors to process. XKeyscore caught some interesting traffic overnight."

    im "XKeyscore — the NSA's most powerful search tool. It can search virtually anything a person does on the internet: emails, browsing history, chat sessions, even webcam feeds. All in near real time, all without a warrant."

    e "Yes sir. I'll pull up the queue."

    supervisor "And don't overthink the 'why.' If the system flags a packet, it's because the math says they're a threat. Your job is to verify the handshake, not question the person."

    im "Verify the handshake. That's NSA-speak for confirming the network connection is legitimate — checking that the source and destination match the selector criteria. But nobody asks whether the criteria themselves are legitimate."

    show colleague neutral at enter_left
    with dissolve

    colleague "Hey Ed. Check this out — I can watch this guy's webcam feed in real time. He's just eating cereal. It's wild what we can access without even a targeted request."

    e "That's... that's a lot of access for an unflagged individual."

    colleague "Welcome to the NSA, man. Everything is accessible. Everything."

    im "The scale of it is staggering. This isn't targeted surveillance. This is a vacuum cleaner, sucking up everything. Emails, phone records, browsing histories — all stored, all searchable, all belonging to ordinary people who've done nothing wrong."

    # --- Choice 1: Follow protocol or explore restricted files? ---
    hide colleague neutral with dissolve
    hide supervisor neutral with dissolve

    menu:
        "Follow protocol. Process the flagged selectors as assigned.":
            $ tree_record_choice("choice_ch1_1", "protocol")
            e "Alright, let's focus on the assignment. Processing the flagged selectors now."
            $ trust_score += 1
            $ renpy.notify("Trust +1")

            scene bg_nsa_terminal at parallax with dissolve
            with dissolve

            im "Stay in your lane, Snowden. Do your job. Don't attract attention."

            narrator_voice "Edward processes the assigned selectors. Standard targets. Foreign IP addresses. But among the flagged traffic, domestic addresses keep appearing."

        "Explore the restricted directories. Something doesn't add up.":
            $ tree_record_choice("choice_ch1_1", "explore")
            e "I need to check something first..."
            $ suspicion_level += 1
            $ renpy.notify("Suspicion +1")

            scene bg_nsa_terminal at parallax with dissolve
            with dissolve

            im "These directories shouldn't be this easy to access. Why does a systems administrator have read access to raw intelligence feeds?"

            narrator_voice "Edward navigates deeper into the classified file system. Folders upon folders of surveillance programs he's never been briefed on. The scope is enormous."

    # --- Tutorial Exposition: Firewall Learning Section ---
    # (Structured as a self-contained briefing — can be branched into the story tree later)

    narrator_voice "On his screen, Edward sees the tools of the trade: network monitoring dashboards tracking millions of connections in real time."

    im "Every network has a firewall — a security system that monitors all incoming and outgoing traffic and decides what gets through based on predefined rules. Think of it as a barrier between trusted and untrusted networks."

    im "The firewall inspects each packet for three things: the source IP address, the destination port number, and the protocol. Get those right and you can tell the difference between normal traffic and an intrusion attempt."

    # --- IP Addresses: Internal vs External ---

    im "First, IP addresses. Every device on a network has one — it's like a street address for computers. But not all addresses are equal."

    im "Private IP ranges — 192.168.x.x, 10.0.x.x, and 172.16.x.x — belong to your own internal network. Traffic from these addresses is usually safe because it's coming from inside the building."

    im "But an IP like 45.33.32.1 or 89.248.174.5? That's an external address — someone on the internet reaching into our network. External IPs demand much more scrutiny."

    sys "// SYSTEM NOTE: Private IPs (192.168.x.x, 10.0.x.x, 172.16.x.x) = internal/trusted. Public IPs = external/unknown — verify before allowing. //"

    # --- Ports: The Doors Into a Network ---

    im "Next, ports. If an IP address is the building's street address, a port is a specific door. Every network service listens on a numbered port, and knowing which port does what is fundamental."

    im "Port 80 is HTTP — standard, unencrypted web traffic. Port 443 is HTTPS — the same thing but encrypted with TLS. These are the two most common ports on the internet, and traffic on them is usually legitimate."

    im "Port 53 is DNS — the Domain Name System. It's how computers translate website names like 'google.com' into IP addresses. Without DNS, nothing works. It's the phone book of the internet."

    im "Port 22 is SSH — Secure Shell. It's used for remote administration, letting an authorised user log into a server from another location. From an internal IP, it's normal. From an external IP, it needs careful review."

    im "Port 3389 is RDP — Remote Desktop Protocol. It lets someone control a computer's desktop remotely. Like SSH, it's fine from a trusted internal source, but dangerous if exposed to the outside."

    sys "// SAFE PORTS (common services): 80 = HTTP | 443 = HTTPS | 53 = DNS | 22 = SSH | 3389 = RDP //"

    # --- Dangerous Ports and Protocols ---

    im "Then there are the ports that should set off alarm bells. Port 23 is Telnet — an ancient protocol that sends everything in plain text, including passwords. It has no encryption at all. Telnet should never be used; SSH replaced it decades ago."

    im "Port 31337 — pronounced 'elite' in hacker culture — is historically associated with the Back Orifice trojan. If you see traffic on port 31337 from an unknown external IP, it's almost certainly malicious."

    im "And port 4444 — the default listener for Metasploit, one of the most widely used hacking frameworks. An external IP connecting on port 4444 usually means someone is trying to establish a reverse shell — giving themselves remote control of the target machine."

    sys "// DANGER PORTS: 23 = Telnet (unencrypted!) | 31337 = Known hacker port | 4444 = Metasploit reverse shell //"

    # --- Putting It Together ---

    im "So the logic is straightforward: check the IP, check the port, check the protocol. Internal IP on a standard port? Probably safe. External IP on a suspicious port with no encryption? Block it immediately."

    sys "// FIREWALL RULE: ALLOW = internal IPs on standard ports | BLOCK = external IPs on suspicious ports or unencrypted protocols. When in doubt, block. //"

    # --- Minigame 1: Firewall Breach ---

    window hide
    $ mg_intro = renpy.call_screen("minigame_intro", title="FIREWALL BREACH", description="You must analyze incoming network packets and decide which to ALLOW through the firewall and which to BLOCK. Look for suspicious ports, unknown source IPs, and insecure protocols.")

    if mg_intro:
        $ quick_menu = False
        $ show_hud = False
        $ mg_firewall_score = renpy.call_screen("minigame_firewall")
        $ quick_menu = True
        $ show_hud = True
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

    im "Working here, I've learned how critical a VPN is. A VPN — Virtual Private Network — creates an encrypted tunnel between your device and a remote server. Anyone watching the local network sees only scrambled data, not what you're actually doing."

    im "On untrusted networks like public Wi-Fi, a VPN is essential. Without one, your browsing history, login credentials, and private messages are all visible to anyone sniffing the network."

    call screen mcq_question(
        question="What does VPN stand for?",
        answers=["Virtual Private Network", "Verified Protocol Node", "Virtual Program Network", "Variable Packet Node"],
        correct_index=0,
        explanation="A VPN (Virtual Private Network) creates an encrypted tunnel between your device and a VPN server, protecting your traffic from surveillance on the local network."
    )

    # --- Choice 2: Report anomaly or stay silent? ---
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
            $ tree_record_choice("choice_ch1_2", "report")
            e "I should file a formal concern with the IG office."
            $ trust_score += 2
            $ renpy.notify("Trust +2")

            supervisor "Do what you have to do. But I'm telling you, this goes nowhere."

            im "I filed the report. I used the proper channels. And nothing happened. Nothing."

            narrator_voice "The report was acknowledged, reviewed, and buried. The system protects itself."

        "Stay silent. Keep working. Gather more information.":
            $ tree_record_choice("choice_ch1_2", "silent")
            scene bg_1 at parallax with dissolve
            im "Not yet. I need to understand the full scope before I act. If I report one anomaly, they'll lock me out. I need to see the whole picture."
            $ trust_score -= 1
            $ renpy.notify("Trust -1")

            narrator_voice "You continue working in silence, but your eyes are open. Every day reveals more."

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
    $ persistent.tree_ch_reached = max(getattr(persistent, 'tree_ch_reached', 0), 2)

    call screen chapter_title_screen(2, "THE PRISM REVELATION", "NSA Servers — Classified Briefings — 2012-2013")

    scene bg_prism at parallax with chapter_transition

    with dissolve

    # --- Snowden discovers PRISM ---

    im "I found it. Hidden in the classified briefing materials — a program so vast it makes everything else look like a hobby project."

    im "They call it PRISM — a direct pipeline into the servers of every major tech company. Google. Facebook. Apple. Microsoft. Yahoo. All of them. Nine companies in total, handing over user data on demand."

    sys "// CLASSIFIED: PRISM — Planning Tool for Resource Integration, Synchronization, and Management. Direct server access to 9 major internet service providers. //"

    im "We aren't looking for needles in haystacks. We're just stealing the whole field. Every email, every photo, every chat message — all vacuumed up and stored in data centres the size of small cities."

    narrator_voice "The PRISM program gave the NSA direct access to user data from the world's largest tech companies. Emails, chat logs, file transfers, photos — all accessible without individual warrants. The legal basis? A secret interpretation of the FISA Amendments Act that no court had publicly reviewed."

    sys "// SYSTEM NOTE: PRISM worked by collecting data 'upstream' — directly from fiber-optic cables and company servers, bypassing traditional warrant requirements through the FISA Amendments Act. //"

    im "And there's more. Boundless Informant — a tool that counts and visualises exactly how much data the NSA collects from each country. In one month alone, 97 billion pieces of intelligence were gathered worldwide. The American public has no idea."

    # --- Internal conflict with colleague ---
    show colleague neutral at enter_left
    with dissolve

    colleague "Ed, you look like you've seen a ghost. What's wrong?"

    e "Have you ever looked at what we're actually collecting? Not the reports. The raw feeds."

    colleague "I try not to think about it too much. We've got clearance, we've got authorization. That's enough for me."

    e "Is it? Because what I'm seeing goes way beyond foreign intelligence. This is domestic surveillance on a massive scale."

    colleague "Ed... be very careful what you say next. The walls have ears. Literally."

    scene bg_prism1 at parallax with dissolve

    # --- Choice 1: Trust colleague or work alone? ---

    menu:
        "Trust the colleague. Share what you've found.":
            $ tree_record_choice("choice_ch2_1", "trust")
            e "Look, I need someone I can trust. What I've found... it's bigger than both of us."
            $ trust_score += 1
            $ renpy.notify("Trust +1")

            colleague "I... I've had my own doubts. But Ed, if you're thinking what I think you're thinking, you need to be incredibly careful."

            colleague "Whatever you do, don't use the internal network. They monitor everything. Every keystroke."

            im "At least I'm not completely alone in this."

        "Work alone. Trust no one inside the NSA.":
            $ tree_record_choice("choice_ch2_1", "alone")
            e "Never mind. Forget I said anything. Just tired."
            $ suspicion_level += 0
            $ trust_score -= 1
            $ renpy.notify("Trust -1")

            colleague "Sure, man. Get some rest."

            im "I can't trust anyone here. One wrong word and I'm done. I need to do this alone."

    hide colleague neutral with dissolve

    # --- Question Segment 2: Text Input ---

    call screen text_input_question_screen(
        question="Type the codename of the surveillance program Snowden found:",
        correct_answer="PRISM",
        hint="It's named after a glass object that splits light into a spectrum...",
        explanation="PRISM was the codename for the NSA program that collected user data from major tech platforms.",
        accepted_answers=["PRISM"],
        helper_text="You just saw the codename in the scene above, so trust your memory more than your IT knowledge."
    )

    # --- Minigame 2: Decrypt the Message — Learning Section ---
    # (Structured as a self-contained briefing — can be branched into the story tree later)

    im "Some of these classified filenames are encoded with a Caesar cipher — one of the oldest encryption methods in history. It's a simple substitution cipher where each letter is shifted by a fixed number of positions in the alphabet."

    # --- How Caesar Cipher Works ---

    im "Here's how it works. The alphabet is a loop: A B C D E F... all the way to Z, and then it wraps back to A. A Caesar cipher shifts every letter forward by a fixed number — the key."

    im "With ROT-3 — a rotation of 3 — the letter A becomes D, B becomes E, C becomes F. The word 'CAT' encrypts to 'FDW'. Every letter moves exactly three places forward."

    sys "// SYSTEM NOTE: Caesar Cipher encryption with ROT-3: A→D, B→E, C→F, D→G ... X→A, Y→B, Z→C //"

    # --- Decryption: Reversing the Shift ---

    im "To decrypt, you do the reverse — shift each letter back by the same number. So D becomes A, E becomes B, F becomes C. Decryption undoes the encryption."

    im "Let me work through an example. If I see the letter 'S', I count back 3: S... R... Q... P. So S decrypts to P. If I see 'U', count back 3: U... T... S... R. So U becomes R."

    sys "// DECRYPTION RULE: Take each letter → count backwards by the key number → that's your plaintext letter. ROT-3 decryption: D→A, E→B, F→C, G→D ... //"

    # --- Why It Matters ---

    im "The Caesar cipher is trivially easy to break — there are only 25 possible shifts, so you can try them all in seconds. But it teaches the fundamental principle behind all encryption: transform readable data into unreadable data using a key, and reverse the process with the same key."

    im "Modern encryption like AES-256 uses the same concept — just with keys that are billions of times more complex, making brute-force attacks effectively impossible."

    sys "// CHALLENGE PREP: You'll see an encrypted word. Shift each letter back by 3 to reveal the name of a classified NSA program. //"

    call minigame_2_decrypt

    # --- Choice 2: Copy the files or take notes only? ---
    scene bg_nsa_servers at parallax with dissolve
    show edward neutral at stage_center
    with dissolve

    im "I have access to everything. The question is: what do I do with it?"

    narrator_voice "You stare at your screen. The classified documents are right there. Proof of mass surveillance. Proof of constitutional violations. But taking them means crossing a line there's no coming back from."

    im "If I copy these files, I'm committing espionage under the law. If I don't, no one will ever know this is happening. The proper channels have already failed me — my report to the Inspector General disappeared into a black hole."

    menu:
        "Copy the files to an encrypted drive. This evidence needs to survive.":
            $ tree_record_choice("choice_ch2_2", "copy")
            im "I need the original documents. Notes won't be enough. Journalists need primary sources — verifiable proof that can't be denied or dismissed."
            $ evidence_secured = True
            $ suspicion_level += 1
            $ renpy.notify("Evidence Secured! | Suspicion +1")

            narrator_voice "You carefully copy selected documents to a micro SD card hidden inside a Rubik's Cube. Every file transfer is a risk — the NSA logs all data movement, and an unusual transfer could trigger an automated alert."

            im "The files are protected with AES-256 encryption — the Advanced Encryption Standard with a 256-bit key. It's the same encryption the US government uses to protect its own top-secret data. Effectively impossible to brute-force with any existing hardware."

            sys "// DATA TRANSFER INITIATED. ENCRYPTION: AES-256. CONTAINER: VERACRYPT HIDDEN VOLUME. //"

        "Take detailed notes only. Digital evidence is too risky.":
            $ tree_record_choice("choice_ch2_2", "notes")
            im "If they catch me with files, it's espionage. Notes are deniable."
            $ trust_score -= 1
            $ renpy.notify("Trust -1")

            narrator_voice "You write down key details from memory. It's safer, but journalists may question the credibility without primary documents."

    hide edward neutral with dissolve

    # --- MCQ Question ---

    im "When transferring these documents, the protocol matters. Standard HTTP sends everything in plain text — anyone on the network can read it. But HTTPS adds a layer of TLS/SSL encryption, securing the data between your browser and the web server."

    im "That padlock icon in your browser's address bar? That's HTTPS at work. It's the difference between shouting your secrets across a room and whispering them through a sealed envelope."

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
    $ persistent.tree_ch_reached = max(getattr(persistent, 'tree_ch_reached', 0), 3)

    call screen chapter_title_screen(3, "THE CONTACT", "Encrypted Communications — January 2013")

    scene bg_hong_kong at parallax with chapter_transition

    show edward neutral at enter_left
    with dissolve

    # --- Snowden must contact journalists ---

    im "I have the evidence. Now I need someone to publish it. But one wrong email, one unencrypted message, and the NSA will know before the ink is dry."

    narrator_voice "You need to contact journalists who can responsibly publish the classified documents. But the NSA monitors virtually all electronic communication — the very programs you plan to expose are the ones hunting for people like you."

    im "The NSA doesn't just collect data in bulk. They have tools that flag specific patterns: a new email address contacting a known journalist, an encrypted connection from a government network, a Tor exit node accessing a news site. Any of these could trigger an alert."

    sys "// SYSTEM NOTE: OpSec (Operational Security) is the practice of protecting critical information from adversaries. Every digital action leaves traces. //"

    im "I can't use my work email. I can't use my personal email. I need a completely new identity, on a completely separate network. And I need to make contact without anyone inside the NSA knowing I've reached out."

    # --- Snowball Effect Check ---
    if suspicion_level >= 3:
        narrator_voice "Your unusual access patterns have already triggered internal alerts. Your options are narrowing."

        sys "// WARNING: INTERNAL SECURITY MONITORING HAS FLAGGED YOUR ACTIVITY //"

        menu:
            "Try to bluff your way through the security review.":
                $ tree_record_choice("choice_ch3_0", "bluff")
                $ suspicion_level += 1
                $ renpy.notify("Suspicion +1")

                im "I told them I was running diagnostic tests on the archival system. They seemed to buy it... for now."

                narrator_voice "The security team notes the explanation but doesn't close the file. The clock is ticking."

            "Accelerate the timeline. Contact journalists immediately.":
                $ tree_record_choice("choice_ch3_0", "accelerate")
                $ trust_score -= 1
                $ renpy.notify("Trust -1")

                im "No more waiting. If I don't move now, I won't get another chance."

                jump ch3_contact_unsafe

    # --- Choice 1: Secure channel or personal email? ---

    im "I've identified two journalists who might have the courage to publish: Laura Poitras, a documentary filmmaker who's been investigating NSA surveillance for years, and Glenn Greenwald, a constitutional lawyer turned journalist at The Guardian."

    im "The challenge is reaching them securely. PGP encryption with Tor would make my messages virtually untraceable — but it requires technical knowledge to set up correctly. One mistake in the key exchange and the whole channel is compromised."

    narrator_voice "You weigh your options. Each method of contact carries its own risks and rewards."

    menu:
        "Set up a PGP-encrypted email channel using Tor (requires knowledge).":
            $ tree_record_choice("choice_ch3_1", "pgp")
            if knowledge_score >= 3:
                jump ch3_secure_success
            else:
                jump ch3_secure_fail

        "Contact Glenn Greenwald directly through his public email.":
            $ tree_record_choice("choice_ch3_1", "email")
            $ contacts_secured += 1
            $ renpy.notify("Contacts +1")
            jump ch3_greenwald_contact

        "Wait for a safer moment to make contact.":
            $ tree_record_choice("choice_ch3_1", "wait")
            $ trust_score -= 1
            $ renpy.notify("Trust -1")
            jump ch3_wait

label ch3_secure_success:
    im "I know how PGP works. Public key, private key. I generate a key pair, publish my public key, and any message encrypted with it can only be read by me."

    sys "// PGP KEY PAIR GENERATED. RSA-4096. FINGERPRINT VERIFIED THROUGH SEPARATE CHANNEL. //"

    $ contacts_secured += 1
    $ knowledge_score += 1
    $ renpy.notify("Contacts +1 | Knowledge +1")

    scene bg_hong_kong_terminal at parallax with dissolve

    narrator_voice "You create an anonymous email account, accessed only through Tor, and use PGP encryption to contact documentary filmmaker Laura Poitras."

    show journalist neutral at enter_right
    with dissolve

    poitras "I received your encrypted message. The fingerprint checks out. Who are you?"

    e "I'm a senior member of the intelligence community. I have evidence of massive, unconstitutional surveillance by the NSA."

    poitras "Can you prove it?"

    e "I can prove everything. But we need to meet in person. I'll also reach out to Glenn Greenwald — together, you can publish the full story."

    jump ch3_continue

label ch3_secure_fail:
    im "I know I need to use PGP, but I'm not confident in the setup. If I make a mistake with the key exchange..."

    sys "// WARNING: INSUFFICIENT KNOWLEDGE TO ESTABLISH SECURE CHANNEL. PROCEEDING WITH PARTIAL ENCRYPTION. //"

    $ suspicion_level += 1
    $ renpy.notify("Suspicion +1")

    narrator_voice "You attempt to set up encrypted communications, but make errors in the key exchange process. The channel may not be fully secure."

    jump ch3_continue

label ch3_greenwald_contact:
    scene bg_hong_kong_street at parallax with dissolve
    show journalist neutral at enter_right
    with dissolve

    narrator_voice "You reach out to Glenn Greenwald through his public contact information. It's faster, but less secure."

    e "Mr. Greenwald, I have information of extreme importance regarding US government surveillance. We need to talk on a secure channel."

    greenwald "I get messages like this every week. Can you give me more details?"

    e "Not over this channel. You need to set up PGP encryption. I'll send you instructions."

    greenwald "PGP? I've never used it. Can't we just talk on the phone?"

    im "This is the problem. The people who need to publish this information don't know the first thing about security."

    $ suspicion_level += 1
    $ renpy.notify("Suspicion +1")

    jump ch3_continue

label ch3_wait:
    narrator_voice "You decide to wait for a safer window. But there may not be one."

    im "Every day I wait is another day they could catch me. But rushing makes mistakes. Mistakes get you caught."

    $ suspicion_level += 1
    $ renpy.notify("Suspicion +1")

    narrator_voice "Weeks pass. Your access patterns grow more suspicious. The window is closing."

    jump ch3_continue

label ch3_contact_unsafe:
    narrator_voice "With time running out, you take risks you normally wouldn't."

    $ suspicion_level += 1
    $ contacts_secured += 1
    $ renpy.notify("Suspicion +1 | Contacts +1")

    im "No time for perfect OpSec. I just need to get the message out."

    jump ch3_continue

label ch3_continue:
    # --- Question Segment 3: MCQ on Encryption ---
    hide journalist neutral with dissolve
    hide edward neutral with dissolve

    im "Everything I've done to contact journalists relies on one tool above all others: Tor — The Onion Router. It's an anonymization network that routes your traffic through multiple relay nodes around the world, each encrypting another layer."

    im "By the time your traffic reaches its destination, tracing it back to the source is nearly impossible. That's what makes Tor the tool of choice for anyone who needs to communicate without being tracked."

    call screen mcq_question(
        question="What is Tor mainly used for?",
        answers=["To hide where your internet traffic is coming from", "To make your laptop charge faster", "To delete files forever", "To boost a Wi-Fi signal"],
        correct_index=0,
        explanation="Tor hides your route by bouncing traffic through several relays, which makes it much harder for observers to trace it back to you.",
        helper_text="Think about privacy and staying hard to track, not the full acronym."
    )

    # --- Minigame 3: OpSec Challenge — Learning Section ---
    # (Structured as a self-contained briefing — can be branched into the story tree later)

    im "But technology alone isn't enough. OpSec — Operational Security — is the practice of thinking like your adversary. What can they learn from your actions? Every digital footprint, every unguarded conversation, every pattern of behaviour is a piece of the puzzle they're assembling."

    im "Good OpSec means denying the adversary those pieces. It means asking yourself before every action: could this reveal my identity, my location, or my intent?"

    # --- IP Address Exposure ---

    im "The most basic OpSec failure is IP exposure. Your home IP address is assigned by your Internet Service Provider and tied directly to your name and physical address. If you log into a secure service from your home IP without a VPN, you've just stamped your real identity on the connection."

    sys "// OPSEC RULE #1: Never access sensitive services from a traceable IP address. Use a VPN or Tor to mask your connection. //"

    # --- Anonymous Communication Tools ---

    im "The right tools make anonymity possible. Tor anonymizes your connection through multiple relay nodes. SecureDrop — an open-source platform used by major newsrooms — lets whistleblowers submit documents anonymously. Burner email accounts, created from public locations like libraries, add another layer of separation between your real identity and your actions."

    sys "// SAFE PRACTICE: Tor + SecureDrop + burner accounts from public locations = maximum anonymity //"

    # --- Work Email and Monitored Channels ---

    im "The biggest mistake an insider can make is using work infrastructure for anything sensitive. Work email, work Wi-Fi, work devices — all of these are monitored, logged, and directly tied to your employee identity. Sending classified documents via work email is essentially confessing."

    sys "// OPSEC RULE #2: Work infrastructure is monitored. Never use work email, devices, or networks for sensitive communication. //"

    # --- Password Hygiene ---

    im "And then there's password reuse — the silent killer. If you use your personal Facebook password for an encrypted file container, you've created a bridge between your public identity and your secret activity. When one account is compromised, every account sharing that password falls."

    sys "// OPSEC RULE #3: Never reuse passwords. Every service gets a unique, strong password. Use a password manager. //"

    # --- Putting It Together ---

    im "Now it's time to put that knowledge into practice. I've drafted an email to Glenn Greenwald — but before I can send it, I need to strip every trace of my identity from the message. One mistake, and the NSA finds me."

    sys "// SYSTEM NOTE: Every digital message carries metadata — sender address, device info, routing headers, file authorship — that can expose your identity even if the content is encrypted. //"

    window hide
    $ mg_intro3 = renpy.call_screen("minigame_intro", title="CLEAN THE MESSAGE", description="Snowden has drafted an email to journalist Glenn Greenwald. Find and remove all 8 dangerous metadata elements before sending. Click on suspicious items to inspect and clean them.")

    if mg_intro3:
        $ quick_menu = False
        $ show_hud = False
        $ mg_opsec_score = renpy.call_screen("minigame_clean_message")
        $ quick_menu = True
        $ show_hud = True
        
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
    show edward neutral at stage_center
    show journalist neutral at enter_right
    with dissolve

    narrator_voice "The journalist asks for more details about the scope of the leaks."

    greenwald "I need to know what we're dealing with. How big is this?"

    menu:
        "Tell everything. Full transparency builds trust.":
            $ tree_record_choice("choice_ch3_2", "full")
            e "It's everything. PRISM, XKeyscore, Boundless Informant, upstream collection — the NSA is collecting data on hundreds of millions of people. American citizens included."
            $ trust_score += 2
            $ contacts_secured += 1
            $ renpy.notify("Trust +2 | Contacts +1")

            greenwald "My God. If this is true... this is the biggest intelligence leak in history."

        "Share only what's necessary. Protect sources and methods.":
            $ tree_record_choice("choice_ch3_2", "partial")
            e "I can confirm the NSA is conducting mass domestic surveillance. I'll share the details when we meet in person."
            $ trust_score += 1
            $ renpy.notify("Trust +1")

            greenwald "Fair enough. Where do we meet?"

        "Be vague. Don't reveal the scope until you're safe.":
            $ tree_record_choice("choice_ch3_2", "vague")
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
    $ persistent.tree_ch_reached = max(getattr(persistent, 'tree_ch_reached', 0), 4)

    call screen chapter_title_screen(4, "THE ESCAPE", "Hong Kong — May 2013")

    scene bg_hong_kong_hotel at parallax with chapter_transition

    show edward neutral at enter_left
    with dissolve

    # --- Snowden in Hong Kong ---

    narrator_voice "Edward Snowden arrives in Hong Kong with a laptop full of classified documents and a plan that's already falling apart."

    im "I chose Hong Kong deliberately. It has its own legal system, independent from mainland China. Extradition would take time — time I need to get the story published before the government can suppress it."

    im "I told my employer I needed medical leave for epilepsy treatment. They didn't question it. That bought me a few weeks."

    im "Now I'm in a hotel room in Hong Kong, waiting for journalists who might not come, hunted by an agency that can find anyone. I've wedged pillows against the door, piled cushions against the window. Even the smoke detector might have a camera."

    sys "// LOCATION: MIRA HOTEL, HONG KONG. STATUS: UNDETECTED — FOR NOW. //"

    # --- Tense dialogue with pressure ---

    show journalist neutral at enter_right
    with dissolve

    greenwald "You do realize what you're asking me to do? If we publish this, both our lives change forever."

    e "My life changed the moment I read those documents. I can't unread them. I can't unknow what the government is doing to its own people."

    im "Greenwald flew here from Rio de Janeiro. Poitras from Berlin. They left their lives behind on the strength of encrypted emails from a stranger. That took courage."

    if suspicion_level >= 3:
        sys "// WARNING: NSA INTERNAL AUDIT HAS FLAGGED YOUR ACCESS ANOMALIES. INVESTIGATION IN PROGRESS. //"

        im "They know something is wrong. I can feel it. The clock is ticking."

    greenwald "The documents check out. Laura and I have verified them. We're ready to publish."

    e "Publish everything. The world needs to see this."

    hide journalist neutral with dissolve

    im "What scares me most isn't just the surveillance — it's the NSA's offensive capabilities. They stockpile zero-day exploits — vulnerabilities in software that the vendor doesn't even know about. Called 'zero-day' because there are zero days of notice before they're exploited. No patch exists yet."

    im "If the NSA wants into your laptop, they don't need your password. They use a zero-day to bypass everything — your firewall, your encryption, your operating system. And the vendor can't fix what they don't know is broken."

    sys "// SYSTEM NOTE: A zero-day exploit targets an unknown software vulnerability. Because no patch exists, even fully updated systems are at risk. Intelligence agencies hoard zero-days as offensive weapons. //"

    # --- Choice 1: Hotel Wi-Fi or mobile hotspot? ---

    narrator_voice "Edward needs to send final instructions to the publication team, but the hotel network is compromised. Every network connection is a potential leak."

    im "The hotel Wi-Fi is managed by the hotel — they can see every device that connects, every connection made. Intelligence agencies routinely request hotel network logs. I need to decide how to send this last message."

    menu:
        "Use the hotel Wi-Fi with a VPN.":
            $ tree_record_choice("choice_ch4_1", "hotel")
            $ suspicion_level += 1
            $ renpy.notify("Suspicion +1")

            im "The VPN encrypts my traffic, but the hotel's network logs will show my room connected to a VPN. That alone is a red flag for anyone watching."

            sys "// WARNING: VPN CONNECTION DETECTED ON LOCAL NETWORK. COMMERCIAL VPN IPs ARE CATALOGUED BY INTELLIGENCE AGENCIES. //"
            sys "// CHOICE REVIEW: Fast and convenient, but the hotel can still log that a protected tunnel came from your room. Good for speed, bad for stealth. //"

        "Use a personal mobile hotspot with Tor.":
            $ tree_record_choice("choice_ch4_1", "mobile")
            $ trust_score += 1
            $ renpy.notify("Trust +1")

            im "A mobile hotspot bypasses the hotel network entirely. With Tor on top of it, my traffic is encrypted and anonymized through multiple relay nodes."

            sys "// SECURE CONNECTION ESTABLISHED. TRAFFIC ROUTED THROUGH 3 TOR RELAY NODES. //"
            sys "// CHOICE REVIEW: Slower, but it avoids hotel logs and adds extra privacy layers. Good for stealth, bad for speed. //"

    # --- Question Segment 4: Text Input ---

    call screen text_input_question_screen(
        question="Type the 3-letter privacy tool that hides your route online:",
        correct_answer="TOR",
        hint="It's the same tool mentioned in the safer option above.",
        explanation="Tor wraps your traffic in several layers and sends it through relays, which helps hide where it started.",
        accepted_answers=["TOR", "THE ONION ROUTER"],
        helper_text="Short answer is fine."
    )

    # --- Minigame 4: Trace the Route — Learning Section ---
    # (Structured as a self-contained briefing — can be branched into the story tree later)

    im "When you route traffic through Tor, you're building a chain of relay nodes. Each node only knows the hop before it and the hop after it — never the full path. Pick the right nodes and your trail goes cold."

    im "But if even one node in the chain is compromised — a monitored relay, a hostile exit point — the entire route is exposed and your identity with it. So understanding what each type of node does is critical."

    # --- The Starting Point: Your Device ---

    im "It all starts at your device — your laptop, your phone. This is where traffic originates. Right now, it carries your real IP address and your real identity. The goal is to strip that identity away before the traffic reaches its destination."

    # --- ISP Router ---

    im "The first hop is usually your ISP router — the Internet Service Provider that connects you to the internet. Your ISP can see every website you visit, every connection you make. They log this data and, in many countries, hand it over to law enforcement on request."

    im "Going through the ISP is unavoidable — it's your on-ramp to the internet. But it's a chokepoint. If someone is watching at this level, they see everything unless you've already encrypted your traffic."

    sys "// NODE TYPE: ISP ROUTER — Your gateway to the internet. Sees all unencrypted traffic. A surveillance chokepoint. //"

    # --- VPN Server ---

    im "A VPN server is your first line of defence. It creates an encrypted tunnel between your device and the VPN server. Your ISP can see that you've connected to a VPN, but they can't see what you're doing through it."

    im "Starting your route through a VPN before entering the Tor network is called 'VPN over Tor' — it hides the fact that you're using Tor from your ISP, adding an extra layer of protection."

    sys "// NODE TYPE: VPN SERVER — Encrypts your traffic before it hits the internet. Hides your activity from your ISP. Safe opening move. //"

    # --- Tor Nodes ---

    im "Tor nodes are the backbone of anonymous routing. Each Tor relay adds a layer of encryption — like nesting your message inside multiple sealed envelopes. The first relay knows who you are but not where you're going. The last relay knows where you're going but not who you are."

    im "The more Tor nodes you route through, the harder it is to trace the connection back to you. But each hop adds latency — there's a trade-off between anonymity and speed."

    sys "// NODE TYPE: TOR NODE — Adds encryption layers and anonymity. Multiple Tor hops = harder to trace. Safe nodes. //"

    # --- Government Monitor (Danger!) ---

    im "The one node you must avoid at all costs is the government monitoring point. Intelligence agencies like the NSA operate surveillance nodes that intercept and log all traffic passing through them. If your route goes through a government monitor, the entire chain is compromised."

    im "It doesn't matter how many Tor nodes you've used — if even one hop routes through a known surveillance point, the adversary can correlate timing data to identify you. This is called a 'traffic correlation attack'."

    sys "// NODE TYPE: GOV MONITOR — Intercepts all traffic. If your route hits this node, your identity is exposed. AVOID AT ALL COSTS. //"

    # --- CDN Server vs Secure Relay ---

    im "Near the end of the route, you'll see two types of final relay. A CDN — Content Delivery Network — is standard internet infrastructure. It's fast but not designed for privacy. Your traffic is delivered efficiently, but CDN logs can be subpoenaed."

    im "A secure relay, on the other hand, is specifically designed for private communication. It doesn't log traffic, strips metadata, and forwards your message with minimal exposure. When anonymity matters, always prefer the secure relay."

    sys "// NODE TYPE: CDN SERVER — Fast but logs traffic. SECURE RELAY — Private, no logs. Choose secure relay for maximum anonymity. //"

    # --- Route Strategy ---

    im "So the optimal route is: start with a VPN to hide your Tor usage, chain through Tor nodes for anonymity, avoid the government monitor completely, and exit through a secure relay to reach the destination without leaving a trail."

    sys "// ROUTE STRATEGY: VPN → Tor nodes → Secure relay → Destination. Avoid GOV MONITOR. Fewer hops = less exposure time. //"

    window hide
    $ mg_intro4 = renpy.call_screen("minigame_intro", title="TRACE THE ROUTE", description="Build a safe route hop by hop. Green nodes help you stay hidden, while the red monitor exposes the whole mission.")

    if mg_intro4:
        $ quick_menu = False
        $ show_hud = False
        $ mg_trace_solved = renpy.call_screen("minigame_trace")
        $ quick_menu = True
        $ show_hud = True
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

    narrator_voice "The first stories are published. The world erupts. And now, Edward Snowden is the most wanted man on Earth."

    im "The US government has revoked my passport. I need to move. Now."

    if suspicion_level >= 4:
        narrator_voice "With his cover blown, Snowden's options have narrowed to almost nothing."

        menu:
            "Head to the airport immediately. Every minute counts.":
                $ tree_record_choice("choice_ch4_2", "airport")
                $ escape_successful = True
                $ renpy.notify("Escape initiated!")

                im "No time to plan. The passport might still work for a few hours before the revocation hits every system."
                sys "// ROUTE REVIEW: Best for immediate movement, worst for preparation. Good if you need speed more than certainty. //"

            "Go to the Russian consulate. They're the only ones who might help.":
                $ tree_record_choice("choice_ch4_2", "russia")
                $ escape_successful = True
                $ trust_score -= 1
                $ renpy.notify("Escape to Russia | Trust -1")

                im "Russia isn't ideal, but beggars can't be choosers. They have their own reasons for helping me."
                sys "// ROUTE REVIEW: Good for immediate shelter, bad for independence. Help comes with political strings attached. //"

    else:
        menu:
            "Fly to Ecuador via Moscow. Multiple stops make tracking harder.":
                $ tree_record_choice("choice_ch4_2", "ecuador")
                $ escape_successful = True
                $ renpy.notify("Escape route planned!")

                im "Ecuador has a history of granting asylum to people the US wants. WikiLeaks arranged the route through Moscow."

                narrator_voice "But Edward will never make it past Moscow. His passport will be revoked mid-flight."
                sys "// ROUTE REVIEW: Strong asylum logic, but the travel chain is fragile. Good long-term idea, risky short-term execution. //"

            "Seek asylum at a European embassy in Hong Kong.":
                $ tree_record_choice("choice_ch4_2", "embassy")
                $ trust_score += 1
                $ renpy.notify("Trust +1")

                if identity_exposed:
                    narrator_voice "With his identity already exposed, no embassy will risk the diplomatic fallout of harboring him."
                    $ escape_successful = False
                else:
                    narrator_voice "The European embassies politely decline. No one wants to challenge the United States."
                    $ escape_successful = False

                im "No one will help. Not officially. Moscow may be my only option."
                sys "// ROUTE REVIEW: Good legal optics, but embassies rarely want the diplomatic fallout. Good principle, poor odds. //"

            "Stay in Hong Kong and face the legal system.":
                $ tree_record_choice("choice_ch4_2", "stay")
                $ escape_successful = False
                $ renpy.notify("Escape abandoned.")

                im "If I stay, Hong Kong will extradite me. The US legal system won't give me a fair trial under the Espionage Act."
                sys "// ROUTE REVIEW: Good if you want to make a stand, bad if your goal is to stay free long enough to keep the story alive. //"

    hide edward neutral with dissolve

    if escape_successful and not identity_exposed:
        scene bg_hk_airport at parallax with dissolve
        narrator_voice "Edward boards an international flight just hours before his name hits the global no-fly lists."

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
    $ persistent.tree_ch_reached = max(getattr(persistent, 'tree_ch_reached', 0), 5)

    call screen chapter_title_screen(5, "PERMANENT RECORD", "Moscow, Russia — 2013 to Present")

    scene bg_sheremetyevo at parallax with chapter_transition

    show edward neutral at enter_left
    with dissolve

    # --- Snowden in Russia ---

    narrator_voice "The Sheremetyevo International Airport transit zone. Edward Snowden has been trapped here for 40 days. Sleeping on chairs, eating airport food, living in legal limbo."

    narrator_voice "His passport is cancelled. No country will grant him asylum without risking the wrath of the United States. Twenty-one countries rejected his application. Russia is his last option."

    show russian_official neutral at enter_right
    with dissolve

    russian_official "Mr. Snowden. The transit zone is a strange place, yes? You are not in Russia, but you are certainly not in America."

    russian_official "You are... nowhere. We can offer you 'somewhere.' Russia can grant you temporary asylum."

    e "I don't want to be a pawn in anyone's geopolitical chess game."

    russian_official "You became a pawn the moment you took those files, Mr. Snowden. The only question is which board you want to play on."

    im "He's right. I have no leverage. The US government pressured every ally to refuse me. Bolivia's presidential plane was even forced to land in Austria because they suspected I was on board. That's how far they'll go."

    # --- Reflection Dialogue ---

    hide russian_official neutral with dissolve

    scene bg_moscow_apartment at parallax with dissolve
    show edward neutral at stage_center
    with dissolve

    im "I'm an exile in the physical world, but I've never been more active in the digital one."

    im "From this small apartment in Moscow, I can still connect to the world. I use encrypted video calls to speak at conferences, secure messaging to coordinate with press freedom organisations. The irony of a surveillance whistleblower living in the surveillance capital of the East is not lost on me."

    narrator_voice "From Moscow, Snowden continues to advocate for digital privacy. He develops tools to help journalists protect their sources, speaks to millions through encrypted channels, and becomes the face of the global privacy debate."

    im "SecureDrop — an open-source whistleblowing platform — was adopted by dozens of major news organizations after the leaks. It allows anonymous document submission, protecting sources the way I wish I had been protected. The tools I helped popularise are now standard practice in investigative journalism."

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

    im "People think metadata is harmless — it's just 'data about data.' Who you called, when, for how long, from where. Not the content of the message itself."

    im "But metadata reveals patterns of life. Call a doctor at midnight, a divorce lawyer the next morning, and a locksmith that afternoon — the content doesn't matter. The pattern tells the whole story. Intelligence agencies consider metadata even more valuable than content in many cases."

    # MCQ
    call screen mcq_question(
        question="What is metadata in the context of surveillance?",
        answers=["The content of a message", "Data about data (who, when, where — not what)", "Encrypted file headers", "User passwords"],
        correct_index=1,
        explanation="Metadata is 'data about data.' In surveillance terms, it includes who you communicated with, when, for how long, and from where — but not the content of the communication. The NSA argued metadata collection wasn't as invasive as content collection, but metadata can reveal intimate patterns of life."
    )

    im "PGP — Pretty Good Privacy. It's the asymmetric encryption system that made the whole operation possible. I publish a public key that anyone can use to encrypt a message to me, but only my private key can decrypt it. Without PGP, every email to the journalists would have been an open letter to the NSA."

    # Text Input
    call screen text_input_question_screen(
        question="Type the 3-letter encryption tool Snowden used to message journalists:",
        correct_answer="PGP",
        hint="It stands for 'Pretty Good' something, and the short version is enough.",
        explanation="PGP lets one key lock a message and another key unlock it, which is why Snowden pushed journalists to learn it.",
        accepted_answers=["PGP", "PRETTY GOOD PRIVACY"],
        helper_text="Just the 3-letter version works."
    )

    im "The scariest attack is one you never see — a man-in-the-middle. An attacker secretly positions themselves between you and the person you're talking to, intercepting every message. Both sides think they're communicating directly, but the attacker sees everything."

    im "The only defence is key verification — confirming encryption fingerprints through a separate, trusted channel. If you skip that step, you could be handing your secrets directly to the adversary."

    # MCQ
    call screen mcq_question(
        question="What is a 'man-in-the-middle' attack?",
        answers=["Physical server theft", "Intercepting communication between two parties", "Overloading a server", "Guessing a password"],
        correct_index=1,
        explanation="A man-in-the-middle (MITM) attack occurs when an attacker secretly intercepts and possibly alters communication between two parties who believe they are communicating directly. This is why verifying encryption keys through a separate channel is critical."
    )

    # --- Final Choice: Culminating Moral Decision ---

    show edward neutral at stage_center
    with dissolve

    narrator_voice "Years have passed. The world has changed — partly because of what Edward Snowden did, and partly in spite of it."

    narrator_voice "A journalist contacts Snowden with a new trove of classified documents from a different whistleblower. The cycle could begin again."

    im "Another person on the inside, seeing what I saw, feeling what I felt. They're asking me what to do."

    menu:
        "Encourage them to leak. The public deserves to know.":
            $ tree_record_choice("choice_ch5_1", "encourage")
            e "The public's right to know outweighs the government's desire for secrecy. If the system won't reform itself, people of conscience have to act."
            $ trust_score += 2
            $ renpy.notify("Trust +2")

            narrator_voice "Snowden helps the new whistleblower establish secure communications, passing on the hard lessons of his own experience."

        "Advise caution. Use official channels first.":
            $ tree_record_choice("choice_ch5_1", "caution")
            e "Try the Inspector General first. Document everything. If the system fails you — and it probably will — then you'll have a record proving you tried."
            $ trust_score += 1
            $ knowledge_score += 1
            $ renpy.notify("Trust +1 | Knowledge +1")

            narrator_voice "Snowden advises a measured approach, hoping the system has improved since his time. Knowing it probably hasn't."

        "Tell them not to do it. The personal cost is too high.":
            $ tree_record_choice("choice_ch5_1", "refuse")
            e "I lost my country, my family, my freedom. I'd do it again, but I won't ask anyone else to pay that price."
            $ trust_score -= 1
            $ renpy.notify("Trust -1")

            narrator_voice "Snowden's honesty about the personal cost weighs heavily on the would-be whistleblower."

    hide edward neutral with dissolve

    # --- Final scene ---

    scene bg_moscow_winter_epilogue at parallax with fade

    narrator_voice "Edward Snowden remains in Russia. He was granted permanent residency in 2020 and Russian citizenship in 2022."

    narrator_voice "His disclosures led to the USA FREEDOM Act, which reformed some surveillance practices. Major tech companies adopted end-to-end encryption."

    narrator_voice "But mass surveillance continues in new forms. The debate between security and privacy is far from over."

    narrator_voice "The tools Snowden used — encryption, Tor, secure communication — are the same tools available to you."

    narrator_voice "The question is: will you use them?"

    # --- Determine Ending ---
    jump determine_ending
