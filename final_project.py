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

sns.set()

st.set_page_config(layout="wide")
st.sidebar.header('Analyzing Pittsburgh\'s Trees')
st.sidebar.markdown('05839 INTERACTIVE DATA SCIENCE| FALL 2021')
st.markdown(
    f'''
        <style>
            .sidebar .sidebar-content {{
                width: 375px;
            }}
        </style>
    ''',
    unsafe_allow_html=True
)

combined_data = pd.read_csv("cleaned_data/tree_density_data.csv")


st.header("Neighborhood Level Analysis")

info = combined_data.drop(labels = ['Unnamed: 0', 'Neighborhood_2010_AREA', 'Neighborhood_2010_ACRES'], axis = 1)
corrMatrix = info.corr()

fig, ax = plt.subplots()
sns.heatmap(corrMatrix, annot=True)

st.pyplot(fig, use_container_width=True, sharing='streamlit')


c1, c2 = st.columns((1, 4))

with c1:
	category = st.radio("Select a category to display", ('Average Tree Density', 'Overall Tree Benefit', 'Average Stromwater Benefit', \
		'Average Property Value Benefit', 'Average Energy (Electricity) Beneift','Average Energy (Gas) Beneift',\
		'Average CO2 Benefit','Average Air Quality Benefit'))

with c2:
	if category == "Average Tree Density":
		tree_density_map = combined_data[['neighborhood', 'tree_count']].copy()
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

	elif category == "Overall Tree Benefit":
		overall_benefit_map = combined_data[['neighborhood', 'overall_benefits_dollar_value']].copy()
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
		stormwater_benefit_map = combined_data[['neighborhood', 'stormwater_benefits_dollar_value']].copy()
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
		property_value_benefit_map = combined_data[['neighborhood', 'property_value_benefits_dollarvalue']].copy()
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

	elif category == "Average Energy (Electricity) Beneift":
		energy_electricity_benefit_map = combined_data[['neighborhood', 'energy_benefits_electricity_dollar_value']].copy()
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

	elif category == "Average Energy (Gas) Beneift":
		energy_gas_benefit_map = combined_data[['neighborhood', 'energy_benefits_gas_dollar_value']].copy()
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
		co2_benefit_map = combined_data[['neighborhood', 'co2_benefits_dollar_value']].copy()
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
		air_quality_benefit_map = combined_data[['neighborhood', 'air_quality_benfits_total_dollar_value']].copy()
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


st.header("Tree Characteristics")


df_trees = pd.read_csv("cleaned_data/cleaned_tree_data_5.csv", encoding="ISO-8859-1", low_memory=False)

option = st.selectbox(
'Choose a Tree Characteristics',
('Height', 'Width'))

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

str1 = "Neighborhoods with the most number of " + str(selected_spec) + " trees in pittsburgh"
st.write(str1)

df_spec1 = df_spec.sort_values(by=['count'], ascending = False)
df_spec1 = df_spec1.head(5)
ax = df_spec1.plot.bar(x='neighborhood', y='count', rot='vertical', ylabel = 'Number of trees', title= str1)

full_neigh = pd.DataFrame({'neighborhood' : df_trees['neighborhood'].unique()})
full_neigh = full_neigh.rename(columns={"id": "count"})
full_neigh = full_neigh.merge(df_spec, how = 'outer', on = ['neighborhood'])
full_neigh['count'] = full_neigh['count'].fillna(0)
full_neigh = full_neigh.drop(labels = ['common_name'], axis = 1)
full_neigh.sort_values(['count'], ascending= False)

str2 = "Distribution of " + selected_spec + " across neighborhoods of Pittsburgh"
st.write(str2)
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
df_trees = pd.read_csv("cleaned_data/cleaned_tree_data_5.csv", encoding="ISO-8859-1", low_memory=False)
tree_stat = df_trees.groupby(["common_name"]).agg(["count", "mean"]).reset_index()
tree_stat = tree_stat[tree_stat["id"]["count"] >= 10]

option = st.selectbox('Select an Attribute',('Storm Water Benefit', 'Property Value Benefit', 'Electricity Saving Benefit',\
	'Gas Saving Benefit', 'Air Quality Benefit', 'CO2 Benefit','Overall Benefit'))


corresponding_cols = {'Storm Water Benefit':"stormwater_benefits_dollar_value",\
					'Property Value Benefit':"property_value_benefits_dollarvalue",\
					'Electricity Saving Benefit':"energy_benefits_electricity_dollar_value",\
					'Gas Saving Benefit':'energy_benefits_gas_dollar_value',\
					'Air Quality Benefit':'air_quality_benfits_total_dollar_value',\
					'CO2 Benefit':"co2_benefits_dollar_value",'Overall Benefit':"overall_benefits_dollar_value"}

top_k = st.slider('Select Top K Species', 10, 30, 15)

fig, ax = plt.subplots(figsize=(3, 3))
graph_data = tree_stat.sort_values([(corresponding_cols[option],"mean")])
graph_data = graph_data.tail(top_k)
plot = sns.barplot(x=graph_data["common_name"], y=graph_data[corresponding_cols[option]]["mean"],color="limegreen")
plot.set_xticklabels(plot.get_xticklabels(), 
					  rotation=90, 
					  horizontalalignment='right')
ax.tick_params(axis='both', which='major', labelsize=6)
ax.tick_params(axis='both', which='minor', labelsize=6)

if option == "Storm Water Benefit":
	plot.set_xlabel("Tree Species", fontsize = 12)
	plot.set_ylabel("Average Stormwater Benefit in Dollar Value", fontsize = 12)
	st.pyplot(fig, use_container_width=True, sharing='streamlit')

elif option == 'Property Value Benefit':
	plot.set_xlabel("Tree Species", fontsize = 12)
	plot.set_ylabel("Average Property Benefit in Dollar Value", fontsize = 12)
	st.pyplot(fig, use_container_width=True, sharing='streamlit')

elif option == 'Electricity Saving Benefit':
	plot.set_xlabel("Tree Species", fontsize = 12)
	plot.set_ylabel("Average Energy (Electricity) Benefit in Dollar Value", fontsize = 12)
	st.pyplot(fig, use_container_width=True, sharing='streamlit')


elif option == 'Gas Saving Benefit':
	plot.set_xlabel("Tree Species", fontsize = 12)
	plot.set_ylabel("Average Energy (Gas) Benefit in Dollar Value", fontsize = 12)
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
		no2_air_quality_total_benefit.set_xlabel("Tree Species", fontsize = 12)
		no2_air_quality_total_benefit.set_ylabel("Average NO2 Decomposition Benefit in Dollar Value", fontsize = 12)
		st.pyplot(fig, use_container_width=True, sharing='streamlit')

	elif pollutant == "SO2":
		so2_air_quality_total_benefit = tree_stat.sort_values([("air_quality_benfits_so2dep_dollar_value","mean")])
		so2_air_quality_total_benefit = so2_air_quality_total_benefit.tail(30)
		so2_air_quality_total_benefit = sns.barplot(x=so2_air_quality_total_benefit["common_name"], y=so2_air_quality_total_benefit["air_quality_benfits_so2dep_dollar_value"]["mean"], color="limegreen")
		so2_air_quality_total_benefit.set_xticklabels(so2_air_quality_total_benefit.get_xticklabels(), 
								rotation=90, 
								horizontalalignment='right')
		so2_air_quality_total_benefit.set_xlabel("Tree Species", fontsize = 12)
		so2_air_quality_total_benefit.set_ylabel("Average SO2 Decomposition Benefit in Dollar Value", fontsize = 12)
		st.pyplot(fig, use_container_width=True, sharing='streamlit')

	elif pollutant == "PM10":
		pm10_air_quality_total_benefit = tree_stat.sort_values([("air_quality_benfits_pm10depdollar_value","mean")])
		pm10_air_quality_total_benefit = pm10_air_quality_total_benefit.tail(30)
		
		pm10_air_quality_total_benefit = sns.barplot(x=pm10_air_quality_total_benefit["common_name"], y=pm10_air_quality_total_benefit["air_quality_benfits_pm10depdollar_value"]["mean"], color="limegreen")
		pm10_air_quality_total_benefit.set_xticklabels(pm10_air_quality_total_benefit.get_xticklabels(), 
								rotation=90, 
								horizontalalignment='right')
		pm10_air_quality_total_benefit.set_xlabel("Tree Species", fontsize = 12)
		pm10_air_quality_total_benefit.set_ylabel("Average SO2 Decomposition Benefit in Dollar Value", fontsize = 12)
		st.pyplot(fig, use_container_width=True, sharing='streamlit')

	elif pollutant == "Overall":
		plot.set_xlabel("Tree Species", fontsize = 12)
		plot.set_ylabel("Average Overall Air Quality Benefit in Dollar Value", fontsize = 12)
		st.pyplot(fig, use_container_width=True, sharing='streamlit')


elif option == "CO2 Benefit":
	plot.set_xlabel("Tree Species", fontsize = 12)
	plot.set_ylabel("Average CO2 Benefit in Dollar Value", fontsize = 12)
	st.pyplot(fig, use_container_width=True, sharing='streamlit')

elif option == "Overall Benefit":

	plot.set_xlabel("Tree Species", fontsize = 12)
	plot.set_ylabel("Average Overall Benefit in Dollar Value", fontsize = 12)

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



st.header("Tree-family benefits and intra-group comparison")
tree_family = st.radio("Select a factor", ('Oak', 'Maple', 'Elm', 'Ash','Magnolia', 'Beech'))
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
	tree_group = specific_trees_to_plot.groupby("common_name").agg('mean')
	grouped_plot = sns.heatmap(tree_group[["stormwater_benefits_dollar_value","property_value_benefits_dollarvalue",\
		"energy_benefits_electricity_dollar_value","energy_benefits_gas_dollar_value","air_quality_benfits_total_dollar_value",\
		"co2_benefits_dollar_value", "overall_benefits_dollar_value"]], annot= True, fmt='g', xticklabels = True, \
		yticklabels = True, cmap = 'Greens', norm=LogNorm())
	st.pyplot(fig, use_container_width=True, sharing='streamlit')


st.header("Exploring Trees and Other Neighborhood Factors")
st.write("exploring the correlation of tree density with different socio-economic factors")

st.write("Tree themselves are definitely interesting and worth understanding, especially given the benefits that\
	they can offer. However, one aspect that is worth investigating is that are tree's benefits enjoyed equally")

factor = st.radio("Select a factor", ('Median Home Value', 'Population Density', 'Industrial Area', \
	'Commercial Area', 'Education'))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

complete_data = pd.read_csv("cleaned_data/neighborhood_features_data.csv")
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








