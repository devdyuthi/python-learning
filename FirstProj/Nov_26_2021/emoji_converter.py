msg = input(">")
words = msg.split(' ')
emojis = {
    ":)":"😊",
    ":(":"😭",
    "*stares*" : "👁️👄👁️"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

