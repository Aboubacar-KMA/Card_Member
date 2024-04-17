# Créé par amhoumadi, le 12/09/2023 en Python 3.7
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk  # Importer ttk pour la combobox
from PIL import Image, ImageDraw, ImageFont, ImageTk
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import VerticalGradiantColorMask, RadialGradiantColorMask

# Définir les coordonnées prédéfinies pour chaque image sous forme de listes de coordonnées
coordonnees_zones_de_texte = [(125, 1265), (715, 1265)]
# Fonction pour ajouter du texte à une zone de texte spécifique sur une imae
def ajouter_texte(texte, zone_index):
    # Charger l'image
    image = Image.open(imagePath)
    # Récupérer les coordonnées de la zone de texte correspondant à l'index
    coordonnees = coordonnees_zones_de_texte
    if 0 <= zone_index < len(coordonnees):
        # Sélectionner les coordonnées de la zone de texte spécifique
        x, y = coordonnees[zone_index]
        # Créer un objet ImageDraw pour dessiner sur l'image
        draw = ImageDraw.Draw(image)
        # Définir la police et la taille du texte
        font = ImageFont.truetype("arial", 55)
        # Ajouter le texte à l'image
        draw.text((x, y), texte, fill="black", font=font)
        # Enregistrer l'image modifiée
        sauvegarder_image(image, imagePath)
        afficher_image(imagePath)

def sauvegarder_image(imageASauvegarder: Image, cheminImage: str):
    qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=0)
    qr.add_data("https://popartech.com")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="#9BB7DB")
    imgPIL: Image.Image = img.get_image()
    imgPIL = imgPIL.resize((250, 250))
    imageASauvegarder.paste(imgPIL, (870, 1575))
    qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=0)
    qr.add_data("https://www.instagram.com/popartech")
    qr.make(fit=True)
    img = qr.make_image(image_factory=StyledPilImage, color_mask=VerticalGradiantColorMask((255, 255, 255), (253, 1, 193), (255, 188, 1)))
    imgPIL: Image.Image = img.get_image()
    imgPIL = imgPIL.resize((210, 210))
    imageASauvegarder.paste(imgPIL, (125, 870))
    qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=0)
    qr.add_data("https://twitter.com/PopArTech")
    qr.make(fit=True)
    img = qr.make_image(fill_color="#1AB2E8", back_color="white")
    imgPIL: Image.Image = img.get_image()
    imgPIL = imgPIL.resize((210, 210))
    imageASauvegarder.paste(imgPIL, (370, 870))
    qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=0)
    qr.add_data("https://www.facebook.com/PopArTech")
    qr.make(fit=True)
    img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask((255, 255, 255), (122, 216, 242), (24, 119, 242)))
    imgPIL: Image.Image = img.get_image()
    imgPIL = imgPIL.resize((210, 210))
    imageASauvegarder.paste(imgPIL, (615, 870))
    qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=0)
    qr.add_data("https://www.tiktok.com/@popartech")
    qr.make(fit=True)
    img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask((255, 255, 255), (255, 56, 55), (0, 0, 0)))
    imgPIL: Image.Image = img.get_image()
    imgPIL = imgPIL.resize((210, 210))
    imageASauvegarder.paste(imgPIL, (860, 870))
    imageASauvegarder.save(cheminImage)

# Fonction appelée lorsque le bouton "Parcourir" est cliqué
def parcourir_image():
    global imagePath
    imagePath = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.jpeg *.png *.gif")])
    newPath = imagePath[:imagePath.rfind('.')] + '.mod' + imagePath[imagePath.rfind('.'):]
    if imagePath:
        Image.open(imagePath).save(newPath)
        afficher_image(imagePath)
        imagePath = newPath

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
    zone_index = zone_texte_combobox.current() # Récupérer l'index de la zone de texte sélectionnée dans la combobox
    ajouter_texte(texte, zone_index)

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
zone_texte_combobox = ttk.Combobox(root, values=["Nom", "Prenom"], state="readonly")
zone_texte_combobox.pack()
zone_texte_combobox.current(0)

# Bouton "Ajouter Texte" pour ajouter du texte à l'image
ajouter_button = tk.Button(root, text="Ajouter Texte", command=ajouter_texte_interface)
ajouter_button.pack()


# Canvas pour afficher l'image
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Variable pour stocker le chemin de l'image
imagePath = ""

# Lancer la boucle principale de l'interface graphique
root.mainloop()
