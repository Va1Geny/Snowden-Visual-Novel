################################################################################
## TRANSLATION_SERVICE.RPY — Single Runtime Translation Layer
## Classified: The Snowden Files
################################################################################

init offset = -2

init python:
    import json
    import os
    import re

    class TranslationService(object):
        LANGUAGES = {
            None: "English",
            "dutch": "Nederlands",
            "french": "Français",
            "ukrainian": "Українська",
        }

        CHANGE_LANGUAGE_MESSAGES = {
            None: "Are you sure you want to change your current language to \"{language}\"?",
            "dutch": "Weet u zeker dat u uw huidige taal wilt wijzigen naar \"{language}\"?",
            "french": "Voulez-vous vraiment changer votre langue actuelle en « {language} » ?",
            "ukrainian": "Ви дійсно хочете змінити вашу поточну мову на «{language}»?",
        }

        def __init__(self):
            self.dialogue = {}
            self.text = {}
            self.templates = {}

        def current_language(self):
            try:
                return _preferences.language
            except Exception:
                return None

        def language_name(self, lang=None, localized=True):
            name = self.LANGUAGES.get(lang, self.LANGUAGES[None])
            if localized:
                return self.ui(name)
            return name

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

            if isinstance(raw, dict):
                return {
                    src: tr
                    for src, tr in raw.items()
                    if isinstance(src, str) and isinstance(tr, str) and src and tr
                }

            data = {}
            if isinstance(raw, list):
                for entry in raw:
                    if isinstance(entry, dict) and isinstance(entry.get("text"), str) and isinstance(entry.get("tr"), str):
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

            if lang is None:
                lang = self.current_language()

            if not lang:
                return source

            catalog = self.dialogue_catalog(lang)
            if source in catalog:
                return catalog[source]

            return self.ui(source, lang)

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
            return Confirm(self.change_language_message(target_lang), Language(target_lang), NullAction())

    translation_service = TranslationService()

    def t(source, lang=None):
        return translation_service.ui(source, lang)

    def td(source, lang=None):
        return translation_service.dialogue_line(source, lang)

    def trich(source):
        return translation_service.rich_dialogue(source)

    # Backward-compatible names used by existing screens.
    def _translate_display_text(text, lang=None, depth=0):
        return translation_service.ui(text, lang, depth)

    def translated_dialogue(text):
        return translation_service.dialogue_line(text)

    def highlighted_dialogue(text):
        return translation_service.rich_dialogue(text)

    def localized_language_name(lang):
        return translation_service.language_name(lang)

    def language_change_message(target_lang):
        return translation_service.change_language_message(target_lang)

    def language_change_action(target_lang):
        return translation_service.change_language_action(target_lang)

    config.say_menu_text_filter = highlighted_dialogue
    config.replace_text = _translate_display_text
