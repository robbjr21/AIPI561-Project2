import pickle
import pandas as pd

def load_method():
    path = "models/DecisionTreeModel.pkl"
    model = pickle.load(open(path, 'rb'))
    return model

def setting_data():
    data = pd.read_csv("data/Iris.csv")
    SepalLengthCm = data["SepalLengthCm"].unique()
    SepalWidthCm = data["SepalWidthCm"].unique()
    PetalLengthCm = data["PetalLengthCm"].unique()
    PetalWidthCm = data["PetalWidthCm"].unique()
    return SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm

def passing_data(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
    data = {"SepalLengthCm": SepalLengthCm,"SepalWidthCm": SepalWidthCm,"PetalLengthCm": PetalLengthCm,"PetalWidthCm": PetalWidthCm}
    test_input = pd.DataFrame(data, index=[0])
    return test_input

def gen_prediction(test_input, model):
    pred = model.predict(test_input)
    return pred[0]
