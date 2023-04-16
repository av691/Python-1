# Zadanie nr 1
# Napisz program, który zapyta użytkownika jaka jest cena jabłek w Biedronce, Lidlu i Żabce.

# Następnie wypisz informację: Ile kosztują najtańsze jabłka?

apple_price_biedronka = float(input("Podaj cenę jabłek z Biedronki? "))
apple_price_lidl = float(input("Podaj cenę jabłek z Lidla? "))
apple_price_zabka = float(input("Podaj cenę jabłek z Żabki? "))

min_apple_price = min(apple_price_biedronka, apple_price_lidl, apple_price_zabka)

print("Najtańsze jabłka kosztują", min_apple_price)