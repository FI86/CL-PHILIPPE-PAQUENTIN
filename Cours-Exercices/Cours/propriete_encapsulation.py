
# Fichier d'exemple de proprietes et d'encapsulation

# Class Vehicule

    # Propriétés en lecture

    # Propriétés en écriture

    # Propriété en suppression


# Class Voiture


def main():
    pass
    # Bonne pratique

    # Par convention le _ indique que l'attribut est privé
    # mais cela ne provoque pas d'erreur d'y accéder
    # Mauvaise pratique

    # Ne provoque pas d'erreur, mais cree comme un autre attribut d'objet
    # au lieu d'utiliser l'attribut demande.
    # Mauvaise pratique
    # v.__nbRoues = 10
    # Bonne pratique

    # Mauvaise pratique
    # print(v.__nbRoues)

if __name__ == "__main__":
    main()
    