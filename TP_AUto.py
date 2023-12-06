import mysql.connector,csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

file_path = "./cleaned_autos.csv"

df = pd.read_csv(file_path)

print(df.head())

print(df.shape)

print(df.dtypes)

#Le Nombre total de vehicule

nombre_vehicules_par_type = df.groupby('vehicleType')['name'].count()
print(nombre_vehicules_par_type)


plt.bar(nombre_vehicules_par_type.index, nombre_vehicules_par_type)

plt.title("nombre de par vehicule type")

plt.ylabel("name")

plt.xlabel("vehicleType")

plt.grid(color="lightgrey", linestyle="dotted", axis="y")

plt.show()



#Annee d'immatriulation

annee_immatriculation = df.groupby('yearOfRegistration')['name'].count().sort_values(ascending=False)
print(annee_immatriculation)

plt.bar(annee_immatriculation.index, annee_immatriculation)

plt.title("année d'immatriculation ")

plt.ylabel("nombre de vehicule")

plt.xlabel("yearOfRegistration")

plt.grid(color="lightgrey", linestyle="dotted", axis="y")

# plt.show()


#vehicule par marque 
vehicule_par_marque = df.groupby('name')['model'].count().sort_values()
print(vehicule_par_marque)

plt.stem(vehicule_par_marque.index, vehicule_par_marque)

plt.title("vehicule par marque")

plt.ylabel("model")

plt.xlabel("marque")

plt.grid(color="lightgrey", linestyle="dotted", axis="y")

# plt.show()

# Prix moyen des véhicules par type de véhicule et type de boîte de vitesses

Prix_moyen_types_typesBV = df.groupby(['vehicleType','gearbox'])['price'].mean()
print(Prix_moyen_types_typesBV)

# Prix moyen des véhicules selon le type de carburant et le type de boîte de vitesses
Prix_moyen_typesCarbu_typesBV = df.groupby(['fuelType','gearbox'])['price'].mean()
print(Prix_moyen_typesCarbu_typesBV)


# heatmap = prix_moy_type_marque.pivot_table(index = "brand", columns = "vehicleType", values = "price")
# plt.figure(figsize=(12, len(heatmap)*0.30))
# sb.heatmap(heatmap, cmap = "YlGn", annot=True, fmt=".2f", linewidth="0.5")
# plt.xlabel("Marque")
# plt.ylabel("Type de véhicule")
# plt.title("Prix")
 
# plt.tight_layout()
# plt.show()
# plt.savefig("./projet/graphiquevert.png")