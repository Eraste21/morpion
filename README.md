# Morpion en Python

Petit jeu de morpion pour deux joueurs, réalisé en programmation orientée objet avec Python et Tkinter.

## Fonctionnalités

- Grille de jeu composée de 9 boutons
- Joueur 1 représenté par un `X` bleu
- Joueur 2 représenté par un `O` rouge
- Affichage du joueur dont c'est le tour
- Détection des victoires et des matchs nuls
- Affichage du résultat dans une fenêtre secondaire
- Score conservé entre les parties
- Boutons pour recommencer ou quitter le jeu

## Prérequis

- Python 3 installé sur l'ordinateur
- Tkinter, généralement inclus avec Python

## Lancer le jeu

Ouvrir un terminal dans le dossier du projet, puis exécuter :

```powershell
python morpion.py
```

## Règles

Les joueurs jouent chacun leur tour en cliquant sur une case vide.

- Joueur 1 place les `X`
- Joueur 2 place les `O`
- Le premier joueur qui aligne trois symboles horizontalement, verticalement ou en diagonale gagne la partie
- Si toutes les cases sont remplies sans alignement, la partie se termine par un match nul

## Structure du projet

```text
morpion/
├── morpion.py  # Code principal du jeu
└── README.md   # Documentation du projet
```
