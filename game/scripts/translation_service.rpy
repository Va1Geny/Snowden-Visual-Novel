init offset = -2

default translation_language = None
default translation_language_initialized = False
default translation_revision = 0

init python:
    import json
    import os
    import re
    import store

    class TranslationService(object):
        LANGUAGES = {
            None: "English",
            "dutch": "Nederlands",
            "french": "Fran\u00e7ais",
            "ukrainian": "\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430",
        }

        CHANGE_LANGUAGE_MESSAGES = {
            None: "Are you sure you want to change your current language to \"{language}\"?",
            "dutch": "Weet u zeker dat u uw huidige taal wilt wijzigen naar \"{language}\"?",
            "french": "Voulez-vous vraiment changer votre langue actuelle en \"{language}\" ?",
            "ukrainian": "\u0412\u0438 \u0434\u0456\u0439\u0441\u043d\u043e \u0445\u043e\u0447\u0435\u0442\u0435 \u0437\u043c\u0456\u043d\u0438\u0442\u0438 \u0432\u0430\u0448\u0443 \u043f\u043e\u0442\u043e\u0447\u043d\u0443 \u043c\u043e\u0432\u0443 \u043d\u0430 \"{language}\"?",
        }

        def __init__(self):
            self.dialogue = {}
            self.text = {}
            self.templates = {}

        def _sync_voice_mixer(self, lang):
            try:
                preferences.set_mute("voice", lang not in (None, "french", "dutch"))
            except Exception:
                pass

        def current_language(self):
            if not store.translation_language_initialized:
                if not hasattr(persistent, "translation_language"):
                    persistent.translation_language = None
                store.translation_language = persistent.translation_language
                store.translation_language_initialized = True
                self._sync_voice_mixer(store.translation_language)
            return store.translation_language

        def revision(self):
            return store.translation_revision

        def set_language(self, lang):
            store.translation_language = lang
            store.translation_language_initialized = True
            store.translation_revision += 1
            persistent.translation_language = lang
            renpy.save_persistent()
            self.preload_language(lang, force=True)
            self._sync_voice_mixer(lang)
            renpy.restart_interaction()

        def english_voice_enabled(self):
            return self.current_language() is None

        def voice_language(self):
            lang = self.current_language()
            if lang == "french":
                return "fr"
            if lang == "dutch":
                return "nl"
            if lang is None:
                return "en"
            return None

        def preload_language(self, lang, force=False):
            if not lang:
                return

            if force:
                self.dialogue.pop(lang, None)
                self.text.pop(lang, None)
                self.templates.pop(lang, None)

            self.text_catalog(lang)
            self.dialogue_catalog(lang)

        def language_name(self, lang=None, localized=True):
            name = self.LANGUAGES.get(lang, self.LANGUAGES[None])
            return self.ui(name) if localized else name

        def _translation_path(self, lang, filename):
            return os.path.join(config.gamedir, "tl", lang, filename)

        def _load_json(self, lang, filename):
            if not lang:
                return {}

            path = self._translation_path(lang, filename)
            if not os.path.exists(path):
                return {}

            try:
                with open(path, "r", encoding="utf-8") as fp:
                    raw = json.load(fp)
            except Exception:
                return {}

            if hasattr(raw, "items"):
                return {
                    src: tr
                    for src, tr in raw.items()
                    if isinstance(src, str) and isinstance(tr, str) and src and tr
                }

            data = {}
            if hasattr(raw, "__iter__"):
                for entry in raw:
                    if hasattr(entry, "get") and isinstance(entry.get("text"), str) and isinstance(entry.get("tr"), str):
                        data[entry["text"]] = entry["tr"]
            return data

        def _compile_templates(self, data):
            exact = {}
            templates = []

            for src, tr in data.items():
                if "[" in src and "]" in src:
                    placeholders = re.findall(r"(\[[^\]]+\])", src)
                    parts = re.split(r"(\[[^\]]+\])", src)
                    pattern = "^"

                    for part in parts:
                        if not part:
                            continue
                        if re.match(r"\[[^\]]+\]", part):
                            pattern += "(.+?)"
                        else:
                            pattern += re.escape(part)

                    pattern += "$"
                    templates.append((re.compile(pattern), placeholders, tr))
                else:
                    exact[src] = tr

            templates.sort(key=lambda item: len(item[0].pattern), reverse=True)
            return exact, templates

        def text_catalog(self, lang):
            if not lang:
                return {}

            if lang not in self.text:
                exact, templates = self._compile_templates(self._load_json(lang, "text.json"))
                self.text[lang] = exact
                self.templates[lang] = templates

            return self.text[lang]

        def dialogue_catalog(self, lang):
            if not lang:
                return {}

            if lang not in self.dialogue:
                self.dialogue[lang] = self._load_json(lang, "dialogue.json")

            return self.dialogue[lang]

        def _translate_template(self, source, lang, depth):
            if depth > 3:
                return source

            self.text_catalog(lang)
            for pattern, placeholders, translated_template in self.templates.get(lang, []):
                match = pattern.match(source)
                if not match:
                    continue

                result = translated_template
                for index, placeholder in enumerate(placeholders, 1):
                    result = result.replace(placeholder, self.ui(match.group(index), lang, depth + 1))
                return result

            return source

        def ui(self, source, lang=None, depth=0):
            if not source:
                return source

            self.revision()

            if lang is None:
                lang = self.current_language()

            if not lang:
                return source

            catalog = self.text_catalog(lang)
            if source in catalog:
                return catalog[source]

            return self._translate_template(source, lang, depth)

        def dialogue_line(self, source, lang=None):
            if not source:
                return source

            self.revision()

            if lang is None:
                lang = self.current_language()

            if not lang:
                return source

            catalog = self.dialogue_catalog(lang)
            if source in catalog:
                return catalog[source]

            return self.ui(source, lang)

        def say_menu_text_filter(self, source):
            return self.dialogue_line(source)

        def rich_dialogue(self, source):
            result = self.dialogue_line(source)

            try:
                terms = sorted(IMPORTANT_TERMS, key=len, reverse=True)
            except Exception:
                terms = []

            for term in terms:
                pattern = re.compile(r"(?<!\{b\})\b(%s)\b(?!\{/b\})" % re.escape(term), re.IGNORECASE)
                result = pattern.sub(lambda match: "{b}%s{/b}" % match.group(1), result)

            return result

        def change_language_message(self, target_lang):
            current_lang = self.current_language()
            template = self.CHANGE_LANGUAGE_MESSAGES.get(current_lang, self.CHANGE_LANGUAGE_MESSAGES[None])
            return template.format(language=self.language_name(target_lang))

        def change_language_action(self, target_lang):
            if self.current_language() == target_lang:
                return NullAction()
            return Confirm(
                self.change_language_message(target_lang),
                Function(self.set_language, target_lang),
                NullAction()
            )

    translation_service = TranslationService()

    def t(source, lang=None):
        return translation_service.ui(source, lang)

    def td(source, lang=None):
        return translation_service.dialogue_line(source, lang)

    def trich(source):
        return translation_service.rich_dialogue(source)

    def localized_language_name(lang):
        return translation_service.language_name(lang)

    def language_change_action(target_lang):
        return translation_service.change_language_action(target_lang)

    def current_translation_language():
        return translation_service.current_language()

    def set_translation_language(lang):
        return translation_service.set_language(lang)

    def should_play_english_voice():
        return translation_service.english_voice_enabled()

    def current_voice_language():
        return translation_service.voice_language()

    config.say_menu_text_filter = translation_service.say_menu_text_filter
