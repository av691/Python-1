# Zadanie nr 1
# Stwórz i wypisz słownik, w którym kluczami będą różne przedmioty szkolne, a wartościami oceny uzyskane z tych przedmiotów.

# school = {
#     "matematyka": 3.0,
#     "fizyka": 3.0,
#     "geografia": 3.0
# }
# print(school)

# Zadanie nr 2
# Stwórz zmienną my_family zawierającą drzewo genealogiczne Twojej rodziny.
# Zacznij od siebie, opisując imię, nazwisko oraz datę urodzenia każdej osoby oraz jej rodziców.
# Podpowiedź: rodzice będą listami zawierającymi w sobie kolejne słowniki.

# my_family = {
#     "PK": {
#         "Imię": "P",
#         "Nazwisko": "K",
#         "Data urodzenia": "1969-12-13",
#         "O" : {
#             "Imię": "Z",
#             "Nazwisko": "K",
#             "Data urodzenia": "1900-01-01"
#         },
#         "M" : {
#             "Imię": "J",
#             "Nazwisko": "K",
#             "Data urodzenia": "1900-01-01"
#         }
#     },
#     "AB": {
#         "Imię": "A",
#         "Nazwisko": "B",
#         "Data urodzenia": "1970-12-03",
#         "O" : {
#             "Imię": "1",
#             "Nazwisko": "B",
#             "Data urodzenia": "1900-01-01"
#         },
#         "M" : {
#             "Imię": "2",
#             "Nazwisko": "B",
#             "Data urodzenia": "1900-01-01"
#         }        
#     }
# } 

# print(my_family)

# Zadanie nr 3
# Zapytaj użytkownika ile miesięcznie wydaje pieniędzy na:

# jedzenie
# rozrywkę
# opłaty
# inne
# Oblicz udział procentowy każdej kategorii w łącznych wydatkach.
# Następnie poproś użytkownika o wybór kategorii i wypisz jaki jest jej udział procentowy.

# print("Podaj ile wydajesz na")
# food = float(input("Jedzenie? "))
# entertainment = float(input("Rozrywkę? "))
# charges = float(input("Opłaty? "))
# other  = float(input("Inne? "))

# total_exp = food + entertainment + charges + other
# expenses = {
#     "Jedzenie": food * 100 / total_exp,
#     "Rozrywka": entertainment * 100 / total_exp,
#     "Opłaty": charges * 100 / total_exp,
#     "Inne": other * 100 / total_exp
# }

# selected_category = input("Wybierz jedną z kategorii Jedzenie/Rozrywka/Opłaty/Inne ")
# print(f"Na {selected_category} wydajesz {expenses[selected_category]:.0f}% wszystkich wydatków")