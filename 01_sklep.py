# Przygotuj słownik zawierający produkty. Produkt to klucz, a cena to wartość. Zapytaj
# użytkownika który produkt chce dodać do koszyka, a następnie w jakiej ilości. Pytaj
# dopóki użytkownik nie odpowie “podsumuj”.
# Wartość zamówienia możesz przechowywać w pojedynczej zmiennej lub posiadać listę
# (dla chętnych) produktów lub słowników jeśli chcesz wyświetlić podsumowanie.

products = {
    "salt": 0.39,
    "cheese": 2.19,
    "ham": 7.26     
}

basket = []
value_basket = 0.0

print("Products:", list(products.keys()))

while True:
    key = input("What you want? (or type stop): ")
    
    if key == "stop":
        break
    if key in products:
        quantity = float(input("How much?: "))
        
        price = products[key]
        cost = quantity * price
        
        basket.append(key)
        value_basket += cost
        
        print(f"Added {quantity} of {key}. Cost: {cost:.2f}")
        
    else:
        print("I don't know what you mean.")

print("--Receipt--")
print("Your basket:", basket)
print(f"Total to pay: {value_basket:.2f}")
    
        
                