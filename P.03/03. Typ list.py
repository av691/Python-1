# Zadanie nr 1
# Stwórz zmienną favourite_sports, która będzie listą zawierającą nazwy dyscyplin sportu, które lubisz.
# Następnie wypisz informacje, jaki sport jest pierwszy na Twojej liście, a jaki ostatni.
# Podmień jeden ze sportów na inny i wypisz całą listę.

# favourite_sports = [
#     "kenjutsu",
#     "taichi",
#     "aikido",
#     "kendo"
# ] 

# print(favourite_sports[0])
# print(favourite_sports[-1])
# favourite_sports[-1] = "nic"
# print(favourite_sports)

# Zadanie nr 2
# Zapytaj użytkownika o 3 ulubione potrawy i zapisz je w postaci listy.

# food_list = []
# dish = input("Podaj pierwszą potrawę ")
# food_list.append(dish)
# dish = input("Podaj drugą potrawę ")
# food_list.append(dish)
# dish = input("Podaj trzecią potrawę ")
# food_list.append(dish)
# print(food_list)

# Zadanie nr 3
# Zapytaj użytkownika o numer telefonu i wypisz go w postaci zanonimizowanej.
# Wypisz pierwszych 6 cyfr, a kolejne zastąp myślnikiem.

phone_no = input("Podaj numer telefonu ")
phone_no = phone_no.replace(' ','').replace('-','')
public_phone_no = phone_no[:6]
number_of_private_digits = len(phone_no) - 6
private_phone_no = '-' * number_of_private_digits
anonymous_phone_numer = f"{public_phone_no}{private_phone_no}"
print("Teraz numer telefonu to", anonymous_phone_numer)