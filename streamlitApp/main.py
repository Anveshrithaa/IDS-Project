import streamlit as st

from pages import home, data, viz, viz2, ml, video, ref
st.sidebar.image: st.sidebar.image("https://www.seekpng.com/png/detail/83-830036_neurogenomics-laboratory-carnegie-mellon-university-logo-png.png", use_column_width=True)
st.sidebar.title('Pittsburgh Trees Analysis')
st.sidebar.header('05839 - Interactive Data Science  |  Fall 2021')
st.sidebar.write("\n")
rad = st.sidebar.radio("Navigation", ["HOME", "DATA", "DATA EXPLORATION", "DATA ANALYSIS", "ADVANCED ANALYTICS", "CONCLUSION", "EXTERNAL LINKS"])
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
if rad == "CONCLUSION":
	ref.write()
if rad == "EXTERNAL LINKS":
	video.write()


