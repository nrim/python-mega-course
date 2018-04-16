import json
import difflib

data = json.load(open("data.json"))


def translate(word):
    if word.lower() in data:
        return data[word.lower()]
    else:
        closeMatch = difflib.get_close_matches(word, data, 1)
        return "Word not found.  Did you mean one of these words?: " + closeMatch


word = input("Enter word: ")

print(translate(word))
