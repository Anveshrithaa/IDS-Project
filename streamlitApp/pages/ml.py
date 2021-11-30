import streamlit as st

import pickle
import numpy as np
import pandas as pd

import sklearn
from sklearn.pipeline import Pipeline

import streamlit as st

#from pages import home

def write():
	st.markdown(
    """
    <style>
    .reportview-container {
        background-image: url("https://media.istockphoto.com/photos/abstract-blurred-leaves-of-tree-in-nature-forest-with-sunny-and-bokeh-picture-id1188216286?k=20&m=1188216286&s=612x612&w=0&h=P8yrDhGYb1QDqw_jDOny10cyyjLbETphiDFxxIE8d2o=");
        background-repeat: no-repeat;
        background-position: top;
        background-size: 100% 100%;
    }
   
    </style>
    """,
    unsafe_allow_html=True)
	#st.header("Prediction")
	st.header("Modeling Tree Density")
	st.write("We observed significant correlations between various socioeconomic factors and the tree density across neighborhoods. The socioeconomic factors analyzed included park space and street density, median income, median home value, percentage of commercial, industrial and residential areas, crime rates, job availability, education, and population density. To create a model to predict the tree density in a given neighborhood, we selected a subset of these variables after examining the correlations between the socioeconomic factors and tree density. The following variables were utilized to create a predictor model:")

	data = [['Percentage of Commercial Area', 0.50],
        ['Percentage of Individuals with Bachelors Degrees', 0.48],
        ['Median Home Value', 0.48],
        ['Population Density', 0.46],
        ['Percentage of Individuals with Masters Degrees', 0.37]]
	df = pd.DataFrame(data, columns = ['Variable', 'Pearson Correlation'])
	df = df.set_index('Variable')
	st.caption("Table 1. Correlation between various Socioeconomic Factors and Tree Density across Neighborhoods")
	st.table(df)
	st.write("We standardized the data and fit a Ridge Regression Model (L1 regularization) on the data. We used 6-fold cross validation to validate the model. We observed a 0.59 R² score on the training data and a 0.33 R² score on the evaluation data averaged across all the folds. The results of training the model indicated a weak relationship between the top-5 most correlated socioeconomic factors and tree density.\n")
	st.write("To view the results of the model, enter the values for the following predictor variables to get the predicted tree density value:")
	model_file = "model.pkl"
	pipe = pickle.load(open(model_file,"rb"))
	col1, _, col2, _ = st.columns([6, 1, 4, 1])
	with col1:
		per_master = st.slider('Percentage of Individuals with Masters Degrees:', 0.0, 100.0, 5.0)
		per_bachelor = st.slider('Percentage of Individuals with Bachelors Degrees:', 0.0, 100.0, 10.0)
		per_commercial = st.slider('Percentage of Commercial Area:', 0.0, 100.0, 15.0)
		median_home_value = st.number_input('Median Home Value ($):', min_value = 0.0, value = 10000.0)
		pop_density = st.number_input('Number of Individuals per Square Mile:', min_value = 0.0, value = 2000.0)
	with col2:    
		tree_density = pipe.predict((np.array([per_master, per_bachelor, per_commercial, median_home_value, pop_density])).reshape(1, -1))
		tree_density = max(0, int(tree_density[0]))
		st.header("Predicted Tree Density")
		st.subheader(tree_density)
		st.caption("Trees per Square Mile")



	