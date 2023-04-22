# Napisz uproszczony kalkulator kredytowy.

# Celem kalkulatora jest sprawdzenie czy użytkownika stać na kredyt hipoteczny o podanych parametrach.

# Zapytaj użytkownika o:

# kwotę kredytu
# oprocentowanie kredytu
# wartość wkładu własnego
# czas kredytowania w latach
# przychód miesięczny
# sumę miesięcznych wydatków

# Oblicz ratę ze wzoru:
# (kwota kredytu * oprocentowanie / 100) / 12 + kwota kredytu / (liczba lat * 12)

# Oblicz dostępne środki jako:
# przychód - suma wydatków

# Oblicz wartość nieruchomości jako:
# wkład własny + kwota kredytu

# Jeżeli wkładu własnego < 10% to nie można wziąć kredytu
# Jeżeli wkład własny od 10% do 20% to dostępne środki muszą być wyższe od raty o 2.000 PLN
# Jeżeli wkład własny > 20% to dostępne środki > rata kredytu o >= 1.000 PLN

print("Podaj dane do kredytu")
loan_amount = float(input("Kwota kredytu: "))
interest_rate = float(input("Oprocentowanie kredytu: "))
own_contribution = float(input("Wartość wkładu własnego: "))
years = int(input("Czas kredytowania: "))
monthly_income = float(input("Przychód miesięczny: "))
monthly_expeditures = float(input("Suma miesięcznych wydatków: "))

avaiable_money = monthly_income - monthly_expeditures
property_value = own_contribution + loan_amount
own_contribution_part = own_contribution / property_value
installment_value = (loan_amount * interest_rate / 100) / 12 + loan_amount / (years * 12)
money_over_installment = avaiable_money - installment_value

matching_lower_own_part = own_contribution >= 0.2 and money_over_installment >= 1000
matching_higher_own_part = own_contribution >= 0.2 and money_over_installment >= 2000

if matching_lower_own_part or matching_higher_own_part:
    print("Można wziąć kredyt")
else:
    print("Nie można wziąć kredytu")