# Zadanie nr 1
# Zmodyfikuj rozwiązania zadań 1 i 2 z poprzedniej lekcji, tak aby wypisywać różne informacje w zależności od wyniku porównań.

# print("Podaj ceny  produktów")
# produkt_1 = float(input("Produkt 1 "))
# produkt_2 = float(input("Produkt 2 "))
# produkt_3 = float(input("Produkt 3 "))

# if produkt_1 > produkt_2:
#     print(f"Cena produktu 1 ({produkt_1}) > Cena produktu 2 ({produkt_2})")
# else:
#     print(f"Cena produktu 1 ({produkt_1}) < Cena produktu 2 ({produkt_2})")

# Zadanie nr 2
# Zmodyfikuj rozwiązanie zadania z kalkulatorem wydatków z lekcji dotyczącej słownika (moduł 3).
# Pobierz te same informacje na temat miesięcznych wydatków w różnych kategoriach.
# Wypisz jednak informacje na temat procentowego udziału najbardziej znaczącej kategorii.

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

# most_important_category = "Jedzenie"

# if expenses["Rozrywka"] > expenses[most_important_category]:
#     most_important_category = "Rozrywka"
# if expenses["Opłaty"] > expenses[most_important_category]:
#     most_important_category = "Opłaty"
# if expenses["Inne"] > expenses[most_important_category]:
#     most_important_category = "Inne"

# print(f"Najbardziej znacząca kategoria wydatków to {most_important_category} = {expenses[most_important_category]:.0f}%")

# Zadanie nr 3
# Zapytaj użytkownika o jego oceny końcowe z kilku przedmiotów (matematyka, fizyka, itd.).
# Następnie, przeanalizuj je i wypisz informację czy zdał/zdała do kolejnej klasy.
# Załóż, że zdać można wtedy jeżeli nie ma się żadnej jedynki albo jeżeli ma się jedną jedynkę, ale średnia ze wszystkich ocen jest wyższa niż 3.5.

# print("Podaj oceny końcowe z następujących przedmiotów") 
# math_grade = float(input("Matematyka "))
# english_grade = float(input("Angielski "))
# physics_grade = float(input("Fizyka "))
# history_grade = float(input("Historia "))
# averange = (math_grade + english_grade + physics_grade + history_grade) / 4
# number_of_failures = 0

# if math_grade <= 2.0:
#     number_of_failures += 1
# if english_grade <= 2.0:
#     number_of_failures += 1
# if physics_grade <= 2.0:
#     number_of_failures += 1
# if history_grade <= 2.0:
#     number_of_failures += 1

# if number_of_failures == 0:
#     print("Gratuluję zdałeś")

# if number_of_failures == 1:
#     if averange > 3.5:
#         print("Gratuluję zdałeś")
#     else:
#         print("Niestety nie zdałeś")
# else:
#     print("Niestety nie zdałeś")

# Zadanie nr 4
# Zapytaj o imię i "rozpoznaj" czy użytkownik to kobieta czy mężczyzna.
# Podpowiedź: Na potrzeby tego zadania możemy założyć, że żeńskie imiona kończą się na "a".

imie = input("Podaj swoje imię ")

if imie[-1] == 'a':
    print("Jesteś kobietą")
else:
    print("Jesteś mężczyzną")
