import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: "
                   % get_close_matches(word, data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "Word not found"
    else:
        return "Word not found."


word = input("Enter word: ")

print(translate(word))
