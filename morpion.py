import tkinter as tk


class Morpion:
    """Jeu de morpion simple pour deux joueurs."""

    def __init__(self, fenetre):
        # La fenêtre principale est reçue lors de la création du jeu.
        self.fenetre = fenetre
        self.fenetre.title("Morpion")
        self.fenetre.geometry("650x750")
        self.fenetre.resizable(False, False)
        self.fenetre.config(bg="#202124")

        # X commence toujours la partie.
        self.joueur_actuel = "X"
        self.partie_terminee = False
        self.scores = {"X": 0, "O": 0}

        # Cette liste contiendra les neuf boutons de la grille.
        self.boutons = []

        self.creer_interface()

    def creer_interface(self):
        """Crée le titre, le score, le texte du tour et la grille."""

        # Le titre du jeu est affiché en grand en haut de la fenêtre.
        tk.Label(
            self.fenetre,
            text="MORPION",
            font=("Arial", 30, "bold"),
            fg="blue",
            bg="#202124",
        ).pack(pady=(25, 10))

        # Le score reste affiché pendant toutes les parties.
        self.label_score = tk.Label(
            self.fenetre,
            text="Joueur 1 : 0     Joueur 2 : 0",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#202124",
        )
        self.label_score.pack(pady=10)

        # Ce label indique quel joueur doit jouer.
        titre = tk.Label(
            self.fenetre,
            text="Au tour de Joueur 1",
            font=("Arial", 16),
            fg="white",
            bg="#202124",
        )
        titre.pack(pady=10)
        self.label_tour = titre

        # Une frame permet de regrouper et centrer les neuf cases.
        cadre_grille = tk.Frame(self.fenetre, bg="#202124")
        cadre_grille.pack(pady=15)

        # Les deux boucles permettent de construire une grille de 3 lignes
        # et 3 colonnes.
        for ligne in range(3):
            ligne_boutons = []

            for colonne in range(3):
                bouton = tk.Button(
                    cadre_grille,
                    text="",
                    font=("Arial", 24, "bold"),
                    width=6,
                    height=3,
                    # l et c mémorisent la position propre à chaque bouton.
                    command=lambda l=ligne, c=colonne: self.jouer(l, c),
                )
                bouton.grid(row=ligne, column=colonne, padx=3, pady=3)
                ligne_boutons.append(bouton)

            self.boutons.append(ligne_boutons)

    def jouer(self, ligne, colonne):
        """Place le symbole du joueur dans la case sélectionnée."""

        bouton = self.boutons[ligne][colonne]

        # Une case déjà utilisée ne peut plus être jouée.
        if bouton["text"] != "" or self.partie_terminee:
            return

        couleur = "blue" if self.joueur_actuel == "X" else "red"
        bouton.config(text=self.joueur_actuel, fg=couleur)

        # Après chaque coup, on recherche une victoire ou un match nul.
        if self.verifier_victoire():
            self.partie_terminee = True
            self.scores[self.joueur_actuel] += 1
            self.actualiser_score()
            nom = self.nom_joueur()
            self.afficher_resultat(f"{nom} a gagné !")
        elif self.grille_pleine():
            self.partie_terminee = True
            self.afficher_resultat("Match nul !")
        else:
            self.changer_joueur()

    def verifier_victoire(self):
        """Renvoie True si le joueur actuel possède trois symboles alignés."""

        # On récupère le texte de chaque bouton pour obtenir une grille simple.
        grille = [[bouton["text"] for bouton in ligne] for ligne in self.boutons]

        # Une victoire est possible sur une ligne, une colonne ou une diagonale.
        combinaisons = [
            # Lignes
            [grille[0][0], grille[0][1], grille[0][2]],
            [grille[1][0], grille[1][1], grille[1][2]],
            [grille[2][0], grille[2][1], grille[2][2]],
            # Colonnes
            [grille[0][0], grille[1][0], grille[2][0]],
            [grille[0][1], grille[1][1], grille[2][1]],
            [grille[0][2], grille[1][2], grille[2][2]],
            # Diagonales
            [grille[0][0], grille[1][1], grille[2][2]],
            [grille[0][2], grille[1][1], grille[2][0]],
        ]

        # La liste [X, X, X] ou [O, O, O] doit être présente.
        return [self.joueur_actuel] * 3 in combinaisons

    def grille_pleine(self):
        """Renvoie True lorsque toutes les cases ont été jouées."""

        return all(
            bouton["text"] != ""
            for ligne in self.boutons
            for bouton in ligne
        )

    def changer_joueur(self):
        """Passe du joueur X au joueur O, ou inversement."""

        self.joueur_actuel = "O" if self.joueur_actuel == "X" else "X"
        self.label_tour.config(
            text=f"Au tour de {self.nom_joueur()}"
        )

    def nom_joueur(self):
        """Renvoie le nom correspondant au symbole du joueur actuel."""

        return "Joueur 1" if self.joueur_actuel == "X" else "Joueur 2"

    def actualiser_score(self):
        """Met à jour le score visible dans la fenêtre principale."""

        self.label_score.config(
            text=f"Joueur 1 : {self.scores['X']}     "
            f"Joueur 2 : {self.scores['O']}"
        )

    def afficher_resultat(self, message):
        """Affiche le résultat dans une nouvelle fenêtre Toplevel."""

        resultat = tk.Toplevel(self.fenetre)
        resultat.title("Résultat")
        resultat.resizable(False, False)
        resultat.config(bg="#202124")
        resultat.transient(self.fenetre)
        resultat.grab_set()
        resultat.protocol("WM_DELETE_WINDOW", self.fenetre.destroy)

        tk.Label(
            resultat,
            text=message,
            font=("Arial", 15),
            fg="white",
            bg="#202124",
        ).pack(
            padx=30,
            pady=20,
        )

        cadre_boutons = tk.Frame(resultat, bg="#202124")
        cadre_boutons.pack(padx=20, pady=(0, 20))

        tk.Button(
            cadre_boutons,
            text="Recommencer",
            width=12,
            command=lambda: self.recommencer(resultat),
        ).pack(side="left", padx=5)

        tk.Button(
            cadre_boutons,
            text="Quitter",
            width=12,
            command=self.fenetre.destroy,
        ).pack(side="left", padx=5)

        # Le Toplevel est centré au-dessus de la fenêtre principale.
        resultat.update_idletasks()
        x = self.fenetre.winfo_x() + (self.fenetre.winfo_width() - resultat.winfo_width()) // 2
        y = self.fenetre.winfo_y() + (self.fenetre.winfo_height() - resultat.winfo_height()) // 2
        resultat.geometry(f"+{x}+{y}")

    def recommencer(self, fenetre_resultat):
        """Réinitialise les données et vide toutes les cases."""

        fenetre_resultat.destroy()
        self.joueur_actuel = "X"
        self.partie_terminee = False
        self.label_tour.config(text="Au tour de Joueur 1")

        for ligne in self.boutons:
            for bouton in ligne:
                bouton.config(text="", fg="black")


if __name__ == "__main__":
    # Point de départ du programme : création puis affichage de la fenêtre.
    fenetre = tk.Tk()
    jeu = Morpion(fenetre)
    fenetre.mainloop()
