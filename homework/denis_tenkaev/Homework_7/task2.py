words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def copying(dict):
    for key, mult in dict.items():
        print (key * mult)

copying(words)
