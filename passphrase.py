import random

open_wordlist = open("wordlist.txt","r")
read_wordlist = open_wordlist.read()
words_to_list = read_wordlist.split()

def paraphrase():
    random_range = random.randrange(15,30)
    words = random.sample(words_to_list,random_range)
    add_space = " ".join(words)
    random_case = "".join(random.choice((str.upper,str.lower))(char) for char in add_space)
    replace_char = {
        "a": "@",
        "A": "4",
        "E": "3",
        "S": "$",
        "I": "1",
        "O": "0"
    }
    for key,value in replace_char.items():
        phrase = random_case.replace(key , value)
    print(phrase)
paraphrase()