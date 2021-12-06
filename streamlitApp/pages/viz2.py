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
	st.header("Exploring Trees and Other Neighborhood Factors")
	st.write("Trees themselves are definitely interesting and worth studying, especially given the \
		benefits that they offer. As seen previously, trees do not just merely provide visual or\
		 aesthetic appeal to the neighborhood; they provide real economic, climate, and health benefits. \
		 These benefits are available to humans in the forms of energy-saving, air quality improvement, carbon dioxide capture, and many more.")
	st.write("According to the non-profit American Forests, trees are more than scenery; instead, they are \
		 critical infrastructure that every person in every neighborhood deserves. In fact, tree-equality is \
		 a topic included in President Biden and the Democrat’s 3.5-trillion dollar spending bill proposal. \
		 Within the bill, approximately 3 billion dollars will be spent to improve tree equality [1]. \
		 The money will be used for “tree planting and related activities to increase community tree canopy and \
		 associated societal and climate co-benefits, with a priority for projects that increase tree equity.” \
		 This raises the questions: what is the extent of tree equality in Pittsburgh? Are trees' benefits enjoyed \
		 equally by all the neighborhoods in Pittsburgh?") 

	st.write("To answer these questions, we performed some neighborhood-level analysis to get a better insight.")

	st.write(" ")
	st.write("The first thing we tried was to investigate whether there is any correlation \
		between tree density and six different socio-economic factors: median home values, population density, \
		industrial area, commercial area, education, and crime rate. We used the 2010 census result and the 2015 American \
		Community Survey results. Among these factors, median home values, crime rate, education can be \
		seen as an indicator of the wealth and financial wellbeing of the neighborhood. One thing we want to \
		investigate is whether wealthier or more well-off neighborhoods have a higher tree density. \
		You can click on the buttons to see the correlation. ")

	st.write(" ")
	st.write("**Exploring the correlation between tree density and different socio-economic factors**")

	# factor = st.radio("Select a factor", ('Median Home Value', 'Population Density', 'Industrial Area', \
	# 	'Commercial Area', 'Education', 'Crime Rate'))
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



	with st.expander("Median Home Value", expanded=True):
		home_value_data = complete_data[['median_home_value', 'area_norm_tree_count', 'area_norm_overall_benefits_dollar_value']]
		# remove rows where median_home_value is 0
		home_value_data = home_value_data[home_value_data['median_home_value'] != 0]
		fig, ax = plt.subplots()
		plot = sns.regplot(x = 'area_norm_tree_count', y = 'median_home_value', data = home_value_data)
		plot.set(xlabel = "Number of Trees (per Acre of land area)", ylabel = "Median Home Value ($)", 
				 title = "Relationship between Median Home Value and Number of Trees \nin Neighborhoods across Pittsburgh")
		_, c, _ = st.columns((1, 8, 1))
		with c:
			st.pyplot(fig, use_container_width=True, sharing='streamlit')
		st.write("We observe a slight positive correlation between the median home value and the tree density. This is expected due to the several inter-related benefits that trees convey, including physical and visual amenity, shade provision, air quality improvement, noise abatement, and increased biodiversity.")
		st.write("In fact, a Philadelphia-based study demonstrated that properties close to new tree plantings increased in price by about 10% (Wachter and Gillen, 2006). That meant an additional $30,000 USD for the average house price.")


	with st.expander("Population Density"):
		fig, ax = plt.subplots()
		plot = sns.regplot(x = 'area_norm_tree_count', y = 'population_density', data = complete_data)
		plot.set(xlabel = "Number of Trees (per Acre of land area)", ylabel = "Population Density (population per Acre of land area)",
				 title = "Population Density vs Number of Trees")
		_, c, _ = st.columns((1, 8, 1))
		with c:
			st.pyplot(fig, use_container_width=True, sharing='streamlit')
		st.write(
			"We observe a slight positive correlation between the population density and the tree density. "
			"Given that Pittsburgh is an urban city without much forest cover, we believe this is due to the fact that efforts are being made in the densely populated areas to increase street tree density. This could also be a result of the increasing trend of urban greening, which is the practise of  realizing a range of socioecological benefits through introducing, conserving, and maintaining outdoor vegetation in urban areas.")


	with st.expander("Industrial Area"):
		fig, ax = plt.subplots()
		plot = sns.regplot(x = 'area_norm_tree_count', y = 'per_industrial_area', data = complete_data)
		plot.set(xlabel = "Number of Trees (per Acre of land area)", ylabel = "Percentage Industrial Area",
				 title = "Percentage Industrial Area vs Number of Trees")
		_, c, _ = st.columns((1, 8, 1))
		with c:
			st.pyplot(fig, use_container_width=True, sharing='streamlit')
		st.write("In this plot, we do not see any correlation between the tree density and the percentage of industrial area. However, we do notice that there are no regions with high percentage of industrial area and high tree density. This is expected since industrialization often corresponds to cutting down of trees or using barren lands to set up the required infrastructure.")


	with st.expander("Commercial Area"):
		fig, ax = plt.subplots()
		plot = sns.regplot(x = 'area_norm_tree_count', y = 'per_commercial_area', data = complete_data)
		plot.set(xlabel = "Number of Trees (per Acre of land area)", ylabel = "Percentage Commercial Area",
				 title = "Percentage Commercial Area vs Number of Trees")
		_, c, _ = st.columns((1, 8, 1))
		with c:
			st.pyplot(fig, use_container_width=True, sharing='streamlit')
		st.write("Interestingly, we do observe a positive correlation between the percentage of commercial areas in a neighborhood and the tree density. This is again could be due to the  increasing trend of urban greening, which is the practise of realizing a range of socioecological benefits through introducing, conserving, and maintaining outdoor vegetation in urban areas.")


	with st.expander("Education"):
		fig, ax = plt.subplots()
		plot = sns.regplot(x = 'area_norm_tree_count', y = 'per_diploma', data = complete_data)
		plot.set(xlabel = "Number of Trees (per Acre of land area)", ylabel = "Percentage High School Diplomas",
				 title = "Percentage High School Diplomas vs Number of Trees")
		_, c, _ = st.columns((1, 8, 1))
		with c:
			st.pyplot(fig, use_container_width=True, sharing='streamlit')
		st.write("We observe no significant correlation between percentage of high school diplomas in a neighborhood and the tree density.")

	with st.expander("Crime Rate"):
		fig, ax = plt.subplots()
		#crime_rate_density_map = combined_data[['neighborhood', 'SNAP_All_csv__Part_1__Major_Cri']].copy()
		plot = sns.regplot(x = 'tree_count', y = 'SNAP_All_csv__Part_1__Major_Cri', data = combined_data)
		plot.set(xlabel = "Number of Trees (per Acre of land area)", ylabel = "Crime Rate(crimes per Acre of land area)",
		title = "Crime Rate vs Number of Trees")
		_, c, _ = st.columns((1, 8, 1))
		with c:
			st.pyplot(fig, use_container_width=True, sharing='streamlit')
		st.write(
			"Interestingly, we do observe a positive correlation between the crime rate in a neighborhood and the tree density. We believe that this is an indirect effect of the population density being positively correlated with tree density. Though they have not been able to provide any explanation, studies have observed a small but statistically significant positive correlation between population density and property/violence crimes.")

	st.write(
		"**Exploring the correlation between tree density and their benefits across neighborhoods**")

	st.write("Next, we wanted to investigate whether the tree benefits are correlated \
		with tree density. Are neighborhoods with higher tree density getting on average \
		more benefits from trees?")
	st.write("Here, we compare the chloropleth maps of the tree density and the tree benefits. By selecting the tree benefit category, we can compared the tree density and that specific tree benefit. A short analysis is provided below.")

	combined_data_n = pd.read_csv("cleaned_data/tree_density_data.csv")

	info = combined_data_n.drop(labels = ['Unnamed: 0', 'Neighborhood_2010_AREA', 'Neighborhood_2010_ACRES'], axis = 1)

	category = st.selectbox("Select a category to display", ('Overall Tree Benefit', 'Average Stromwater Benefit', \
		'Average Property Value Benefit', 'Average Energy (Electricity) Benefit','Average Energy (Gas) Benefit',\
		'Average CO2 Benefit','Average Air Quality Benefit'))
	st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

	c1, c2 = st.columns((2, 1))
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
		fig.update_layout(margin={"r":0,"l":0})
		st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

	with c2:
		tree_density_map = combined_data_n[
			['neighborhood', 'tree_count']].copy()
		table_data = tree_density_map.sort_values('tree_count',
		                                          ascending=False).head(5)
		table_data = table_data.rename(columns={"neighborhood": "Neighborhood",
		                                        "tree_count": "Tree Density"})
		st.write("Top 5 neighborhoods with Highest Tree Density")
		st.table(data=table_data)

	c3, c4 = st.columns((2, 1))

	with c3:
		if category == "Overall Tree Benefit":
			overall_benefit_map = combined_data_n[['neighborhood', 'overall_benefits_dollar_value']].copy()
			fig=px.choropleth(overall_benefit_map,
					 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
					 featureidkey='properties.name',
					 locations='neighborhood',        #column in dataframe
					 color='overall_benefits_dollar_value',
					  color_continuous_scale='greens',
					   title='Average Overall benefit in USD across Neighborhoods' ,
					   height=500,
					   width=1250
					  )
			fig.layout.coloraxis.colorbar.title = "overall benefit"
			fig.update_geos(fitbounds="locations", visible=False)
			fig.update_layout(margin={"r":0,"l":0})
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

		elif category == "Average Stromwater Benefit":
			stormwater_benefit_map = combined_data_n[['neighborhood', 'stormwater_benefits_dollar_value']].copy()
			fig=px.choropleth(stormwater_benefit_map,
					 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
					 featureidkey='properties.name',   
					 locations='neighborhood',        #column in dataframe
					 color='stormwater_benefits_dollar_value',
					  color_continuous_scale='greens',
					   title='Average Stormwater benefit in USD across Neighborhoods' ,
					   height=500,
					   width=1250
					  )
			fig.layout.coloraxis.colorbar.title = "stormwater benefit"
			fig.update_geos(fitbounds="locations", visible=False)
			fig.update_layout(margin={"r":0,"l":0})
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

		elif category == "Average Property Value Benefit":
			property_value_benefit_map = combined_data_n[['neighborhood', 'property_value_benefits_dollarvalue']].copy()
			fig=px.choropleth(property_value_benefit_map,
					 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
					 featureidkey='properties.name',   
					 locations='neighborhood',        #column in dataframe
					 color='property_value_benefits_dollarvalue',
					  color_continuous_scale='greens',
					   title='Average Property Value benefit in USD across Neighborhoods' ,
					   height=500,
					   width=1250
					  )
			fig.layout.coloraxis.colorbar.title = "property value benefit"
			fig.update_geos(fitbounds="locations", visible=False)
			fig.update_layout(margin={"r":0,"l":0})
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

		elif category == "Average Energy (Electricity) Benefit":
			energy_electricity_benefit_map = combined_data_n[['neighborhood', 'energy_benefits_electricity_dollar_value']].copy()
			fig=px.choropleth(energy_electricity_benefit_map,
					 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
					 featureidkey='properties.name',   
					 locations='neighborhood',        #column in dataframe
					 color='energy_benefits_electricity_dollar_value',
					  color_continuous_scale='greens',
					   title='Average Energy Electricity benefit in USD across Neighborhoods' ,
					   height=500,
					   width=1250
					  )
			fig.layout.coloraxis.colorbar.title = "electricity benefit"
			fig.update_geos(fitbounds="locations", visible=False)
			fig.update_layout(margin={"r":0,"l":0})
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

		elif category == "Average Energy (Gas) Benefit":
			energy_gas_benefit_map = combined_data_n[['neighborhood', 'energy_benefits_gas_dollar_value']].copy()
			fig=px.choropleth(energy_gas_benefit_map,
						 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
						 featureidkey='properties.name',   
						 locations='neighborhood',        #column in dataframe
						 color='energy_benefits_gas_dollar_value',
						  color_continuous_scale='greens',
						   title='Average Energy Gas benefit in USD across Neighborhoods' ,
						   height=500,
						   width=1250
						  )
			fig.layout.coloraxis.colorbar.title = "gas benefit"
			fig.update_geos(fitbounds="locations", visible=False)
			fig.update_layout(margin={"r":0,"l":0})
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

		elif category == "Average CO2 Benefit":
			co2_benefit_map = combined_data_n[['neighborhood', 'co2_benefits_dollar_value']].copy()
			fig=px.choropleth(co2_benefit_map,
						 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
						 featureidkey='properties.name',   
						 locations='neighborhood',        #column in dataframe
						 color='co2_benefits_dollar_value',
						  color_continuous_scale='greens',
						   title='Average CO2 benefit in USD across Neighborhoods' ,
						   height=500,
						   width=1250
						  )
			fig.layout.coloraxis.colorbar.title = "co2 benefit"
			fig.update_geos(fitbounds="locations", visible=False)
			fig.update_layout(margin={"r":0,"l":0})
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')


		elif category == "Average Air Quality Benefit":
			air_quality_benefit_map = combined_data_n[['neighborhood', 'air_quality_benfits_total_dollar_value']].copy()
			fig=px.choropleth(air_quality_benefit_map,
						 geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
						 featureidkey='properties.name',   
						 locations='neighborhood',        #column in dataframe
						 color='air_quality_benfits_total_dollar_value',
						  color_continuous_scale='greens',
						   title='Average Air Quality benefit in USD across Neighborhoods' ,
						   height=500,
						   width=1250
						  )
			fig.layout.coloraxis.colorbar.title = "air quality benefit"
			fig.update_geos(fitbounds="locations", visible=False)
			fig.update_layout(margin={"r":0,"l":0})
			st.plotly_chart(fig, use_container_width=True, sharing='streamlit')


	if category == "Overall Tree Benefit":
		with c4:
			overall_benefit_map = combined_data_n[['neighborhood', 'overall_benefits_dollar_value']].copy()
			table_data = overall_benefit_map.sort_values('overall_benefits_dollar_value', ascending=False).head(5)
			table_data = table_data.rename(
				columns={"neighborhood": "Neighborhood",
				         "overall_benefits_dollar_value": "Overall benefits (USD)"})
			st.write("Top 5 neighborhoods with highest overall benefits")
			st.table(data=table_data)
		st.write("3 of the top 5 neighborhoods with the highest overall benefits are also in the top 5 neighborhoods with highest tree density. This exhibhits a clear positive correlation between the two.")

	elif category == "Average Stromwater Benefit":
		with c4:
			stormwater_benefit_map = combined_data_n[['neighborhood', 'stormwater_benefits_dollar_value']].copy()
			table_data = stormwater_benefit_map.sort_values(
				'stormwater_benefits_dollar_value', ascending=False).head(5)
			table_data = table_data.rename(
				columns={"neighborhood": "Neighborhood",
				         "stormwater_benefits_dollar_value": "Stormwater benefits (USD)"})
			st.write("Top 5 neighborhoods with highest stormwater benefits")
			st.table(data=table_data)
		st.write("3 of the top 5 neighborhoods with the highest stormwater benefits are also in the top 5 neighborhoods with highest tree density. This exhibhits a clear positive correlation between the two")

	elif category == "Average Property Value Benefit":
		with c4:
			property_value_benefit_map = combined_data_n[['neighborhood', 'property_value_benefits_dollarvalue']].copy()
			table_data = property_value_benefit_map.sort_values(
				'property_value_benefits_dollarvalue', ascending=False).head(5)
			table_data = table_data.rename(
				columns={"neighborhood": "Neighborhood",
				         "property_value_benefits_dollarvalue": "Property value benefits (USD)"})
			st.write("Top 5 neighborhoods with highest property value benefits")
			st.table(data=table_data)
		st.write("4 of the top 5 neighborhoods with the highest property value benefits are also in the top 5 neighborhoods with highest tree density. This exhibhits a clear positive correlation between the two")


	elif category == "Average Energy (Electricity) Benefit":
		with c4:
			energy_electricity_benefit_map = combined_data_n[['neighborhood', 'energy_benefits_electricity_dollar_value']].copy()
			table_data = energy_electricity_benefit_map.sort_values(
				'energy_benefits_electricity_dollar_value', ascending=False).head(5)
			table_data = table_data.rename(
				columns={"neighborhood": "Neighborhood",
				         "energy_benefits_electricity_dollar_value": "Energy (Electricity) benefits (USD)"})
			st.write("Top 5 neighborhoods with highest energy (electricity) benefits")
			st.table(data=table_data)

		st.write("3 of the top 5 neighborhoods with the highest energy (electricity) benefits are also in the top 5 neighborhoods with highest tree density. This exhibhits a clear positive correlation between the two")

	elif category == "Average Energy (Gas) Benefit":
		with c4:
			energy_gas_benefit_map = combined_data_n[['neighborhood', 'energy_benefits_gas_dollar_value']].copy()
			table_data = energy_gas_benefit_map.sort_values(
				'energy_benefits_gas_dollar_value', ascending=False).head(5)
			table_data = table_data.rename(
				columns={"neighborhood": "Neighborhood",
				         "energy_benefits_gas_dollar_value": "Energy (Gas) benefits (USD)"})
			st.write("Top 5 neighborhoods with highest energy (gas) benefits")
			st.table(data=table_data)

		st.write("3 of the top 5 neighborhoods with the highest energy (gas) benefits are also in the top 5 neighborhoods with highest tree density. This exhibhits a clear positive correlation between the two")


	elif category == "Average CO2 Benefit":
		with c4:
			co2_benefit_map = combined_data_n[['neighborhood', 'co2_benefits_dollar_value']].copy()
			table_data = co2_benefit_map.sort_values(
				'co2_benefits_dollar_value', ascending=False).head(5)
			table_data = table_data.rename(
				columns={"neighborhood": "Neighborhood",
				         "co2_benefits_dollar_value": "CO2 benefits (USD)"})
			st.write("Top 5 neighborhoods with highest CO2 benefits")
			st.table(data=table_data)
		st.write("3 of the top 5 neighborhoods with the highest CO2 benefits are also in the top 5 neighborhoods with highest tree density. This exhibhits a clear positive correlation between the two")


	elif category == "Average Air Quality Benefit":
		with c4:
			air_quality_benefit_map = combined_data_n[['neighborhood', 'air_quality_benfits_total_dollar_value']].copy()
			table_data = air_quality_benefit_map.sort_values(
				'air_quality_benfits_total_dollar_value', ascending=False).head(5)
			table_data = table_data.rename(
				columns={"neighborhood": "Neighborhood",
				         "air_quality_benfits_total_dollar_value": "Air Quality benefits (USD)"})
			st.write("Top 5 neighborhoods with highest air quality benefits")
			st.table(data=table_data)

		st.write(" 3 of the top 5 neighborhoods with the highest air quality benefits are also in the top 5 neighborhoods with highest tree density. This exhibhits a clear positive correlation between the two")



	st.write("**Tree Density and Environmental/Climatic Factors**")
	st.write("Trees can also provide environmental benefits. We also analyzed whether neighborhoods with \
			higher tree density are less prone to flooding or landslide.")

	env_factor = st.radio("Select a factor", ('Landslide Prone', 'Flooding Prone'))
	st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
	fig, ax = plt.subplots()

	print(combined_data.head(5))

	if env_factor == "Landslide Prone":
		_,c1,_ = st.columns((2, 10, 2))
		with c1:
			#landslide_map = combined_data[['neighborhood', 'SNAP_All_csv_Landslide_Prone___']].copy()
			plot = sns.regplot(x = 'tree_count', y = 'SNAP_All_csv_Landslide_Prone___', data = combined_data)
			plot.set(xlabel = "Number of Trees (per Acre of land area)", ylabel = "Landslide susceptibility",
			title = "Landslide susceptibility vs Number of Trees")
			st.pyplot(fig, use_container_width=True, sharing='streamlit')

		landslide_map = combined_data[
	       		['neighborhood', 'SNAP_All_csv_Landslide_Prone___']].copy()
		fig = px.choropleth(landslide_map,
			            geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
			            featureidkey='properties.name',
			            locations='neighborhood',
			            # column in dataframe
			            color='SNAP_All_csv_Landslide_Prone___',
			            color_continuous_scale='brwnyl',
			            title='Landslide susceptibility across Neighborhoods',
			            height=500
			            )
		fig.update_geos(fitbounds="locations", visible=False)
		fig.layout.coloraxis.colorbar.title = "susceptibility"
		st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

		st.write("We see a negative correlation between the Landslide susceptibility and tree density. This should be expected as trees reduce soil erosion and lower soil moisture levels, thereby lowering the risk of landslides.")

	elif env_factor == "Flooding Prone":
		_,c1,_ = st.columns((2, 10, 2))
		with c1:
			#flooding_map = combined_data[['neighborhood', 'SNAP_All_csv_Flood_Plain____lan']].copy()
			plot = sns.regplot(x = 'tree_count', y = 'SNAP_All_csv_Flood_Plain____lan', data = combined_data)
			plot.set(xlabel = "Number of Trees (per Acre of land area)", ylabel = "Flooding susceptibility",
			title = "Flooding susceptibility vs Number of Trees")
			st.pyplot(fig, use_container_width=True, sharing='streamlit')
                        
		flooding_map = combined_data[
	       		['neighborhood', 'SNAP_All_csv_Flood_Plain____lan']].copy()
		fig = px.choropleth(flooding_map,
			            geojson="https://raw.githubusercontent.com/blackmad/neighborhoods/master/gn-pittsburgh.geojson",
			            featureidkey='properties.name',
			            locations='neighborhood',
			            # column in dataframe
			            color='SNAP_All_csv_Flood_Plain____lan',
			            color_continuous_scale='blues',
			            title='Flooding susceptibility across Neighborhoods',
			            height=500
			            )
		fig.update_geos(fitbounds="locations", visible=False)
		fig.layout.coloraxis.colorbar.title = "susceptibility"
		st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

		st.write("We do not see any correlation between the flooding susceptibility of a neighborohood and it's tree density. We believe that this is mainly due to other geographical features such as proximity to the rivers that primarily affect the flooding susceptibility of the neighborhoods.")

	st.write("**Tree Stumps and Vacant Sites**")
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
	stump_factor = st.selectbox("Select a factor", ('Population Density', 'Crime Rate', 'Median Income','Percentage of the Population Under Poverty'))
	st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
	fig, ax = plt.subplots()

	_, c1, _ = st.columns((1, 8, 1))
	with c1:
		if stump_factor == "Population Density":
			plot = sns.regplot(x = 'tree_count', y = 'Pop__2010', data = combined_stump)
			plot.set(xlabel = "Number of Stumps/Vacant sites (per Acre of land area)", ylabel = "Population Density",
			title = "Population Density vs Number of Stumps/Vacant sites")
			st.pyplot(fig, use_container_width=True, sharing='streamlit')


		elif stump_factor == "Crime Rate":
			plot = sns.regplot(x = 'tree_count', y = 'SNAP_All_csv__Part_1__Major_Cri', data = combined_stump)
			plot.set(xlabel = "Number of Stumps/Vacant sites (per Acre of land area)", ylabel = "Crime Rate(per Acre of land area)",
			title = "Crime Rate vs Number of Stumps/Vacant sites")	
			st.pyplot(fig, use_container_width=True, sharing='streamlit')


		elif stump_factor == "Median Income":
			plot = sns.regplot(x = 'tree_count', y = 'SNAP_All_csv_2009_Median_Income', data = combined_stump)
			plot.set(xlabel = "Number of Stumps/Vacant sites (per Acre of land area)", ylabel = "Median income",
			title = "Median income vs Number of Stumps/Vacant sites")	
			st.pyplot(fig, use_container_width=True, sharing='streamlit')


		elif stump_factor == "Percentage of the Population Under Poverty":
			plot = sns.regplot(x = 'tree_count', y = 'Est__Percent_Under_Poverty__201', data = combined_stump)
			plot.set(xlabel = "Number of Stumps/Vacant sites (per Acre of land area)", ylabel = "Percentage population under poverty",
			title = "Crime Rate vs Number of Stumps/Vacant sites")	
			st.pyplot(fig, use_container_width=True, sharing='streamlit')


	st.write("Based on our investigation, we found that there may be some correlations between socioeconomic \
		factors and tree density and subsequently tree benefits. We did find that there are uneven distributions \
		of tree density across Pittsburgh, and there is a positive correlation between median home values and \
		tree density. This indicates that there may be tree-benefits disparity across neighborhoods, and urban \
		planners should keep this in mind when deciding the urban tree scenery in the future. \
		However, we should keep in mind that this is only a correlation, and to establish a more \
		conclusive relationship, more studies and analyses need to be conducted. ")

	st.write(
		"**What if we had trees in place of these stumps and vacant sites?**")
	st.write("Given that there were 5270 stumps and vacant sites in Pittsburgh, "
	         "we couldn't help but think about the immense benefits of planting trees in these spots.")
	st.write("Though we are now aware that the Oak family of trees have very high overall benefits to mankind, "
	         "it is not possible to plant Oak trees in all of these spots as some vacant sites are not big"
	         " enough. Additionally, there are also a few vacant sites that aren't suitable for growing any "
	         "trees as they are on in pits, wells, lack of sunlight, etc. "
	         "Hence, amongst the vacant sites that could suuport the growth of tree, we first categorized them "
	         "based on the height and width they could offer and then picked the best tree to be planted on that site."
	         "While this was the case with vacant sites, fortuntely most stumps were in spots that supported the "
	         "growth of large tress such Oak." )
	st.write("Based on this analysis, we have calculated the benefits as shown below")
	st.markdown(
		"""
        | **Site type** | **Count** | **Best Fit Tree Species** | **Overall Benefit in USD** |
		| --- | --- | --- | --- |
		| Stump | 1079 | Oak: Pin | 263366.49 |
		| Vacant Site Small	 | 2418 | Pine: Scotch | 189738.06 |
		| Vacant Site Medium | 365 | Tuliptree | 76032.31 |
		| Vacant Site Large | 562 | Oak: Pin | 137175.14 |
		| Vacant Site Not Suitable | 846 | NA | 0.0 |
		""")

	st.write("Hence, by undertaking this mission of replacing the stumps and vacant sites which offer"
	         "no benefits to the residents, with trees the overall annual benefits would estimate to 0.66 million USD!")
