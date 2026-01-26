# # 1. Przygotuj funkcję, która odbierze dwie listy, wynikiem powinna być nowa lista.
# e.g.:
# a = [2, 4, 7]
# b = [8, 6, 4]

# # sum_list(a, b)
# # #zwróci [10, 10, 10]

# def sum_list(a: list, b: list) -> list:
#     sum_ab = zip(a, b)
#     wynik = []
#     for x, y in sum_ab: 
#         wynik.append(x + y)
#     return wynik

# print(sum_list(a = [2, 4, 7], b = [8, 6, 3]))

# 2. Przygotuj funkcję, która będzie potrafiła przefiltrować liczby parzyste z listy przekazanej w argumencie.

# def filter_of_even(a: list):
#     a_even = []
#     for element in a:
#         if element % 2 == 0:
#             a_even.append(element)
#     return a_even    
        
# print(filter_of_even([1, 2, 3, 4, 6, 10, 11]))            
            
# 3. Napisz funkcję, która rekurencyjnie policzy sumę wszystkich wartości od 1 do n..
# dla przykładu sum_it(5) wykona 5 + 4 + 3 + 2 + 1

# def sum_it(number):
#     if number == 0:
#         return 0
    
#     return number + sum_it(number - 1)

# print(sum_it(5)) 


# 4. PIN może składać się wyłącznie z czterech cyfr. Napisz funkcję która zwróci prawdę
# lub fałsz w zależności od tego czy to wymaganie jest spełnione.

def validate_pin(pin: str) -> bool:
    
    if len(pin) != 4:
        return False
    
    for char in pin:
        if not char.isdigit():
            return False
        
    return True

print(validate_pin('1234'))



