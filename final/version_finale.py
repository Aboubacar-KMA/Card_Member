"""
© Aboubacar M'houmadi
© Ewen FLEURY
"""

import tkinter as tk
from tkinter import ttk

def submit_form():
    file_choice = file_combobox.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    status = status_combobox.get()
    is_referent = referent_var.get()
    is_bureau = bureau_var.get()
    identifier = identifier_entry.get()

    # Vous pouvez faire ce que vous voulez avec les données ici, par exemple les imprimer
    print(f"File Choice: {file_choice}")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Status: {status}")
    print(f"Is Referent: {is_referent}")
    print(f"Is Bureau: {is_bureau}")
    print(f"Identifier: {identifier}")

def actualiserSelectionImage(_=None):
    print(file_combobox.get())

# Création de la fenêtre principale
root = tk.Tk()
root.geometry("600x300")
root.resizable(False, False)
root.title("Formulaire")

formulaire = ttk.Frame()
formulaire.grid(column=0)

# Choix de fichier (combobox)
file_label = ttk.Label(formulaire, text="Choix de fichier:")
file_label.grid(row=0, column=0, padx=10, pady=10)

file_options = ["Carte HxH", "Fichier 2", "Fichier 3"]
file_combobox = ttk.Combobox(formulaire, values=file_options)
file_combobox.bind("<<ComboboxSelected>>", actualiserSelectionImage)
file_combobox.current(0)
actualiserSelectionImage()
file_combobox.grid(row=0, column=1, padx=10, pady=10)

# Nom
first_name_label = ttk.Label(formulaire, text="Nom:")
first_name_label.grid(row=1, column=0, padx=10, pady=10)

first_name_entry = ttk.Entry(formulaire)
first_name_entry.grid(row=1, column=1, padx=10, pady=10)

# Prénom
last_name_label = ttk.Label(formulaire, text="Prénom:")
last_name_label.grid(row=2, column=0, padx=10, pady=10)

last_name_entry = ttk.Entry(formulaire)
last_name_entry.grid(row=2, column=1, padx=10, pady=10)

# Status
status_label = ttk.Label(formulaire, text="Status:")
status_label.grid(row=3, column=0, padx=10, pady=10)
status_combobox = ttk.Combobox(formulaire, values=["Membre", "Trésorier", "Secrétaire", "Président"], state="readonly")
status_combobox.current(0)
status_combobox.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

# Case à cocher pour le référent
referent_var = tk.BooleanVar()
referent_checkbox = ttk.Checkbutton(formulaire, text="Référent", variable=referent_var)
referent_checkbox.grid(row=4, column=0, padx=10, pady=10)

# Case à cocher pour le bureau
bureau_var = tk.BooleanVar()
bureau_checkbox = ttk.Checkbutton(formulaire, text="Bureau", variable=bureau_var)
bureau_checkbox.grid(row=4, column=1, padx=10, pady=10)

# Identifiant
identifier_label = ttk.Label(formulaire, text="Identifiant:")
identifier_label.grid(row=5, column=0, padx=10, pady=10)

identifier_entry = ttk.Entry(formulaire)
identifier_entry.grid(row=5, column=1, padx=10, pady=10)

# Bouton Soumettre
submit_button = ttk.Button(formulaire, text="Soumettre", command=submit_form)
submit_button.grid(row=6, column=0, columnspan=2, pady=10)

canvas = tk.Canvas(root, width=300, height=300)
canvas.grid(column=1)

# Lancement de la boucle principale
root.mainloop()
