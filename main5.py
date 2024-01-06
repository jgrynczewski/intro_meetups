# Wykres
import matplotlib.pyplot as plt
import random

# Generowanie losowych danych
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y_values = [32,54,46,70,63,20,73,60,90]

# Tworzenie wykresu
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label='Dane')

# Dodanie tytułów i etykiet
plt.title('Wykres')
plt.xlabel('Oś X')
plt.ylabel('Oś Y')

# Dodanie legendy
plt.legend()

# Wyświetlanie wykresu
plt.show()
