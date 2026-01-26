# 1. Przygotuj funkcję, która na podstawie czasu pracy, ilości
# zużywanych kilowatogodzin odpowie ile zapłacę za prąd, który
# zużywa urządzenie. Domyślny koszt 1 kwh to 0,617.

# 2. Przygotuj funkcję, której deklaracja będzie wyglądała następująco:
# def count_numbers(numbers: list, count_odd:bool = True, count_even:bool = True):
# Zadaniem funkcji będzie odpowiedź na pytanie ile jest liczb
# spełniających podane w argumentach wymagania w liście
# przekazanej w pierwszym przedziale.
    
def calculate_cost(time: float, unit_price = 0.617) -> float:
    """Function calculate the cost of electricity.

    Args:
        time (float): How many time the device is working? (Give me and hours e.g. 1.6)
        unit_price (float, optional): Unit price for 1 kwh. Defaults is 0.617.

    Returns: Device cost.
    """
    return time * unit_price

print(calculate_cost(3.0))

def count_numbers(numbers: list, count_odd: bool = True, count_even: bool = True):
    return 