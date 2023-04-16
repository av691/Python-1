# Zadanie nr 1
# Zapytaj użytkownika ile ma lat i wypisz ile to miesięcy.

years  = int(input("podaj ile masz lat? "))
month_per_year = 12
total_month = years * month_per_year

print("Masz", years, "lat - czyli", total_month, "miesięcy")

# Zadanie nr 2
# Zapytaj ile kilometrów przeszedł w tym tygodniu i policz ile tygodni zajmie mu okrążenie Ziemi.
# Pamiętaj, że obwód Ziemi to 40 075 km.

distance = int(input("Ile przeszedłeś km w tym tygodniu? "))
earth_perimeter = 40075

time = earth_perimeter / distance

print("W tym tygodniu przeszedłeś", distance, "km")
print("W tym tempie Ziemię okrążysz za", time, "tygodnie")

# Zadanie nr 3
# Zastosuj wzór do obliczenia wartości lokaty, pobierając od użytkownika następujące dane:

# początkowa wartość
# oprocentowanie
# czas trwania w latach

initial_value = int(input("Podaj wartość początkową lokaty "))
percentage  = int(input("Podaj wartość oprocentowania? "))
years_time = int(input("podaj czas trwania w latach? "))

investment_value = initial_value * (1 + percentage / 100) ** years_time
print("Wartość lokaty po ", years_time, "latach to ", investment_value)