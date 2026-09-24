text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
    " Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)
text = text.split()
for word in text:
    if word.endswith(","):
        print(word.rstrip((",")) + "ing", end=", ")
    elif word.endswith("."):
        print(word.rstrip((".")) + "ing", end=". ")
    else:
        word = word + "ing"
        print(word, end=" ")
