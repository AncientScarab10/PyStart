# Korzystając ze zdobytej wiedzy napisz funkcję liczącą silnie dla podanej
# przez użytkownika w argumencie liczby.

# L! = L * (L-1)!
# silnia(L) = L * silnia(L-1)

def factorial(l):
    if l==1:
        return 1
    return l*factorial(l-1)

print(factorial(5))
