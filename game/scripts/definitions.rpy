################################################################################
## DEFINITIONS.RPY — Character Definitions, Flags, Images, Transforms
## Classified: The Snowden Files
################################################################################

init offset = -1

################################################################################
## CHARACTER DEFINITIONS
################################################################################

# === PROTAGONIST ===
define e = Character("You",
    image="edward",
    color="#00FFD1",
    what_color="#E8E8E8",
    who_size=22,
    what_size=20,
    who_bold=True)

# === JOURNALISTS ===
define greenwald = Character("Grayson Wardell",
    image="greenwald",
    color="#FFD700",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=22,
    what_size=20)

define poitras = Character("Leah Portman",
    image="poitras",
    color="#FF69B4",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=22,
    what_size=20)

# === ANTAGONISTS / AUTHORITY ===
define nsa_chief = Character("Director Marcus Hale",
    color="#FF2D55",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=22,
    what_size=20)

define supervisor = Character("Supervisor Daniel Cross",
    image="supervisor",
    color="#FF6B35",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=22,
    what_size=20)

# === ALLIES / NEUTRAL ===
define colleague = Character("COLLEAGUE [[CLASSIFIED]]",
    image="colleague",
    color="#888888",
    what_color="#CCCCCC",
    who_bold=False,
    who_size=22,
    what_size=20)

define russian_official = Character("Agent Viktor Malenkov",
    image="russian_official",
    color="#CC2222",
    what_color="#E8E8E8",
    who_bold=True,
    who_size=22,
    what_size=20)

# === SYSTEM / NARRATOR ===
define sys = Character("// SYSTEM //",
    color="#00FF00",
    what_color="#00FF00",
    who_bold=True,
    who_size=20,
    what_size=18)

define narrator_voice = Character(None,
    what_color="#AAAAAA",
    what_italic=True,
    what_size=22)

define im = Character("INTERNAL MONOLOGUE",
    what_prefix="*",
    what_suffix="*",
    color="#888888",
    what_color="#AAAAAA",
    who_size=18,
    what_size=20)


################################################################################
## STORY FLAGS
################################################################################

# === Core Metrics ===
default trust_score = 0
default knowledge_score = 0
default suspicion_level = 0
default contacts_secured = 0
default evidence_secured = False
default identity_exposed = False
default escape_successful = False

# === Chapter Completion Flags ===
default ch1_outcome = ""
default ch2_outcome = ""
default ch3_outcome = ""
default ch4_outcome = ""

# === Ending Tracker ===
default ending_type = ""

# === UI State ===
default current_chapter = 1
default show_hud = True
default notebook_entries = []
default notebook_draft = ""
default suspicion_lockdown_triggered = False

# === Minigame State ===
default mg_firewall_score = 0
default mg_decrypt_solved = False
default mg_opsec_score = 0
default mg_trace_solved = False

# === Question Tracking ===
default text_input_attempts = 0


################################################################################
## PARALLAX SYSTEM
################################################################################

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
    ]

    DOSSIER_ENTRIES = [
        ("AES-256", "Advanced Encryption Standard with a 256-bit key. Strong symmetric encryption that is effectively impossible to brute-force with current consumer hardware."),
        ("Boundless Informant", "A data analysis tool used by the NSA to summarize and visualize the metadata and communications records they collect globally."),
        ("Caesar Cipher", "Simple substitution cipher where each letter is shifted by a fixed number. Easy to break but historically significant. Example: ROT-3 shifts A to D, B to E, and so on."),
        ("CIA (Central Intelligence Agency)", "A civilian foreign intelligence service of the federal government of the United States, tasked with gathering, processing, and analyzing national security information."),
        ("DNS (Domain Name System)", "The phonebook of the Internet. Translates human-readable domain names (like example.com) into machine-readable IP addresses."),
        ("Domestic Surveillance", "The monitoring of citizens within a country's borders by its own government, often a point of legal and ethical controversy."),
        ("Edward Snowden", "An American former computer intelligence consultant who leaked highly classified information from the NSA in 2013, revealing numerous global surveillance programs."),
        ("Encryption Fingerprints", "Unique patterns or metadata in encrypted traffic that can reveal the type of encryption used, the application generating it, or even the user, without breaking the encryption itself."),
        ("Firewall", "Network security system that monitors and filters incoming and outgoing traffic based on predefined rules. Acts as a barrier between trusted and untrusted networks."),
        ("FISA (Foreign Intelligence Surveillance Act)", "A United States federal law that establishes procedures for the physical and electronic surveillance and collection of foreign intelligence information."),
        ("Foreign Intelligence", "Information relating to the capabilities, intentions, or activities of foreign governments, organizations, or persons."),
        ("HTTP (Hypertext Transfer Protocol)", "The foundation of data communication for the World Wide Web. It is unencrypted, meaning data sent via HTTP can be intercepted."),
        ("HTTPS", "HTTP with TLS/SSL encryption. Secures data between your browser and a web server. Look for the padlock icon in your browser's address bar."),
        ("Inspector General", "An investigative official in a civil or military organization. In the intelligence community, they are responsible for internal audits and investigating whistleblowers' claims."),
        ("Man-in-the-Middle Attack", "An attacker secretly intercepts communication between two parties. Both parties think they're talking directly to each other. Key verification prevents this."),
        ("Mass Surveillance", "The intricate surveillance of an entire or a substantial fraction of a population in order to monitor that group of citizens."),
        ("Metadata", "Data about data — who you communicated with, when, for how long, from where. Does not include the message content but can reveal intimate patterns of life."),
        ("National Security", "The security and defense of a nation state, including its citizens, economy, and institutions, which is regarded as a duty of government."),
        ("Network Security", "Policies and practices adopted to prevent and monitor unauthorized access, misuse, modification, or denial of a computer network and network-accessible resources."),
        ("NSA (National Security Agency)", "A national-level intelligence agency of the United States Department of Defense, under the authority of the Director of National Intelligence."),
        ("OpSec (Operational Security)", "The practice of protecting critical information by identifying what intelligence the adversary could gather from your actions and taking steps to prevent it."),
        ("PGP (Pretty Good Privacy)", "Asymmetric encryption system using public/private key pairs. Public key encrypts, only the matching private key can decrypt. Used for secure email communication."),
        ("PRISM", "NSA surveillance program providing direct access to user data from major tech companies. Exposed by Snowden in 2013."),
        ("Private IP Ranges", "IP addresses reserved for internal network use (like 192.168.x.x) that are not routable on the public internet."),
        ("Public Wi-Fi", "Unsecured wireless networks open to the public. Highly vulnerable to interception and man-in-the-middle attacks."),
        ("RDP (Remote Desktop Protocol)", "A proprietary protocol developed by Microsoft that provides a user with a graphical interface to connect to another computer over a network connection."),
        ("Reverse Shell", "A type of shell in which the target machine communicates back to the attacking machine. Often used to bypass firewalls that block incoming connections."),
        ("SecureDrop", "An open-source whistleblowing platform that allows anonymous document submission. Used by major news organizations to protect sources."),
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

    def notebook_entry_count():
        return len(store.notebook_entries)

    def add_notebook_entry(text):
        entry = (text or "").strip()
        if not entry:
            renpy.notify("Write a note first.")
            return

        store.notebook_entries = list(store.notebook_entries) + [entry]
        store.notebook_draft = ""
        renpy.notify("Saved to notebook.")
        renpy.restart_interaction()

    def clear_notebook_entries():
        store.notebook_entries = []
        store.notebook_draft = ""
        renpy.notify("Notebook cleared.")
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

    def export_notebook_txt():
        if not store.notebook_entries:
            renpy.notify("No notes to export.")
            return

        export_dir = get_notebook_export_dir()
        if not export_dir:
            renpy.notify("Could not determine a writable export location.")
            return

        filename = datetime.now().strftime("field_notebook_%Y%m%d_%H%M%S.txt")
        path = os.path.join(export_dir, filename)

        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(get_notebook_export_text())

            renpy.notify("Your notebook has been exported")
        except Exception as exc:
            renpy.notify(f"Failed to export notebook: {exc}")

    def get_dossier_export_text():
        header = "NETWORK SECURITY DOSSIER\nClassified: The Snowden Files\n\n"
        lines = []
        for term, definition in DOSSIER_ENTRIES:
            lines.append(f"{term}\n  {definition}")
        return header + "\n\n".join(lines)

    def export_dossier_txt():
        export_dir = get_notebook_export_dir()
        if not export_dir:
            renpy.notify("Could not determine a writable export location.")
            return

        filename = datetime.now().strftime("dossier_%Y%m%d_%H%M%S.txt")
        path = os.path.join(export_dir, filename)

        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(get_dossier_export_text())

            renpy.notify("Dossier exported to " + export_dir)
        except Exception as exc:
            renpy.notify(f"Failed to export dossier: {exc}")

    def highlighted_dialogue(text):
        if not text:
            return text

        result = text
        for term in sorted(IMPORTANT_TERMS, key=len, reverse=True):
            pattern = re.compile(r"(?<!\{b\})(%s)(?!\{/b\})" % re.escape(term), re.IGNORECASE)
            result = pattern.sub(lambda match: "{b}%s{/b}" % match.group(1), result)

        return result

    config.say_menu_text_filter = highlighted_dialogue

    def speaker_dimmer(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "begin":
            speaker = renpy.get_say_image_tag()
            
            # Keep only the actually visible speaker bright.
            char_tags = [
                "edward",
                "supervisor",
                "colleague",
                "greenwald",
                "poitras",
                "journalist",
                "editor",
                "nsa_chief",
                "russian_official",
            ]
            
            for tag in char_tags:
                if renpy.showing(tag):
                    if tag == speaker:
                        renpy.show(tag, at_list=[active_char])
                    else:
                        renpy.show(tag, at_list=[inactive_char])

    config.character_callback = speaker_dimmer

    def autosave_chapter(chapter_num):
        """Autosave after a chapter completes and show a notification."""
        try:
            # Save to a dedicated 'chapter' page so it gets its own tab in the Load screen
            renpy.save("chapter-%d" % chapter_num, extra_info="Chapter %d" % chapter_num)
            renpy.notify("Chapter %d autosave complete." % chapter_num)
        except Exception:
            renpy.notify("Autosave failed.")

    def mouse_parallax(trans, st, at):
        # Provide a subtle parallax based on mouse
        # Ren'Py get_mouse_pos() might return a tuple
        import pygame
        x, y = renpy.get_mouse_pos()
        
        # Calculate offset from center (assuming 1920x1080)
        trans.xoffset = (960 - x) * 0.02
        trans.yoffset = (540 - y) * 0.02
        return 0

transform parallax:
    zoom 1.05
    align (0.5, 0.5)
    function mouse_parallax

################################################################################
## IMAGE DEFINITIONS
################################################################################

# === Character Sprites ===

# -- Edward --
image edward neutral:
    "sprites/edward neutral.png"
    zoom 1.02
image edward thoughtful:
    "sprites/edward thoughtful.png"
    zoom 1.02
image edward concerned:
    "sprites/edward concerned.png"
    zoom 1.02
image edward shocked:
    "sprites/edward shocked.png"
    zoom 1.02
image edward tense:
    "sprites/edward tense.png"
    zoom 1.02
image edward determined:
    "sprites/edward determined.png"
    zoom 1.02
image edward defiant:
    "sprites/edward defiant.png"
    zoom 1.02
image edward sad:
    "sprites/edward sad.png"
    zoom 1.02
image edward tired:
    "sprites/edward tired.png"
    zoom 1.02
image edward relieved:
    "sprites/edward relieved.png"
    zoom 1.02

# -- Supervisor --
image supervisor neutral:
    "sprites/supervisor neutral.png"
    zoom 1.0
image supervisor stern:
    "sprites/supervisor stern.png"
    zoom 1.0
image supervisor authoritative:
    "sprites/supervisor authoritative.png"
    zoom 1.0
image supervisor suspicious:
    "sprites/supervisor suspicious.png"
    zoom 1.0
image supervisor annoyed:
    "sprites/supervisor annoyed.png"
    zoom 1.0
image supervisor cold:
    "sprites/supervisor cold.png"
    zoom 1.0

# -- Colleague --
image colleague neutral:
    "sprites/colleague neutral.png"
    zoom 0.98
image colleague casual:
    "sprites/colleague casual.png"
    zoom 0.98
image colleague amused:
    "sprites/colleague amused.png"
    zoom 0.98
image colleague smug:
    "sprites/colleague smug.png"
    zoom 0.98
image colleague uneasy:
    "sprites/colleague uneasy.png"
    zoom 0.98
image colleague cautious:
    "sprites/colleague cautious.png"
    zoom 0.98

# -- Greenwald --
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

# -- Poitras --
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

# -- Russian Official --
image russian_official neutral:
    "sprites/russian official neutral.png"
    zoom 1.0
image russian_official smug:
    "sprites/russian official smug.png"
    zoom 1.0
image russian_official calculating:
    "sprites/russian official calculating.png"
    zoom 1.0
image russian_official cold:
    "sprites/russian official cold.png"
    zoom 1.0
image russian_official pressuring:
    "sprites/russian official pressuring.png"
    zoom 1.0
image russian_official confident:
    "sprites/russian official confident.png"
    zoom 1.0

# -- NSA Chief --
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

# -- Journalist --
image journalist neutral:
    "sprites/journalist neutral.png"
    zoom 1.02
image journalist skeptical:
    "sprites/journalist skeptical.png"
    zoom 1.02
image journalist focused:
    "sprites/journalist focused.png"
    zoom 1.02
image journalist serious:
    "sprites/journalist serious.png"
    zoom 1.02
image journalist shocked:
    "sprites/journalist shocked.png"
    zoom 1.02
image journalist resolved:
    "sprites/journalist resolved.png"
    zoom 1.02
image journalist concerned:
    "sprites/journalist concerned.png"
    zoom 1.02

# -- Editor --
image editor neutral:
    "sprites/editor neutral.png"
    zoom 1.0
# === Logo Watermark ===
image logo_watermark:
    "images/logo.png"
    xalign 0.5
    yalign 0.5
    zoom 1.15
    alpha 0.15

# === Backgrounds ===
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


################################################################################
## ATL TRANSFORMS — Character Animations
################################################################################

# === ACTIVE / INACTIVE STATES ===

transform active_char:
    xanchor 0.5 yanchor 1.0
    ease 0.25 matrixcolor SaturationMatrix(1.0) zoom 1.18 alpha 1.0

transform inactive_char:
    xanchor 0.5 yanchor 1.0
    ease 0.25 matrixcolor SaturationMatrix(0.3) zoom 1.12 alpha 0.9

# === ENTRANCE TRANSFORMS ===

# Slide in from left
transform enter_left:
    xanchor 0.5
    yanchor 1.0
    xpos -0.20 ypos 1.60 alpha 0.0 zoom 1.0
    ease 0.6 xpos 0.25 ypos 1.60 alpha 1.0 zoom 1.18

# Slide in from right
transform enter_right:
    xanchor 0.5
    yanchor 1.0
    xpos 1.20 ypos 1.60 alpha 0.0 zoom 1.0
    ease 0.6 xpos 0.75 ypos 1.60 alpha 1.0 zoom 1.18

# Fade in from center
transform enter_center:
    xanchor 0.5
    yanchor 1.0
    xpos 0.5 ypos 1.60 alpha 0.0 zoom 1.0
    ease 0.5 xpos 0.5 ypos 1.60 alpha 1.0 zoom 1.18

transform stage_center:
    xanchor 0.5
    yanchor 1.0
    xpos 0.5
    ypos 1.60

# === IDLE TRANSFORMS ===

# Subtle breathing idle animation
transform idle_breathe:
    zoom 1.0
    linear 2.0 zoom 1.01
    linear 2.0 zoom 1.0
    repeat

# === EXIT TRANSFORMS ===

# Slide out to left
transform exit_left:
    ease 0.5 xpos -0.4 alpha 0.0

# Slide out to right
transform exit_right:
    ease 0.5 xpos 1.4 alpha 0.0

# Fade out
transform exit_fade:
    ease 0.4 alpha 0.0

# Nervous/tense exit (for high suspicion moments)
transform exit_panic:
    linear 0.1 xoffset 5
    linear 0.1 xoffset -5
    linear 0.1 xoffset 3
    linear 0.1 xoffset 0
    ease 0.3 xpos 1.4 alpha 0.0

# === MENU / UI TRANSFORMS ===

# Title glitch effect
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

# Button hover glow
transform btn_glow:
    linear 0.2 zoom 1.02
    linear 0.2 zoom 1.0
    repeat

# Scanline effect for UI
transform scanline_move:
    ypos 0.0
    linear 4.0 ypos 1.0
    ypos 0.0
    repeat

# Fade in for chapter cards
transform chapter_fade_in:
    alpha 0.0
    linear 1.0 alpha 1.0

# Fade out for chapter cards
transform chapter_fade_out:
    alpha 1.0
    linear 1.0 alpha 0.0

# Typing cursor blink
transform cursor_blink:
    alpha 1.0
    pause 0.5
    alpha 0.0
    pause 0.5
    repeat


################################################################################
## SCENE TRANSITIONS
################################################################################

# Between dialogue segments
define fade_quick = Fade(0.3, 0.0, 0.3)

# Between chapters (more dramatic)
define chapter_transition = Fade(1.0, 0.5, 1.0, color="#000000")

# Glitch-style cut
define glitch_cut = Fade(0.1, 0.05, 0.1, color="#00FFD1")


################################################################################
## PERSISTENT STORY-TREE INITIALISATION
## (ensures all tree vars exist before the screen tries to read them)
################################################################################

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
