#### Hello, world
# wbudowane rzeczy (I) - funckja print
print("Hello, world!")

#### Typy
"string"
3  # int
3.3  # float
print(3)
print(3.3)

#### Zmienne
imie = "Anna"
print("Hello ", imie)
wiek = 25
print("Cześć, nazywam się", imie, "i mam", wiek, "lat.")

#### Wbudowane rzeczy (II) - input
imie = input("Podaj swoje imię: ")
print("Cześć ", imie)
wiek = input("Podaj swój wiek: ")
print("Cześć, nazywam się", imie, "i mam", wiek, "lat.")

#### Operatory
x = 3
y = 5
print(x+y)
print(x-y)

#### Wbudowane rzeczy (input)

#### Prosty kalkulator
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

suma = liczba1 + liczba2
roznica = liczba1 - liczba2
iloczyn = liczba1 * liczba2

print("Suma:", suma)
print("Różnica:", roznica)
print("Iloczyn:", iloczyn)


#### Przykład warunków
temperatura = 22

if temperatura > 20:
    print("Jest ciepło!")
else:
    print("Jest chłodno.")



#### Gra w zgadywanie liczby
# Wbudowane rzeczy (III) - random - moduły
import random


liczba_do_zgadniecia = random.randint(1, 10)

print("Zgadnij liczbę z zakresu 1-10.")

zgadywana_liczba = int(input("Podaj swoją propozycję: "))

if zgadywana_liczba == liczba_do_zgadniecia:
    print("Brawo! Zgadłeś.")
else:
    print("Niestety, to nie ta liczba. Prawidłowa liczba to:", liczba_do_zgadniecia)


#### To już raczej nie
#### Przykład pętli
liczba_powtorzen = int(input("Ile razy chcesz wyświetlić komunikat? "))

counter = 0
while counter < liczba_powtorzen:
    print("Witaj")
    counter += 1


#### Gra w zgadywanie liczby z użyciem pętli
import random


liczba_do_zgadniecia = random.randint(1, 10)

print("Zgadnij liczbę z zakresu 1-10.")

zgadywana_liczba = int(input("Podaj swoją propozycję: "))

while zgadywana_liczba != liczba_do_zgadniecia:
    print("Niestety, to nie ta liczba. Próbuj dalej")

print("Brawo! Zgadłeś.")
