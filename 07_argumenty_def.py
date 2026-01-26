# Przygotuj funkcję, która będzie szukała wspólnych dzielników dla dwóch
# liczb. Funkcja posiada trzeci argument domyślny określający wartość
# początkową, gdzie największy wspólne dzielniki muszą być zawsze
# większe niż ta wartość.

# def common_devisor (number1 = 0, number2 = 0, start_value = 1):
#     list_of_common_devisor = []
#     for i in range(1, 100):
#         if number1 % i == 0 and number2 % i == 0 and i > start_value:
#             list_of_common_devisor.append(i)
#     return list_of_common_devisor

# print(common_devisor(8, 16))

# Napisz funkcję, która przyjmuje dwa argumenty, gdzie drugi będzie
# miał domyślną wartością równą 2. Funkcja powinna zwracać podaną
# liczbę pomnożoną przez mnożnik.            

def f (a, b=2, m=6):
    return a * b * m

print(f(2))
