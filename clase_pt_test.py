import math


class Dreptunghi:
    lungime = 0
    latime = 0
    culoare = ''

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Dreptunghiul are culoarea {self.culoare}, are lungimea {self.lungime} si latimea {self.latime}')

    def aria(self):
        return self.latime * self.lungime

    def perimetru(self):
        return 2 * (self.latime + self.lungime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


class Cerc:
    raza = 0
    culoare = ''

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Culoarea cercului este {self.culoare} si raza cercului este {self.raza}')

    def aria(self):
        return math.floor(math.pi * (self.raza ** 2))

    def diametru(self):
        return math.floor(self.raza * 2)

    def circumferinta(self):
        return math.floor(2 * self.raza * math.pi)


class Angajat:
    nume = ''
    prenume = ''
    salariu = 0

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Angajatul cu numele {self.nume} si prenumele {self.prenume} are salariul {self.salariu}')

    def nume_complet(self):
        return self.nume+' '+self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        return self.salariu + ((self.salariu * procent)/100)


class Cont:
    iban = ''
    titular_cont = ''
    sold = 0

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

    def debitare_cont(self, suma):
        self.sold -= suma
        return self.sold

    def creditare_cont(self, suma):
        self.sold += suma
        return self.sold