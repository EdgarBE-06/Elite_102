vowels = ["a","e","i","o","u"]
word = input("Enter a word")

def vowels(string):
    vowel_counter = []
    for character in string:
        if character in vowels:
            vowel_counter += 1
    return vowel_counter


vowels(word)