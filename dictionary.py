import json

data = json.load(open("data.json"))

def translate(w):
    return data[w]

word = input("Enter world: ")

print(translate(word))
