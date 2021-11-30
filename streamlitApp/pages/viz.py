import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import plotly.offline as py
import plotly.express as px
import random
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json, ast
import plotly.express as px
import ipywidgets as widgets
from IPython.display import display
from IPython.display import Image
import plotly
import plotly.express as px
from matplotlib.colors import LogNorm, Normalize



#from pages import home

def write():
	st.markdown(
    """
    <style>
    .reportview-container {
        text-align: justify;
    }
   
    </style>
    """,
    unsafe_allow_html=True)
	st.header("Exploratory Data Analysis")
	st.header("Tree Characteristics")
	st.write("To start with our analysis, we explore the tree characteristics across Pittsburgh. We analyze the average tree height and average tree width across the neighborhoods in Pittsburgh. The tree height and width are important traits that directly or indirectly determine various factors including tree benefits. Hence, we shall start by exploring the average height and width of trees in each neighborhood.")
	sns.set()
	df_trees = pd.read_csv("cleaned_data/cleaned_tree_data_5.csv", encoding="ISO-8859-1", low_memory=False)
	option = st.selectbox('Choose a Tree Characteristics',('Height', 'Width'))
	if option == "Height":
		df_height = df_trees.groupby("neighborhood")["height"].mean()
		df_height = df_height.to_frame().reset_index()
		df_height.columns = ['neighborhood', 'average_height']
		fig=px.choropleth(df_height,
				 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
				 featureidkey='properties.name',   
				 locations='neighborhood',        #column in dataframe
				 color='average_height',
				  color_continuous_scale='blues',
				   title='Average Tree Height across Neighborhood' ,  
				   height=700
				  )
		fig.update_geos(fitbounds="locations", visible=False)
		st.plotly_chart(fig, use_container_width=True, sharing='streamlit')
	elif option == "Width":
		df_width = df_trees.groupby("neighborhood")["width"].mean()
		df_width = df_width.to_frame().reset_index()
		df_width.columns = ['neighborhood', 'average_width']
		fig=px.choropleth(df_width,
		 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
		 featureidkey='properties.name',   
		 locations='neighborhood',        #column in dataframe
		 color='average_width',
		  color_continuous_scale='blues',
		   title='Average Tree Width across Neighborhood' ,  
		   height=700
		  )
		fig.update_geos(fitbounds="locations", visible=False)
		st.plotly_chart(fig, use_container_width=True, sharing='streamlit')
	st.write("While there seems to be weak positive correlation between the average height and average width (neighborhoods with tall trees tend to have higher average tree width), this can't be considered as a strong correlation. A strange observation is that the neighborhood 'Hays' has the highest average tree height in pittsburgh. However, it has one of the lowest average tree width in Pittsburgh!")
	st.header("The most prevalent species in each neighborhood")
	groupBySpeciesAndNeighborhood = df_trees.groupby(['neighborhood','common_name'])['id'].count()
	groupBySpeciesAndNeighborhood = groupBySpeciesAndNeighborhood.to_frame().reset_index()
	prevalent_species = groupBySpeciesAndNeighborhood.loc[groupBySpeciesAndNeighborhood.groupby(['neighborhood'])['id'].idxmax()].reset_index(drop=True)
	st.write("We also observe that different tree species have different distributions across various neighborhoods. We determine the most prevalent tree species for each neighborhood and observe the distribution.")
	fig=px.choropleth(prevalent_species,
			 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
			 featureidkey='properties.name',   
			 locations='neighborhood',        #column in dataframe
			 color='common_name',
			  color_continuous_scale='Inferno',
			   title='Most prevalent species in each Neighborhood' ,  
			   height=700
			  )
	fig.update_geos(fitbounds="locations", visible=False)
	st.plotly_chart(fig, use_container_width=True, sharing='streamlit')
	st.write("It can be observed that some nearby neighborhoods have the same most prevalent tree species. It can be seen that Maple:Norway is the most prevalent species in 18 neighborhoods!")
	st.header("Distribution of Species across Neighborhood")
	st.write("We observed a wide variety of tree species across Pittsburgh. We noticed that the benefits provided by the trees were dependent on the tree species. Given that certain species provided more environmental benefits compared to other tree species, we analyzed the trends in the distribution of tree species across neighborhoods within Pittsburgh. Here we analyze the number of trees of a selected species (and even stumps and vacant sites) across the neighborhoods.")
	df_trees_thresh = df_trees.groupby(['common_name'])['id'].count()
	df_trees_thresh1 = df_trees_thresh.to_frame().reset_index()
	df_trees_thresh1 = df_trees_thresh1.sort_values(by=['id'], ascending = False)
	df_trees_thresh1 = df_trees_thresh1[df_trees_thresh1['id'] > 50]
	selected_spec = st.selectbox('Select a Species:',df_trees_thresh1.common_name)
	df_spec = df_trees.groupby(['common_name', 'neighborhood'])['id'].count()
	df_spec = df_spec.to_frame().reset_index()
	df_spec = df_spec.loc[df_spec['common_name'] == selected_spec]
	#df_spec['percent'] = ((df_spec['id']/df_spec['id'].sum()) * 100)
	df_spec = df_spec.rename(columns={"id": "count"})


	full_neigh = pd.DataFrame({'neighborhood' : df_trees['neighborhood'].unique()})
	full_neigh = full_neigh.rename(columns={"id": "count"})
	full_neigh = full_neigh.merge(df_spec, how = 'outer', on = ['neighborhood'])
	full_neigh['count'] = full_neigh['count'].fillna(0)
	full_neigh = full_neigh.drop(labels = ['common_name'], axis = 1)
	full_neigh.sort_values(['count'], ascending= False)

	str2 = "Distribution of " + selected_spec + " across neighborhoods of Pittsburgh"
	fig=px.choropleth(full_neigh,
				 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
				 featureidkey='properties.name',   
				 locations='neighborhood',        #column in dataframe
				 color='count',
				  color_continuous_scale= 'blues',
				   title= str2 ,  
				   height=700,
				  )
	fig.update_geos(fitbounds="locations", visible=False)
	fig.layout.template = None
	st.plotly_chart(fig, use_container_width=True, sharing='streamlit')


	st.header("Tree Species Specific Benefits")
	st.write("The benefits of trees extend far beyond the aesthetic beauty and the shade they bring to the landscape. Some of these benefits include:")
	st.write("1. **CO2 Benefit**")
	st.write("Trees absorb CO2, removing and storing the carbon while releasing oxygen back into the air. This benefit is quantified by estimating the financial cost of industrially removing from atmosphere, the additional CO2 that would have been present had that tree not been present.")
	st.write("2. **Electricity Saving Benefit**")
	st.write("Trees lower surface and air temperatures by providing shade and through evapotranspiration. Hence, trees drastically reduce the electricity required for cooling indoor spaces.")
	st.write("3. **Gas Saving Benefit**")
	st.write("During winter, the trees lose their leaves and allow the sun to heat homes in addition to breaking the cold winds. Hence, in the colder months, tree help keep the indoor spaces warm and reduce the natural gas consumption required for heating purposes.")
	st.write("4. **Air Quality Benefit**")
	st.write("Trees absorb pollutants such as ozone, carbon monoxide, sulfur dioxide, nitrogen oxides, and particulates. Additionally, owing to the reduced energy consumption in the presence of trees, the generation of such pollutants is decreases too.")
	st.write("5. **Storm Water Benefit**")
	st.write("Trees reduce the storm water runoff, which reduces flooding, saves city storm water management costs, and decreases the flow of polluted water into the nearby water bodies.")
	st.write("6. **Property Value Benefit**")
	st.write("Due to the aesthetic, cooling and other invaluable benefits the presence of trees drives up the property value in a given neighborhood.")

	df_trees = pd.read_csv("cleaned_data/cleaned_tree_data_5.csv", encoding="ISO-8859-1", low_memory=False)
	tree_stat = df_trees.groupby(["common_name"]).agg(["count", "mean"]).reset_index()
	tree_stat = tree_stat[tree_stat["id"]["count"] >= 10]

	st.write("Let us now explore the benefits (quantified in terms of dollar value) of different species of trees.")
	option = st.selectbox('Select an Attribute',('Storm Water Benefit', 'Property Value Benefit', 'Electricity Saving Benefit',\
		'Gas Saving Benefit', 'Air Quality Benefit', 'CO2 Benefit','Overall Benefit'))


	corresponding_cols = {'Storm Water Benefit':"stormwater_benefits_dollar_value",\
						'Property Value Benefit':"property_value_benefits_dollarvalue",\
						'Electricity Saving Benefit':"energy_benefits_electricity_dollar_value",\
						'Gas Saving Benefit':'energy_benefits_gas_dollar_value',\
						'Air Quality Benefit':'air_quality_benfits_total_dollar_value',\
						'CO2 Benefit':"co2_benefits_dollar_value",'Overall Benefit':"overall_benefits_dollar_value"}

	top_k = st.slider('Select Top K Species', 10, 30, 15)
	sns.set()
	fig, ax = plt.subplots(figsize=(4, 2))
	graph_data = tree_stat.sort_values([(corresponding_cols[option],"mean")])
	graph_data = graph_data.tail(top_k)
	plot = sns.barplot(x=graph_data["common_name"], y=graph_data[corresponding_cols[option]]["mean"],color="limegreen")
	plot.set_xticklabels(plot.get_xticklabels(), 
						  rotation=90, 
						  horizontalalignment='right')
	ax.tick_params(axis='both', which='major', labelsize=4)
	ax.tick_params(axis='both', which='minor', labelsize=4)
	label_font_size = 6

	if option == "Storm Water Benefit":
		plot.set_xlabel("Tree Species", fontsize = label_font_size)
		plot.set_ylabel("Average Stormwater Benefit in Dollar Value", fontsize = label_font_size)
		st.pyplot(fig, use_container_width=True, sharing='streamlit')

	elif option == 'Property Value Benefit':
		plot.set_xlabel("Tree Species", fontsize = label_font_size)
		plot.set_ylabel("Average Property Benefit in Dollar Value", fontsize = label_font_size)
		st.pyplot(fig, use_container_width=True, sharing='streamlit')

	elif option == 'Electricity Saving Benefit':
		plot.set_xlabel("Tree Species", fontsize = label_font_size)
		plot.set_ylabel("Average Energy (Electricity) Benefit in Dollar Value", fontsize = label_font_size)
		st.pyplot(fig, use_container_width=True, sharing='streamlit')


	elif option == 'Gas Saving Benefit':
		plot.set_xlabel("Tree Species", fontsize = label_font_size)
		plot.set_ylabel("Average Energy (Gas) Benefit in Dollar Value", fontsize = label_font_size)
		st.pyplot(fig, use_container_width=True, sharing='streamlit')

	elif option == "Air Quality Benefit":
		pollutant = st.selectbox('Select a pollutant category',options=('O3', 'NO2', 'SO2', 'PM10', 'Overall'))
		if pollutant == "O3":
			o3_air_quality_total_benefit = tree_stat.sort_values([("air_quality_benfits_o3dep_dollar_value","mean")])
			o3_air_quality_total_benefit = o3_air_quality_total_benefit.tail(top_k)
			o3_air_quality_total_benefit = sns.barplot(x=o3_air_quality_total_benefit["common_name"], y=o3_air_quality_total_benefit["air_quality_benfits_o3dep_dollar_value"]["mean"], color="limegreen")
			o3_air_quality_total_benefit.set_xticklabels(o3_air_quality_total_benefit.get_xticklabels(), 
									rotation=90, 
									horizontalalignment='right',
									fontsize = 6)
			o3_air_quality_total_benefit.set_xlabel("Tree Species", fontsize = 6)
			o3_air_quality_total_benefit.set_ylabel("Average O3 Decomposition Benefit in Dollar Value", fontsize = 6)
			st.pyplot(fig, use_container_width=True, sharing='streamlit')

		elif pollutant == "NO2":
			no2_air_quality_total_benefit = tree_stat.sort_values([("air_quality_benfits_no2dep_dollar_value","mean")])
			no2_air_quality_total_benefit = no2_air_quality_total_benefit.tail(30)

			no2_air_quality_total_benefit = sns.barplot(x=no2_air_quality_total_benefit["common_name"], y=no2_air_quality_total_benefit["air_quality_benfits_no2dep_dollar_value"]["mean"], color="limegreen")
			no2_air_quality_total_benefit.set_xticklabels(no2_air_quality_total_benefit.get_xticklabels(), 
								rotation=90, 
								horizontalalignment='right')
			no2_air_quality_total_benefit.set_xlabel("Tree Species", fontsize = label_font_size)
			no2_air_quality_total_benefit.set_ylabel("Average NO2 Decomposition Benefit in Dollar Value", fontsize = label_font_size)
			st.pyplot(fig, use_container_width=True, sharing='streamlit')

		elif pollutant == "SO2":
			so2_air_quality_total_benefit = tree_stat.sort_values([("air_quality_benfits_so2dep_dollar_value","mean")])
			so2_air_quality_total_benefit = so2_air_quality_total_benefit.tail(30)
			so2_air_quality_total_benefit = sns.barplot(x=so2_air_quality_total_benefit["common_name"], y=so2_air_quality_total_benefit["air_quality_benfits_so2dep_dollar_value"]["mean"], color="limegreen")
			so2_air_quality_total_benefit.set_xticklabels(so2_air_quality_total_benefit.get_xticklabels(), 
									rotation=90, 
									horizontalalignment='right')
			so2_air_quality_total_benefit.set_xlabel("Tree Species", fontsize = label_font_size)
			so2_air_quality_total_benefit.set_ylabel("Average SO2 Decomposition Benefit in Dollar Value", fontsize = label_font_size)
			st.pyplot(fig, use_container_width=True, sharing='streamlit')

		elif pollutant == "PM10":
			pm10_air_quality_total_benefit = tree_stat.sort_values([("air_quality_benfits_pm10depdollar_value","mean")])
			pm10_air_quality_total_benefit = pm10_air_quality_total_benefit.tail(30)
			
			pm10_air_quality_total_benefit = sns.barplot(x=pm10_air_quality_total_benefit["common_name"], y=pm10_air_quality_total_benefit["air_quality_benfits_pm10depdollar_value"]["mean"], color="limegreen")
			pm10_air_quality_total_benefit.set_xticklabels(pm10_air_quality_total_benefit.get_xticklabels(), 
									rotation=90, 
									horizontalalignment='right')
			pm10_air_quality_total_benefit.set_xlabel("Tree Species", fontsize = label_font_size)
			pm10_air_quality_total_benefit.set_ylabel("Average SO2 Decomposition Benefit in Dollar Value", fontsize = label_font_size)
			st.pyplot(fig, use_container_width=True, sharing='streamlit')

		elif pollutant == "Overall":
			plot.set_xlabel("Tree Species", fontsize = label_font_size)
			plot.set_ylabel("Average Overall Air Quality Benefit in Dollar Value", fontsize = label_font_size)
			st.pyplot(fig, use_container_width=True, sharing='streamlit')


	elif option == "CO2 Benefit":
		plot.set_xlabel("Tree Species", fontsize = label_font_size)
		plot.set_ylabel("Average CO2 Benefit in Dollar Value", fontsize = label_font_size)
		st.pyplot(fig, use_container_width=True, sharing='streamlit')

	elif option == "Overall Benefit":

		plot.set_xlabel("Tree Species", fontsize = label_font_size)
		plot.set_ylabel("Average Overall Benefit in Dollar Value", fontsize = label_font_size)

		for bar in plot.patches:
			if bar.get_height() > 225:
				bar.set_color('red')    
			else:
				bar.set_color('grey')

		for i,t in enumerate(plot.get_xticklabels()):
			if t.get_text() in ["Oak: Pin", "Oak: Shingle", "Oak: Chestnut"]:
				## bold ticklabels
				t.set_weight("bold")
				## bar edges
				plot.patches[i].set_edgecolor("k")
				plot.patches[i].set_linewidth(2)
		st.pyplot(fig, use_container_width=True, sharing='streamlit')



	st.header("Tree-family Benefits and Intra-group Comparison")
	st.write("After examining the tree species specific benefits, we observed that certain tree families exhibited similar benefits. To understand the similarities and differences between similar tree species we group the species by tree families and analyze the benefits of the tree species within a tree family.")
	tree_family = st.radio("Select a tree-family", ('Oak', 'Maple', 'Elm', 'Ash','Magnolia', 'Beech'))
	st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

	c1, c2 = st.columns((1, 1))
	specific_trees = df_trees[df_trees['common_name'].str.contains(tree_family)]
	#Again only take oaks species that contains more than 10 data points. 
	specific_trees_count = specific_trees.groupby("common_name").agg("count").reset_index()
	specific_trees_count = specific_trees_count[specific_trees_count["id"] >= 10]
	specific_trees_selected = specific_trees_count["common_name"].unique()
	specific_trees_to_plot = specific_trees[specific_trees.common_name.isin(specific_trees_selected)]

	with c1:
		selected = st.selectbox("select a benefit category", ('Storm Water Benefit', 'Property Value Benefit', 'Electricity Saving Benefit',\
		'Gas Saving Benefit', 'Air Quality Benefit', 'CO2 Benefit','Overall Benefit'))

		corresponding_cols = {'Storm Water Benefit':"stormwater_benefits_dollar_value",\
						'Property Value Benefit':"property_value_benefits_dollarvalue",\
						'Electricity Saving Benefit':"energy_benefits_electricity_dollar_value",\
						'Gas Saving Benefit':'energy_benefits_gas_dollar_value',\
						'Air Quality Benefit':'air_quality_benfits_total_dollar_value',\
						'CO2 Benefit':"co2_benefits_dollar_value",'Overall Benefit':"overall_benefits_dollar_value"}


		fig, ax = plt.subplots()

		specific_trees_to_plot_bar_plot = sns.barplot(x=specific_trees_to_plot["common_name"], y=specific_trees_to_plot[corresponding_cols[selected]])
		specific_trees_to_plot_bar_plot.set_xticklabels(specific_trees_to_plot_bar_plot.get_xticklabels(), 
								  rotation=90, 
								  horizontalalignment='right')

		title = tree_family + " Tree " + "Family"
		specific_trees_to_plot_bar_plot.set_xlabel(title, fontsize = 12)
		y_label = "Average " + selected + " in Dollar Value"
		specific_trees_to_plot_bar_plot.set_ylabel(y_label, fontsize = 12)
		st.pyplot(fig, use_container_width=True, sharing='streamlit')

	with c2:
		fig, ax = plt.subplots()
		specific_trees_to_plot = specific_trees_to_plot.rename(columns={"common_name": "Common Name",
										"stormwater_benefits_dollar_value":"Stormwater Benefits Dollar Value",
										"property_value_benefits_dollarvalue":"Property Value Benefits Dollar Value",
										"energy_benefits_electricity_dollar_value":"Energy Benefits Electricity Dollar Value",
										"energy_benefits_gas_dollar_value":"Energy Benefits Gas Dollar Value",
										"air_quality_benfits_total_dollar_value":"Air Quality Benefits Total Dollar Value",
										"co2_benefits_dollar_value":"CO2 Benefits Dollar Value",
										"overall_benefits_dollar_value":"Overall Benefits Dollar Value"})
		tree_group = specific_trees_to_plot.groupby("Common Name").agg('mean')
		grouped_plot = sns.heatmap(tree_group[["Stormwater Benefits Dollar Value","Property Value Benefits Dollar Value",\
			"Energy Benefits Electricity Dollar Value","Energy Benefits Gas Dollar Value","Air Quality Benefits Total Dollar Value",\
			"CO2 Benefits Dollar Value", "Overall Benefits Dollar Value"]], annot= True, fmt='.1f', xticklabels = True, \
			yticklabels = True, cmap = 'Greens', norm=LogNorm())
		st.pyplot(fig, use_container_width=True, sharing='streamlit')


	