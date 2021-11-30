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
	#st.header("Visualizations")
	st.header("Tree Characteristics")
	st.write("To start with our analysis we explore the tree characteristics across Pittsburgh. We analyze the average tree height and average tree width across the neighborhoods in Pittsburgh.")
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
	groupBySpeciesAndNeighborhood = df_trees.groupby(['neighborhood','common_name'])['id'].count()
	groupBySpeciesAndNeighborhood = groupBySpeciesAndNeighborhood.to_frame().reset_index()
	prevalent_species = groupBySpeciesAndNeighborhood.loc[groupBySpeciesAndNeighborhood.groupby(['neighborhood'])['id'].idxmax()].reset_index(drop=True)
	st.write("We also observe that different tree species have different distributions across various neighborhoods. We determine the most prevalent tree species for each neighborhood and observe the distribution. We notice that some nearby neighborhoods have the same most prevalent tree species.")
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
	st.write("1. CO2 Benefit")
	st.write("Trees absorb CO2, removing and storing the carbon while releasing oxygen back into the air. This benefit is quantified by estimating the financial cost of industrially removing from atmosphere, the additional CO2 that would have been present had that tree not been present.")
	st.write("2. Electricity Saving Benefit")
	st.write("Trees lower surface and air temperatures by providing shade and through evapotranspiration. Hence, trees drastically reduce the electricity required for cooling indoor spaces.")
	st.write("3. Gas Saving Benefit")
	st.write("During winter, the trees lose their leaves and allow the sun to heat homes in addition to breaking the cold winds. Hence, in the colder months, tree help keep the indoor spaces warm and reduce the natural gas consumption required for heating purposes.")
	st.write("4. Air Quality Benefit")
	st.write("Trees absorb pollutants such as ozone, carbon monoxide, sulfur dioxide, nitrogen oxides, and particulates. Additionally, owing to the reduced energy consumption in the presence of trees, the generation of such pollutants is decreases too.")
	st.write("5. Storm Water Benefit")
	st.write("Trees reduce the storm water runoff, which reduces flooding, saves city storm water management costs, and decreases the flow of polluted water into the nearby water bodies.")
	st.write("6. Property Value Benefit")
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


	st.header("Exploring Trees and Other Neighborhood Factors")
	st.write("Tree themselves are definitely interesting and worth understanding, especially given the \
		benefits that they can offer. As we have seen previously, trees do not merely provide visual or\
		 aesthetic appeals to the neighborhood; they provide real economic, climate, and health benefits \
		 in the forms of energy-saving, air quality improvement, carbon dioxide capture, and many more. \
		 According to the non-profit American Forests, trees are more than scenery; instead, they are \
		 critical infrastructure that every person in every neighborhood deserves. In fact, tree-equality is \
		 a topic included in President Biden and the Democrat’s 3.5-trillion dollar spending bill proposal. \
		 Within the bill, approximately 3.5 billion dollars will be spent to improve tree equality \
		 (source: https://nypost.com/2021/09/27/biden-dems-3-5t-bill-includes-money-for-tree-equity-bias-training/). \
		 The money will be used for “tree planting and related activities to increase community tree canopy and \
		 associated societal and climate co-benefits, with a priority for projects that increase tree equity.” \
		 This raises the questions: what is the extent of tree equality in Pittsburgh? Are trees' benefits enjoyed \
		 equally by all the neighborhoods in Pittsburgh?") 

	st.write("To answer these questions, we performed some neighborhood-level analysis to get a better insight.")

	st.write(" ")
	st.write("The first thing we tried to look at is by trying to investigate whether there is any correlation \
		between tree density and six different socio-economic factors: median home values, population density, \
		industrial area, commercial area, education, and crime rate. We used the 2010 census result and the 2015 American \
		Community Survey results. The 2020 census result was still unavailable at the time of this analysis \
		and will only be released in mid-2022. Among these factors, median home values, crime rate, education can be \
		seen as an indicator of the wealth and financial wellbeing of the neighborhood. One thing we want to \
		investigate is whether wealthier or more well-off neighborhoods have a higher tree density. \
		You can click on the buttons to see the correlation. ")

	st.write(" ")
	st.write("**Exploring the correlation between tree density and different socio-economic factors**")

	factor = st.radio("Select a factor", ('Median Home Value', 'Population Density', 'Industrial Area', \
		'Commercial Area', 'Education', 'Crime Rate'))
	st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

	complete_data = pd.read_csv("cleaned_data/neighborhood_features_data.csv")

	raw_df_trees = pd.read_csv("cleaned_data/cleaned_tree_data_5.csv", encoding="ISO-8859-1", low_memory=False)
	df_trees = raw_df_trees[(raw_df_trees['common_name'] != 'Stump') & 
						   (raw_df_trees['scientific_name'] != 'Stump') &
						   (raw_df_trees['common_name'] != 'Vacant Site Small') & 
						   (raw_df_trees['common_name'] != 'Vacant Site Medium') & 
						   (raw_df_trees['common_name'] != 'Vacant Site Not Suitable') & 
						   (raw_df_trees['common_name'] != 'Vacant Site Large')]

	df_trees['tree_count'] = 1

	df_tree_density = df_trees[['neighborhood', 'tree_count', 'stormwater_benefits_dollar_value', 
								'property_value_benefits_dollarvalue', 'energy_benefits_electricity_dollar_value', 
								'energy_benefits_gas_dollar_value', 'air_quality_benfits_total_dollar_value', 
							   'co2_benefits_dollar_value', 'overall_benefits_dollar_value', ]]


	convert_dict = {'stormwater_benefits_dollar_value': float,
					'property_value_benefits_dollarvalue': float,
					'energy_benefits_electricity_dollar_value': float,
					'energy_benefits_gas_dollar_value': float,
					'air_quality_benfits_total_dollar_value': float,
					'co2_benefits_dollar_value': float,
					'overall_benefits_dollar_value': float
				   }
	df_tree_density = df_tree_density.astype(convert_dict)
	df_tree_density = df_tree_density.groupby('neighborhood', as_index=False).agg({"tree_count": "sum", 
																"stormwater_benefits_dollar_value": "sum",
																"property_value_benefits_dollarvalue": "sum",
																"energy_benefits_electricity_dollar_value": "sum",
																"energy_benefits_gas_dollar_value": "sum",
																"air_quality_benfits_total_dollar_value": "sum",
																"co2_benefits_dollar_value": "sum",
																"overall_benefits_dollar_value": "sum"})


	neighborhood_data = pd.read_csv("cleaned_data/neighborhood_data.csv", encoding="ISO-8859-1", dtype='unicode')

	neighborhood_data_area = neighborhood_data[['SNAP_All_csv_Neighborhood', 'Neighborhood_2010_AREA',
												'Neighborhood_2010_ACRES', 'Pop__2010', 'SNAP_All_csv__Part_1__Major_Cri',
												'SNAP_All_csv_Landslide_Prone___', 'SNAP_All_csv_Flood_Plain____lan',
											   'Est__Percent_Under_Poverty__201', 'SNAP_All_csv_2009_Median_Income']].copy()

	neighborhood_data_area['SNAP_All_csv_Landslide_Prone___'] = neighborhood_data_area['SNAP_All_csv_Landslide_Prone___'].str[:-1]

	neighborhood_data_area['SNAP_All_csv_Flood_Plain____lan'] = neighborhood_data_area['SNAP_All_csv_Flood_Plain____lan'].str[:-1]

	neighborhood_data_area['Est__Percent_Under_Poverty__201'] = neighborhood_data_area['Est__Percent_Under_Poverty__201'].str[:-1]

	neighborhood_data_area.rename({'SNAP_All_csv_Neighborhood': 'neighborhood'}, axis=1, inplace=True)

	neighborhood_convert_dict = {'Neighborhood_2010_AREA': float,
								 'Neighborhood_2010_ACRES': float,
								 'Pop__2010': float,
								 'SNAP_All_csv__Part_1__Major_Cri': float,
								 'SNAP_All_csv_Landslide_Prone___': float,
								 'SNAP_All_csv_Flood_Plain____lan': float,
								 'Est__Percent_Under_Poverty__201': float,
								 'SNAP_All_csv_2009_Median_Income': float
								}

	neighborhood_data_area = neighborhood_data_area.astype(neighborhood_convert_dict)


	combined_data = df_tree_density.merge(neighborhood_data_area, on='neighborhood', how='left')
	print(combined_data.columns)

	combined_data[['tree_count', 'stormwater_benefits_dollar_value', 'property_value_benefits_dollarvalue', 
				   'energy_benefits_electricity_dollar_value', 'energy_benefits_gas_dollar_value',
				  'air_quality_benfits_total_dollar_value', 'co2_benefits_dollar_value', 'overall_benefits_dollar_value',
				   'Pop__2010', 'SNAP_All_csv__Part_1__Major_Cri']] = combined_data[['tree_count', 'stormwater_benefits_dollar_value', 'property_value_benefits_dollarvalue', 
				   'energy_benefits_electricity_dollar_value', 'energy_benefits_gas_dollar_value',
				  'air_quality_benfits_total_dollar_value', 'co2_benefits_dollar_value', 'overall_benefits_dollar_value',
				   'Pop__2010', 'SNAP_All_csv__Part_1__Major_Cri']].div(combined_data.Neighborhood_2010_ACRES, axis=0)


	fig, ax = plt.subplots()

	if factor == "Median Home Value":
		home_value_data = complete_data[['median_home_value', 'area_norm_tree_count', 'area_norm_overall_benefits_dollar_value']]
		# remove rows where median_home_value is 0
		home_value_data = home_value_data[home_value_data['median_home_value'] != 0]

		plot = sns.regplot(x = 'area_norm_tree_count', y = 'median_home_value', data = home_value_data)
		plot.set(xlabel = "Number of Trees (Normalized by Area)", ylabel = "Median Home Value ($)", 
				 title = "Relationship between Median Home Value and Number of Trees \nin Neighborhoods across Pittsburgh")
		st.pyplot(fig, use_container_width=True, sharing='streamlit')


	elif factor == "Population Density":
		plot = sns.regplot(x = 'area_norm_tree_count', y = 'population_density', data = complete_data)
		plot.set(xlabel = "Number of Trees (Normalized by Area)", ylabel = "Population Density",
				 title = "Population Density vs Number of Trees")
		st.pyplot(fig, use_container_width=True, sharing='streamlit')


	elif factor == "Industrial Area":
		plot = sns.regplot(x = 'area_norm_tree_count', y = 'per_industrial_area', data = complete_data)
		plot.set(xlabel = "Number of Trees (Normalized by Area)", ylabel = "Percentage Industrial Area",
				 title = "Percentage Industrial Area vs Number of Trees")
		st.pyplot(fig, use_container_width=True, sharing='streamlit')


	elif factor == "Commercial Area":
		plot = sns.regplot(x = 'area_norm_tree_count', y = 'per_commercial_area', data = complete_data)
		plot.set(xlabel = "Number of Trees (Normalized by Area)", ylabel = "Percentage Commercial Area",
				 title = "Percentage Commercial Area vs Number of Trees")
		st.pyplot(fig, use_container_width=True, sharing='streamlit')


	elif factor == "Education":
		plot = sns.regplot(x = 'area_norm_tree_count', y = 'per_diploma', data = complete_data)
		plot.set(xlabel = "Number of Trees (Normalized by Area)", ylabel = "Percentage High School Diplomas",
				 title = "Percentage High School Diplomas vs Number of Trees")
		st.pyplot(fig, use_container_width=True, sharing='streamlit')

	elif factor == "Crime Rate":
		#crime_rate_density_map = combined_data[['neighborhood', 'SNAP_All_csv__Part_1__Major_Cri']].copy()
		plot = sns.regplot(x = 'tree_count', y = 'SNAP_All_csv__Part_1__Major_Cri', data = combined_data)
		plot.set(xlabel = "Number of Trees (Normalized by Area)", ylabel = "Crime Rate(Normalized by Area)",
		title = "Crime Rate vs Number of Trees")
		st.pyplot(fig, use_container_width=True, sharing='streamlit')


	st.write("Then, we wanted to investigate whether other tree benefits are correlated \
		with tree density. Are neighborhoods with higher tree density getting on average \
		more benefits from trees?")

	combined_data_n = pd.read_csv("cleaned_data/tree_density_data.csv")

	info = combined_data_n.drop(labels = ['Unnamed: 0', 'Neighborhood_2010_AREA', 'Neighborhood_2010_ACRES'], axis = 1)

	category = st.radio("Select a category to display", ('Overall Tree Benefit', 'Average Stromwater Benefit', \
		'Average Property Value Benefit', 'Average Energy (Electricity) Benefit','Average Energy (Gas) Benefit',\
		'Average CO2 Benefit','Average Air Quality Benefit'))
	st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

	c1, c2 = st.columns((1, 1))
	with c1:
		tree_density_map = combined_data_n[['neighborhood', 'tree_count']].copy()
		fig=px.choropleth(tree_density_map,
					 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
					 featureidkey='properties.name',   
					 locations='neighborhood',        #column in dataframe
					 color='tree_count',
					  color_continuous_scale='greens',
					   title='Average Tree Density (trees per acre) across Neighborhoods',  
					   height=500,
					   width=1250
					  )
		fig.update_geos(fitbounds="locations", visible=False)
		st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

	with c2:
		if category == "Overall Tree Benefit":
			overall_benefit_map = combined_data_n[['neighborhood', 'overall_benefits_dollar_value']].copy()
			fig=px.choropleth(overall_benefit_map,
					 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
					 featureidkey='properties.name',   
					 locations='neighborhood',        #column in dataframe
					 color='overall_benefits_dollar_value',
					  color_continuous_scale='greens',
					   title='Average Overall benefit in Dollar Value across Neighborhoods' ,  
					   height=500,
					   width=1250
					  )
			fig.layout.coloraxis.colorbar.title = "overall benefit"
			fig.update_geos(fitbounds="locations", visible=False)
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

		elif category == "Average Stromwater Benefit":
			stormwater_benefit_map = combined_data_n[['neighborhood', 'stormwater_benefits_dollar_value']].copy()
			fig=px.choropleth(stormwater_benefit_map,
					 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
					 featureidkey='properties.name',   
					 locations='neighborhood',        #column in dataframe
					 color='stormwater_benefits_dollar_value',
					  color_continuous_scale='greens',
					   title='Average Stormwater benefit in Dollar Value across Neighborhoods' ,  
					   height=500,
					   width=1250
					  )
			fig.layout.coloraxis.colorbar.title = "stormwater benefit"
			fig.update_geos(fitbounds="locations", visible=False)
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

		elif category == "Average Property Value Benefit":
			property_value_benefit_map = combined_data_n[['neighborhood', 'property_value_benefits_dollarvalue']].copy()
			fig=px.choropleth(property_value_benefit_map,
					 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
					 featureidkey='properties.name',   
					 locations='neighborhood',        #column in dataframe
					 color='property_value_benefits_dollarvalue',
					  color_continuous_scale='greens',
					   title='Average Property Value benefit in Dollar Value across Neighborhoods' ,  
					   height=500,
					   width=1250
					  )
			fig.layout.coloraxis.colorbar.title = "property value benefit"
			fig.update_geos(fitbounds="locations", visible=False)
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

		elif category == "Average Energy (Electricity) Benefit":
			energy_electricity_benefit_map = combined_data_n[['neighborhood', 'energy_benefits_electricity_dollar_value']].copy()
			fig=px.choropleth(energy_electricity_benefit_map,
					 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
					 featureidkey='properties.name',   
					 locations='neighborhood',        #column in dataframe
					 color='energy_benefits_electricity_dollar_value',
					  color_continuous_scale='greens',
					   title='Average Energy Electricity benefit in Dollar Value across Neighborhoods' ,  
					   height=500,
					   width=1250
					  )
			fig.layout.coloraxis.colorbar.title = "electricity benefit"
			fig.update_geos(fitbounds="locations", visible=False)
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

		elif category == "Average Energy (Gas) Benefit":
			energy_gas_benefit_map = combined_data_n[['neighborhood', 'energy_benefits_gas_dollar_value']].copy()
			fig=px.choropleth(energy_gas_benefit_map,
						 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
						 featureidkey='properties.name',   
						 locations='neighborhood',        #column in dataframe
						 color='energy_benefits_gas_dollar_value',
						  color_continuous_scale='greens',
						   title='Average Energy Gas benefit in Dollar Value across Neighborhoods' ,  
						   height=500,
						   width=1250
						  )
			fig.layout.coloraxis.colorbar.title = "gas benefit"
			fig.update_geos(fitbounds="locations", visible=False)
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

		elif category == "Average CO2 Benefit":
			co2_benefit_map = combined_data_n[['neighborhood', 'co2_benefits_dollar_value']].copy()
			fig=px.choropleth(co2_benefit_map,
						 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
						 featureidkey='properties.name',   
						 locations='neighborhood',        #column in dataframe
						 color='co2_benefits_dollar_value',
						  color_continuous_scale='greens',
						   title='Average CO2 benefit in Dollar Value across Neighborhoods' ,  
						   height=500,
						   width=1250
						  )
			fig.layout.coloraxis.colorbar.title = "co2 benefit"
			fig.update_geos(fitbounds="locations", visible=False)
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')


		elif category == "Average Air Quality Benefit":
			air_quality_benefit_map = combined_data_n[['neighborhood', 'air_quality_benfits_total_dollar_value']].copy()
			fig=px.choropleth(air_quality_benefit_map,
						 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
						 featureidkey='properties.name',   
						 locations='neighborhood',        #column in dataframe
						 color='air_quality_benfits_total_dollar_value',
						  color_continuous_scale='greens',
						   title='Average Air Quality benefit in Dollar Value across Neighborhoods' ,  
						   height=500,
						   width=1250
						  )
			fig.layout.coloraxis.colorbar.title = "air quality benefit"
			fig.update_geos(fitbounds="locations", visible=False)
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

	st.write("Trees can also provide environmental benefits. We also analyzed whether neighborhoods with \
		higher tree density are less prone to flooding or landslide.")

	st.write("**Tree Density and Environmental/Climatic Factors**")
	env_factor = st.radio("Select a factor", ('Landslide Prone', 'Flooding Prone'))
	st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
	fig, ax = plt.subplots()

	print(combined_data.head(5))

	c1, c2 = st.columns((1, 1))

	with c1:
		if env_factor == "Landslide Prone":
			#landslide_map = combined_data[['neighborhood', 'SNAP_All_csv_Landslide_Prone___']].copy()
			plot = sns.regplot(x = 'tree_count', y = 'SNAP_All_csv_Landslide_Prone___', data = combined_data)
			plot.set(xlabel = "Number of Trees (Normalized by Area)", ylabel = "Landslide susceptibility",
			title = "Landslide susceptibility vs Number of Trees")
			st.pyplot(fig, use_container_width=True, sharing='streamlit')

		elif env_factor == "Flooding Prone":
			#flooding_map = combined_data[['neighborhood', 'SNAP_All_csv_Flood_Plain____lan']].copy()
			plot = sns.regplot(x = 'tree_count', y = 'SNAP_All_csv_Flood_Plain____lan', data = combined_data)
			plot.set(xlabel = "Number of Trees (Normalized by Area)", ylabel = "Flooding susceptibility",
			title = "Flooding susceptibility vs Number of Trees")
			st.pyplot(fig, use_container_width=True, sharing='streamlit')
	with c2:
		if env_factor == "Landslide Prone":
			landslide_map = combined_data[['neighborhood', 'SNAP_All_csv_Landslide_Prone___']].copy()
			fig=px.choropleth(landslide_map,
						 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
						 featureidkey='properties.name',   
						 locations='neighborhood',        #column in dataframe
						 color='SNAP_All_csv_Landslide_Prone___',
						  color_continuous_scale='brwnyl',
						   title='Landslide susceptibility across Neighborhoods' ,  
						   height=500
						  )
			fig.update_geos(fitbounds="locations", visible=False)
			fig.layout.coloraxis.colorbar.title = "susceptibility"
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

		elif env_factor == "Flooding Prone":
			flooding_map = combined_data[['neighborhood', 'SNAP_All_csv_Flood_Plain____lan']].copy()
			fig=px.choropleth(flooding_map,
						 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
						 featureidkey='properties.name',   
						 locations='neighborhood',        #column in dataframe
						 color='SNAP_All_csv_Flood_Plain____lan',
						  color_continuous_scale='blues',
						   title='Flooding susceptibility across Neighborhoods' ,  
						   height=500
						  )
			fig.update_geos(fitbounds="locations", visible=False)
			fig.layout.coloraxis.colorbar.title = "susceptibility"
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')



	st.write("In the tree dataset, there are data points for tree stumps and vacant sites of various sizes, \
		where trees could be planted but have not been planted. Naturally, this leads us to wonder whether \
		there is any correlation between socioeconomic factors and tree stumps and vacant planting spots? \
		Intuitively, there should be some kind of relationship since poorer neighborhoods should have fewer \
		resources to manage trees or plant new trees. We want to see whether this is the case in Pittsburgh, \
		and if so, how severe is the situation.") 

	st.write("Below is a density map of tree stumps and vacant sites across diffrent neighborhood in Pittsburgh")


	df_stump_vacant = raw_df_trees[(raw_df_trees['common_name'] == 'Stump') | 
						   (raw_df_trees['scientific_name'] == 'Stump') |
						   (raw_df_trees['common_name'] == 'Vacant Site Small') | 
						   (raw_df_trees['common_name'] == 'Vacant Site Medium') | 
						   (raw_df_trees['common_name'] == 'Vacant Site Not Suitable') | 
						   (raw_df_trees['common_name'] == 'Vacant Site Large')]

	df_stump_vacant['tree_count'] = 1
	df_stump_density = df_stump_vacant[['neighborhood', 'tree_count', 'stormwater_benefits_dollar_value', 
								'property_value_benefits_dollarvalue', 'energy_benefits_electricity_dollar_value', 
								'energy_benefits_gas_dollar_value', 'air_quality_benfits_total_dollar_value', 
							   'co2_benefits_dollar_value', 'overall_benefits_dollar_value', ]] 
	df_stump_density = df_stump_density.astype(convert_dict)
	df_stump_density = df_stump_density.groupby('neighborhood', as_index=False).agg({"tree_count": "sum", 
																"stormwater_benefits_dollar_value": "sum",
																"property_value_benefits_dollarvalue": "sum",
																"energy_benefits_electricity_dollar_value": "sum",
																"energy_benefits_gas_dollar_value": "sum",
																"air_quality_benfits_total_dollar_value": "sum",
																"co2_benefits_dollar_value": "sum",
																"overall_benefits_dollar_value": "sum"})
	combined_stump = df_stump_density.merge(neighborhood_data_area, on='neighborhood', how='left')
	combined_stump[['tree_count', 'stormwater_benefits_dollar_value', 'property_value_benefits_dollarvalue', 
				   'energy_benefits_electricity_dollar_value', 'energy_benefits_gas_dollar_value',
				  'air_quality_benfits_total_dollar_value', 'co2_benefits_dollar_value', 'overall_benefits_dollar_value',
				   'Pop__2010', 'SNAP_All_csv__Part_1__Major_Cri']] = combined_stump[['tree_count', 'stormwater_benefits_dollar_value', 'property_value_benefits_dollarvalue', 
				   'energy_benefits_electricity_dollar_value', 'energy_benefits_gas_dollar_value',
				  'air_quality_benfits_total_dollar_value', 'co2_benefits_dollar_value', 'overall_benefits_dollar_value',
				   'Pop__2010', 'SNAP_All_csv__Part_1__Major_Cri']].div(combined_stump.Neighborhood_2010_ACRES, axis=0)


	stump_density_map = combined_stump[['neighborhood', 'tree_count']].copy()
	fig=px.choropleth(stump_density_map,
	             geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
	             featureidkey='properties.name',   
	             locations='neighborhood',        #column in dataframe
	             color='tree_count',
	              color_continuous_scale='greens',
	               title='Average Stump/Vacant Sites Density across Neighborhoods' ,  
	               height=500
	              )
	fig.update_geos(fitbounds="locations", visible=False)
	fig.layout.coloraxis.colorbar.title = "count"
	st.plotly_chart(fig, use_container_width=True, sharing='streamlit')


	st.write("**Correlating tree stumps and vacant sites with different socio-economic factors**")
	stump_factor = st.radio("Select a factor", ('Population Density', 'Crime Rate', 'Median Income','Percentage of the Population Under Poverty'))
	st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
	fig, ax = plt.subplots()


	if stump_factor == "Population Density":
		plot = sns.regplot(x = 'tree_count', y = 'Pop__2010', data = combined_stump)
		plot.set(xlabel = "Number of Stumps/Vacant sites (Normalized by Area)", ylabel = "Population Density",
		title = "Population Density vs Number of Stumps/Vacant sites")
		st.pyplot(fig, use_container_width=True, sharing='streamlit')


	elif stump_factor == "Crime Rate":
		plot = sns.regplot(x = 'tree_count', y = 'SNAP_All_csv__Part_1__Major_Cri', data = combined_stump)
		plot.set(xlabel = "Number of Stumps/Vacant sites (Normalized by Area)", ylabel = "Crime Rate(Normalized by Area)",
		title = "Crime Rate vs Number of Stumps/Vacant sites")	
		st.pyplot(fig, use_container_width=True, sharing='streamlit')


	elif stump_factor == "Median Income":
		plot = sns.regplot(x = 'tree_count', y = 'SNAP_All_csv_2009_Median_Income', data = combined_stump)
		plot.set(xlabel = "Number of Stumps/Vacant sites (Normalized by Area)", ylabel = "Median income",
		title = "Median income vs Number of Stumps/Vacant sites")	
		st.pyplot(fig, use_container_width=True, sharing='streamlit')


	elif stump_factor == "Percentage of the Population Under Poverty":
		plot = sns.regplot(x = 'tree_count', y = 'Est__Percent_Under_Poverty__201', data = combined_stump)
		plot.set(xlabel = "Number of Stumps/Vacant sites (Normalized by Area)", ylabel = "Percentage population under poverty",
		title = "Crime Rate vs Number of Stumps/Vacant sites")	
		st.pyplot(fig, use_container_width=True, sharing='streamlit')


	st.write("Based on our investigation, we found that there may be some correlations between socioeconomic \
		factors and tree density and subsequently tree benefits. We did find that there are uneven distributions \
		of tree density across Pittsburgh, and there is a positive correlation between median home values and \
		tree density. This indicates that there may be tree-benefits disparity across neighborhoods, and urban \
		planners should keep this in mind when deciding the urban tree scenery in the future. \
		However, we should keep in mind that this is only a correlation, and to establish a more \
		conclusive relationship, more studies and analyses need to be conducted. ")
		
