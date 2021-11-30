import streamlit as st

#from pages import home

def write():
	st.title("Pittsburgh Trees Analysis")

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
	st.header("Introduction")
	st.write("Trees are the life support system for the planet. Trees themselves are definitely interesting and worth understanding, especially given the benefits that they can offer. The diverse array of data available today allow us to assess how the number of trees at regional levels is related to local characteristics such as climate, topography, vegetation, soil conditions, and human impacts. Analysis of this data is useful to understand the benefits of trees and their impact on various aspects and also to inform policy-makers and conservationists to quantify and increase the numbers of these “most prominent and critical organisms of life on Earth.”")
	st.header("Goal")
	st.write("Our goal in this project is to analyze tree data specific to the neighborhoods of Pittsburgh, Pennsylvania. The first thing we did is explore the tree characteristics, the distribution of the tree species across neighborhoods and the species specific benefits. More interestingly, we investigate whether there is any correlation between tree density and six different socio-economic factors: median home values, population density, industrial area, commercial area, education, and crime rate. The main objective of this project is to:")
	st.write("- Prepare an initial exploratory analysis that shows a deeper understanding of the data.")
	st.write("- Carry out graphing and statistical analysis to define potential research questions.")
	st.write("- Combine multiple datasets and apply statistical analysis.")
	st.write("- Employ advanced data concepts, visualization techniques and machine learning to tell a compelling story")
	st.write("- Design and deploy an interactive, end-user focused and data-centric application that helps readers in making sense of the data.")
	st.header("Questions to explore")
	st.write("Tree-equality is a topic included in President Biden and the Democrat’s 3.5-trillion dollar spending bill proposal. Within the bill, approximately 3.5 billion dollars will be spent to improve tree equality. The money will be used for “tree planting and related activities to increase community tree canopy and associated societal and climate co-benefits, with a priority for projects that increase tree equity.” This raises interesting questions like:")
	st.write("- What is the extent of tree equality in Pittsburgh?")
	st.write("- Are trees' benefits enjoyed equally by all the neighborhoods in Pittsburgh?")
	st.write("- Does tree density of a neighborhood play a role in determining its socio-economic status?")
	st.write("To answer these questions, we performed some neighborhood-level analysis and created interactive visualizations to get better insights.")
	
