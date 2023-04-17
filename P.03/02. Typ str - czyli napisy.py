# Zadanie nr 1
# Dostosuj program liczący wartość lokaty, tak aby wyświetlał ją z dokładnością do groszy (dwóch cyfr po przecinku).

# initial_value = int(input("Podaj wartość początkową lokaty "))
# percentage  = int(input("Podaj wartość oprocentowania? "))
# years_time = int(input("podaj czas trwania w latach? "))

# investment_value = initial_value * (1 + percentage / 100) ** years_time
# print(f"Wartość lokaty po {years_time} latach to {investment_value:.2f}") 

# Zadanie nr 2
# Zapytaj użytkownika o imię i wypisz ile liter zawiera.

# user_name = input("Podaj swoje imię? ")
# print(f"Imię {user_name} ma {len(user_name)} znaków")

# Zadanie nr 3
# Zapytaj użytkownika gdzie mieszka i wypisz odpowiedź, np. "Jak miło, że mieszkasz w Gdańsku".
# W razie nieuwagi użytkownika popraw wprowadzoną nazwę miasta, tak by zaczynała się z wielkiej litery.

# city = input("Gdzie mieszkasz? ") 
# print(f"Jak miło, że mieszkasz w {city.title()}")

# Zadanie nr 4
# Wyobraź sobie, że przetwarzasz dane dotyczące samochodów.
# Numery tablic rejestracyjnych zostały jednak zapisane w niespójny sposób:

# ford = "ab100100"
# audi = "EEE 123123"
# citroen = "Zk-300300"
# honda = "AB210210"

# Stwórz zmienne jak powyżej i zmodyfikuj ich wartość, tak aby wszystkie były w formacie takim jak Honda, czyli wielkie litery i bez przerw w ciągu cyfr.
# Wypisz wszystkie wyniki.

# variable define
# ford = "ab100100"
# audi = "EEE 123123"
# citroen = "Zk-300300"
# honda = "AB210210"

# # print 
# print(f"Tablice dla Forda\t {ford.upper()}")
# print(f"Tablice dla Audi\t {audi.replace(' ','')}")
# print(f"Tablice dla Citroena\t {citroen.replace('-','').upper()}")
# print(f"Tablice dla Honda\t {honda}")