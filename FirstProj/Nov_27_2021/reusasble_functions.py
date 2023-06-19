def emoji_converter(msg):
    words = msg.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😭",
        "*stares*":  "👁️👄👁️"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

msg = input(">")
print(emoji_converter(msg))
