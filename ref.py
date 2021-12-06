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
    
    st.header("About")
    st.write("This web application was developed using Streamlit as a part of the project component for Prof. John Stamper's 05839 - Interactive Data Science course at Carnegie Mellon University during Fall 2021. This project was carried out by a team of four Master of Computational Data Science students: Presksha Patel, Sai Vishwas Padigi, Andy and Anveshrithaa Sundareswaran.")
    st.header("References")
    st.write("1. https://nypost.com/2021/09/27/biden-dems-3-5t-bill-includes-money-for-tree-equity-bias-training/")
    st.write("2. Western Pennsylvania Regional Data Center - https://data.wprdc.org/dataset/city-trees")
    st.write("3. National Tree Benefit Calculator Web Service -  http://www.treebenefits.com/calculator/")
    st.write("4. Pittsburgh American Community Survey 2015 - Miscellaneous Data - https://data.wprdc.org/dataset/pittsburgh-american-community-survey-2015-miscellaneous-data")
    st.write("5. Neighborhoods with SNAP Data - https://data.wprdc.org/dataset/neighborhoods-with-snap-data")
    st.write("6. Streamlit API Reference - https://docs.streamlit.io/library/api-reference")
    st.write("7. Plotly API Reference - https://plotly.com/python-api-reference/")
	
	

	