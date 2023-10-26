import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

def calculate_properties(smiles):
    mol = Chem.MolFromSmiles(smiles)
    properties = {}

    properties["Molecular Weight"] = Descriptors.MolWt(mol)
    properties["Number of Heavy Atoms"] = Descriptors.HeavyAtomMolWt(mol)
    properties["FractionCSP3"] = Descriptors.FractionCSP3(mol)
    properties["Number of Rotatable Bonds"] = Descriptors.NumRotatableBonds(mol)
    properties["Descriptors.NumHAcceptors"] = Descriptors.NumHAcceptors(mol)
    properties["Descriptors.NumHDonors"] = Descriptors.NumHDonors(mol)
    properties["Molar Refractivity"] = Descriptors.MolMR(mol)
    properties["TPSA"] = Descriptors.TPSA(mol)
    properties["Log P"] = Descriptors.MolLogP(mol)

    return properties

def check_lipinski(properties):
    k = properties["Molecular Weight"]
    x = properties["Log P"]
    a = properties["Descriptors.NumHAcceptors"]
    l = properties["Descriptors.NumHDonors"]

    return l <= 5 and a <= 10 and k <= 500 and x <= 5

def check_ghose(properties):
    x = properties["Log P"]
    o = properties["Molar Refractivity"]
    k = properties["Molecular Weight"]
    C = properties["TPSA"]

    return -0.4 <= x <= 5.6 and 40 <= o <= 130 and 160 <= k <= 480 and 70 <= C <= 20

def check_veber(properties):
    i = properties["Number of Rotatable Bonds"]
    C = properties["TPSA"]

    return i <= 10 and C <= 140

def check_egan(properties):
    x = properties["Log P"]
    C = properties["TPSA"]

    return x <= 5.88 and C <= 131.6

def check_muegge(properties):
    k = properties["Molecular Weight"]
    x = properties["Log P"]
    C = properties["TPSA"]
    m = properties["Number of Heavy Atoms"]
    t = properties["Number of Heavy Atoms"]
    i = properties["Number of Rotatable Bonds"]
    a = properties["Descriptors.NumHAcceptors"]
    l = properties["Descriptors.NumHDonors"]

    return 200 <= k <= 600 and -2 <= x <= 5 and 150 <= C <= 140 and m <= 7 and t > 1 and i <= 15 and a <= 10 and l <= 10

def check_leadlikeness(properties):
    k = properties["Molecular Weight"]
    x = properties["Log P"]
    i = properties["Number of Rotatable Bonds"]

    return 250 <= k <= 350 and x <= 3.5 and i <= 7

smiles = input("Enter the Smile Format: ")
properties = calculate_properties(smiles)

if check_lipinski(properties):
    print("Lipinski: Yes; 0 violation")
else:
    print("Lipinski: No; violation")

if check_ghose(properties):
    print("Ghose: No")
else:
    print("Ghose: Yes")

if check_veber(properties):
    print("Veber: Yes")
else:
    print("Veber: No")

if check_egan(properties):
    print("Egan: Yes")
else:
    print("Egan: No")

if check_muegge(properties):
    print("Muegge: Yes")
else:
    print("Muegge: No; Voilation Found")

if check_leadlikeness(properties):
    print("Leadlikeness: Yes")
else:
    print("Leadlikeness: No; Voilation Found")

data = {
    "Molecular Weight": [properties["Molecular Weight"]],
    "Number of Heavy Atoms": [properties["Number of Heavy Atoms"]],
    "Log P": [properties["Log P"]],
    "TPSA": [properties["TPSA"]],
    "Molar Refractivity": [properties["Molar Refractivity"]],
    "Descriptors.NumHDonors": [properties["Descriptors.NumHDonors"]],
    "Descriptors.NumHAcceptors": [properties["Descriptors.NumHAcceptors"]],
    "Number of Rotatable Bonds": [properties["Number of Rotatable Bonds"]],
    "FractionCSP3": [properties["FractionCSP3"]],
}

df = pd.DataFrame(data)
df.to_csv("df.csv", index=False)