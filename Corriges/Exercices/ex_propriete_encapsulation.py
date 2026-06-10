# Exercice propriete, encapsulation et destructeur
# Créez une classe Animal :
#     Attributs privés : _nom, _age
#     Propriétés pour accéder et modifier nom et age avec vérification (âge >= 0).
#     Une méthode parler() qui affiche "L'animal fait un bruit."
#     Un destructeur (__del__) qui affiche :
#     "{nom} a été retiré du zoo."
# Créez deux classes filles :
#     Chien, redéfinit parler() → affiche "{nom} aboie : Woof!"
#     Chat,  redéfinit parler() → affiche "{nom} miaule : Miaou!"
# Créez une fonction faire_parler(animaux) qui prend une liste d’objets Animal et appelle leur méthode parler().


# Classe Animal
class Animal:
    """Classe définisant un animal au sens général."""

    # Constructeur
    def __init__(self, nom="mon animal", age=0):
        """Constructeur classe Animal."""
        # Valeurs par defaut avant de passer par les setters
        self._nom = ""
        self._age = 0

        # Attribution des valeur par setteurs.
        self.nom = nom
        self.age = age

    # Proprietes
    @property
    def nom(self):
        """Getteur pour le nom de l'animal."""
        return self._nom

    @property
    def age(self):
        """Getteur pour l'age de l'animal."""
        return self._age

    @age.setter
    def age(self, age):
        """Setter pour mofier l'age."""
        if isinstance(age, float | int): 
            if age < 0:
                print("L'âge ne peut pas être négatif.")
            else:
                self._age = age
        else:
            print("L'âge doit etre un nombre.")
    
    @nom.setter
    def nom(self, nom):
        """Setter pour mofier le nom."""
        self._nom = nom

    # Methode parler
    def parler(self):
        """Methode qui fait parler un animal."""
        print(f"L'animal {self.nom} fait un bruit.")

    # Destructeur
    def __del__(self):
        """Destructeur."""
        print(f"{self.nom} a été retiré du zoo.")

    def affiche_info(self):
        """Affichage des infos sur l'animal."""
        print(f"L'animal {self.nom} à {self.age} ans.")
    

# Classe Chien
class Chien(Animal):
    """Classe définisant un chien."""
    def __init__(self, nom, age):
        """Constructeur classe Chien."""
        super().__init__(nom, age)
    
    def parler(self):
        """Methode qui fait parler un chien."""
        print(f"{self.nom} aboie : Woof!")

    def affiche_info(self):
        """Affichage des infos sur le chien."""
        print(f"Le chien {self.nom} à {self.age} ans.")


# Classe Chat
class Chat(Animal):
    """Classe définisant un chien."""
    def __init__(self, nom, age):
        """Constructeur classe Chat."""
        super().__init__(nom, age)
    
    def parler(self):
        """Methode qui fait parler le chat."""
        print(f"{self.nom} miaule : Miaou!")

    def affiche_info(self):
        """Affichage des infos sur le chat."""
        print(f"Le chat {self.nom} à {self.age} ans.")


# Fonction qui fait parler un animal
def faire_parler(animaux: list[Animal]):
    """Methode qui fait parler tous les animaux."""
    for animal in animaux:
        animal.parler()

# Programme principal
def main():
    """Fonction principale."""
    animal = Animal("toto", 4)
    rex = Chien("Rex", 5)
    minou = Chat("Minou", 3)

    animal.affiche_info()
    rex.affiche_info()
    minou.affiche_info()
    print()

    liste_animaux: list[Animal] = [animal, rex, minou]
    faire_parler(liste_animaux)
    print()

    animal.age = "toto"
    animal.affiche_info()
    print()

# Point d'netree du programme principal.
if __name__ == "__main__":
    main()

    # La fin de programme Déclenche le destrcuteur __del__ pour chaque objet crée.
