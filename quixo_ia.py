from quixo import Quixo
from plateau import Plateau
from quixo_error import QuixoError


class QuixoIA(Quixo):
    def valider_diagonale(plateau, nb_pions=5):
        if nb_pions < 3 or nb_pions > 5:
            raise QuixoError("Le nombre de pions doit être entre 3 et 5.")
        
        n = 0
        m = 0
        x = 0
        y = 0
        diago_1 = [1, 1], [5, 5]
        diago_2 = [1, 5], [5, 1]
        dico = {'X': [], 'O': []}
        
        for ligne, liste in enumerate(plateau):
            if liste[ligne] == 'X':
                n += 1
            if liste[ligne] == 'O':
                x += 1
            if liste[4-ligne] == 'X':
                m += 1
            if liste[4-ligne] == 'O':
                y += 1

        if n >= nb_pions:
            dico['X'] = diago_1
        if m >= nb_pions:
            dico['X'] = diago_2
        if x >= nb_pions:
            dico['O'] = diago_1
        if y >= nb_pions:
            dico['O'] = diago_2

        return dico

    def valider_horizontale():
        pass

    def valider_verticale():
        pass

    def partie_terminée():
        pass

    def trouver_coup_gagnant():
        pass

    def trouver_coup_bloquant():
        pass

    def jouer_le_coup():
        pass