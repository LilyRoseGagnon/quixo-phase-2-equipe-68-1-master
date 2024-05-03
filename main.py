"""Jeu Quixo

Ce programme permet de joueur au jeu Quixo.
"""
from api import débuter_partie, jouer_coup, lister_parties
from quixo import Quixo, analyser_commande, formater_les_parties
from quixo_ia import QuixoIA
from plateau import Plateau

# Mettre ici votre secret récupérer depuis le site de PAX
SECRET = "8e8b6465-4770-4d87-9732-556be32d6786"


if __name__ == "__main__":
    args = analyser_commande()
    if args.parties:
        parties = lister_parties(args.idul, SECRET)
        print(formater_les_parties(parties))
    if args.automatique:
        id_partie, joueurs, plateau = débuter_partie(args.idul, SECRET)
        while True:
            # Créer une instance de Quixo
            quixo = Quixo(joueurs, plateau)
            # Afficher la partie
            print(quixo)
            # Jouer le coup
            QuixoIA.jouer_le_coup()
            print(Plateau.self.plateau)
            if QuixoIA.partie_terminée(Plateau.self.plateau) is True:
                print(QuixoIA.partie_terminée(Plateau.self.plateau))
    else:
        id_partie, joueurs, plateau = débuter_partie(args.idul, SECRET)
        while True:
            # Créer une instance de Quixo
            quixo = Quixo(joueurs, plateau)
            # Afficher la partie
            print(quixo)
            # Demander au joueur de choisir son prochain coup
            origine, direction = quixo.récupérer_le_coup()
            # Envoyez le coup au serveur
            id_partie, joueurs, plateau = jouer_coup(
                id_partie,
                origine,
                direction,
                args.idul,
                SECRET,
            )
