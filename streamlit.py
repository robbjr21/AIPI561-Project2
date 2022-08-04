import streamlit as st
from main import load_method, setting_data, passing_data, gen_prediction

st.title("Iris Classification")
st.image("images/Iris.png")

SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm = setting_data()

#get user input
INPUT_sepal_length = st.selectbox("Sepal Length", SepalLengthCm)
INPUT_sepal_width = st.selectbox("Sepal Width", SepalWidthCm)
INPUT_petal_length = st.selectbox("Petal Length", PetalLengthCm)
INPUT_petal_width = st.selectbox("Petal Width", PetalWidthCm)

button = st.button("Predict Species")

if button:
    model = load_method()
    input = passing_data(INPUT_sepal_length,INPUT_sepal_width,INPUT_petal_length,INPUT_petal_width)
    prediction = gen_prediction(input, model)
    prediction = prediction
    st.subheader("Predicted Species:")
    st.write(prediction)
