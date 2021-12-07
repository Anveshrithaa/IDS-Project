import streamlit as st

#from pages import home

def write():
    st.subheader("Video Presentation")
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
    st.video("https://youtu.be/UXj5W-qrotw")
    st.subheader("Github project repository")
    st.write("https://github.com/prekshaupatel/IDS-Project")



	
