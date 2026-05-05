################################################################################
## MINIGAME 3: CLEAN THE MESSAGE (Chapter 3)
## Educational: metadata leakage, OpSec, email safety
################################################################################

init python:
    ctm_threats = [
        {"id":"from_email","dangerous":"edward.snowden@nsa.gov","safe":"anon7742@protonmail.com","level":"CRITICAL","label":"Work email reveals identity","category":"Identity",
         "title":"IDENTITY EXPOSED — NSA EMAIL ADDRESS","explanation":"Using your work email is like signing the letter with your employee badge number. The NSA can trace any email sent from @nsa.gov instantly.\n\n✓ FIX: Use an anonymous ProtonMail account created through TOR with no personal information attached."},
        {"id":"cc_field","dangerous":"laura.poitras@documentary.org","safe":"[CC removed]","level":"HIGH","label":"CC exposes your other contacts","category":"Network",
         "title":"NETWORK EXPOSED — CC FIELD","explanation":"Adding a CC connects TWO contacts to the same leaked communication. If one is intercepted, the other is immediately compromised.\n\n✓ FIX: Send separate, independent messages to each contact. Never link sources together."},
        {"id":"subject_line","dangerous":"Re: our phone call on Tuesday","safe":"[No subject]","level":"HIGH","label":"Subject reveals prior contact","category":"History",
         "title":"HISTORY EXPOSED — SUBJECT LINE","explanation":"'Re:' proves prior contact. The subject reveals a phone call on a specific day. NSA call records can now be cross-referenced.\n\n✓ FIX: Leave the subject blank. Never reference past communications in metadata."},
        {"id":"device_sig","dangerous":"Sent from iPhone (NSA-issued)","safe":"[Device signature removed]","level":"CRITICAL","label":"Device ID links to your hardware","category":"Device",
         "title":"DEVICE EXPOSED — EMAIL SIGNATURE","explanation":"'Sent from iPhone' is auto-appended by iOS Mail. 'NSA-issued' identifies EXACTLY which hardware asset sent this message.\n\n✓ FIX: Disable automatic device signatures. Never use government hardware for sensitive communications."},
        {"id":"location_body","dangerous":"my apartment in Honolulu, Hawaii","safe":"[location removed]","level":"CRITICAL","label":"Real location in message body","category":"Location",
         "title":"LOCATION EXPOSED — MESSAGE BODY","explanation":"Mentioning your physical city and state is one of the most dangerous OpSec mistakes. Combined with employer name, this gives investigators your home address.\n\n✓ FIX: Never mention any physical location in sensitive communications."},
        {"id":"signature","dangerous":"Best, Edward","safe":"— (no signature)","level":"HIGH","label":"First name confirms identity","category":"Identity",
         "title":"IDENTITY CONFIRMED — SIGNATURE","explanation":"Signing with your real first name, combined with NSA email and Honolulu location, creates a complete identity confirmation.\n\n✓ FIX: Never sign anonymous communications with any real name. Use a pre-agreed codename."},
        {"id":"attachment","dangerous":"PRISM_full_slides_FINAL_v2.pdf | Author: E. Snowden, NSA","safe":"document.pdf [Metadata stripped]","level":"CRITICAL","label":"File contains embedded author metadata","category":"Files",
         "title":"METADATA IN FILE — ATTACHMENT","explanation":"Every PDF contains hidden metadata: author name, company, creation date. Your name is literally written INSIDE the file.\n\n✓ FIX: Use a metadata stripping tool (MAT2 / ExifTool) before sending. Rename the file to something generic."},
        {"id":"routing","dangerous":"Sent via NSA internal mail relay. ID: NSA-HIFO-2847","safe":"[Headers stripped / sent via TOR]","level":"HIGH","label":"Server header reveals mail infrastructure","category":"Infra",
         "title":"INFRASTRUCTURE EXPOSED — MAIL RELAY","explanation":"Email routing headers reveal which mail server sent your message. 'NSA internal mail relay' confirms the sender works at the NSA.\n\n✓ FIX: Route emails through TOR and use a provider that strips routing headers (ProtonMail, Tutanota)."},
    ]

    ctm_categories = ["Identity","Network","History","Device","Location","Files","Infra"]

    ctm_state = {"cleaned":[],"selected":None,"phase":"playing","log_lines":[]}

    def ctm_reset():
        ctm_state["cleaned"] = []
        ctm_state["selected"] = None
        ctm_state["phase"] = "playing"
        ctm_state["log_lines"] = ["> Scanning message...","> 8 vulnerabilities detected","> CRITICAL: Message NOT safe"]

    def ctm_is_cleaned(tid):
        return tid in ctm_state["cleaned"]

    def ctm_get_threat(tid):
        for t in ctm_threats:
            if t["id"] == tid:
                return t
        return None

    def ctm_select(tid):
        if tid in ctm_state["cleaned"]:
            return
        ctm_state["selected"] = tid
        t = ctm_get_threat(tid)
        if t:
            ctm_state["log_lines"].append("> Analyzing: " + t["label"])
        renpy.restart_interaction()

    def ctm_clean():
        tid = ctm_state["selected"]
        if tid is None or tid in ctm_state["cleaned"]:
            return
        ctm_state["cleaned"].append(tid)
        t = ctm_get_threat(tid)
        if t:
            ctm_state["log_lines"].append("> CLEANED: " + t["label"])
        ctm_state["selected"] = None
        if len(ctm_state["cleaned"]) >= 8:
            ctm_state["phase"] = "complete"
            ctm_state["log_lines"].append("> ALL THREATS NEUTRALIZED")
        renpy.restart_interaction()

    def ctm_dismiss():
        ctm_state["selected"] = None
        renpy.restart_interaction()

    def ctm_remaining():
        return 8 - len(ctm_state["cleaned"])

    def ctm_level():
        r = ctm_remaining()
        if r >= 7: return "CRITICAL"
        if r >= 5: return "HIGH"
        if r >= 3: return "MEDIUM"
        if r >= 1: return "LOW"
        return "SECURE"

    def ctm_level_color():
        return {"CRITICAL":"#FF3355","HIGH":"#FF8C00","MEDIUM":"#FFD700","LOW":"#00D4FF","SECURE":"#00FF88"}.get(ctm_level(),"#FF3355")

    def ctm_cat_status(cat):
        for t in ctm_threats:
            if t["category"] == cat and t["id"] not in ctm_state["cleaned"]:
                return "EXPOSED"
        return "SECURED"

    def ctm_cat_color(cat):
        return "#FF3355" if ctm_cat_status(cat) == "EXPOSED" else "#00FF88"


# ── ATL Transforms ──

transform ctm_threat_glow:
    alpha 0.85
    linear 0.8 alpha 1.0
    linear 0.8 alpha 0.85
    repeat

transform ctm_scanner_pulse:
    alpha 0.6
    linear 1.2 alpha 1.0
    linear 1.2 alpha 0.6
    repeat

transform ctm_explain_enter:
    yoffset 40 alpha 0.0
    ease 0.3 yoffset 0 alpha 1.0

transform ctm_clean_flash:
    alpha 0.0 zoom 0.95
    ease 0.2 alpha 1.0 zoom 1.0

transform ctm_bar_pulse:
    alpha 0.7
    linear 1.0 alpha 1.0
    linear 1.0 alpha 0.7
    repeat


# ── Helper screen: single email field row ──

screen ctm_field(label, threat_id=None, static_value=""):
    hbox:
        spacing 12
        ysize 28
        text label style "ctm_field_label" yalign 0.5 xsize 90

        if threat_id is not None:
            if ctm_is_cleaned(threat_id):
                $ _cv = ctm_get_threat(threat_id)["safe"]
                text "[_cv]" style "ctm_cleaned_text" yalign 0.5
            else:
                $ _dv = ctm_get_threat(threat_id)["dangerous"]
                textbutton "[_dv]":
                    style "ctm_threat"
                    text_style "ctm_threat_text"
                    yalign 0.5
                    action Function(ctm_select, threat_id)
                    at ctm_threat_glow
        else:
            text static_value style "ctm_field_value" yalign 0.5


# ── Helper screen: threat inline in body ──

screen ctm_body_threat(threat_id):
    if ctm_is_cleaned(threat_id):
        $ _cv = ctm_get_threat(threat_id)["safe"]
        text "[_cv]" style "ctm_cleaned_text"
    else:
        $ _dv = ctm_get_threat(threat_id)["dangerous"]
        textbutton "[_dv]":
            style "ctm_threat"
            text_style "ctm_threat_text"
            action Function(ctm_select, threat_id)
            at ctm_threat_glow


# ══════════════════════════════════════════════════════════════
#  MAIN GAME SCREEN
# ══════════════════════════════════════════════════════════════

screen minigame_clean_message():
    modal True
    on "show" action Function(ctm_reset)

    default time_left = 300

    if ctm_state["phase"] == "playing" and time_left > 0:
        timer 1.0 repeat True action SetScreenVariable("time_left", max(0, time_left - 1))

    add "#07090F"

    add "images/logo.png":
        xalign 0.5
        yalign 0.5
        alpha 0.15
        fit "contain"
        xsize 900
        ysize 900

    # ── TOP BAR ──
    $ _ctm_rem = ctm_remaining()
    $ _ctm_cleaned = len(ctm_state["cleaned"])
    $ _ctm_mins = time_left // 60
    $ _ctm_secs = time_left % 60
    $ _ctm_lvl = ctm_level()
    $ _ctm_lvl_col = ctm_level_color()

    frame:
        xpos 52 ypos 16 xsize 1540 ysize 56
        background Solid("#0C1018F0")
        padding (24, 10)

        hbox:
            xfill True
            text "// CLEAN THE MESSAGE //" color "#00D4FF" size 20 bold True font "DejaVuSans.ttf" yalign 0.5
            hbox:
                spacing 28 xalign 1.0
                text "Threats: [_ctm_cleaned]/8" color "#D8E4F0" size 17 bold True font "DejaVuSans.ttf" yalign 0.5
                text "Risk: [_ctm_lvl]" color _ctm_lvl_col size 17 bold True font "DejaVuSans.ttf" yalign 0.5
                text "[_ctm_mins]:[_ctm_secs:02d]" color ("#FF3355" if time_left <= 30 else "#FFD700" if time_left <= 60 else "#00D4FF") size 17 bold True font "DejaVuSans.ttf" yalign 0.5

    # ── LEFT PANEL: EMAIL CLIENT ──
    frame:
        xpos 52 ypos 86 xsize 1150 ysize 680
        background Solid("#0E1520")
        padding (0, 0)

        vbox:
            # Email header
            frame:
                xfill True
                background Solid("#111520")
                padding (20, 14)

                vbox:
                    spacing 6
                    text "✉  COMPOSE: DRAFT" color "#00D4FF" size 16 bold True font "DejaVuSans.ttf"
                    add Solid("#00D4FF20") xsize 1110 ysize 1
                    null height 4
                    use ctm_field("FROM:", threat_id="from_email")
                    use ctm_field("TO:", static_value="glenn.greenwald@theguardian.com")
                    use ctm_field("CC:", threat_id="cc_field")
                    use ctm_field("SUBJECT:", threat_id="subject_line")
                    use ctm_field("DATE:", static_value="Mon, 13 May 2013, 09:42 +0800")
                    use ctm_field("DEVICE:", threat_id="device_sig")

            # Email body
            viewport:
                xfill True ysize 405
                scrollbars "vertical"
                mousewheel True

                frame:
                    xfill True
                    background Solid("#0E1520")
                    padding (24, 18)

                    vbox:
                        spacing 6

                        text "Glenn," style "ctm_body_text"
                        null height 6
                        text "I am writing to you from" style "ctm_body_text"
                        use ctm_body_threat("location_body")
                        text "I have been working at the NSA's Oahu facility for the past eight months as a Booz Allen Hamilton contractor. I have access to a large volume of classified documents." style "ctm_body_text"
                        null height 6
                        text "I want to share something with you — something that the American public has a right to know. Please review the attached file." style "ctm_body_text"
                        null height 6
                        use ctm_body_threat("signature")

                        null height 12
                        add Solid("#5A708040") xsize 800 ysize 1

                        null height 8
                        text "📎 ATTACHMENT:" color "#5A7080" size 14 bold True font "DejaVuSans.ttf"
                        use ctm_body_threat("attachment")

                        null height 12
                        add Solid("#5A708040") xsize 800 ysize 1

                        null height 8
                        text "ROUTING INFO:" color "#5A7080" size 14 bold True font "DejaVuSans.ttf"
                        use ctm_body_threat("routing")

    # ── RIGHT PANEL: NSA THREAT SCANNER ──
    frame:
        xpos 1218 ypos 86 xsize 650 ysize 680
        background Solid("#161C28")
        padding (22, 18)

        vbox:
            spacing 12

            text "📡  NSA INTERCEPT RISK" color "#FF3355" size 18 bold True font "DejaVuSans.ttf" xalign 0.5 at ctm_scanner_pulse

            # Threat level bar
            frame:
                xfill True ysize 60
                background Solid("#0C1018")
                padding (16, 10)

                vbox:
                    spacing 6
                    text "THREAT LEVEL: [_ctm_lvl]" color _ctm_lvl_col size 20 bold True font "DejaVuSans.ttf" xalign 0.5

                    frame:
                        xfill True ysize 10
                        background Solid("#1A1A2E")
                        padding (0, 0)

                        frame:
                            xsize int(586 * ctm_remaining() / 8.0)
                            ysize 10
                            background _ctm_lvl_col
                            at ctm_bar_pulse

            null height 4

            # Category scan results
            text "SCAN RESULTS:" color "#5A7080" size 14 bold True font "DejaVuSans.ttf"

            for _cat in ctm_categories:
                $ _cat_st = ctm_cat_status(_cat)
                $ _cat_col = ctm_cat_color(_cat)
                hbox:
                    xfill True
                    text "> [_cat]:" color "#5A7080" size 15 font "DejaVuSans.ttf" yalign 0.5
                    text "[_cat_st]" color _cat_col size 15 bold True font "DejaVuSans.ttf" xalign 1.0 yalign 0.5

            null height 8
            add Solid("#00D4FF20") xsize 606 ysize 1

            # Threat log
            text "⬡  THREAT LOG  ⬡" color "#00D4FF" size 16 bold True font "DejaVuSans.ttf"

            viewport:
                xfill True ysize 200
                scrollbars "vertical"
                mousewheel True

                vbox:
                    spacing 3
                    $ _log = ctm_state.get("log_lines", [])[-12:]
                    for _line in _log:
                        text "[_line]" color "#5A7080" size 13 font "DejaVuSans.ttf"

    # ── EXPLANATION PANEL (when threat selected) ──
    if ctm_state["selected"] is not None and ctm_state["phase"] == "playing":
        $ _sel = ctm_get_threat(ctm_state["selected"])
        if _sel is not None:
            frame at ctm_explain_enter:
                xpos 52 ypos 780 xsize 1816 ysize 240
                background Solid("#0C1018F8")
                padding (28, 18)

                hbox:
                    spacing 24

                    # Explanation text
                    vbox:
                        xsize 1350
                        spacing 8

                        $ _sel_lvl = _sel["level"]
                        $ _sel_col = "#FF3355" if _sel_lvl == "CRITICAL" else "#FF8C00"
                        hbox:
                            spacing 12
                            text "⚠ [_sel['title']]" color _sel_col size 20 bold True font "DejaVuSans.ttf"
                            text "[_sel_lvl]" color _sel_col size 14 bold True font "DejaVuSans.ttf" yalign 0.5

                        $ _sel_exp = _sel["explanation"]
                        text "[_sel_exp]" color "#B8C8D8" size 15 font "DejaVuSans.ttf" line_spacing 3

                    # Action buttons
                    vbox:
                        xsize 380
                        yalign 0.5
                        spacing 14

                        textbutton "> CLEAN THIS THREAT":
                            style "modal_action_button"
                            xsize 340
                            text_style "modal_action_button_text"
                            xalign 1.0
                            action Function(ctm_clean)

                        textbutton "> DISMISS":
                            xalign 0.5
                            text_color "#5A7080"
                            text_hover_color "#D8E4F0"
                            text_size 16
                            action Function(ctm_dismiss)

    # ── COMPLETE / TIME UP OVERLAY ──
    if ctm_state["phase"] == "complete" or (time_left <= 0 and ctm_state["phase"] == "playing"):
        $ _ctm_score = len(ctm_state["cleaned"])
        $ _ctm_passed = _ctm_score >= 4
        add "#07090FDD"

        frame:
            xalign 0.5 yalign 0.5 xsize 900 ysize 520
            background Solid("#0C1018F8")
            padding (40, 34)

            vbox:
                xalign 0.5 yalign 0.5
                spacing 16

                if ctm_state["phase"] == "complete":
                    text "// TRANSMISSION SECURE //" color "#00FF88" size 32 bold True xalign 0.5 font "DejaVuSans.ttf"
                    text "All 8 threats neutralized. The message is safe to send." color "#D8E4F0" size 20 xalign 0.5 text_align 0.5
                elif time_left <= 0:
                    text "// TIME EXPIRED //" color "#FF3355" size 32 bold True xalign 0.5 font "DejaVuSans.ttf"
                    text "You cleaned [_ctm_score] of 8 threats before time ran out." color "#D8E4F0" size 20 xalign 0.5 text_align 0.5

                null height 8

                text "THREATS CLEANED: [_ctm_score] / 8" color "#FFD700" size 24 bold True xalign 0.5 font "DejaVuSans.ttf"

                null height 4

                frame:
                    xalign 0.5 xsize 760
                    background Solid("#111520")
                    padding (24, 18)

                    vbox:
                        spacing 4
                        text "⬡  WHAT YOU LEARNED  ⬡" color "#00D4FF" size 18 bold True font "DejaVuSans.ttf"
                        null height 4
                        text "Every digital message carries hidden metadata — sender address, device info, routing headers, file authorship — that can expose your identity even if the content is encrypted." color "#B8C8D8" size 15 font "DejaVuSans.ttf"
                        null height 4
                        text "Real whistleblowers and journalists strip ALL identifying traces before communicating. Tools like TOR, ProtonMail, and metadata strippers (MAT2, ExifTool) are essential for operational security." color "#B8C8D8" size 15 font "DejaVuSans.ttf"

                null height 8

                textbutton "> CONTINUE MISSION":
                    style "modal_action_button"
                    text_style "modal_action_button_text"
                    xalign 0.5
                    action Return(_ctm_score)
