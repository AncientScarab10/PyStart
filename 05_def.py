# # def jakaś_nazwa_funkcji (a, b): ## a, b to parametry
# #     return a + b ## a + b czyli jakaś operacja, return zwraca nam jakiś oczekiwany wynik


def add_numbers (a, b):
    return a + b

print(add_numbers(10, 5))

# # return dając nam wynik przydaje się w momencie gdy chcemy coś nazwać. 
# #Pisząc print(brutto) my tylko obliczamy, jednak chcąc by kwotę brutto używać w dalszej części kodu,
# # liczymy już wartość brutto np. 

# def policz vat(netto, vat):
#     brutto = netto * (1 + vat)
#     return brutto #tutaj dając print(brutto nic nam to nie daje, prócz widoku)


# def is_leap_year(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# def get_days_in_month(month, year):
#     if month in (4, 6, 9, 11):
#         return 30
#     elif month == 2:
#         if is_leap_year(year):
#             return 29
#         return 28
#     else:
#         return 31
    


# for year_to_test in range(2000, 2025):
#     for month_to_test in range(1, 13):
#         print(year_to_test, month_to_test, get_days_in_month(month_to_test, year_to_test))
        