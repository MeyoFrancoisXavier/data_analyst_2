# Import de modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
# Pour la boite de dialogue
import tkinter as tk
from tkinter import simpledialog

file_path_1 = "./TP_fin_de_fomation/cleaned_chicago_city.csv"
file_path_2 = "./TP_fin_de_fomation/cleaned_new_york_city.csv"
file_path_3 = "./TP_fin_de_fomation/cleaned_washington_city.csv"
 
df1 = pd.read_csv(file_path_1)
df2 = pd.read_csv(file_path_2)
df3 = pd.read_csv(file_path_3)
 
# data_chicago = pd.read_csv(file_path_1)
# data_newyork = pd.read_csv(file_path_2)
# data_washington = pd.read_csv(file_path_3)

# df1 = pd.read_csv(data_chicago)
# df2 = pd.read_csv(data_newyork)
# df3 = pd.read_csv(data_washington)

# print(df1.shape)
# print(df2.shape)
# print(df3.shape)

# Nettoyage du datetime 

# data_chicago['Start Time'] = pd.to_datetime(data_chicago['Start Time'])
# data_chicago['End Time'] = pd.to_datetime(data_chicago['End Time'])
 
# data_newyork['Start Time'] = pd.to_datetime(data_newyork['Start Time'])
# data_newyork['End Time'] = pd.to_datetime(data_newyork['End Time'])
 
# data_washington['Start Time'] = pd.to_datetime(data_washington['Start Time'])
# data_washington['End Time'] = pd.to_datetime(data_washington['End Time'])
 
# print(data_chicago.columns)

""""Index(['Trip Duration', 'Start Time', 'End Time', 'Start Station ID',
       'Start Station Name', 'Start Station Latitude',
       'Start Station Longitude', 'End Station ID', 'End Station Name',
       'End Station Latitude', 'End Station Longitude', 'Bike ID', 'User Type',
       'Birth Year', 'Gender;']"""

# creer l'application pour selectinner la ville 

# Selectionner l'une des 3 villes (New york city, Washington ou Chicago)


# def choisir_ville():
#     root = tk.Tk()
#     root.withdraw()  # Pour cacher la fenêtre principale
 
#     villes = ["Chicago", "New York", "Washington"]
 
#     # Boîte de dialogue pour le choix de la ville
#     ville = simpledialog.askstring("Choisir une ville", "Choisissez une ville : Chicago, New York ou Washington :", parent=root)
 
#     if ville:
#         if ville in villes:
#             print("Vous avez choisi :", ville)
#             # Attribution des données en fonction du choix de l'utilisateur
#             if ville == "Chicago":
#                 return df1
#                 print(df1)
#             elif ville == "New York":
#                 return df2
#                 print(df2)
#             elif ville == "Washington":
#                 return df3
#                 print(df3)
#         else:
#             print("Ville non valide.")
#     else:
#         print("Aucune ville choisie.")
#     return None
 
#     root.destroy()  # Fermer la fenêtre Tkinter après l'utilisation
 
    
# # Appeler la fonction pour choisir la ville
# dataV = choisir_ville()
# print(dataV.head(5))


# # Pour les jours de la semaine en français
# from locale import setlocale, LC_TIME
# setlocale(LC_TIME, 'fr_FR.UTF-8')
 
# # Import des fichiers de Chicago, New York et Washington
# data_chicago = pd.read_csv("cleaned_chicago_city.csv")
# data_newyork = pd.read_csv("cleaned_new_york_city.csv")
# data_washington = pd.read_csv("cleaned_washington_city.csv")
 
# # Je convertis les datetime pour après récuperer les mois et jours
# data_chicago['Start Time'] = pd.to_datetime(data_chicago['Start Time'])
# data_chicago['End Time'] = pd.to_datetime(data_chicago['End Time'])
 
# data_newyork['Start Time'] = pd.to_datetime(data_newyork['Start Time'])
# data_newyork['End Time'] = pd.to_datetime(data_newyork['End Time'])
 
# data_washington['Start Time'] = pd.to_datetime(data_washington['Start Time'])
# data_washington['End Time'] = pd.to_datetime(data_washington['End Time'])
 
# def choisir_ville():
#     root = tk.Tk()
#     root.withdraw()  # Pour cacher la fenêtre principale
 
#     villes = ["Chicago", "New York", "Washington"]
#     mois = {
#              1: "Janvier", 
#              2: "Février",
#              3: "Mars",
#              4: "Avril",
#              5: "Mais",
#              6: "Juin",
#              7: "Juillet",
#              8: "Août",
#              9: "Septembre",
#             10: "Octobre",
#             11: "Novembre",
#             12: "Décembre"
#            }
 
 
#     # Boîte de dialogue pour le choix de la ville
#     ville = simpledialog.askstring("Choisir une ville", "Choisissez une ville : Chicago, New York ou Washington :", parent=root)
 
#     if ville:
#         if ville in villes:
#             print("Vous avez choisi :", ville)
#             # Attribution des données en fonction du choix de l'utilisateur
#             # Boîte de dialogue pour le choix du mois
#             #mois_choisi = simpledialog.askinteger("Choisir un mois", "Choisissez un mois (1-12) :", parent=root, minvalue=1, maxvalue=12)
#             mois_choisi = simpledialog.askinteger("Choisir un mois", "Choisissez un mois: 1 pour Janvier,... :\n Chicago :", parent=root, minvalue=1, maxvalue=12)
#             if mois_choisi:
#                 print("Vous avez choisi le mois :", mois[mois_choisi])
#             else:
#                 print("Mois non valide.")
#             if ville == "Chicago":
#                 resultat = data_chicago[data_chicago['Start Time'].dt.month == mois_choisi], ville, mois[mois_choisi]
#                 return resultat
#             elif ville == "New York":
#                 resultat = data_newyork[data_newyork['Start Time'].dt.month == mois_choisi], ville, mois[mois_choisi]
#                 return resultat
#             elif ville == "Washington":
#                 resultat = data_washington[data_washington['Start Time'].dt.month == mois_choisi], ville, mois[mois_choisi]
#                 return resultat
#         else:
#             print("Ville non valide.")
#     else:
#         print("Aucune ville choisie.")
#     return None
 
#     root.destroy()  # Fermer la fenêtre Tkinter après l'utilisation
 
    
# # Appeler la fonction pour choisir la ville
# sortie = choisir_ville()
# data = sortie[0]
