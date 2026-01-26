# Przygotuj funkcję, która będzie odbierała od użytkownika słowo,
# a następnie zwróci zbiór samogłosek znajdujących się w tym słowie.

def get_vowels(word):
    vowels_in_word = set()
    vowels = "aeiouyąę"
    for vowel in vowels:
        word = word.lower()
        if vowel in word:
            vowels_in_word.add(vowel)
        
    return vowels_in_word
    
print(get_vowels("Abrakadabra"))
    
        