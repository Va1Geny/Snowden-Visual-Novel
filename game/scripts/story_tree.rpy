################################################################################
## STORY_TREE.RPY — Story Flowchart Screen (Detroit: Become Human Style)
## Classified: The Snowden Files
################################################################################

init python:
    # ── Helper functions ─────────────────────────────────────────────────────

    def _ch():
        """How many chapters have been reached."""
        return getattr(persistent, 'tree_ch_reached', 0)

    def _cv(var):
        return getattr(persistent, var, '')

    def _finished(ch):
        """Check if a chapter is finished."""
        if getattr(persistent, 'tree_ending', '') != "":
            if ch <= _ch():
                return True
        if ch < 5:
            return _ch() > ch
        return False

    def _uv(var):
        return list(getattr(persistent, var + "_unlocked", []) or [])

    def _is_active(var, val):
        return _cv(var) == val

    def _is_unlocked(var, val):
        return tree_choice_is_unlocked(var, val)

    def picked_count():
        return tree_unlocked_choice_count()

    def progress_pct():
        total = tree_total_choice_count()
        return int((float(picked_count()) / total) * 100) if total else 0

    # Node background color
    def nbg(var, val, ch):
        if not _finished(ch):
            return "#1A1D2D" # Locked look until chapter is finished
        if _is_active(var, val):
            return "#002922"
        if _is_unlocked(var, val):
            return "#191C31"
        return "#131421"

    # Node text color
    def ntc(var, val, ch):
        if not _finished(ch):
            return "#40466D" # Locked text until finished
        if _is_active(var, val):
            return "#F2FFFC"
        if _is_unlocked(var, val):
            return "#C9D0F3"
        return "#AAB0D6"

    # Node bold
    def nbd(var, val, ch):
        return _finished(ch) and _is_active(var, val)

    # Line / connector color
    def lnc(var, val, ch):
        if not _finished(ch):
            return "#20253D"
        if _is_active(var, val):
            return "#008069"
        if _is_unlocked(var, val):
            return "#4D5186"
        return "#20253D"

    # Chapter-wide stem color (becomes teal once chapter is finished)
    def stc(ch):
        return "#006654" if _finished(ch) else "#20253D"

    # Chapter title text color (bright once finished)
    def chc(ch):
        return "#EAF4F1" if _finished(ch) else "#52597F"

    # ── Ending label ─────────────────────────────────────────────────────────
    _ending_labels = {
        'hero':       'THE HERO',
        'fugitive':   'THE FUGITIVE',
        'imprisoned': 'IMPRISONED',
        'silenced':   'SILENCED',
        'betrayed':   'BETRAYED',
    }
    def ending_label():
        e = getattr(persistent, 'tree_ending', '')
        return _ending_labels.get(e, 'CLASSIFIED')

    def ending_color():
        e = getattr(persistent, 'tree_ending', '')
        if e == 'hero':
            return "#008069"
        if e in ('fugitive',):
            return "#8B8FCC"
        return "#D86C8A"

    def ending_panel_bg(code):
        if _ch() < 5:
            return "#131421"
        if getattr(persistent, 'tree_ending', '') == code:
            return "#002922"
        if tree_ending_is_unlocked(code):
            return "#191C31"
        return "#131421"


################################################################################
## STORY TREE SCREEN
## Canvas: 1800 px wide. Two-choice nodes: left center x=500, right x=1300.
## Three-choice nodes: left x=280, centre x=900, right x=1520.
################################################################################

screen story_tree():
    tag menu

    ## ── Background ──────────────────────────────────────────────────────────
    add "#131421"
    add "logo_watermark"

    ## ── Top header bar ──────────────────────────────────────────────────────
    frame:
        xfill True
        ypos 0
        ysize 96
        background "#0C111CEB"
        padding (54, 0)

        hbox:
            xfill True
            yalign 0.5
            spacing 28

            vbox:
                yalign 0.5
                spacing 3

                text "BRANCH NETWORK":
                    style "tree_hud_kicker"

                text "STORY TREE":
                    color "#EAF4F1"
                    size 32
                    bold True

            frame:
                yalign 0.5
                xsize 2
                ysize 42
                background "#1F2A48"

            vbox:
                yalign 0.5
                spacing 4

                text "VISUAL ANALYSIS":
                    color "#8B8FCC"
                    size 14
                    bold True

                text "Track every major choice, risk, and ending route in one cinematic branch web.":
                    color "#AAB0D6"
                    size 16

            null width 190

            frame:
                xalign 1.0
                yalign 0.5
                xsize 460
                background "#111728"
                padding (18, 12)

                hbox:
                    xfill True
                    spacing 24

                    vbox:
                        spacing 3
                        text "CHAPTERS":
                            style "tree_hud_kicker"
                        text "[_ch()]/5":
                            style "tree_hud_value"
                        text "Unlocked nodes by chapter":
                            style "tree_hud_meta"

                    vbox:
                        spacing 3
                        text "BRANCHES":
                            style "tree_hud_kicker"
                        text "[picked_count()]/[tree_total_choice_count()]":
                            style "tree_hud_value"
                        text "Discovered across all runs":
                            style "tree_hud_meta"

    ## ── Legend ──────────────────────────────────────────────────────────────
    frame:
        xpos 72
        ypos 120
        xsize 420
        background "#0D1322D8"
        padding (18, 16)

        vbox:
            spacing 14

            hbox:
                spacing 14

                vbox:
                    spacing 3
                    text "NETWORK LEGEND":
                        style "tree_hud_kicker"
                    text "[progress_pct()]% reconstructed":
                        color "#EAF4F1"
                        size 22
                        bold True

                frame:
                    xalign 1.0
                    yalign 0.5
                    xsize 120
                    ysize 8
                    background "#20253D"

                    frame:
                        xsize max(12, int(120 * progress_pct() / 100.0))
                        yfill True
                        background "#008069"

            hbox:
                spacing 20

                hbox:
                    spacing 8
                    frame:
                        xsize 14
                        ysize 14
                        background "#006654"
                        yalign 0.5
                    text "CURRENT RUN":
                        color "#EAF4F1"
                        size 13
                        yalign 0.5

                hbox:
                    spacing 8
                    frame:
                        xsize 14
                        ysize 14
                        background "#191C31"
                        yalign 0.5
                    text "DISCOVERED BRANCH":
                        color "#AAB0D6"
                        size 13
                        yalign 0.5

                hbox:
                    spacing 8
                    frame:
                        xsize 14
                        ysize 14
                        background "#131421"
                        yalign 0.5
                    text "LOCKED":
                        color "#6A719A"
                        size 13
                        yalign 0.5

    frame:
        xalign 1.0
        ypos 120
        xoffset -92
        xsize 360
        background "#0D1322D8"
        padding (18, 16)

        vbox:
            spacing 10

            text "ENDING FORECAST":
                style "tree_hud_kicker"

            text "[ending_label()]":
                color (ending_color() if _ch() >= 5 else "#EAF4F1")
                size 24
                bold True

            text ("Ending is locked until chapter 5 is reached." if _ch() < 5 else "Forecast updated from your current branch selections."):
                color "#AAB0D6"
                size 15
                xmaximum 360

    ## ── Scrollable tree canvas ──────────────────────────────────────────────
    viewport:
        id "story_tree_vp"
        xpos 72
        ypos 214
        xsize 1756
        ysize 760
        scrollbars "vertical"
        mousewheel True
        draggable True

        vbox:
            xalign 0.5
            xsize 1800
            spacing 0
            yoffset 26

            ##################################################################
            ## CHAPTER 1 — INSIDE THE MACHINE
            ##################################################################

            # Chapter header
            fixed:
                xsize 1800
                ysize 74

                frame:
                    xpos 600
                    ypos 0
                    xsize 600
                    ysize 56
                    background "#171B31"
                    padding (15, 0)

                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 14

                        text "CH.01":
                            color ("#4D518655" if not _finished(1) else "#8B8FCC")
                            size 13
                            bold True
                            yalign 0.5

                        text "INSIDE THE MACHINE":
                            color chc(1)
                            size 19
                            bold True
                            yalign 0.5

                # Stem going down
                add Solid(stc(1)):
                    xpos 899
                    ypos 56
                    xsize 2
                    ysize 18

            # ── Choice 1-1: Follow Protocol vs Explore Files ─────────────
            # Splitter
            fixed:
                xsize 1800
                ysize 38

                add Solid("#232843"):
                    xpos 500
                    ypos 14
                    xsize 800
                    ysize 2

                add Solid(lnc('choice_ch1_1', 'protocol', 1)):
                    xpos 499
                    ypos 14
                    xsize 2
                    ysize 24

                add Solid(lnc('choice_ch1_1', 'explore', 1)):
                    xpos 1299
                    ypos 14
                    xsize 2
                    ysize 24

            # Nodes
            fixed:
                xsize 1800
                ysize 72

                button:
                    xpos 340
                    ypos 5
                    xsize 320
                    ysize 55
                    background nbg('choice_ch1_1', 'protocol', 1)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (10, 5)
                    action If(_finished(1), Start("chapter_1"), NullAction())

                    text "Follow Protocol":
                        color ntc('choice_ch1_1', 'protocol', 1)
                        size 16
                        bold (nbd('choice_ch1_1', 'protocol', 1))
                        xalign 0.5
                        yalign 0.5

                button:
                    xpos 1140
                    ypos 5
                    xsize 320
                    ysize 55
                    background nbg('choice_ch1_1', 'explore', 1)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (10, 5)
                    action If(_finished(1), Start("chapter_1"), NullAction())

                    text "Explore Restricted Files":
                        color ntc('choice_ch1_1', 'explore', 1)
                        size 15
                        bold (nbd('choice_ch1_1', 'explore', 1))
                        xalign 0.5
                        yalign 0.5

                # Stub lines going down
                add Solid(lnc('choice_ch1_1', 'protocol', 1)):
                    xpos 499
                    ypos 60
                    xsize 2
                    ysize 12

                add Solid(lnc('choice_ch1_1', 'explore', 1)):
                    xpos 1299
                    ypos 60
                    xsize 2
                    ysize 12

            # Merger → stem to Choice 1-2
            fixed:
                xsize 1800
                ysize 40

                add Solid(lnc('choice_ch1_1', 'protocol', 1)):
                    xpos 500
                    ypos 18
                    xsize 400
                    ysize 2

                add Solid(lnc('choice_ch1_1', 'explore', 1)):
                    xpos 900
                    ypos 18
                    xsize 400
                    ysize 2

                add Solid(stc(1)):
                    xpos 899
                    ypos 18
                    xsize 2
                    ysize 22

            # ── Choice 1-2: Report Anomaly vs Stay Silent ─────────────────
            # Splitter
            fixed:
                xsize 1800
                ysize 38

                add Solid("#232843"):
                    xpos 500
                    ypos 14
                    xsize 800
                    ysize 2

                add Solid(lnc('choice_ch1_2', 'report', 1)):
                    xpos 499
                    ypos 14
                    xsize 2
                    ysize 24

                add Solid(lnc('choice_ch1_2', 'silent', 1)):
                    xpos 1299
                    ypos 14
                    xsize 2
                    ysize 24

            # Nodes
            fixed:
                xsize 1800
                ysize 72

                button:
                    xpos 340
                    ypos 5
                    xsize 320
                    ysize 55
                    background nbg('choice_ch1_2', 'report', 1)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (10, 5)
                    action If(_finished(1), Start("chapter_1"), NullAction())

                    text "Report to Inspector General":
                        color ntc('choice_ch1_2', 'report', 1)
                        size 14
                        bold (nbd('choice_ch1_2', 'report', 1))
                        xalign 0.5
                        yalign 0.5

                button:
                    xpos 1140
                    ypos 5
                    xsize 320
                    ysize 55
                    background nbg('choice_ch1_2', 'silent', 1)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (10, 5)
                    action If(_finished(1), Start("chapter_1"), NullAction())

                    text "Stay Silent":
                        color ntc('choice_ch1_2', 'silent', 1)
                        size 16
                        bold (nbd('choice_ch1_2', 'silent', 1))
                        xalign 0.5
                        yalign 0.5

                add Solid(lnc('choice_ch1_2', 'report', 1)):
                    xpos 499
                    ypos 60
                    xsize 2
                    ysize 12

                add Solid(lnc('choice_ch1_2', 'silent', 1)):
                    xpos 1299
                    ypos 60
                    xsize 2
                    ysize 12

            # Merger → bridge to Chapter 2
            fixed:
                xsize 1800
                ysize 52

                add Solid(lnc('choice_ch1_2', 'report', 1)):
                    xpos 500
                    ypos 18
                    xsize 400
                    ysize 2

                add Solid(lnc('choice_ch1_2', 'silent', 1)):
                    xpos 900
                    ypos 18
                    xsize 400
                    ysize 2

                add Solid(stc(2)):
                    xpos 899
                    ypos 18
                    xsize 2
                    ysize 34

            ##################################################################
            ## CHAPTER 2 — THE PRISM REVELATION
            ##################################################################

            fixed:
                xsize 1800
                ysize 74

                frame:
                    xpos 600
                    ypos 0
                    xsize 600
                    ysize 56
                    background "#171B31"
                    padding (15, 0)

                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 14

                        text "CH.02":
                            color ("#4D518655" if not _finished(2) else "#8B8FCC")
                            size 13
                            bold True
                            yalign 0.5

                        text "THE PRISM REVELATION":
                            color chc(2)
                            size 19
                            bold True
                            yalign 0.5

                add Solid(stc(2)):
                    xpos 899
                    ypos 56
                    xsize 2
                    ysize 18

            # ── Choice 2-1: Trust Colleague vs Work Alone ─────────────────
            fixed:
                xsize 1800
                ysize 38

                add Solid("#232843"):
                    xpos 500
                    ypos 14
                    xsize 800
                    ysize 2

                add Solid(lnc('choice_ch2_1', 'trust', 2)):
                    xpos 499
                    ypos 14
                    xsize 2
                    ysize 24

                add Solid(lnc('choice_ch2_1', 'alone', 2)):
                    xpos 1299
                    ypos 14
                    xsize 2
                    ysize 24

            fixed:
                xsize 1800
                ysize 72

                button:
                    xpos 340
                    ypos 5
                    xsize 320
                    ysize 55
                    background nbg('choice_ch2_1', 'trust', 2)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (10, 5)
                    action If(_finished(2), Start("chapter_2"), NullAction())

                    text "Trust the Colleague":
                        color ntc('choice_ch2_1', 'trust', 2)
                        size 16
                        bold (nbd('choice_ch2_1', 'trust', 2))
                        xalign 0.5
                        yalign 0.5

                button:
                    xpos 1140
                    ypos 5
                    xsize 320
                    ysize 55
                    background nbg('choice_ch2_1', 'alone', 2)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (10, 5)
                    action If(_finished(2), Start("chapter_2"), NullAction())

                    text "Work Alone":
                        color ntc('choice_ch2_1', 'alone', 2)
                        size 16
                        bold (nbd('choice_ch2_1', 'alone', 2))
                        xalign 0.5
                        yalign 0.5

                add Solid(lnc('choice_ch2_1', 'trust', 2)):
                    xpos 499
                    ypos 60
                    xsize 2
                    ysize 12

                add Solid(lnc('choice_ch2_1', 'alone', 2)):
                    xpos 1299
                    ypos 60
                    xsize 2
                    ysize 12

            # Merger
            fixed:
                xsize 1800
                ysize 40

                add Solid(lnc('choice_ch2_1', 'trust', 2)):
                    xpos 500
                    ypos 18
                    xsize 400
                    ysize 2

                add Solid(lnc('choice_ch2_1', 'alone', 2)):
                    xpos 900
                    ypos 18
                    xsize 400
                    ysize 2

                add Solid(stc(2)):
                    xpos 899
                    ypos 18
                    xsize 2
                    ysize 22

            # ── Choice 2-2: Copy Files vs Take Notes ─────────────────────
            fixed:
                xsize 1800
                ysize 38

                add Solid("#232843"):
                    xpos 500
                    ypos 14
                    xsize 800
                    ysize 2

                add Solid(lnc('choice_ch2_2', 'copy', 2)):
                    xpos 499
                    ypos 14
                    xsize 2
                    ysize 24

                add Solid(lnc('choice_ch2_2', 'notes', 2)):
                    xpos 1299
                    ypos 14
                    xsize 2
                    ysize 24

            fixed:
                xsize 1800
                ysize 72

                button:
                    xpos 340
                    ypos 5
                    xsize 320
                    ysize 55
                    background nbg('choice_ch2_2', 'copy', 2)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (10, 5)
                    action If(_finished(2), Start("chapter_2"), NullAction())

                    text "Copy Files to Drive":
                        color ntc('choice_ch2_2', 'copy', 2)
                        size 16
                        bold (nbd('choice_ch2_2', 'copy', 2))
                        xalign 0.5
                        yalign 0.5

                button:
                    xpos 1140
                    ypos 5
                    xsize 320
                    ysize 55
                    background nbg('choice_ch2_2', 'notes', 2)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (10, 5)
                    action If(_finished(2), Start("chapter_2"), NullAction())

                    text "Take Notes Only":
                        color ntc('choice_ch2_2', 'notes', 2)
                        size 16
                        bold (nbd('choice_ch2_2', 'notes', 2))
                        xalign 0.5
                        yalign 0.5

                add Solid(lnc('choice_ch2_2', 'copy', 2)):
                    xpos 499
                    ypos 60
                    xsize 2
                    ysize 12

                add Solid(lnc('choice_ch2_2', 'notes', 2)):
                    xpos 1299
                    ypos 60
                    xsize 2
                    ysize 12

            # Merger → bridge to Chapter 3
            fixed:
                xsize 1800
                ysize 52

                add Solid(lnc('choice_ch2_2', 'copy', 2)):
                    xpos 500
                    ypos 18
                    xsize 400
                    ysize 2

                add Solid(lnc('choice_ch2_2', 'notes', 2)):
                    xpos 900
                    ypos 18
                    xsize 400
                    ysize 2

                add Solid(stc(3)):
                    xpos 899
                    ypos 18
                    xsize 2
                    ysize 34

            ##################################################################
            ## CHAPTER 3 — THE CONTACT
            ## 3-choice layout: left x=280, mid x=900, right x=1520
            ##################################################################

            fixed:
                xsize 1800
                ysize 74

                frame:
                    xpos 600
                    ypos 0
                    xsize 600
                    ysize 56
                    background "#171B31"
                    padding (15, 0)

                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 14

                        text "CH.03":
                            color ("#4D518655" if not _finished(3) else "#8B8FCC")
                            size 13
                            bold True
                            yalign 0.5

                        text "THE CONTACT":
                            color chc(3)
                            size 19
                            bold True
                            yalign 0.5

                add Solid(stc(3)):
                    xpos 899
                    ypos 56
                    xsize 2
                    ysize 18

            # ── Choice 3-1: PGP+Tor vs Email vs Wait (3-way) ──────────────
            fixed:
                xsize 1800
                ysize 38

                add Solid("#232843"):
                    xpos 280
                    ypos 14
                    xsize 1240
                    ysize 2

                add Solid(lnc('choice_ch3_1', 'pgp', 3)):
                    xpos 279
                    ypos 14
                    xsize 2
                    ysize 24

                add Solid(lnc('choice_ch3_1', 'email', 3)):
                    xpos 899
                    ypos 14
                    xsize 2
                    ysize 24

                add Solid(lnc('choice_ch3_1', 'wait', 3)):
                    xpos 1519
                    ypos 14
                    xsize 2
                    ysize 24

            fixed:
                xsize 1800
                ysize 78

                button:
                    xpos 130
                    ypos 5
                    xsize 300
                    ysize 60
                    background nbg('choice_ch3_1', 'pgp', 3)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (8, 5)
                    action If(_finished(3), Start("chapter_3"), NullAction())

                    text "PGP + Tor\nSecure Channel":
                        color ntc('choice_ch3_1', 'pgp', 3)
                        size 14
                        bold (nbd('choice_ch3_1', 'pgp', 3))
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

                button:
                    xpos 750
                    ypos 5
                    xsize 300
                    ysize 60
                    background nbg('choice_ch3_1', 'email', 3)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (8, 5)
                    action If(_finished(3), Start("chapter_3"), NullAction())

                    text "Public Email\n(Greenwald)":
                        color ntc('choice_ch3_1', 'email', 3)
                        size 14
                        bold (nbd('choice_ch3_1', 'email', 3))
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

                button:
                    xpos 1370
                    ypos 5
                    xsize 300
                    ysize 60
                    background nbg('choice_ch3_1', 'wait', 3)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (8, 5)
                    action If(_finished(3), Start("chapter_3"), NullAction())

                    text "Wait for\nSafer Moment":
                        color ntc('choice_ch3_1', 'wait', 3)
                        size 14
                        bold (nbd('choice_ch3_1', 'wait', 3))
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

                add Solid(lnc('choice_ch3_1', 'pgp', 3)):
                    xpos 279
                    ypos 65
                    xsize 2
                    ysize 13

                add Solid(lnc('choice_ch3_1', 'email', 3)):
                    xpos 899
                    ypos 65
                    xsize 2
                    ysize 13

                add Solid(lnc('choice_ch3_1', 'wait', 3)):
                    xpos 1519
                    ypos 65
                    xsize 2
                    ysize 13

            # 3-way merger
            fixed:
                xsize 1800
                ysize 40

                add Solid(lnc('choice_ch3_1', 'pgp', 3)):
                    xpos 280
                    ypos 18
                    xsize 620
                    ysize 2

                add Solid(lnc('choice_ch3_1', 'wait', 3)):
                    xpos 900
                    ypos 18
                    xsize 620
                    ysize 2

                add Solid(stc(3)):
                    xpos 899
                    ypos 18
                    xsize 2
                    ysize 22

            # ── Choice 3-2: Tell Everything vs Partial vs Vague (3-way) ───
            fixed:
                xsize 1800
                ysize 38

                add Solid("#232843"):
                    xpos 280
                    ypos 14
                    xsize 1240
                    ysize 2

                add Solid(lnc('choice_ch3_2', 'full', 3)):
                    xpos 279
                    ypos 14
                    xsize 2
                    ysize 24

                add Solid(lnc('choice_ch3_2', 'partial', 3)):
                    xpos 899
                    ypos 14
                    xsize 2
                    ysize 24

                add Solid(lnc('choice_ch3_2', 'vague', 3)):
                    xpos 1519
                    ypos 14
                    xsize 2
                    ysize 24

            fixed:
                xsize 1800
                ysize 78

                button:
                    xpos 130
                    ypos 5
                    xsize 300
                    ysize 60
                    background nbg('choice_ch3_2', 'full', 3)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (8, 5)
                    action If(_finished(3), Start("chapter_3"), NullAction())

                    text "Tell Everything":
                        color ntc('choice_ch3_2', 'full', 3)
                        size 15
                        bold (nbd('choice_ch3_2', 'full', 3))
                        xalign 0.5
                        yalign 0.5

                button:
                    xpos 750
                    ypos 5
                    xsize 300
                    ysize 60
                    background nbg('choice_ch3_2', 'partial', 3)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (8, 5)
                    action If(_finished(3), Start("chapter_3"), NullAction())

                    text "Share Partially":
                        color ntc('choice_ch3_2', 'partial', 3)
                        size 15
                        bold (nbd('choice_ch3_2', 'partial', 3))
                        xalign 0.5
                        yalign 0.5

                button:
                    xpos 1370
                    ypos 5
                    xsize 300
                    ysize 60
                    background nbg('choice_ch3_2', 'vague', 3)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (8, 5)
                    action If(_finished(3), Start("chapter_3"), NullAction())

                    text "Be Vague":
                        color ntc('choice_ch3_2', 'vague', 3)
                        size 15
                        bold (nbd('choice_ch3_2', 'vague', 3))
                        xalign 0.5
                        yalign 0.5

                add Solid(lnc('choice_ch3_2', 'full', 3)):
                    xpos 279
                    ypos 65
                    xsize 2
                    ysize 13

                add Solid(lnc('choice_ch3_2', 'partial', 3)):
                    xpos 899
                    ypos 65
                    xsize 2
                    ysize 13

                add Solid(lnc('choice_ch3_2', 'vague', 3)):
                    xpos 1519
                    ypos 65
                    xsize 2
                    ysize 13

            # 3-way merger → bridge to Chapter 4
            fixed:
                xsize 1800
                ysize 52

                add Solid(lnc('choice_ch3_2', 'full', 3)):
                    xpos 280
                    ypos 18
                    xsize 620
                    ysize 2

                add Solid(lnc('choice_ch3_2', 'vague', 3)):
                    xpos 900
                    ypos 18
                    xsize 620
                    ysize 2

                add Solid(stc(4)):
                    xpos 899
                    ypos 18
                    xsize 2
                    ysize 34

            ##################################################################
            ## CHAPTER 4 — THE ESCAPE
            ##################################################################

            fixed:
                xsize 1800
                ysize 74

                frame:
                    xpos 600
                    ypos 0
                    xsize 600
                    ysize 56
                    background "#171B31"
                    padding (15, 0)

                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 14

                        text "CH.04":
                            color ("#4D518655" if not _finished(4) else "#8B8FCC")
                            size 13
                            bold True
                            yalign 0.5

                        text "THE ESCAPE":
                            color chc(4)
                            size 19
                            bold True
                            yalign 0.5

                add Solid(stc(4)):
                    xpos 899
                    ypos 56
                    xsize 2
                    ysize 18

            # ── Choice 4-1: Hotel Wi-Fi vs Mobile Hotspot ─────────────────
            fixed:
                xsize 1800
                ysize 38

                add Solid("#232843"):
                    xpos 500
                    ypos 14
                    xsize 800
                    ysize 2

                add Solid(lnc('choice_ch4_1', 'hotel', 4)):
                    xpos 499
                    ypos 14
                    xsize 2
                    ysize 24

                add Solid(lnc('choice_ch4_1', 'mobile', 4)):
                    xpos 1299
                    ypos 14
                    xsize 2
                    ysize 24

            fixed:
                xsize 1800
                ysize 72

                button:
                    xpos 340
                    ypos 5
                    xsize 320
                    ysize 55
                    background nbg('choice_ch4_1', 'hotel', 4)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (10, 5)
                    action If(_finished(4), Start("chapter_4"), NullAction())

                    text "Hotel Wi-Fi\nFast but exposed":
                        color ntc('choice_ch4_1', 'hotel', 4)
                        size 13
                        bold (nbd('choice_ch4_1', 'hotel', 4))
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

                button:
                    xpos 1140
                    ypos 5
                    xsize 320
                    ysize 55
                    background nbg('choice_ch4_1', 'mobile', 4)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (10, 5)
                    action If(_finished(4), Start("chapter_4"), NullAction())

                    text "Mobile hotspot\nSlower but safer":
                        color ntc('choice_ch4_1', 'mobile', 4)
                        size 13
                        bold (nbd('choice_ch4_1', 'mobile', 4))
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

                add Solid(lnc('choice_ch4_1', 'hotel', 4)):
                    xpos 499
                    ypos 60
                    xsize 2
                    ysize 12

                add Solid(lnc('choice_ch4_1', 'mobile', 4)):
                    xpos 1299
                    ypos 60
                    xsize 2
                    ysize 12

            # Merger
            fixed:
                xsize 1800
                ysize 40

                add Solid(lnc('choice_ch4_1', 'hotel', 4)):
                    xpos 500
                    ypos 18
                    xsize 400
                    ysize 2

                add Solid(lnc('choice_ch4_1', 'mobile', 4)):
                    xpos 900
                    ypos 18
                    xsize 400
                    ysize 2

                add Solid(stc(4)):
                    xpos 899
                    ypos 18
                    xsize 2
                    ysize 22

            # ── Choice 4-2: Escape Route (5 options, all shown) ───────────
            # Sub-label
            fixed:
                xsize 1800
                ysize 52

                frame:
                    xpos 650
                    ypos 0
                    xsize 500
                    ysize 42
                    background "#171B31"
                    padding (12, 0)

                    text "ESCAPE ROUTE DECISION":
                        color chc(4)
                        size 15
                        bold True
                        xalign 0.5
                        yalign 0.5

                add Solid(stc(4)):
                    xpos 899
                    ypos 42
                    xsize 2
                    ysize 10

            # 5-way splitter (centers at 230, 500, 900, 1300, 1570)
            fixed:
                xsize 1800
                ysize 38

                add Solid("#232843"):
                    xpos 230
                    ypos 14
                    xsize 1340
                    ysize 2

                add Solid(lnc('choice_ch4_2', 'airport', 4)):
                    xpos 229
                    ypos 14
                    xsize 2
                    ysize 24

                add Solid(lnc('choice_ch4_2', 'russia', 4)):
                    xpos 499
                    ypos 14
                    xsize 2
                    ysize 24

                add Solid(lnc('choice_ch4_2', 'ecuador', 4)):
                    xpos 899
                    ypos 14
                    xsize 2
                    ysize 24

                add Solid(lnc('choice_ch4_2', 'embassy', 4)):
                    xpos 1299
                    ypos 14
                    xsize 2
                    ysize 24

                add Solid(lnc('choice_ch4_2', 'stay', 4)):
                    xpos 1569
                    ypos 14
                    xsize 2
                    ysize 24

            # 5 escape nodes
            fixed:
                xsize 1800
                ysize 82

                button:
                    xpos 100
                    ypos 5
                    xsize 260
                    ysize 60
                    background nbg('choice_ch4_2', 'airport', 4)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (8, 5)
                    action If(_finished(4), Start("chapter_4"), NullAction())

                    text "Airport dash\nFast but messy":
                        color ntc('choice_ch4_2', 'airport', 4)
                        size 13
                        bold (nbd('choice_ch4_2', 'airport', 4))
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

                button:
                    xpos 370
                    ypos 5
                    xsize 260
                    ysize 60
                    background nbg('choice_ch4_2', 'russia', 4)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (8, 5)
                    action If(_finished(4), Start("chapter_4"), NullAction())

                    text "Russian consulate\nShelter with strings":
                        color ntc('choice_ch4_2', 'russia', 4)
                        size 12
                        bold (nbd('choice_ch4_2', 'russia', 4))
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

                button:
                    xpos 750
                    ypos 5
                    xsize 300
                    ysize 60
                    background nbg('choice_ch4_2', 'ecuador', 4)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (8, 5)
                    action If(_finished(4), Start("chapter_4"), NullAction())

                    text "Ecuador via Moscow\nStrong asylum play":
                        color ntc('choice_ch4_2', 'ecuador', 4)
                        size 12
                        bold (nbd('choice_ch4_2', 'ecuador', 4))
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

                button:
                    xpos 1170
                    ypos 5
                    xsize 260
                    ysize 60
                    background nbg('choice_ch4_2', 'embassy', 4)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (8, 5)
                    action If(_finished(4), Start("chapter_4"), NullAction())

                    text "European embassy\nLegal, but unlikely":
                        color ntc('choice_ch4_2', 'embassy', 4)
                        size 12
                        bold (nbd('choice_ch4_2', 'embassy', 4))
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

                button:
                    xpos 1440
                    ypos 5
                    xsize 260
                    ysize 60
                    background nbg('choice_ch4_2', 'stay', 4)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (8, 5)
                    action If(_finished(4), Start("chapter_4"), NullAction())

                    text "Stay in Hong Kong\nPrincipled, but risky":
                        color ntc('choice_ch4_2', 'stay', 4)
                        size 12
                        bold (nbd('choice_ch4_2', 'stay', 4))
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

                # Central stub going down
                add Solid(stc(5)):
                    xpos 899
                    ypos 65
                    xsize 2
                    ysize 17

            # Bridge to Chapter 5
            fixed:
                xsize 1800
                ysize 34

                add Solid(stc(5)):
                    xpos 899
                    ypos 0
                    xsize 2
                    ysize 34

            ##################################################################
            ## CHAPTER 5 — PERMANENT RECORD
            ##################################################################

            fixed:
                xsize 1800
                ysize 74

                frame:
                    xpos 600
                    ypos 0
                    xsize 600
                    ysize 56
                    background "#171B31"
                    padding (15, 0)

                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 14

                        text "CH.05":
                            color ("#4D518655" if not _finished(5) else "#8B8FCC")
                            size 13
                            bold True
                            yalign 0.5

                        text "PERMANENT RECORD":
                            color chc(5)
                            size 19
                            bold True
                            yalign 0.5

                add Solid(stc(5)):
                    xpos 899
                    ypos 56
                    xsize 2
                    ysize 18

            # ── Choice 5-1: Encourage vs Caution vs Refuse (3-way) ────────
            fixed:
                xsize 1800
                ysize 38

                add Solid("#232843"):
                    xpos 280
                    ypos 14
                    xsize 1240
                    ysize 2

                add Solid(lnc('choice_ch5_1', 'encourage', 5)):
                    xpos 279
                    ypos 14
                    xsize 2
                    ysize 24

                add Solid(lnc('choice_ch5_1', 'caution', 5)):
                    xpos 899
                    ypos 14
                    xsize 2
                    ysize 24

                add Solid(lnc('choice_ch5_1', 'refuse', 5)):
                    xpos 1519
                    ypos 14
                    xsize 2
                    ysize 24

            fixed:
                xsize 1800
                ysize 78

                button:
                    xpos 130
                    ypos 5
                    xsize 300
                    ysize 60
                    background nbg('choice_ch5_1', 'encourage', 5)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (8, 5)
                    action If(_finished(5), Start("chapter_5"), NullAction())

                    text "Encourage\nNew Leak":
                        color ntc('choice_ch5_1', 'encourage', 5)
                        size 14
                        bold (nbd('choice_ch5_1', 'encourage', 5))
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

                button:
                    xpos 750
                    ypos 5
                    xsize 300
                    ysize 60
                    background nbg('choice_ch5_1', 'caution', 5)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (8, 5)
                    action If(_finished(5), Start("chapter_5"), NullAction())

                    text "Advise Caution\n(Official Channels)":
                        color ntc('choice_ch5_1', 'caution', 5)
                        size 13
                        bold (nbd('choice_ch5_1', 'caution', 5))
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

                button:
                    xpos 1370
                    ypos 5
                    xsize 300
                    ysize 60
                    background nbg('choice_ch5_1', 'refuse', 5)
                    hover_background "#1F2A48"
                    insensitive_background "#131421"
                    padding (8, 5)
                    action If(_finished(5), Start("chapter_5"), NullAction())

                    text "Refuse —\nToo High a Price":
                        color ntc('choice_ch5_1', 'refuse', 5)
                        size 13
                        bold (nbd('choice_ch5_1', 'refuse', 5))
                        xalign 0.5
                        yalign 0.5
                        text_align 0.5

                add Solid(lnc('choice_ch5_1', 'encourage', 5)):
                    xpos 279
                    ypos 65
                    xsize 2
                    ysize 13

                add Solid(lnc('choice_ch5_1', 'caution', 5)):
                    xpos 899
                    ypos 65
                    xsize 2
                    ysize 13

                add Solid(lnc('choice_ch5_1', 'refuse', 5)):
                    xpos 1519
                    ypos 65
                    xsize 2
                    ysize 13

            # Merger → ENDING node
            fixed:
                xsize 1800
                ysize 52

                add Solid(lnc('choice_ch5_1', 'encourage', 5)):
                    xpos 280
                    ypos 18
                    xsize 620
                    ysize 2

                add Solid(lnc('choice_ch5_1', 'refuse', 5)):
                    xpos 900
                    ypos 18
                    xsize 620
                    ysize 2

                add Solid(stc(5)):
                    xpos 899
                    ypos 18
                    xsize 2
                    ysize 34

            ##################################################################
            ## ENDING NODE
            ##################################################################

            fixed:
                xsize 1800
                ysize 80

                frame:
                    xpos 550
                    ypos 0
                    xsize 700
                    ysize 64
                    background ending_panel_bg(getattr(persistent, 'tree_ending', ''))
                    padding (20, 5)

                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 20

                        text "// ENDING:":
                            color ("#8B8FCC" if _ch() >= 5 else "#40466D")
                            size 18
                            bold True
                            yalign 0.5

                        text (ending_label()):
                            color (ending_color() if _ch() >= 5 else "#40466D")
                            size 20
                            bold True
                            yalign 0.5

                        text "//":
                            color ("#8B8FCC" if _ch() >= 5 else "#40466D")
                            size 18
                            bold True
                            yalign 0.5

            # Footer padding
            null height 20

    ## ── Return button ───────────────────────────────────────────────────────
    hbox:
        xalign 0.5
        yalign 1.0
        yoffset -24
        spacing 18

        textbutton "RETURN":
            background "#002922"
            hover_background "#006654"
            text_color "#EAF4F1"
            text_hover_color "#F2FFFC"
            text_size 22
            text_bold True
            xsize 220
            ysize 54
            text_xalign 0.5
            action If(main_menu, true=ShowMenu("main_menu"), false=ShowMenu("pause_hub"))

        textbutton "OPEN ESC MENU":
            background "#171B31"
            hover_background "#4D5186"
            text_color "#EAF4F1"
            text_hover_color "#F2FFFC"
            text_size 22
            text_bold True
            xsize 300
            ysize 54
            text_xalign 0.5
            action ShowMenu("pause_hub")

    key "game_menu" action If(main_menu, true=ShowMenu("main_menu"), false=ShowMenu("pause_hub"))
