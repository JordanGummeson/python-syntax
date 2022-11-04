def print_upper_words(words):
    """prints the list of words in all caps"""
    for i in words:
        print(i.upper())

def print_upper_wordse(words):
    """prints the list of words in all caps if they start with e"""
    for i in words:
        if i.startswith("e") or i.startswith("E"):
            print(i.upper())

def print_upper_words_final(words,must_start_with):
    """prints the list of words in all caps that start with letters in list"""
    for i in words:
        for l in must_start_with:
            if i.startswith(l):
                print(i.upper())
                break
