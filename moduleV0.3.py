# Créé par amhoumadi, le 12/09/2023 en Python 3.7

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Définir les coordonnées prédéfinies pour chaque image sous forme de listes de coordonnées
coordonnees_zones_de_texte = {
    "image1.jpg": [
        (50, 50, 200, 100),  # Zone de texte 1 pour image1.jpg
        (10, 10, 100, 50),   # Zone de texte 2 pour image1.jpg (coin gauche)
    ],
    "image2.jpg": [
        (80, 80, 250, 120),  # Zone de texte 1 pour image2.jpg
        # Ajoutez d'autres zones de texte pour image2.jpg ici
    ],
    # Ajoutez d'autres images et leurs zones de texte ici
}

# Fonction pour ajouter du texte à une zone de texte spécifique sur une image
def ajouter_texte(image_path, texte, zone_index):
    # Charger l'image
    image = Image.open(image_path)

    # Récupérer les coordonnées de la zone de texte correspondant à l'index
    coordonnees = coordonnees_zones_de_texte.get(image_path)

    if coordonnees and 0 <= zone_index < len(coordonnees):
        # Sélectionner les coordonnées de la zone de texte spécifique
        x, y, largeur, hauteur = coordonnees[zone_index]

        # Créer un objet ImageDraw pour dessiner sur l'image
        draw = ImageDraw.Draw(image)

        # Définir la police et la taille du texte
        font = ImageFont.load_default()
        font_size = 20

        # Calculer la position pour centrer le texte dans la zone de texte
        x = x + (largeur - font_size * len(texte)) / 2
        y = y + (hauteur - font_size) / 2

        # Ajouter le texte à l'image
        draw.text((x, y), texte, fill="white", font=font)

        # Enregistrer l'image modifiée
        image.save("image_modifiee.jpg")

        print("Texte ajouté à la zone de texte {}. L'image modifiée a été enregistrée sous 'image_modifiee.jpg'.".format(zone_index))
    else:
        print("L'image n'a pas de zone de texte à l'index spécifié.")

# Fonction appelée lorsque le bouton "Parcourir" est cliqué
def parcourir_image():
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.jpeg *.png *.gif")])
    if image_path:
        afficher_image(image_path)

# Fonction pour afficher l'image sur le canvas
def afficher_image(image_path):
    image = Image.open(image_path)
    image.thumbnail((300, 300))  # Réduire la taille de l'image pour l'afficher sur le canvas
    img = ImageTk.PhotoImage(image=image)

    # Mettre à jour l'image affichée sur le canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=img)
    canvas.image = img  # Conserver une référence à l'objet PhotoImage pour éviter la suppression par le garbage collector

# Fonction appelée lorsque le bouton "Ajouter Texte" est cliqué
def ajouter_texte_interface():
    texte = texte_entry.get()
    zone_index = zone_texte_combobox.current()  # Récupérer l'index de la zone de texte sélectionnée dans la combobox
    ajouter_texte(image_path, texte, zone_index)

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Ajouter du Texte à une Image")

# Créer un bouton "Parcourir" pour sélectionner une image
parcourir_button = tk.Button(root, text="Parcourir", command=parcourir_image)
parcourir_button.pack()

# Entrée pour saisir le texte
texte_entry = tk.Entry(root, width=30)
texte_entry.pack()

# Combobox pour sélectionner la zone de texte
zone_texte_combobox = ttk.Combobox(root, values=[], state="readonly")
zone_texte_combobox.pack()

# Canvas pour afficher l'image
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Variable pour stocker le chemin de l'image
image_path = ""

# Lancer la boucle principale de l'interface graphique
root.mainloop()
