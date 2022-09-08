import random


def tehtava(num):
    viiva = "-" * 50
    print(f"\n{viiva}")
    print(f"Tehtava {num}:")
    print(viiva)


# --------------------------------------------------------------
# Tehtava 1. Outputs. Avaa Spyder editori ja tee perinteinen 'Hello World'  tulostus konsoliin.
tehtava(1)
print("Hello world")

# --------------------------------------------------------------
# Tehtava 2. If..else. Tee ohjelma, joka kysyy kaksi numeroa kayttajalta. Jos a on isompi, tulostetaan: 'a isompi'.
# Jos b isompi: 'b isompi'. Jos yhtasuuret: 'yhtasuuret'.
tehtava(2)
luku_a = int(input("Anna luku a: "))
luku_b = int(input("Anna luku b: "))


def task_2(a, b):
    print(f"Input a: {a}\nInput b: {b}")
    if a > b:
        print("a isompi")
    elif a < b:
        print("b isompi")
    else:
        print("yhtasuuret")
    print("\n")


task_2(luku_a, luku_b)

# --------------------------------------------------------------
# Tehtava 3. Random, imports. Muokkaa tehtavaa 2 siten, etta kone arpoo luvut valilta 0-100.
tehtava(3)
luku_a = random.randint(0, 100)
luku_b = random.randint(0, 100)
task_2(luku_a, luku_b)

# --------------------------------------------------------------
# Tehtava 4. Tee ohjelma, joka arpoo kaksi satunnaislukua valilla 0-10 ja tulostaa niiden summan.
# Tee summan tulostuksesta erillinen funktio, joka saa kaksi parametria (edella mainitut arvot),
# ja tulostaa parametrien summan. Esimerkkiajo:
# Lukujen 9 ja 1 summa on: 10
tehtava(4)
summa_a = random.randint(0, 10)
summa_b = random.randint(0, 10)


def summa(a, b):
    total_sum = a + b
    print(f"Lukujen {a} ja {b} summa on: {total_sum}\n\n")


summa(summa_a, summa_b)

# --------------------------------------------------------------
# Tehtava 5. Tee kertolaskujen harjaanuttamisohjelma. Ohjelma arpoo viisi kertolaskua numeroilla 0-10.
# Laskut tulostetaan naytolle.
# Kayttaja antaa omat vastauksensa ja lopuksi tulostetaan laskukohtainen palaute ja yhteenveto. Esimerkkiajo:
tehtava(5)


def kertolaskuri():
    print("Laske kertolaskut: ")
    oikein = []
    laskut = []
    tulos = 0
    for i in range(5):
        luku_1 = random.randint(0, 10)
        luku_2 = random.randint(0, 10)
        print(f"Laskutoimitus {i+1}: {luku_1} * {luku_2}")
        laskut.append(f"{luku_1} * {luku_2}")
        oikein.append(luku_1 * luku_2)

    for x, i in enumerate(oikein):
        vastaus = int(input(f"Anna vastaus {x + 1}: "))
        if vastaus == i:
            print(f"Oikein! {laskut[x]} = {i}")
            tulos += 1
        else:
            print(f"Vaarin! Oikea vastaus on: {laskut[x]} = {i}")

    print(f"\nLaskut: {laskut}\nOikeat vastaukset: {oikein}\nTulos: {tulos}/5")
    if tulos == 5:
        print("Onnittelut! Sait kaikki oikein!")
    elif tulos == 4:
        print("Sait 4 oikein!")
    elif tulos == 3:
        print("Sait 3 oikein, tarkkana!")
    else:
        print("Sait vahemman kuin 3 oikein, kertauksen aika!")


kertolaskuri()


# --------------------------------------------------------------
# Tehtava 6. Luokat ja oliot. Tee luokka: Murtoluku.
# Silla on kaksi attribuuttia: osoittaja ja nimittaja. Totetuta __init__ rutiini.
# Lisaa myos tulosta() -metodi, joka tulostaa murtoluvun muodossa: osoittaja / nimittaja.
# Toteuta myos sievenna()-metodi, joka sieventaa murtoluvun, esim 2/4 on sievennettyna 1/2.


class Murtoluku:
    def __init__(self, osoittaja, nimittaja):
        self.osoittaja = osoittaja
        self.nimittaja = nimittaja

    def print(self):
        print(f"{self.osoittaja} / {self.nimittaja}")

    def sievenna(self):
        if self.osoittaja > self.nimittaja:
            return Murtoluku(self.osoittaja // self.nimittaja, 1)
        else:
            return Murtoluku(1, self.nimittaja // self.osoittaja)


tehtava(6)

fraction = Murtoluku(34562, 311058)
fraction.print()
fraction.sievenna().print()


def run_murtoluku(a, b):
    fraction = Murtoluku(a, b)
    fraction.print()
    fraction.sievenna().print()


for i in range(5):
    print(f"Murtoluku {i + 1}")
    a = random.randint(1, 100000)
    b = random.randint(1, 100000)
    run_murtoluku(a, b)
    print("\n")

