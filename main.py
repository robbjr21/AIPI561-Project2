import pickle
import numpy as np
import pandas as pd

def load_method():
    path = "models/DecisionTreeModel.pkl"
    model = pickle.load(open(path, 'rb'))
    return model

def test_case():
    data = {"SepalLengthCm": 5.4,"SepalWidthCm": 3.9,"PetalLengthCm": 0.1,"PetalWidthCm": 1.4}
    test_input = pd.DataFrame(data, index=[0])
    return test_input

if __name__ == '__main__':
    model = load_method()
    input = test_case()
    pred = model.predict(input)
    print(pred[0])
