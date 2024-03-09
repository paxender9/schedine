quante = int(input("da quante partite è composta? "))

numeri = input("riporta tutte le quote separate con una virgola ")

quotestr = numeri.split(',')

quote = [float(numero) for numero in quotestr]

somma_quote = sum(quote)

print(somma_quote)

somma_100 = float(quante * 100)

print(somma_100)

probabilità_finale = somma_100 / somma_quote

print(f"la probabilità di vincita è: {probabilità_finale}")