import streamlit as st

from pages import home, data, viz, viz2, ml, video

st.sidebar.title('Pittsburgh Trees Analysis')
st.sidebar.header('05839 - Interactive Data Science  |  Fall 2021')
st.sidebar.write("\n")
rad = st.sidebar.radio("Navigation", ["HOME", "DATA", "DATA EXPLORATION", "DATA ANALYSIS", "ADVANCED ANALYTICS", "VIDEO"])
if rad == "HOME":
	home.write()
if rad == "DATA":
	data.write()
if rad == "DATA EXPLORATION":
	viz.write()
if rad == "DATA ANALYSIS":
	viz2.write()
if rad == "ADVANCED ANALYTICS":
	ml.write()
if rad == "VIDEO":
	video.write()


