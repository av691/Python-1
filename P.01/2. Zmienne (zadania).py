# Zadanie nr 1
# W ciągu 3 godzin biegu biegacz pokonał 38 kilometrów. Wyznacz średnią prędkość korzystając ze zmiennych.

time = 3
distance = 38
avg_speed = distance / time
print("Średnia prędkość = ", avg_speed)

# Zadanie nr 2
# Zakładając, że na lokatę wpłacono 1000 zł, a oprocentowanie wynosi 4% w skali roku, oblicz jaka będzie wartość lokaty po 5 latach.

# Wzór to:
# wartość = wartość pocz. * (1 + procent/100) ^ liczba lat
value = 1000
percentage  = 4
years_time = 5
investment_value = value * (1 + percentage / 100) ** years_time
print("Wartośc lokalty po ", years_time, "latach to ", investment_value)

# Zadanie 3
# Oblicz jaką drogę pokonasz idąc do sklepu po czerwonych liniach i wypisz tyle myślników (-) jaki będzie wynik.
# a = 9
# b = 12
import math
a = 9
b = 12
total_distance = 2 * math.sqrt(a*a + b*b)
line  = "-"
print("Długość drogi wynosi - ", total_distance)
print(line * int(total_distance))