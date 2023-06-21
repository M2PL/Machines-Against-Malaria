import numpy as np
import sys
import joblib

from sklearn.ensemble import RandomForestClassifier
from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs

smi = sys.argv[1]
model = sys.argv[2]

def smi_to_fps(smi):
    mol = Chem.MolFromSmiles(smi)
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, 5, nBits=500) # gets the vector
    arr = np.zeros((0,))
    DataStructs.ConvertToNumpyArray(fp,arr)  # converts the vector to numpy array
    return arr

def _load_model(model):
    mdl = joblib.load(model)
    return mdl

def predict(model, x):
    mdl = _load_model(model)
    y_pred = mdl.predict_proba(x)
    return y_pred

if __name__ == "__main__":
    x = smi_to_fps(smi)
    y_pred = predict(model, np.array([x]))
    print(y_pred)