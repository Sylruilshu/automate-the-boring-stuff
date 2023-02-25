import re


sentence = " string is a string "
char_to_remove = ""


def regex_strip_method(sentence: str, char_to_remove: str | None = None) -> str:

    if char_to_remove == None or char_to_remove == "":
        word_detector = re.compile(
            r"""
            (\s+)?          # Optional whitespace group at the start of the string.
            (\w+(\s+)?)     # Actual string group with an optional space group nested.
            (\s+)?          # Optional whitespace group at the end of the string.
            """,
            re.VERBOSE,
        )

        return word_detector.sub(r"\2", sentence)

    if char_to_remove != None:
        letter_detector = re.compile(rf"[{char_to_remove}]")

        return letter_detector.sub("", sentence)


print(regex_strip_method(sentence, char_to_remove))
