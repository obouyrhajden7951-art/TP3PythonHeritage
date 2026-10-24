class Document:
    def __init__(self, intitule, annee_pub):
        self.intitule = intitule
        self.annee_pub = annee_pub

    def afficher(self):
        print(f"{self.intitule} ({self.annee_pub})")


class Livre(Document):
    def __init__(self, intitule, annee_pub, ecrivain):
        super().__init__(intitule, annee_pub)
        self.ecrivain = ecrivain

    def afficher(self):
        print(f"Livre: {self.intitule} par {self.ecrivain} ({self.annee_pub})")


class Magazine(Document):
    def __init__(self, intitule, annee_pub, num_edition):
        super().__init__(intitule, annee_pub)
        self.num_edition = num_edition

    def afficher(self):
        print(f"Magazine: {self.intitule} No. {self.num_edition} ({self.annee_pub})")


# Test
collection = [
    Livre("1984", 1949, "George Orwell"),
    Magazine("Science & Vie", 2023, 456),
    Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry")
]

for doc in collection:
    doc.afficher()