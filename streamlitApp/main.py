import streamlit as st

from pages import home, data, viz, ml, video
st.sidebar.header('Analyzing Pittsburgh\'s Trees')
st.sidebar.markdown('05839 INTERACTIVE DATA SCIENCE | FALL 2021')
rad = st.sidebar.radio("Navigation", ["Home", "Data", "Visualization", "Prediction", "Video"])
if rad == "Home":
	home.write()
if rad == "Data":
	data.write()
if rad == "Visualization":
	viz.write()
if rad == "Prediction":
	ml.write()
if rad == "Video":
	video.write()

