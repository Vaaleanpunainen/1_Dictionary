import json

data = json.load(open("data.json"))

def translate(w):

    if w in data:
        return data[w]
    else:
        return "No such a word in a dictionary. Please double check it."
word = (input("Enter world: ")).lower()

print(translate(word))
