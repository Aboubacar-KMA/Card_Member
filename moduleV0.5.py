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
donnes = {"recto-paint.png": {"coordonnesNom": (125, 1265), "coordonnesPrenom": (715, 1265), "coordonnesStatut": (110, 1435), "coordonnesDeuxiemeStatut": (110, 1485), "coordonnesBureauStatut": (110, 1535), "coordonnesIdentifiant": (110, 1675)}}
# Fonction pour ajouter du texte à une zone de texte spécifique sur une imae
def ajouter_texte(texte: str, coordonnees: tuple[int, int], fontSize=55, fontType: str="arial", fontColor: str="black"):
    # Sélectionner les coordonnées de la zone de texte spécifique
    x, y = coordonnees
    # Créer un objet ImageDraw pour dessiner sur l'image
    draw = ImageDraw.Draw(image)
    # Définir la police et la taille du texte
    font = ImageFont.truetype(fontType, fontSize)
    # Ajouter le texte à l'image
    draw.text((x, y), texte, fill=fontColor, font=font)

def sauvegarder_image_pour_de_vrai():
    image.save(imagePath)

def sauvegarder_image():
    tailleQRCodes = 210
    tailleIcones = 50
    pos = ((tailleQRCodes - tailleIcones) // 2, (tailleQRCodes - tailleIcones) // 2)
    # QR Code vers le site :
    qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=0)
    qr.add_data("https://popartech.com")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="#9BB7DB")
    imgPIL: Image.Image = img.get_image()
    imgPIL = imgPIL.resize((390, 390))
    image.paste(imgPIL, (710, 1435))
    # Url vers le site au dessus du QR Code vers le site:
    ajouter_texte("https://popartech.com", (710, 1385), fontSize=37, fontType="arialbd", fontColor="black")
    # Impression du status du memebre sur la carte :
    ajouter_texte("Statut du membre :", (110, 1385), fontSize=53, fontType="arialbd", fontColor="black")
    # Impression de l'indentifiant du membre sur la carte :
    ajouter_texte("Identifiant du membre :", (110, 1625), fontSize=53, fontType="arialbd", fontColor="black")
    # QR Code vers l'instagram :
    qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=0)
    qr.add_data("https://www.instagram.com/popartech")
    qr.make(fit=True)
    img = qr.make_image(image_factory=StyledPilImage, color_mask=VerticalGradiantColorMask((255, 255, 255), (253, 1, 193), (255, 188, 1)))
    imgPIL: Image.Image = img.get_image()
    imgPIL = imgPIL.resize((210, 210))
    imgPIL.paste(Image.open("instagram.webp").resize((tailleIcones, tailleIcones)), pos)
    image.paste(imgPIL, (125, 870))
    # QR Code vers le Twitter :
    qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=0)
    qr.add_data("https://twitter.com/PopArTech")
    qr.make(fit=True)
    img = qr.make_image(fill_color="#1AB2E8", back_color="white")
    imgPIL: Image.Image = img.get_image()
    imgPIL = imgPIL.resize((210, 210))
    imgPIL.paste(Image.open("twitter.webp").resize((tailleIcones, tailleIcones)), pos)
    image.paste(imgPIL, (370, 870))
    # QR Code vers le Facebook :
    qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=0)
    qr.add_data("https://www.facebook.com/PopArTech")
    qr.make(fit=True)
    img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask((255, 255, 255), (122, 216, 242), (24, 119, 242)))
    imgPIL: Image.Image = img.get_image()
    imgPIL = imgPIL.resize((210, 210))
    imgPIL.paste(Image.open("facebook.png").resize((tailleIcones, tailleIcones)), pos)
    image.paste(imgPIL, (615, 870))
    # QR Code vers le Tiktok :
    qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=0)
    qr.add_data("https://www.tiktok.com/@popartech")
    qr.make(fit=True)
    img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask((255, 255, 255), (182, 182, 182), (0, 0, 0)))
    imgPIL: Image.Image = img.get_image()
    imgPIL = imgPIL.resize((210, 210))
    imgPIL.paste(Image.open("tiktok.png").resize((tailleIcones, tailleIcones)), pos)
    image.paste(imgPIL, (860, 870))

    sauvegarder_image_pour_de_vrai()

# Fonction appelée lorsque le bouton "Parcourir" est cliqué
def parcourir_image():
    global imagePath, image, imageName
    imagePathTemp = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.jpeg *.png *.gif")])
    newPath = imagePathTemp[:imagePathTemp.rfind('.')] + '.mod' + imagePathTemp[imagePathTemp.rfind('.'):]
    if imagePathTemp:
        imageName = imagePathTemp[imagePathTemp.rfind("/")+1:]
        print(f"{imageName = }")
        Image.open(imagePathTemp).save(newPath)
        imagePath = newPath
        rechargerImage()
        # Enregistrer l'image modifiée
        sauvegarder_image()
        # Charger l'image sur l'écran
        afficher_image()

def rechargerImage():
    global image
    image = Image.open(imagePath)

# Fonction pour afficher l'image sur le canvas
def afficher_image():
    global image
    image2 = Image.open(imagePath)
    image2.thumbnail((300, 300))  # Réduire la taille de l'image pour l'afficher sur le canvas
    img = ImageTk.PhotoImage(image=image2)

    # Mettre à jour l'image affichée sur le canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=img)
    canvas.image = img  # Conserver une référence à l'objet PhotoImage pour éviter la suppression par le garbage collector

# Fonction appelée lorsque le bouton "Ajouter Texte" est cliqué
def ajouter_texte_interface():
    texte = texte_entry.get()
    zone_index = zone_texte_combobox.current() # Récupérer l'index de la zone de texte sélectionnée dans la combobox
    if zone_index == 0:
        ajouter_texte(texte, donnes[imageName]["coordonnesNom"])
    elif zone_index == 1:
        ajouter_texte(texte, donnes[imageName]["coordonnesPrenom"])
    elif zone_index == 2:
        ajouter_texte(texte, donnes[imageName]["coordonnesStatut"], fontSize=50, fontType="arial", fontColor="black")
    elif zone_index == 3:
        ajouter_texte("Référent", donnes[imageName]["coordonnesDeuxiemeStatut"], fontSize=50, fontType="arial", fontColor="black")
    elif zone_index == 4:
        ajouter_texte("Bureau", donnes[imageName]["coordonnesBureauStatut"], fontSize=50, fontType="arial", fontColor="black")
    elif zone_index == 5:
        ajouter_texte(texte, donnes[imageName]["coordonnesIdentifiant"], fontSize=50, fontType="arial", fontColor="black")
    sauvegarder_image_pour_de_vrai()
    rechargerImage()
    afficher_image()

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
zone_texte_combobox = ttk.Combobox(root, values=["Nom", "Prenom", "Statut", "Est référent ?", "Est du bureau ?", "Identifiant"], state="readonly")
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

imageName = ""

image: Image

# Lancer la boucle principale de l'interface graphique
root.mainloop()
