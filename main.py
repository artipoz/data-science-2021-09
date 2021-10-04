print("Hello World")

# komentarz liniowy - hash
"""
komentarz wielowierszowy
"""

# zmienna imie
imie = 'Artur'

print('Na imię mam ' + imie)

# pętla licząca
for i in range (5):
    print(i)

"""
operatory
<=
>=    
"""
#lista - nawias kwadratowy
lista_imion = ["Leszek", "Maciej", "Karol", "Artur"]
print(lista_imion)
print(lista_imion [3])
imie_dodatkowe = ["Katarzyna"]
lista_imion = lista_imion + imie_dodatkowe
print(lista_imion)

lista = []
print(lista)
for i in range(10):
    lista.append(i)

print(lista)

#tuple - nawias okrągły - śa obiektami, których nuie można nadpisywać
lista_imion = ("Leszek", "Maciej", "Karol", "Artur")

# sprawdzenie typu zmiennych
z=2.5 + 1j
print(type(z))

# zmienne typu logicznego
a='Ala ma kotka'
print(a)
print(type(a))

# w pythonie string moze być potraktowany jako tabela
napis='Ala ma kota'
# wyświetlamy do 10 znaku
print(napis[:10])
# wyświetlamy od 3
print(napis[3:-1])

napis_2 = "Ala ma koty"
nowy_napis = napis + napis_2
print(nowy_napis)

#tuple zabezpieczają przed nadpisaniem - w nawiasach oką
c=3
c=5
print(c)
d=("22")
d=5
print(c)
#nie działa???

a = 3
a = 3
print("to jest nasza obecna wartość: ", + a)