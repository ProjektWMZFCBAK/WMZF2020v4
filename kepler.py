import math
import matplotlib.pyplot as plt
import numpy
#użytkownik wpisuje wymagane dane do działania programu
#bedzie tez tu system pilnowania, aby uzytkownik wpisywal dane odpowiedniego typu
print('Proszę podać dane')

print('Odcinek między środkiem a jednym z ognisk elipsy: ')
a = float(input()) #odcinek miedzy srodkiem a jednym z ognisk elipsy
if a != 0:
    pass
elif a == 0:
    print('a NIE MOŻE BY RÓWNE 0')
    exit()
print('Wielka półoś elipsy: ')
c = float(input()) #wielka polos elipsy




if c == 0:
    print('c NIE MOŻE BY RÓWNE 0')
    exit()
elif c < a:
    pass
elif c >= a:
    print('c NIE MOŻE BY WIĘKSZE OD LUB RÓWNE a')
    exit()


"""
print('Pole powierzchni zakreślane przez promień wodzący: ')
S = float(input()) #pole powierzchni zakreslane przez promien wodzacy
print('Czas zakreślania pola powierzchni: ')
t = float(input()) #czas zakreslania pola powierzchni
print('Odległość słońca od planet: ')
r = float(input()) #odleglosc slonca od planet
print('Prędkość kątowa obrotu linii łączącej słońce z planetą: ')
w = float(input()) #predkosc katowa obrotu linii laczacej slonce z planeta
print('Półoś wielka planet 1: ')
R1 = float(input()) #polos wielka planety 1
print('Półoś wielka planety 2: ')
R2 = float(input()) #polos wielka planety 2
print('Okres obiegu planety 1: ')
T1 = float(input()) #okres obiegu planety 1
print('Okres obiegu planety 2: ')
T2 = float(input()) #okres obiegu planety 2
"""

#program pobiera zdefiniowane funkcje 1,2 i 3 prawa keplera

def prawo_1(c, a): # e = c/a (mimośród elipsy)
    return c / a
print('Mimośród elipsy wynosi: ', prawo_1(c, a))

#def prawo_2(): # (dS)/(dT)=(1/2)(r^2)
#    return prawo_2()

#def prawo_3(): # (R1^3)/(R2^3) = (T1^3)/(T2^3)
#    return prawo_3()

#w tej częsci program wylicza orbite w funkcji 'orbita' na podstawie wpisanych danych wstawionych do trzech zdefiniowanych funkcji praw keplera

#def orbita():
#    return orbita()


#rysowanie wykresu
plt.title('Orbita obiektu')
