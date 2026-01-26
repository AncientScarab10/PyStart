# Napisz funkcję, która przyjmuje jeden argument pozycyjny (tekst) i
# dwa argumenty nazwane (delimiter i repeat) z domyślnymi
# wartościami "," i 1. Funkcja powinna zwracać tekst powtórzony
# odpowiednią liczbę razy i rozdzielony podanym delimiterem.

def repeat (text, delimiter=',', repeat=1):
    output = []
    for _ in (repeat):
        output.append(text)
    # ';'.join(fruits) - przykład joina, którego można zastąpić argumentem "delimiter"
    return delimiter.join(output)
        
print(repeat("Ala ma kota"))

print(repeat("Python", delimiter=";", repeat=3))


