import streamlit as st
import os

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
        text-align: justify;
    }
   
    </style>
    """,
    unsafe_allow_html=True)
	#st.header("Prediction")
	st.header("Advanced Analysis using Machine Learning")
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
	path = os.path.dirname(__file__)
	model_file = path+"/model.pkl"
	pipe = pickle.load(open(model_file,"rb"))
	col1, _, col2, _ = st.columns([6, 1, 4, 1])
	with col1:
		per_commercial = st.slider('Percentage of Commercial Area:', 0.0, 100.0, 25.0)/100
		per_bachelor = st.slider('Percentage of Individuals with Bachelors Degrees:', 0.0, 100.0, 30.0)/100
		per_master = st.slider('Percentage of Individuals with Masters Degrees:', 0.0, 100.0, 5.0)/100
		median_home_value = st.number_input('Median Home Value ($):', min_value = 0.0, value = 20000.0)
		pop_density = st.number_input('Number of Individuals per Square Mile:', min_value = 0.0, value = 4000.0)
	with col2:    
		tree_density = pipe.predict((np.array([per_master, per_bachelor, per_commercial, median_home_value, pop_density])).reshape(1, -1))
		tree_density = max(0, int(tree_density[0]))
		st.header("Predicted Tree Density")
		st.subheader(tree_density)
		st.caption("Trees per Square Mile")

	st.write("We observe that changing the values for different factors changes the tree density (trees per square mile).")
	st.write("Increasing the percentage of commercial area results in a corresponding increase in the tree density. This direct relationship could be the result of urban greening, which is defined as public landscaping and urban forestry projects which create mutually beneficial relations between individuals living in the city and their environments.")
	st.write("Moreover, an increase in the percentage of individuals with a Bachelors degree also results in a corresponding increase in the tree density. This could be a result of increased awareness and understanding of the interaction between individuals and their environments.")
	st.write("In contrast, we observe that an increase in the percentage of individuals with a Masters degree results in a corresponding decrease in tree density. This feature of the model is definitely interesting given that a postive correlation is observed between the percentage of individuals with a Masters degree and the tree density across neighborhoods. Moreover, we observe that increasing the percentage of individuals with a Masters degree beyond a certain threshold, results in the tree density being predicted as zero. This could be due to the fact that the range of percentage of individuals with Masters degree ranged from 0.0% - 50% with an average of 9.7%. Thus, the model was only able to learn from data in this range.")
	st.write("Additionally, we observe that an increase in the median home value corresponds to an increase in the tree density. This could be a result of the aesthetic appeal of trees which could raise median home values. Moreover, the environmental benefits of trees could make the home more pleasant to live in thereby raising the median home value.")
	st.write("We also observe that increasing the population density results in a corresponding increase in the predicted tree density. Given all the environmental benefits of trees, it is possible that most individuals prefer to live in areas with high tree densities, thereby leading to the positive correlation between population and tree density.")

	
