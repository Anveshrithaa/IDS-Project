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
	st.write("Trees are the life support system for the planet. Trees themselves are definitely interesting and worth understanding, especially given the plethora of benefits that they can offer. The diverse array of data available today allow us to assess how the number of trees at regional levels is related to local characteristics such as climate, topography, vegetation, soil conditions, and human impacts. Analysis of this data is useful to understand the benefits of trees and their impact on various aspects and also to inform policy-makers and conservationists to quantify and increase the numbers of these “most prominent and critical organisms of life on Earth.”")
	st.header("Goals")
	st.write("Our goal in this project is to analyze tree data specific to the neighborhoods of Pittsburgh, Pennsylvania in depth. The main objective of this project is to:")
	st.write("- Prepare an initial exploratory analysis that shows a deeper understanding of the data.")
	st.write("- Carry out graphing and statistical analysis to define potential research questions.")
	st.write("- Combine multiple datasets and apply statistical analysis.")
	st.write("- Employ advanced data concepts, visualization techniques and machine learning to tell a compelling story")
	st.write("- Design and deploy an interactive, end-user focused and data-centric application that helps readers in making sense of the data.")
	st.header("Questions to Explore")
	st.write(" First, we want to explore the tree characteristics, the distribution of the tree species across neighborhoods, and the benefits offered by trees. More interestingly, we want to explore the question: are trees' benefits being enjoyed equally by everyone? American Forest defines tree equity as \"having enough trees in an area so that everyone can experience the health, climate, and economic benefits\". In fact, tree equity is a topic included in President Biden and the Democrat’s 3.5-trillion dollar Infrastructure Investment and Jobs Act and Build Back Better Act. Out of the 3.5 trillion dollars planned, approximately 3 billion dollars will be spent to improve tree equity [1]. The money will be used for “tree planting and related activities to increase community tree canopy and associated societal and climate co-benefits, with a priority for projects that increase tree equity.” With tree equity being such an important topic, we want to explore a series of interesting questions related to Pittsburgh's trees and tree equity:")
	st.write("- What are the characteristics of Pittsburgh's trees?")
	st.write("- What is the distribution of trees across neighborhoods in Pittsburgh?")
	st.write("- Why are Pittsburgh's trees distributed in the way they are?")
	st.write("- What kinds of benefits do trees offer? Is there a significant difference in benefits offered across species or even within the same species?")
	st.write("- What is the extent of tree equity in Pittsburgh?")
	st.write("- Are trees' benefits enjoyed equally by all the neighborhoods in Pittsburgh?")
	st.write("- In Pittsburgh, is the tree density of a neighborhood correlated with its socio-economic status?")
	st.write("- If so, how and why are they correlated?")
	st.write("- Are some neighborhoods missing out on more potential benefits? For example, vacant sites that could be planted but not? If so, what are the reasons?")
	st.write("- Can we predict the tree density of a neighborhood using its socio-economic information?")
	st.write("To answer these questions, we performed neighborhood-level analysis and created interactive visualizations to get better insights.")
