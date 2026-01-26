# Odbierz od użytkownika słowa rozdzielone przecinkami, a następnie
# wyświetl te słowa wiersz pod wierszem, ale każde tylko jeden raz.

sentence = "I know I should, go to sleep, but, the voices in my, head"
words = set()

for word in sentence.split(','):
    words.add(word.strip())
    
print(words)


    