# AIPI561-Project2
[![Python application test with Github Actions](https://github.com/robbjr21/AIPI561-Project2/actions/workflows/main.yml/badge.svg)](https://github.com/robbjr21/AIPI561-Project2/actions/workflows/main.yml)

In Project 2 I created an AutoML solution using DataBricks on Azure. I found the Iris Dataset from Kaggle which is a highly explainable dataset with four features distinguishing three types of Iris plants. 

I trained 200 models and selected a Decision Tree Model with the highest validation accuracy. I then downloaded this model as a pickle file and then loaded the model and operationalized it to handle dynamic user input from a streamlit front-end. 

## Using the prediction tool: 

1) ``$ git clone https://github.com/robbjr21/AIPI561-Project2.git``
2) Open directory and create and run a virtual environment
3) ``$ make install`` or ``pip install -r requirements.txt``
4) ``$ streamlit run streamlit.py``
