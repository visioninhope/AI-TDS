import os
import warnings

import joblib
import numpy as np

warnings.filterwarnings('ignore')


def predict_1(s):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    remo = list(current_dir.rsplit("\\"))
    remo = remo[:len(remo) - 1]
    ram_maha = "\\".join(remo)

    fourth_model_path = os.path.join(ram_maha, 'Modals_proj\\fourth_model.pkl')

    my_model = joblib.load(fourth_model_path)

    engdict = {}

    with open(s, "rb") as f:
        tem = f.read(1024)
        for i in range(0, 1024):
            engdict.update({i: int(tem[i])})

    feats = []

    for i in range(0, 1024):
        try:
            feats.append(engdict[i])
        except:
            pass

    probs = my_model.predict_proba(np.array([feats]))

    maino = [my_model.predict(np.array([feats])), probs]
    return maino
