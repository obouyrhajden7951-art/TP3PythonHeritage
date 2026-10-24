class Employe:
    def __init__(self, nom_emp, salaire_de_base):
        self.nom_emp = nom_emp
        self.salaire_de_base = salaire_de_base

    def salaire_total(self):
        return self.salaire_de_base

    def __str__(self):
        return f"{self.nom_emp} gagne {self.salaire_total()} €"


class Manager(Employe):
    def __init__(self, nom_emp, salaire_de_base, montant_prime):
        super().__init__(nom_emp, salaire_de_base)
        self.montant_prime = montant_prime

    def salaire_total(self):
        return self.salaire_de_base + self.montant_prime


class Developpeur(Employe):
    def __init__(self, nom_emp, salaire_de_base, techno):
        super().__init__(nom_emp, salaire_de_base)
        self.techno = techno

    def salaire_total(self):
        supplement = 500 if self.techno == 'Python' else 300
        return self.salaire_de_base + supplement


if __name__ == '__main__':
    emp1 = Employe("Alice", 2000)
    mgr = Manager("Bob", 2500, 800)
    dev = Developpeur("Charlie", 2200, "Python")

    for salarie in [emp1, mgr, dev]:
        print(salarie)