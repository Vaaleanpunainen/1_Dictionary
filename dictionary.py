import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = (input("Maybe you mean %s instead? Enter Y for yes or N for no: " % get_close_matches(w, data.keys())[0])).upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "No such a word in a dictionary. Please double check it."
        else:
            return "Incorrect enter."
    else:
        return "No such a word in a dictionary. Please double check it."
word = (input("Enter world: ")).lower()



output = translate(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
