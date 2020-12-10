import math
import matplotlib.pyplot as plt
import numpy
#użytkownik wpisuje wymagane dane do działania programu
#bedzie tez tu system pilnowania, aby uzytkownik wpisywal dane odpowiedniego typu
dane = str(input('Podaj metodę wprowadzania danych (ręcznie/z_pliku): '))
if dane == 'ręcznie':
    print('Proszę podać dane')
    print('Odcinek między środkiem a jednym z ognisk elipsy: ')
    a = float(input()) #odcinek miedzy srodkiem a jednym z ognisk elipsy
    if a != 0:
        pass
    elif a == 0:
        print('a NIE MOŻE BY RÓWNE 0')
        exit()
    print('Wielka półoś elipsy: ')
    c = float(input('Podaj odcinek między środkiem a jednym z ognisk elipsy: '))
    if c == 0:
        print('c NIE MOŻE BY RÓWNE 0')
        exit()
    elif c < a:
        pass
    elif c >= a:
        print('c NIE MOŻE BY WIĘKSZE OD LUB RÓWNE a')
        exit()

    a = float(input('Podaj wielką półoś elipsy: '))
    if a == 0:
        print('a NIE MOŻE BY RÓWNE 0')
        exit()
    S = float(input('Podaj pole powierzchni zakreslane przez promien wodzacy: '))
    if S == 0:
        print('S NIE MOŻE BY RÓWNE 0')
        exit()
    t = float(input('Podaj czas zakreslania pola powierzchni: '))
    if t == 0:
        print('t NIE MOŻE BY RÓWNE 0')
        exit()
    r = float(input('Podaj wielką odległość słońca od planet: '))
    if r == 0:
        print('r NIE MOŻE BY RÓWNE 0')
        exit()
    w = float(input('Podaj prędkość kątową: '))
    if w == 0:
        print('w NIE MOŻE BY RÓWNE 0')
        exit()
    R1 = float(input('Podaj półoś wielka pierwsza: '))
    if R1 == 0:
        print('R1 NIE MOŻE BY RÓWNE 0')
        exit()
    R2 = float(input('Podaj półoś wielka druga: '))
    if R2 == 0:
        print('R2 NIE MOŻE BY RÓWNE 0')
        exit()
    T1 = float(input('Podaj okres pierwszy: '))
    if T1 == 0:
        print('T1 NIE MOŻE BY RÓWNE 0')
        exit()
    T2 = float(input('Podaj okres drugi: '))
    if T2 == 0:
        print('T2 NIE MOŻE BY RÓWNE 0')
        exit()
elif dane == 'z_pliku':
    c = open('odcinki.txt', "r")
    a = open('półosie.txt', "r")
    S = open('pola.txt', "r")
    t =  open('czasy.txt', "r")
    r = open('promienie.txt', "r")
    w = open('prędkościkątowe.txt', "r")
    R1 = open('promienie.txt', "r")
    R2 = open('promienie.txt', "r")
    T1 = open('okresy.txt', "r")
    T2 = open('okresy.txt', "r")
else:
    print('Błędne dane! Uruchom program ponownie!')
#program pobiera zdefiniowane funkcje 1,2 i 3 prawa keplera

def prawo_1(c, a): # e = c/a (mimośród elipsy)
    return c / a
print('Mimośród elipsy wynosi: ', prawo_1(c, a))

def prawo_2(): # (dS)/(dT)=(1/2)*(r^2)*w
    if S/t == 0.5*(r^2)*w:
        print('Drugie prawo Keplera jest spełnione')
    return prawo_2(S, t, r, w)

def prawo_3(): # (R1^3)/(R2^3) = (T1^2)/(T2^2) #w zadaniach prawo te może służyć do wyliczania poszczególnych wartości z ujętyh wzorem, co zostanie przedstawione w funkcji
    warunek1 = str(input('Czy dane są wprowadzane ręcznie? (TAK/NIE): '))
    if warunek1 == 'TAK':
        warunek2 = str(input('Podaj czynnik szukany (z racji na specyfikę zadania korzystamy z oznaczeń R11, R22, T11, T22): '))
        if warunek2 == 'R11':
            R22 = float(input('Podaj promień orbity drugiej planety: '))
            T11 = float(input('Podaj okres orbitalny pierwszej planety: '))
            T22 = float(input('Podaj okres orbitalny drugiej planety: '))
            print('R11 jest równe ', (((R22)^3)(((T11)^2)/((T22)^2)))^(1/3))
        elif warunek2 == 'R22':
            R11 = float(input('Podaj promień orbity drugiej planety: '))
            T11 = float(input('Podaj okres orbitalny drugiej planety: '))
            T22 = float(input('Podaj okres orbitalny pierwszej planety: '))
            print('R11 jest równe ', (((R11)^3)(((T22)^2)/((T11)^2)))^(1/3))
        elif warunek2 == 'T11':
            R11 = float(input('Podaj promień orbity pierwszej planety: '))
            R22 = float(input('Podaj promień orbity drugiej planety: '))
            T22 = float(input('Podaj okres orbitalny drugiej planety: '))
            print('R11 jest równe ', (((T22)^2)(((R11)^3)/((R22)^3)))^(1/2))
        elif warunek2 == 'T22':
            R11 = float(input('Podaj promień orbity drugiej planety: '))
            T11 = float(input('Podaj okres orbitalny drugiej planety: '))
            R22 = float(input('Podaj promień orbity pierwszej planety: '))
            print('R11 jest równe ', (((T11)^2)(((R22)^3)/((R11)^3)))^(1/2))
    else:
        warunek3 = str(input('Podaj czynnik szukany: '))
        if warunek3 == 'R1':
            print('R1') #dalszy rozwój funkcji będzie wprowadzony w przyszłotygodniowym commicie

    return prawo_3()

#w tej częsci program wylicza orbite w funkcji 'orbita' na podstawie wpisanych danych wstawionych do trzech zdefiniowanych funkcji praw keplera

#def orbita():
#    return orbita()


#rysowanie wykresu
#plt.title('Orbita obiektu')
#class matplotlib.patches.Ellipse((0,0), 20, 20, angle=0, )