# Przygotuj funkcję o nazwie word_counter, powinna jako argument
# odbierać dowolny tekst i zwracać ilość słów z których ten tekst się
# składa.

def word_counter(text):
    words = text.split(" ")
    return len(words)

sentence = "Ala ma kota"
print(word_counter(sentence))




                              
