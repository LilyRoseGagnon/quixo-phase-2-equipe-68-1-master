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

    def valider_horizontale(plateau, nb_pions=5):
        if nb_pions < 3 or nb_pions > 5:
            raise QuixoError("Le nombre de pions doit être entre 3 et 5.")
        
        dico = {'X': [], 'O': []}
        
        for ligne, liste in enumerate(plateau):
            n = 0
            x = 0
            for case in liste:
                if case == 'X':
                    n += 1
                if case == 'O':
                    x += 1
            if n >= nb_pions:
                dico['X'] += [[1, ligne+1], [5, ligne+1]]
            if x >= nb_pions:
                dico['O'] += [[1, ligne+1], [5, ligne+1]]

        return dico        

    def valider_verticale(plateau, nb_pions=5):
        if nb_pions < 3 or nb_pions > 5:
            raise QuixoError("Le nombre de pions doit être entre 3 et 5.")
        
        X_1 = 0
        X_2 = 0
        X_3 = 0
        X_4 = 0
        X_5 = 0
        O_1 = 0
        O_2 = 0
        O_3 = 0
        O_4 = 0
        O_5 = 0
        vert1 = [[1, 1], [1, 5]]
        vert2 = [[2, 1], [2, 5]]
        vert3 = [[3, 1], [3, 5]]
        vert4 = [[4, 1], [4, 5]]
        vert5 = [[5, 1], [5, 5]]
        dico = {'X': [], 'O': []}

        for liste in plateau:
            if liste[0] == 'X':
                X_1 += 1
            if liste[1] == 'X':
                X_2 += 1
            if liste[2] == 'X':
                X_3 += 1
            if liste[3] == 'X':
                X_4 += 1
            if liste[4] == 'X':
                X_5 += 1
            if liste[0] == 'O':
                O_1 += 1
            if liste[1] == 'O':
                O_2 += 1
            if liste[2] == 'O':
                O_3 += 1
            if liste[3] == 'O':
                O_4 += 1
            if liste[4] == 'O':
                O_5 += 1            

        if X_1 >= nb_pions:
            dico['X'] += vert1
        if X_2 >= nb_pions:
            dico['X'] += vert2
        if X_3 >= nb_pions:
            dico['X'] += vert3
        if X_4 >= nb_pions:
            dico['X'] += vert4
        if X_5 >= nb_pions:
            dico['X'] += vert5
        if O_1 >= nb_pions:
            dico['O'] += vert1
        if O_2 >= nb_pions:
            dico['O'] += vert2
        if O_3 >= nb_pions:
            dico['O'] += vert3
        if O_4 >= nb_pions:
            dico['O'] += vert4
        if O_5 >= nb_pions:
            dico['O'] += vert5

        return dico

    def partie_terminée():
        pass

    def trouver_coup_gagnant():
        pass

    def trouver_coup_bloquant():
        pass

    def jouer_le_coup():
        pass