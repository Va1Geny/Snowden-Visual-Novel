# Characters
define pro = Character("Edward", color="#ffffff")
define sup = Character("Supervisor", color="#ffcc00")
define col = Character("Colleague", color="#aaccff")
define jour = Character("Journalist", color="#ffaa55")
define ed = Character("Editor", color="#cc5555")
define ro = Character("russian Official", color="#cc2222")

# Narrative voices
define im = Character("Internal Monologue", what_prefix="*", what_suffix="*", color="#888888")
define sys = Character("System Prompt", color="#00ff00")

# Images
image edward neutral:
    "sprites/edward neutral.png"
    zoom 0.7

image supervisor neutral:
    "sprites/supervisor neutral.png"
    zoom 0.7

image colleague neutral:
    "sprites/colleague neutral.png"
    zoom 0.7

image journalist neutral:
    "sprites/journalist neutral.png"
    zoom 0.7

image editor neutral:
    "sprites/editor neutral.png"
    zoom 0.7

image russian official neutral:
    "sprites/russian official neutral.png"
    zoom 0.7

image bg_nsa:
    "backgrounds/Working inside the NSA's surveillance apparatus.png"
    xysize (1920, 1080)

image bg_prism:
    "backgrounds/Discovering the PRISM mass surveillance program.png"
    xysize (1920, 1080)

image bg_hong_kong:
    "backgrounds/The escape to Hong Kong and contact with journalists.png"
    xysize (1920, 1080)

image bg_leak:
    "backgrounds/The Leak and Global Fallout.png"
    xysize (1920, 1080)

image bg_russia:
    "backgrounds/Asylum in russia — and life as a fugitive.png"
    xysize (1920, 1080)

label start:
    jump scene_1_nsa

label scene_1_nsa:
    scene bg_nsa with fade

    show supervisor neutral at right
    sup "Don't overthink the 'why,' 302. Just focus on the selectors. If the system flags a packet, it’s because the math says they’re a threat. Your job is to verify the handshake, not the person."

    show colleague neutral at left
    col "You see this? I can watch this guy’s webcam in real-time. He’s just eating cereal. It’s wild what we can grab without even a ping."

    show edward neutral at center
    menu:
        "Copy that. Just keeping the signal clean. Narrowing the search parameters now.":
            pro "Copy that. Just keeping the signal clean. Narrowing the search parameters now."
            pass
        "Do we ever check if the warrant covers the metadata, or just the content?":
            pro "Do we ever check if the warrant covers the metadata, or just the content?"
            sup "You're asking the wrong questions. The system decides what's covered."
            pass

    sup "Before you access the XKeyscore buffer, I need you to re-verify. We’ve had too many 'credential leaks' lately. You know the drill—password alone is just a polite suggestion to a hacker."

label lesson_1_input:
    sys "The system requires a secondary token. A code has been sent to your hardware key."
    $ totp = renpy.input("Task: Please enter the 6-digit TOTP (Time-based One-Time Password) from your authenticator app to sync the session:", length=6).strip()

    if len(totp) == 6 and totp.isdigit():
        sys "AUTHENTICATION SUCCESSFUL. ACCESSING XKEYSCORE."
        jump scene_2_prism
    else:
        sys "ERROR: INVALID TOTP LENGTH OR FORMAT."
        im "That's not right. The code needs to be exactly six numbers. High-security environments require more than just a password."
        jump lesson_1_input


label scene_2_prism:
    scene bg_prism with fade
    show edward neutral at center

    im "The architecture is... infinite. It’s not a targeted tap anymore. It’s a vacuum. We aren't looking for needles in haystacks; we’re just stealing the whole field."

    sys "CRITICAL ACCESS GRANTED. DIRECT LINK TO EXTERNAL SERVERS ACTIVE. DATA HARVEST RATIO: 1:1."

    menu:
        "(Silently copy the directory to the encrypted drive)":
            pro "Just doing some routine backup... nothing to see here."
            pass
        "\"This doesn't look like foreign intelligence. These are domestic IP addresses. Thousands of them.\"":
            pro "This doesn't look like foreign intelligence. These are domestic IP addresses. Thousands of them."
            pass

    im "I need to move these files to a hidden partition. If the system admins see a folder named 'LEAKS,' I’m done. I need a passphrase that a brute-force attack couldn't crack in a billion years."

label lesson_2_input:
    sys "Task: Create a Master Passphrase for the encrypted volume."
    $ passphrase = renpy.input("Task: Enter a highly secure password (minimum 12 characters, non-predictable):").strip()

    if len(passphrase) < 12:
        sys "WARNING: ENTROPY TOO LOW. BRUTE-FORCE VULNERABILITY DETECTED."
        im "Too short. A simple password will be cracked in seconds. I need something longer, ideally a phrase or at least 12 characters."
        jump lesson_2_input
    elif passphrase.lower() in ["password", "p@ssw0rd123", "admin123", "1234567890", "qwertyuiop"]:
        sys "WARNING: KNOWN WEAK PASSWORD DETECTED."
        im "That's one of the most common passwords in the world. A dictionary attack would crack this instantly. I need something truly unique."
        jump lesson_2_input
    else:
        sys "MASTER PASSPHRASE ACCEPTED. ENCRYPTION IN PROGRESS."
        im "Good. Length and randomness are far superior to complex but short passwords."
        jump scene_3_hong_kong


label scene_3_hong_kong:
    scene bg_hong_kong with fade
    show journalist neutral at right
    show edward neutral at left

    jour "You’re late. And why a Rubik's Cube? It’s a bit theatrical, don't you think?"

    pro "Theatrical keeps us alive. Put your phones in the microwave. Now. We aren't talking until the batteries are physically shielded."

    menu:
        "If you don't use the PGP key I sent, I’m walking out that door. No more unencrypted talk.":
            pro "If you don't use the PGP key I sent, I’m walking out that door. No more unencrypted talk."
            pass
        "My girlfriend thinks I’m on a business trip. By tomorrow, she’ll think I’m a traitor. We need to move fast.":
            pro "My girlfriend thinks I’m on a business trip. By tomorrow, she’ll think I’m a traitor. We need to move fast."
            pass

    pro "The hotel Wi-Fi is a sieve. Every packet we send is being sniffed by local intelligence or the NSA's 'Stellar Wind' sensors. We can't send the invite to the journalists on an open line."

label lesson_3_input:
    sys "The connection is 'UNSECURED'. Configure the Secure Tunnel."
    menu:
        sys "Task: Select the correct protocol to wrap your traffic in an encrypted layer."
        "WEP":
            pro "No, that's not secure. WEP is completely broken. Any script kiddie in the lobby could read it."
            jump lesson_3_input
        "HTTP":
            pro "No, HTTP sends data in plain text. Anyone on the network can sniff the packets."
            jump lesson_3_input
        "FTP":
            pro "FTP is not encrypted. I need something secure."
            jump lesson_3_input
        "AES-256 VPN":
            sys "ENCRYPTION LAYER ACTIVE. SECURE TUNNEL ESTABLISHED."
            pro "The tunnel is secure. It's an absolute necessity to encrypt traffic on untrusted networks."
            jump scene_4_leak


label scene_4_leak:
    scene bg_leak with fade
    show editor neutral at right
    show edward neutral at left
    show journalist neutral at center

    ed "If we print this, the government will come for us with everything they have. Are you 100%% sure these documents are authenticated?"

    pro "The documents speak for themselves. The question is: do the people have a right to know what's being done in their name?"

    menu:
        "Put my name on it. I’m not hiding in the shadows. I want them to know who did this.":
            pro "Put my name on it. I’m not hiding in the shadows. I want them to know who did this."
            pass
        "Just leak the tech. The story is the surveillance, not the man behind the keyboard.":
            pro "Just leak the tech. The story is the surveillance, not the man behind the keyboard."
            pass

    jour "We’re ready to upload the slides to our public server, but wait—if we post the raw files, the NSA will see the 'Author' field in the document properties. They'll know it was you before the ink is dry."

label lesson_4_input:
    sys "SANITIZE THE EVIDENCE. RUNNING EXIFCLEANER."
    menu:
        sys "Task: Which of the following 'Metadata' should be stripped to ensure anonymity?"
        "GPS Coordinates":
            jour "Wait... if we only strip the GPS, the other metadata points can still identify the software version or the exact printer used. Are you sure we shouldn't strip absolutely everything?"
            jump lesson_4_input
        "Creation Date":
            jour "Wait... if we only strip the date, the GPS data could still lead them straight to this hotel. We need to strip more."
            jump lesson_4_input
        "Printer Serial Number":
            jour "Wait... removing the printer serial is good, but what about the creation date and GPS? They'll still know where and when it was made."
            jump lesson_4_input
        "All of the Above":
            jour "Good thinking. Files carry 'invisible' data that can easily identify the creator. We can't leave any breadcrumbs."
            jump scene_5_russia


label scene_5_russia:
    scene bg_russia with fade
    show russian official neutral at right
    show edward neutral at left

    ro "The airport transit zone is a strange place. You are not in russia, but you are certainly not in America. You are... nowhere. We can offer you 'somewhere,' for a price."

    pro "I’m an exile in the physical world, but I’ve never been more active in the digital one. The walls are thick, but the fiber-optics are thin."

    menu:
        "I’m not a guest here. I’m a prisoner of circumstance. But I’d do it all again.":
            pro "I’m not a guest here. I’m a prisoner of circumstance. But I’d do it all again."
            pass
        "Sometimes I stare at the snow and wonder if anyone back home even remembers why I left.":
            pro "Sometimes I stare at the snow and wonder if anyone back home even remembers why I left."
            pass

    pro "I’m leaving the hotel room for an hour. If someone enters and installs a hardware keylogger or a 'Rubber Ducky' USB, my encryption is useless. I need a way to know if the hardware was tampered with."

label lesson_5_input:
    sys "SET PROCEDURAL HARDWARE TRIPWIRE."
    menu:
        sys "Task: Where should you place the unique glitter-nail-polish mark to ensure the laptop casing hasn't been opened?"
        "On the screen":
            im "That won't tell me if someone opened the machine to bypass the encryption cleanly."
            jump lesson_5_input
        "On the keyboard":
            im "That's not the vulnerable point. They need to get inside the machine."
            jump lesson_5_input
        "On the laptop casing screws":
            im "Perfect. If they unscrew the bottom panel or open the casing to plant a bug, the hardened polish will crack, and I'll immediately know."
            im "Digital security is completely irrelevant if physical security is compromised. The 'Evil Maid' attack won't work on me today."
            jump end_game


label end_game:
    scene black with fade
    "To be continued..."
    return