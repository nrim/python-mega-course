import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    """Return definitions of the entered word."""
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        answer = input("Did you mean %s instead? Enter Y if yes, or N if no: "
                       % get_close_matches(word, data.keys())[0])
        if answer.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "Word not found"
    else:
        return "Word not found."


inputWord = input("Enter word: ")

output = translate(inputWord)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
