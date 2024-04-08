"""Module Quixo

Classes:
    * Quixo - Classe principale du jeu Quixo.
    * QuixoError - Classe d'erreur pour le jeu Quixo.

Functions:
    * analyser_commande - Génère un interpréteur de commande.
    * formater_les_parties - Formater la liste des dernières parties.
"""
import argparse

from plateau import Plateau
from quixo_error import QuixoError


class Quixo:
    def __init__(self, joueurs, plateau=None) -> None:
        self.joueurs = joueurs
        self.plateau = Plateau(plateau)

    def état_partie(self):
        return {
            "joueurs": self.joueurs,
            "plateau": self.plateau.état_plateau(),
        }

    def __str__(self):
        joueur1 = self.joueurs[0]
        joueur2 = self.joueurs[1]
        légende = f'Légende: X={joueur1}, O={joueur2}\n'

        état = Plateau.__str__(self.plateau)

        return légende + état

    def déplacer_pion(self, pion, origine, direction):
        """Déplacer un pion dans une direction donnée.

        Applique le changement au Plateau de jeu

        Args:
            pion (str): Le pion à déplacer, soit "X" ou "O".
            origine (list[int]): La position (x, y) du pion sur le plateau.
            direction (str): La direction du déplacement, soit "haut", "bas", "gauche" ou "droite".
        """
        Plateau.insertion(self.plateau, pion, origine, direction)

    def récupérer_le_coup(self):
        """Demander le prochain coup à jouer au joueur.

        Déplacer le code de votre fonction récupérer_le_coup ici et ajuster le en conséquence.
        Vous devez maintenant valider les entrées de l'utilisateur.

        Returns:
            tuple: Tuple de 2 éléments composé de l'origine du bloc à déplacer et de sa direction.
                L'origine est une liste de 2 entiers [x, y].
                La direction est une chaîne de caractères.

        Raises:
            QuixoError: Les positions x et y doivent être entre 1 et 5 inclusivement.
            QuixoError: La direction doit être "haut", "bas", "gauche" ou "droite".

        Examples:
            Donnez la position d'origine du bloc (x,y) :
            Quelle direction voulez-vous insérer? ('haut', 'bas', 'gauche', 'droite') :
        """
        origine = input("Donnez la position d'origine du bloc (x,y) :")
        origine = list(origine)
        origine.remove(',')
        for element in origine[:]:
            origine.remove(element)
            origine.append(int(element))

        for coordonnée in origine:
            if coordonnée < 1 or coordonnée > 5:
                raise QuixoError('QuixoError: Les positions x et y doivent être entre 1 et 5 inclusivement.')

        direction = input("Quelle direction voulez-vous insérer? ('haut', 'bas', 'gauche', 'droite') :")

        if direction != 'haut' and direction != 'bas' and direction != 'gauche' and direction != 'droite':
            raise QuixoError('QuixoError: La direction doit être "haut", "bas", "gauche" ou "droite".')

        return origine, direction


def analyser_commande():
    parser = argparse.ArgumentParser()

    # Complétez le code ici
    # vous pourriez aussi avoir à ajouter des arguments dans ArgumentParser(...)
    
    parser.add_argument('idul', help='IDUL du joueur')
    parser.add_argument('-p', '--parties', 
                        help='Lister les parties existantes', action='store_true')

    return parser.parse_args()


def formater_les_parties(parties):
    sortie = ''
    for indice, partie in enumerate(parties):
        index = indice + 1
        datetime = partie['date']
        joueur1 = partie['joueurs'][0]
        joueur2 = partie['joueurs'][1]
        joueur_gagnant = partie['gagnant']

        sortie += f'{index} : ' + datetime + ', ' + joueur1 + ' vs ' + joueur2

        if joueur_gagnant == joueur1 or joueur_gagnant == joueur2:
            sortie += ', gagnant: ' + joueur_gagnant

        sortie += '\n'

    return sortie