import streamlit as st

#from pages import home

def write():
	st.header("Data")
	st.markdown(
    """
    <style>
    .reportview-container {
        background-image: url("https://media.istockphoto.com/photos/abstract-blurred-leaves-of-tree-in-nature-forest-with-sunny-and-bokeh-picture-id1188216286?k=20&m=1188216286&s=612x612&w=0&h=P8yrDhGYb1QDqw_jDOny10cyyjLbETphiDFxxIE8d2o=");
        background-repeat: no-repeat;
        background-position: top;
        background-size: 100% 100%;
    }
   
    </style>
    """,
    unsafe_allow_html=True)

st.header("Datasets")

st.write("The main dataset that we explored is the \"City of Pittsburgh Trees\" dataset found from Western \
        Pennsylvania Regional Data Center: https://data.wprdc.org/dataset/city-trees. It contains \
        45,709 entries and 58 features. The data include trees cared for and managed by the City of\
        Pittsburgh Department of Public Works Forestry Division. In this data, the benefits of the trees \
        are quantified to numerical values and are calculated using the National Tree Benefit Calculator \
        Web Service. Besides trees, the dataset also includes tree stumps that are yet to be removed and\
        vacant spots of various sizes where trees could be planted. These data points offer more dimensions\
        for analysis. Here are all of the features for each tree datapoint. Some interesting ones will be \
        commented.")

st.markdown(
        """
        | **id** | **id** | **type** | **comments** |
| --- | --- | --- | --- |
| 1 | id | text |
| 2 | address_number | text | 
| 3 | street | text | 
 | 4 | common_name | text | 
 | 5 | scientific_name | text | 
 | 6 | height | float |
| 7 | width | float |
| 8 | growth_space_length | float |
| 9 | growth_space_width | float |
| 10 | growth_space_type | text | *what types of environment the tree is planted in. e.g. well, pit, unrestricted, etc.*  |
| 11 | stems | int |
| 12 | overhead_utilities | text | *whether there is overhead utilities and whether the tree is conflicting with utilities.* |
| 13 | land_use | text | *residential, commercial, park, etc.* |
| 14 | condition | text | *condition of the tree. Good, fair, poor, etc.* |
| 15 | stormwater_benefits_dollar_value | float | *trees can control stormwater runoff by acting as mini-reservoirs. This value represents the benefit of stromwater runoff control in dollar te\
rms in a year.* |
| 16 | stormwater_benefits_runoff_elim | float | *number of gallons of stormwater the tree can intercept annually.* |
| 17 | property_value_benefits_dollarvalue | float |
| 18 | property_value_benefits_leaf_surface_area | float |
| 19 | energy_benefits_electricity_dollar_value | float |
| 20 | energy_benefits_gas_dollar_value | float |
| 21 | air_quality_benfits_o3dep_dollar_value | float | *dep means deposition. This is the tree absorbing or intercepting the pollutant . o3 is ozone. * |
| 22 | air_quality_benfits_o3dep_lbs | float |
| 23 | air_quality_benfits_vocavd_dollar_value | float | *voc means volatile organic compounds. avd means avoided. This is the tree lessening the need for creation of these pollutants in the f\
irst place by reducing energy production needs.* |
| 24 | air_quality_benfits_vocavd_lbs | float |
| 25 | air_quality_benfits_no2dep_dollar_value | float | *no2 is nitrogen dioxide.* |
| 26 | air_quality_benfits_no2dep_lbs | float |
| 27 | air_quality_benfits_no2avd_dollar_value | float |
| 28 | air_quality_benfits_no2avd_lbs | float |
| 29 | air_quality_benfits_so2dep_dollar_value | float | *so2 is sulfur dioxide.* |
| 30 | air_quality_benfits_so2dep_lbs | float |
| 31 | air_quality_benfits_so2avd_dollar_value | float |
| 32 | air_quality_benfits_so2avd_lbs | float |
| 33 | air_quality_benfits_pm10depdollar_value | float | *pm10 are inhalable particles with diameters that are generally 10 micrometers and smaller.* |
| 34 | air_quality_benfits_pm10dep_lbs | float |
| 35 | air_quality_benfits_pm10avd_dollar_value | float |
| 36 | air_quality_benfits_pm10avd_lbs | float |
| 37 | air_quality_benfits_total_dollar_value | float |
| 38 | air_quality_benfits_total_lbs | float |
| 39 | co2_benefits_dollar_value | float |
| 40 | co2_benefits_sequestered_lbs | float |
| 41 | co2_benefits_sequestered_value | float |
| 42 | co2_benefits_avoided_lbs | float |
| 43 | co2_benefits_avoided_value | float |
| 44 | co2_benefits_decomp_lbs | float | *CO2 released when tree decomposes. A negative number to indicate emission.* |
| 45 | co2_benefits_maint_lbs | float | *CO2 released for tree maintenance. A negative number to indicate emission.* |
| 46 | co2_benefits_totalco2_lbs | float | *net CO2 benefits* |
| 47 | overall_benefits_dollar_value | float |
| 48 | neighborhood | text |
| 49 | council_district | text |
| 50 | ward | text |
| 51 | tract | text |
| 52 | public_works_division | text |
| 53 | pli_division | text |
| 54 | police_zone | text |
| 55 | fire_zone | text |
| 56 | latitude | float |
| 57 | longitude | float |
| 58 | diameter_base_height | float |
"""
)

st.write("For more detailed explanations for each benefit category, please check out the National Tree Benefit Calculator website (http://www.treebenefits.com/calculator/)")
st.write("The following links also provide useful background information for some of the benefit categories: https://planting.itreetools.org/help/ , https://planting.itreetools.org/references/ , https://www.itreetools.org/documents/248/Streets_Manual_v5.pdf ")

st.write("The other two datasets that we worked with are Pittsburgh American Community Survey 2015 - Miscellaneous Data (https://data.wprdc.org/dataset/pittsburgh-american-community-survey-2015-miscellaneous-data) \
    and Neighborhoods with SNAP Data (https://data.wprdc.org/dataset/neighborhoods-with-snap-data), both of which are also found\
    from Western Pennsylvania Regional Data Center. These two datasets provide neighborhood-level statistics across\
    Pittsburgh, and include information such as population, median home incomes, education attainment, crime rate etc.\
    across the neighborhood. Both datasets contain 90 entries that cover the 90 neighborhoods around Pittsburgh.")

st.header("Data Cleaning")

st.write("For the tree dataset, we performed the following cleaning step: ")
st.write("1. Some datapoints are missing the basic tree name information. Only a few datapoints (13 in total)\
so we decided to drop them.")
st.write("2. There are around 300 data points that are missing its geolocation info. We decided to drop them. \
    Our team is interested in the neighborhood-level granularity so as long as the data point \
    contains neighborhood information, it is valuable to us. ")
st.write("3. Some data points are missing critical information such as tree name. Those are dropped.")
st.write("4. Assume tree stumps has no benefit values so replace NaN with 0.0.")
st.write("5. Assume vacant sites has no benefit values so replace NaN with 0.0")
st.write("6. Some trees are missing some of the height, width, or benefit values. \
    By missing, we mean that these values are either 0.0 or NaN.\
    We replaced them with the average for that tree type so we do not have to drop that tree datapoint.\
    These values should be relatively independent of which neighborhood that tree is located in.\
    For example, it is unlikely that there will be a statistically significant difference in height\
    for the same type of tree across the neighborhoods. Similarly, the air quality value a type of tree provides\
    should be independent of the neighborhood.") 
st.write("7. Some attributes,on the other hand, may depend on the neighborhood.\
    For example, the property value benefits should be heavily influenced by the property value\
    in that neighborhood. Similarly, stormwater benefits can vary across neighborhoods\
    based on the sewage condition. For these attributes, we replaced them with the average for that tree type based on neighborhoods")


st.write("For the neighborhood information datasets, those are very well-maintained and organized datasets, \
    and there was nothing particular that we had to do to clean the dataset. We performed a join of the neighborhood\
    datasets and the tree dataset through the \"neighborhood\" field.")

st.header("4C's of Data")
st.write("Cleaning: Rows having missing values are appropriately cleaned based on reasonable assumptions.")
st.write("Coherent: All the values in the rows are within appropriate limits. No abnormal variations or extreme outliers were detected.")
st.write("Correctness: We did not observe any noticeable evidence that there were measurement issues with the tree data, and since\
    it was supposed to be a comprehensive dataset there is no issue with sampling. The census data could have some inherent\
    bias such as no response bias, but with large enough sample size the bias should be minimized. Also, there are no better alternative census data gathered by reliable entities.")
st.write("aCcountability: The data is publicly available on Western Pennsylvania Regional Data Center and is part of the government database. \
    The neighborhood data are collected by US Census Bureau and the tree dataset is collected by City of\
        Pittsburgh Department of Public Works Forestry Division. These are relatively accountable entities.")