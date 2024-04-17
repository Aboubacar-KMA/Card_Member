import tkinter as tk               # Importer la bibliothèque Tkinter pour créer une interface graphique
from tkinter import filedialog    # Importer filedialog pour gérer les boîtes de dialogue de sélection de fichier
from PIL import Image, ImageDraw, ImageFont, ImageTk  # Importer la bibliothèque Pillow pour la manipulation d'images

# Définir les coordonnées prédéfinies pour chaque image
coordonnees_zones_de_texte = {
    "image1": (100, 100, 400, 200),  # Coordonnées de la zone de texte pour image1.jpg
    "image2.jpg": (50, 50, 300, 150),    # Coordonnées de la zone de texte pour image2.jpg
    # Ajoutez d'autres images et coordonnées ici
}

# Fonction pour ajouter du texte à une image
def ajouter_texte(image_path, texte):
    # Charger l'image
    image = Image.open(image_path)

    # Récupérer les coordonnées de la zone de texte correspondant à l'image
    coordonnees = coordonnees_zones_de_texte.get(image_path)

    if coordonnees:
        # Créer un objet ImageDraw pour dessiner sur l'image
        draw = ImageDraw.Draw(image)

        # Définir la police et la taille du texte
        font = ImageFont.load_default()
        font_size = 20

        # Définir la position de la zone de texte
        x, y, largeur, hauteur = coordonnees

        # Calculer la largeur et la hauteur du texte
        text_width, text_height = draw.textsize(texte, font=font)

        # Calculer la position pour centrer le texte dans la zone de texte
        x = x + (largeur - text_width) / 2
        y = y + (hauteur - text_height) / 2

        # Ajouter le texte à l'image
        draw.text((x, y), texte, fill="white", font=font)

        # Enregistrer l'image modifiée
        image.save("image_modifiee.jpg")

        print("Texte ajouté à l'image. L'image modifiée a été enregistrée sous 'image_modifiee.jpg'.")
    else:
        print("L'image n'a pas de coordonnées de zone de texte prédéfinies.")

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
    ajouter_texte(image_path, texte)

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Ajouter du Texte à une Image")

# Créer un bouton "Parcourir" pour sélectionner une image
parcourir_button = tk.Button(root, text="Parcourir", command=parcourir_image)
parcourir_button.pack()

# Entrée pour saisir le texte
texte_entry = tk.Entry(root, width=30)
texte_entry.pack()

# Bouton "Ajouter Texte" pour ajouter du texte à l'image
ajouter_button = tk.Button(root, text="Ajouter Texte", command=ajouter_texte_interface)
ajouter_button.pack()

# Canvas pour afficher l'image
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Variable pour stocker le chemin de l'image
image_path = ""

# Lancer la boucle principale de l'interface graphique
root.mainloop()
