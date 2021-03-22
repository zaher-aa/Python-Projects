def convertors(u_input):
    splitted = u_input.split(" ")
    emojies = {
        ":(": "😒",
        ":)": "😂",
        "*": "😎"
    }
    res = ""
    for word in splitted:
        res += emojies.get(word, word) + " "
    return res


u_input = input("enter: ")
print(convertors(u_input))
