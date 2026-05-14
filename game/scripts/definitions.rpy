init offset = -1

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LEGAL SANITIZATION — Agency Alias Variables
# Use these interpolated variables in all .rpy script files instead of
# hardcoding real organization names. Change here for global effect.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
define ag_cia = "The Obsidian Oversight"
define ag_fbi = "Bureau of Internal Security"
define ag_nsa = "Signal Reach Network"

define config.default_fullscreen = True
define config.allow_skipping = True
define e = Character("You",
    image="edward",
    color="#00FFD1",
    what_color="#E8E8E8",
    who_size=26,
    what_size=26,
    who_bold=True)

define greenwald = Character("Grayson Wardell",
    image="greenwald",
    color="#FFD700",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=26,
    what_size=26)

define poitras = Character("Leah Portman",
    image="poitras",
    color="#FF69B4",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=26,
    what_size=26)

define nsa_chief = Character("Director Marcus Hale",
    image="nsa_chief",
    color="#FF2D55",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=26,
    what_size=26)

define supervisor = Character("Supervisor Daniel Cross",
    image="supervisor",
    color="#FF6B35",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=26,
    what_size=26)

define colleague = Character("COLLEAGUE [[CLASSIFIED]]",
    image="colleague",
    color="#888888",
    what_color="#CCCCCC",
    who_bold=False,
    who_size=26,
    what_size=26)

define russian_official = Character("Agent Viktor Malenkov",
    image="russian_official",
    color="#CC2222",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=26,
    what_size=26)

define sys = Character("// SYSTEM //",
    color="#00FF00",
    what_color="#00FF00",
    who_bold=True,
    who_size=24,
    what_size=24)

define narrator_voice = Character(None,
    what_color="#AAAAAA",
    what_italic=True,
    what_size=28)

define im = Character("INTERNAL MONOLOGUE",
    what_prefix="*",
    what_suffix="*",
    color="#888888",
    what_color="#AAAAAA",
    who_size=24,
    what_size=27)

default trust_score = 0
default knowledge_score = 0
default suspicion_level = 0
default contacts_secured = 0
default evidence_secured = False
default identity_exposed = False
default escape_successful = False

default ch1_outcome = ""
default ch2_outcome = ""
default ch3_outcome = ""
default ch4_outcome = ""

default ending_type = ""

default current_chapter = 1
default show_hud = True
default notebook_entries = []
default notebook_draft = ""
default english_voice_bootstrap_done = False
default suspicion_lockdown_triggered = False

default mg_firewall_score = 0
default mg_decrypt_solved = False
default mg_opsec_score = 0
default mg_trace_solved = False
default cover_wiped = 0
default cover_failed = 0

default text_input_attempts = 0

init python:
    import re
    import os
    from datetime import datetime
    import store

    IMPORTANT_TERMS = [
        "USA FREEDOM Act",
        "Virtual Private Network",
        "The Onion Router",
        "man-in-the-middle",
        "Inspector General",
        "reverse shell",
        "traffic correlation attack",
        "Domain Name System",
        "Boundless Informant",
        "SecureDrop",
        "Edward Snowden",
        "national security",
        "private IP ranges",
        "public Wi-Fi",
        "foreign intelligence",
        "domestic surveillance",
        "encryption fingerprints",
        "network security",
        "mass surveillance",
        "XKeyscore",
        "metadata",
        "firewall",
        "VPN",
        "PGP",
        "PRISM",
        "Tor",
        "TLS",
        "SSH",
        "RDP",
        "DNS",
        "HTTP",
        "HTTPS",
        "Telnet",
        "AES-256",
        "OpSec",
        "zero-day",
        "FISA",
        "NSA",
        "CIA",
        "bcrypt",
        "dictionary attack",
        "digital forensics",
        "EXIF metadata",
        "hash function",
        "John the Ripper",
        "Kali Linux",
        "MAC address",
        "MD5",
        "secure deletion",
        "session token",
    ]

    DOSSIER_ENTRIES = [
        ("AES-256", "Advanced Encryption Standard with a 256-bit key. Strong symmetric encryption that is effectively impossible to brute-force with current consumer hardware."),
        ("Bcrypt", "A password-hashing function designed to be computationally expensive and intentionally slow, making brute-force and dictionary attacks highly ineffective."),
        ("Boundless Informant", "A data analysis tool used by the NSA to summarize and visualize the metadata and communications records they collect globally."),
        ("Caesar Cipher", "Simple substitution cipher where each letter is shifted by a fixed number. Easy to break but historically significant. Example: ROT-3 shifts A to D, B to E, and so on."),
        ("CIA — The Obsidian Oversight (Central Intelligence Agency)", "A civilian foreign intelligence service of the federal government of the United States, tasked with gathering, processing, and analyzing national security information. Known in-world as The Obsidian Oversight."),
        ("Dictionary Attack", "A method of breaking into a password-protected system by systematically entering every word in a dictionary or a list of common passwords (like rockyou.txt)."),
        ("Digital Forensics", "The recovery and investigation of material found in digital devices, often used to uncover deleted files, internet history, and hidden metadata."),
        ("DNS (Domain Name System)", "The phonebook of the Internet. Translates human-readable domain names (like example.com) into machine-readable IP addresses."),
        ("Domestic Surveillance", "The monitoring of citizens within a country's borders by its own government, often a point of legal and ethical controversy."),
        ("Edward Snowden", "An American former computer intelligence consultant who leaked highly classified information from the NSA in 2013, revealing numerous global surveillance programs."),
        ("Encryption Fingerprints", "Unique patterns or metadata in encrypted traffic that can reveal the type of encryption used, the application generating it, or even the user, without breaking the encryption itself."),
        ("EXIF Metadata", "Hidden information embedded in image files, such as the camera model, date/time, and exact GPS coordinates of where the photo was taken."),
        ("Firewall", "Network security system that monitors and filters incoming and outgoing traffic based on predefined rules. Acts as a barrier between trusted and untrusted networks."),
        ("FISA (Foreign Intelligence Surveillance Act)", "A United States federal law that establishes procedures for the physical and electronic surveillance and collection of foreign intelligence information."),
        ("Foreign Intelligence", "Information relating to the capabilities, intentions, or activities of foreign governments, organizations, or persons."),
        ("Hash Function", "A one-way mathematical algorithm that maps data of arbitrary size to a fixed-size string. You cannot 'decrypt' a hash; you must guess the original input."),
        ("HTTP (Hypertext Transfer Protocol)", "The foundation of data communication for the World Wide Web. It is unencrypted, meaning data sent via HTTP can be intercepted."),
        ("HTTPS", "HTTP with TLS/SSL encryption. Secures data between your browser and a web server. Look for the padlock icon in your browser's address bar."),
        ("Inspector General", "An investigative official in a civil or military organization. In the intelligence community, they are responsible for internal audits and investigating whistleblowers' claims."),
        ("John the Ripper", "A fast, open-source password cracking software tool used to perform dictionary attacks and rule-based mutations against password hashes."),
        ("Kali Linux", "A Debian-derived Linux distribution designed for digital forensics and penetration testing. It comes pre-installed with hundreds of security and hacking tools."),
        ("MAC Address", "A unique hardware identifier assigned to a network interface controller. Used by local networks and routers to identify specific devices."),
        ("Man-in-the-Middle Attack", "An attacker secretly intercepts communication between two parties. Both parties think they're talking directly to each other. Key verification prevents this."),
        ("Mass Surveillance", "The intricate surveillance of an entire or a substantial fraction of a population in order to monitor that group of citizens."),
        ("MD5", "An older, widely used hashing algorithm that is now considered cryptographically broken and vulnerable to rapid brute-force attacks."),
        ("Metadata", "Data about data — who you communicated with, when, for how long, from where. Does not include the message content but can reveal intimate patterns of life."),
        ("National Security", "The security and defense of a nation state, including its citizens, economy, and institutions, which is regarded as a duty of government."),
        ("Network Security", "Policies and practices adopted to prevent and monitor unauthorized access, misuse, modification, or denial of a computer network and network-accessible resources."),
        ("NSA — Signal Reach Network (National Security Agency)", "A national-level intelligence agency of the United States Department of Defense, under the authority of the Director of National Intelligence. Known in-world as the Signal Reach Network."),
        ("OpSec (Operational Security)", "The practice of protecting critical information by identifying what intelligence the adversary could gather from your actions and taking steps to prevent it."),
        ("PGP (Pretty Good Privacy)", "Asymmetric encryption system using public/private key pairs. Public key encrypts, only the matching private key can decrypt. Used for secure email communication."),
        ("PRISM", "NSA surveillance program providing direct access to user data from major tech companies. Exposed by Snowden in 2013."),
        ("Private IP Ranges", "IP addresses reserved for internal network use (like 192.168.x.x) that are not routable on the public internet."),
        ("Public Wi-Fi", "Unsecured wireless networks open to the public. Highly vulnerable to interception and man-in-the-middle attacks."),
        ("RDP (Remote Desktop Protocol)", "A proprietary protocol developed by Microsoft that provides a user with a graphical interface to connect to another computer over a network connection."),
        ("Reverse Shell", "A type of shell in which the target machine communicates back to the attacking machine. Often used to bypass firewalls that block incoming connections."),
        ("Secure Deletion", "The process of permanently destroying digital data by overwriting the physical disk sectors with random data (e.g., using 'shred'), preventing forensic recovery."),
        ("SecureDrop", "An open-source whistleblowing platform that allows anonymous document submission. Used by major news organizations to protect sources."),
        ("Session Token", "A unique piece of data generated by a server and stored in a user's browser (often as a cookie) to keep them authenticated after logging in."),
        ("SSH (Secure Shell)", "A cryptographic network protocol for operating network services securely over an unsecured network, often used for remote command-line login."),
        ("Telnet", "An application protocol providing a bidirectional interactive text-oriented communication facility. Unencrypted and largely obsolete for secure networks."),
        ("TLS (Transport Layer Security)", "A cryptographic protocol designed to provide communications security over a computer network, widely used in HTTPS."),
        ("TOR (The Onion Router)", "Anonymization network that routes traffic through multiple relay nodes, each encrypting a layer. Makes it very difficult to trace traffic to its source."),
        ("Traffic Correlation Attack", "A method used to de-anonymize Tor users by matching the timing and volume of traffic entering the Tor network with traffic exiting it."),
        ("USA FREEDOM Act", "A US law enacted in 2015 that restored and modified several provisions of the Patriot Act, imposing some new limits on the bulk collection of telecommunication metadata."),
        ("VPN (Virtual Private Network)", "Creates an encrypted tunnel between your device and a server, hiding your traffic from local network surveillance. Essential on untrusted networks like public Wi-Fi."),
        ("XKeyscore", "NSA tool for searching and analyzing internet data. It could search email content, browsing history, and other digital activity in near real time."),
        ("Zero-Day Exploit", "A vulnerability in software unknown to the vendor. Called zero-day because there are zero days of notice before it is exploited. No patch exists yet.")
    ]

    def current_viewport_size():
        width = config.screen_width
        height = config.screen_height

        try:
            physical_size = renpy.get_physical_size()
            if physical_size:
                width, height = physical_size
        except Exception:
            pass

        return width, height

    def fullscreen_prompt_supported():
        return renpy.variant("pc") or renpy.variant("web")

    def should_prompt_for_fullscreen():
        return fullscreen_prompt_supported() and not preferences.fullscreen

    def is_compact_layout():
        width, height = current_viewport_size()
        return renpy.variant("small") or width <= 1280 or height <= 760

    def is_medium_layout():
        width, height = current_viewport_size()
        return renpy.variant("touch") or width <= 1600 or height <= 900

    def localized_text_font(semibold=False, mono=False):
        if current_translation_language() == "ukrainian":
            return "fonts/DejaVuSans.ttf"
        if mono:
            return "fonts/DejaVuSans.ttf"
        if semibold:
            return "fonts/DejaVuSans.ttf"
        return "fonts/DejaVuSans.ttf"

    def voice_for_current_language(english_path):
        lang = current_translation_language()
        if lang is None:
            return english_path
        if lang == "french":
            french_path = english_path.replace("audio/voice/en/", "audio/voice/fr/")
            if renpy.loadable(french_path):
                return french_path
        if lang == "dutch":
            dutch_path = english_path.replace("audio/voice/en/", "audio/voice/nl/")
            if renpy.loadable(dutch_path):
                return dutch_path
        return None

    def notebook_entry_count():
        return len(store.notebook_entries)

    def add_notebook_entry(text):
        entry = (text or "").strip()
        if not entry:
            renpy.notify(t("Write a note first."))
            return

        store.notebook_entries = list(store.notebook_entries) + [entry]
        store.notebook_draft = ""
        renpy.notify(t("Saved to notebook."))
        renpy.restart_interaction()

    def clear_notebook_entries():
        store.notebook_entries = []
        store.notebook_draft = ""
        renpy.notify(t("Notebook cleared."))
        renpy.restart_interaction()

    def get_notebook_export_text():
        header = "FIELD NOTEBOOK\nClassified: The Snowden Files\n\n"
        body = "\n".join(f"{index}. {entry}" for index, entry in enumerate(store.notebook_entries, 1))
        return header + body

    def get_notebook_export_dir():
        paths = [
            os.path.join(config.basedir, "exports"),
            os.path.join(os.path.expanduser("~"), "RenPyNotebookExports"),
        ]

        for path in paths:
            try:
                os.makedirs(path, exist_ok=True)
                return path
            except Exception:
                pass

        return None

    def choose_notebook_export_path(default_filename="field_notebook.txt"):
        root = None

        try:
            import tkinter as tk
            from tkinter import filedialog

            root = tk.Tk()
            root.withdraw()
            root.attributes("-topmost", True)
            root.update_idletasks()
            root.lift()
            root.focus_force()

            path = filedialog.asksaveasfilename(
                title=t("Save notebook as..."),
                initialdir=os.path.expanduser("~"),
                initialfile=default_filename,
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            )

            root.destroy()
            return path
        except Exception:
            try:
                if root is not None:
                    root.destroy()
            except Exception:
                pass

        if hasattr(renpy, "filepicker"):
            try:
                path = renpy.filepicker(
                    title=t("Save notebook as..."),
                    save=True,
                    default=default_filename,
                )
                if path is None:
                    return ""
                return path
            except TypeError:
                try:
                    path = renpy.filepicker(
                        title=t("Save notebook as..."),
                        save=True,
                    )
                    if path is None:
                        return ""
                    return path
                except Exception:
                    pass
            except Exception:
                pass

        return None

    def export_notebook_txt():
        if not store.notebook_entries:
            renpy.notify(t("No notes to export."))
            return

        default_filename = datetime.now().strftime("field_notebook_%Y%m%d_%H%M%S.txt")
        path = choose_notebook_export_path(default_filename)

        if path == "":
            renpy.notify(t("Notebook export canceled."))
            return

        if path is None:
            export_dir = get_notebook_export_dir()
            if not export_dir:
                renpy.notify(t("Could not determine a writable export location."))
                return

            path = os.path.join(export_dir, default_filename)
            renpy.notify(t("Could not open a save dialog. Exporting to the default exports folder."))

        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(get_notebook_export_text())

            renpy.notify(f"Notebook exported to {path}")
        except Exception as exc:
            renpy.notify(f"Failed to export notebook: {exc}")

    def get_dossier_export_text():
        header = "NETWORK SECURITY DOSSIER\nClassified: The Snowden Files\n\n"
        lines = []
        for term, definition in DOSSIER_ENTRIES:
            lines.append(f"{term}\n  {definition}")
        return header + "\n\n".join(lines)

    def export_dossier_txt():
        default_filename = datetime.now().strftime("dossier_%Y%m%d_%H%M%S.txt")
        path = choose_notebook_export_path(default_filename)

        if path == "":
            renpy.notify(t("Dossier export canceled."))
            return

        if path is None:
            export_dir = get_notebook_export_dir()
            if not export_dir:
                renpy.notify(t("Could not determine a writable export location."))
                return

            path = os.path.join(export_dir, default_filename)
            renpy.notify(t("Could not open a save dialog. Exporting to the default exports folder."))

        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(get_dossier_export_text())

            renpy.notify(t("Dossier exported to ") + path)
        except Exception as exc:
            renpy.notify(f"Failed to export dossier: {exc}")

    SPEAKER_HIGHLIGHT_TAGS = (
        "edward",
        "supervisor",
        "colleague",
        "greenwald",
        "poitras",
        "journalist",
        "editor",
        "nsa_chief",
        "russian_official",
    )

    def _strip_speaker_state(at_list):
        if not at_list:
            return []

        return [
            transform
            for transform in at_list
            if transform is not active_char and transform is not inactive_char
        ]

    def speaker_dimmer(event, interact=True, **kwargs):
        if not interact or event != "begin":
            return

        speaker_tag = renpy.get_say_image_tag()

        for tag in SPEAKER_HIGHLIGHT_TAGS:
            if not renpy.showing(tag):
                continue

            try:
                current = renpy.get_at_list(tag, "master")
            except Exception:
                current = None

            base_transforms = _strip_speaker_state(list(current or ()))
            new_state = active_char if tag == speaker_tag else inactive_char
            renpy.show(tag, at_list=base_transforms + [new_state])

    config.character_callback = speaker_dimmer

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # LEGAL FILTER — config.say_menu_text_filter
    # Safety-net replacement applied at the Ren'Py text-render layer to any
    # dialogue `what` text AND menu item captions. Acts as a backstop so that
    # hardcoded agency names never reach the player, even if script lines
    # were not updated to use the ag_* interpolation variables.
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    _AGENCY_REPLACEMENTS = [
        ("NSA",  "Signal Reach Network (SRN)"),
        ("CIA",  "The Obsidian Oversight (OO)"),
        ("FBI",  "Bureau of Internal Security (BIS)"),
    ]

    def _legal_text_filter(s):
        """Replace real agency acronyms with their fictional counterparts."""
        for real, alias in _AGENCY_REPLACEMENTS:
            s = s.replace(real, alias)
        return s

    config.say_menu_text_filter = _legal_text_filter

    def autosave_chapter(chapter_num):
        """Autosave after a chapter completes and show a notification."""
        try:

            renpy.save("chapter-%d" % chapter_num, extra_info="Chapter %d" % chapter_num)
            renpy.notify(t("Chapter %d autosave complete.") % chapter_num)
        except Exception:
            renpy.notify(t("Autosave failed."))

    def mouse_parallax(trans, st, at):

        import pygame
        x, y = renpy.get_mouse_pos()

        trans.xoffset = (960 - x) * 0.02
        trans.yoffset = (540 - y) * 0.02
        return 0

    def portrait_sprite(path, width=900, height=1396, yoffset=0):
        return renpy.display.transform.Transform(
            path,
            fit="contain",
            xsize=width,
            ysize=height,
            xalign=0.5,
            yalign=1.0,
            yoffset=yoffset,
            subpixel=True,
        )

transform parallax:
    zoom 1.05
    align (0.5, 0.5)
    function mouse_parallax

image edward neutral = portrait_sprite("sprites/edward neutral.png", yoffset=9)
image edward thoughtful = portrait_sprite("sprites/edward thoughtful.png", yoffset=9)
image edward concerned = portrait_sprite("sprites/edward concerned.png", yoffset=9)
image edward shocked = portrait_sprite("sprites/edward shocked.png", yoffset=9)
image edward tense = portrait_sprite("sprites/edward tense.png", yoffset=9)
image edward determined = portrait_sprite("sprites/edward determined.png", yoffset=9)
image edward defiant = portrait_sprite("sprites/edward defiant.png", yoffset=9)
image edward sad = portrait_sprite("sprites/edward sad.png", yoffset=9)
image edward tired = portrait_sprite("sprites/edward tired.png", yoffset=9)
image edward relieved = portrait_sprite("sprites/edward relieved.png", yoffset=9)

image supervisor neutral = portrait_sprite("sprites/supervisor neutral.png", yoffset=21)
image supervisor stern = portrait_sprite("sprites/supervisor stern.png", yoffset=21)
image supervisor authoritative = portrait_sprite("sprites/supervisor authoritative.png", yoffset=21)
image supervisor suspicious = portrait_sprite("sprites/supervisor suspicious.png", yoffset=21)
image supervisor annoyed = portrait_sprite("sprites/supervisor annoyed.png", yoffset=21)
image supervisor cold = portrait_sprite("sprites/supervisor cold.png", yoffset=21)

image colleague neutral = portrait_sprite("sprites/colleague neutral.png", yoffset=19)
image colleague casual = portrait_sprite("sprites/colleague casual.png", yoffset=19)
image colleague amused = portrait_sprite("sprites/colleague amused.png", yoffset=19)
image colleague smug = portrait_sprite("sprites/colleague smug.png", yoffset=19)
image colleague uneasy = portrait_sprite("sprites/colleague uneasy.png", yoffset=19)
image colleague cautious = portrait_sprite("sprites/colleague cautious.png", yoffset=19)

image greenwald neutral:
    "sprites/greenwald neutral.png"
    zoom 1.02
image greenwald skeptical:
    "sprites/greenwald skeptical.png"
    zoom 1.02
image greenwald confused:
    "sprites/greenwald confused.png"
    zoom 1.02
image greenwald curious:
    "sprites/greenwald curious.png"
    zoom 1.02
image greenwald shocked:
    "sprites/greenwald shocked.png"
    zoom 1.02
image greenwald serious:
    "sprites/greenwald serious.png"
    zoom 1.02
image greenwald resolved:
    "sprites/greenwald resolved.png"
    zoom 1.02
image greenwald concerned:
    "sprites/greenwald concerned.png"
    zoom 1.02

image poitras neutral:
    "sprites/poitras neutral.png"
    zoom 1.02
image poitras focused:
    "sprites/poitras focused.png"
    zoom 1.02
image poitras cautious:
    "sprites/poitras cautious.png"
    zoom 1.02
image poitras serious:
    "sprites/poitras serious.png"
    zoom 1.02
image poitras concerned:
    "sprites/poitras concerned.png"
    zoom 1.02
image poitras resolved:
    "sprites/poitras resolved.png"
    zoom 1.02

image russian_official neutral = portrait_sprite("sprites/russian official neutral.png", yoffset=34)
image russian_official smug = portrait_sprite("sprites/russian official smug.png", yoffset=34)
image russian_official calculating = portrait_sprite("sprites/russian official calculating.png", yoffset=34)
image russian_official cold = portrait_sprite("sprites/russian official cold.png", yoffset=34)
image russian_official pressuring = portrait_sprite("sprites/russian official pressuring.png", yoffset=34)
image russian_official confident = portrait_sprite("sprites/russian official confident.png", yoffset=34)

image nsa_chief neutral:
    "sprites/nsa chief neutral.png"
    zoom 1.0
image nsa_chief authoritative:
    "sprites/nsa chief authoritative.png"
    zoom 1.0
image nsa_chief angry:
    "sprites/nsa chief angry.png"
    zoom 1.0
image nsa_chief cold:
    "sprites/nsa chief cold.png"
    zoom 1.0

image journalist neutral = portrait_sprite("sprites/journalist neutral.png", yoffset=20)
image journalist skeptical = portrait_sprite("sprites/journalist skeptical.png", yoffset=20)
image journalist focused = portrait_sprite("sprites/journalist focused.png", yoffset=20)
image journalist serious = portrait_sprite("sprites/journalist serious.png", yoffset=20)
image journalist shocked = portrait_sprite("sprites/journalist shocked.png", yoffset=20)
image journalist resolved = portrait_sprite("sprites/journalist resolved.png", yoffset=20)
image journalist concerned = portrait_sprite("sprites/journalist concerned.png", yoffset=20)

image editor neutral:
    "sprites/editor neutral.png"
    zoom 0.76

image logo_watermark:
    "images/logo.png"
    xalign 0.5
    yalign 0.5
    zoom 1.15
    alpha 0.15

image bg_1:
    "backgrounds/chapter_1/bg_1.png"
    xysize (1920, 1080)

image bg_nsa_main:
    "backgrounds/chapter_1/bg_nsa_main.png"
    xysize (1920, 1080)

image bg_nsa_terminal = Movie(play="images/backgrounds/chapter_1/bg_nsa_terminal.webm", loop=True)

image bg_nsa_servers:
    "backgrounds/chapter_2/bg_nsa_servers.png"
    xysize (1920, 1080)

image bg_nsa_exterior = Movie(play="images/backgrounds/chapter_1/bg_nsa_exterior.webm", loop=True)
image bg_nsa_checkpoint = Movie(play="images/backgrounds/chapter_1/bg_nsa_checkpoint.webm", loop=True)

image bg_prism:
    "backgrounds/chapter_2/bg_prism.png"
    xysize (1920, 1080)

image bg_prism1:
    "backgrounds/chapter_2/bg_prism1.png"
    xysize (1920, 1080)

image bg_hong_kong:
    "backgrounds/chapter_3/bg_hong_kong.png"
    xysize (1920, 1080)

image bg_hong_kong_street:
    "backgrounds/chapter_3/bg_hong_kong_street.png"
    xysize (1920, 1080)

image bg_hong_kong_terminal:
    "backgrounds/chapter_3/bg_hong_kong_terminal.png"
    xysize (1920, 1080)

image bg_kali_net:
    "backgrounds/chapter_3/kali-net.jpg"
    xysize (1920, 1080)

image bg_hk_airport:
    "backgrounds/chapter_4/bg_hk_airport.png"
    xysize (1920, 1080)

image bg_hong_kong_hotel:
    "backgrounds/chapter_4/bg_hong_kong_hotel.png"
    xysize (1920, 1080)

image bg_leak:
    "backgrounds/chapter_4/bg_leak.png"
    xysize (1920, 1080)

image bg_moscow_apartment:
    "backgrounds/chapter_5/bg_moscow_apartment.png"
    xysize (1920, 1080)

image bg_moscow_winter_epilogue:
    "backgrounds/chapter_5/bg_moscow_winter_epilogue.png"
    xysize (1920, 1080)

image bg_sheremetyevo:
    "backgrounds/chapter_5/bg_sheremetyevo.png"
    xysize (1920, 1080)

transform active_char:
    ease 0.2 matrixcolor SaturationMatrix(1.0) alpha 1.0

transform inactive_char:
    ease 0.2 matrixcolor SaturationMatrix(0.45) alpha 0.82

transform enter_left:
    xanchor 0.5
    yanchor 1.0
    on show:
        xpos -0.20 ypos 1.50 alpha 0.0 zoom 1.0
        ease 0.6 xpos 0.15 ypos 1.50 alpha 1.0 zoom 1.40
    on replace:
        xpos 0.15 ypos 1.50 alpha 1.0 zoom 1.40

transform enter_right:
    xanchor 0.5
    yanchor 1.0
    on show:
        xpos 1.40 ypos 1.50 alpha 0.0 zoom 1.0
        ease 0.6 xpos 0.85 ypos 1.50 alpha 1.0 zoom 1.40
    on replace:
        xpos 0.85 ypos 1.50 alpha 1.0 zoom 1.40

transform enter_center:
    xanchor 0.5
    yanchor 1.0
    on show:
        xpos 0.3 ypos 1.50 alpha 0.0 zoom 1.0
        ease 0.5 xpos 0.5 ypos 1.50 alpha 1.0 zoom 1.40
    on replace:
        xpos 0.5 ypos 1.50 alpha 1.0 zoom 1.40

transform stage_center:
    xanchor 0.5
    yanchor 1.0
    xpos 0.5
    ypos 1.15

transform idle_breathe:
    zoom 1.0
    linear 2.0 zoom 1.01
    linear 2.0 zoom 1.0
    repeat

transform exit_left:
    ease 0.5 xpos -0.4 alpha 0.0

transform exit_right:
    ease 0.5 xpos 1.4 alpha 0.0

transform exit_fade:
    ease 0.4 alpha 0.0

transform exit_panic:
    linear 0.1 xoffset 5
    linear 0.1 xoffset -5
    linear 0.1 xoffset 3
    linear 0.1 xoffset 0
    ease 0.3 xpos 1.4 alpha 0.0

transform title_glitch:
    alpha 1.0
    pause 3.0
    alpha 0.85
    pause 0.05
    alpha 1.0
    pause 0.1
    alpha 0.9
    pause 0.05
    alpha 1.0
    repeat

transform btn_glow:
    linear 0.2 zoom 1.02
    linear 0.2 zoom 1.0
    repeat

transform scanline_move:
    ypos 0.0
    linear 4.0 ypos 1.0
    ypos 0.0
    repeat

transform chapter_fade_in:
    alpha 0.0
    linear 1.0 alpha 1.0

transform chapter_fade_out:
    alpha 1.0
    linear 1.0 alpha 0.0

transform cursor_blink:
    alpha 1.0
    pause 0.5
    alpha 0.0
    pause 0.5
    repeat

define fade_quick = Fade(0.3, 0.0, 0.3)

define chapter_transition = Fade(1.0, 0.5, 1.0, color="#000000")

define glitch_cut = Fade(0.1, 0.05, 0.1, color="#00FFD1")

init python:
    _tree_choice_map = {
        'choice_ch1_1': ("protocol", "explore"),
        'choice_ch1_2': ("report", "silent"),
        'choice_ch2_1': ("trust", "alone"),
        'choice_ch2_2': ("copy", "notes"),
        'choice_ch3_0': ("bluff", "accelerate"),
        'choice_ch3_1': ("pgp", "email", "wait"),
        'choice_ch3_2': ("full", "partial", "vague"),
        'choice_ch4_1': ("hotel", "mobile"),
        'choice_ch4_2': ("airport", "russia", "ecuador", "embassy", "stay"),
        'choice_ch5_1': ("encourage", "caution", "refuse"),
    }
    _tree_endings = ("hero", "fugitive", "imprisoned", "silenced", "betrayed")

    _tree_defaults = {
        'choice_ch1_1': '', 'choice_ch1_2': '',
        'choice_ch2_1': '', 'choice_ch2_2': '',
        'choice_ch3_0': '', 'choice_ch3_1': '', 'choice_ch3_2': '',
        'choice_ch4_1': '', 'choice_ch4_2': '',
        'choice_ch5_1': '',
        'tree_ch_reached': 0,
        'tree_ending': '',
        'tree_ending_unlocked': [],
    }

    for _choice_var in _tree_choice_map:
        _tree_defaults[_choice_var + "_unlocked"] = []

    for _tk, _tv in _tree_defaults.items():
        if getattr(persistent, _tk, None) is None:
            setattr(persistent, _tk, _tv)

    for _choice_var in _tree_choice_map:
        _current_value = getattr(persistent, _choice_var, "")
        _unlocked_name = _choice_var + "_unlocked"
        _unlocked_values = list(getattr(persistent, _unlocked_name, []) or [])
        if _current_value and _current_value not in _unlocked_values:
            _unlocked_values.append(_current_value)
            setattr(persistent, _unlocked_name, _unlocked_values)

    _ending_value = getattr(persistent, "tree_ending", "")
    _ending_unlocked = list(getattr(persistent, "tree_ending_unlocked", []) or [])
    if _ending_value and _ending_value not in _ending_unlocked:
        _ending_unlocked.append(_ending_value)
        setattr(persistent, "tree_ending_unlocked", _ending_unlocked)

    def tree_record_choice(choice_var, value):
        setattr(persistent, choice_var, value)
        unlocked_name = choice_var + "_unlocked"
        unlocked_values = list(getattr(persistent, unlocked_name, []) or [])
        if value not in unlocked_values:
            unlocked_values.append(value)
            setattr(persistent, unlocked_name, unlocked_values)
        renpy.save_persistent()

    def tree_reset_current_run():
        for _name in _tree_choice_map:
            setattr(persistent, _name, "")
        setattr(persistent, "tree_ch_reached", 0)
        setattr(persistent, "tree_ending", "")
        renpy.save_persistent()

    def tree_choice_is_unlocked(choice_var, value):
        return value in list(getattr(persistent, choice_var + "_unlocked", []) or [])

    def tree_unlocked_choice_count():
        total = 0
        for _name in _tree_choice_map:
            total += len(list(getattr(persistent, _name + "_unlocked", []) or []))
        return total

    def tree_total_choice_count():
        return sum(len(_values) for _values in _tree_choice_map.values())

    def tree_record_ending(value):
        setattr(persistent, "tree_ending", value)
        unlocked_endings = list(getattr(persistent, "tree_ending_unlocked", []) or [])
        if value not in unlocked_endings:
            unlocked_endings.append(value)
            setattr(persistent, "tree_ending_unlocked", unlocked_endings)
        renpy.save_persistent()

    def tree_ending_is_unlocked(value):
        return value in list(getattr(persistent, "tree_ending_unlocked", []) or [])

    del _tree_defaults, _tk, _tv, _choice_var, _current_value, _unlocked_name, _unlocked_values, _ending_value, _ending_unlocked
