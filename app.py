import streamlit as st
import pandas as pd
import plotly.express as px
import os # import os module to check if the file exists

vehicles_df = pd.read_csv

if not os.path.exists(vehicles_df):
    st.error(f"Error: Dataset not found at {vehicles_df}. Please ensure the CSV file is in the correct location.")
    st.stop() # Stop the Streamlit app if data is not found

try:
    vehicles_df = pd.read_csv
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

required_columns = ['price', 'odometer', 'year']
for col in required_columns:
    if col not in vehicles_df.columns:
        st.error(f"Error: Required column '{col}' not found in the dataset. Please check your CSV file.")
        st.stop()

vehicles_df_cleaned = vehicles_df.dropna(subset=required_columns, axis=0)

if 'year' in vehicles_df_cleaned.columns:
    vehicles_df_cleaned['year'] = pd.to_numeric(vehicles_df_cleaned['year'], errors='coerce').fillna(0).astype(int)
    vehicles_df_cleaned = vehicles_df_cleaned[vehicles_df_cleaned['year'] != 0]

st.header("Car Advertisement Data Explorer")
st.write("Explore distributions and relationships within the car advertisement dataset.")

st.subheader("Distribution of Car Prices")
fig_hist_price = px.histogram(vehicles_df_cleaned, x='price', nbins=50, title='Car Prices Distribution', labels={'price': 'Price'})
st.plotly_chart(fig_hist_price, use_container_width=True)

st.subheader("Distribution of Odometer Readings")
fig_hist_odometer = px.histogram(vehicles_df_cleaned, x='odometer', nbins=50, title='Odometer Readings Distribution', labels={'odometer': 'Odometer (miles)'})
st.plotly_chart(fig_hist_odometer, use_container_width=True)

st.subheader("Prive vs Odometer Reading")
st.write("Investigate the relationship between a car's price and it's odometer reading.")

filter_odometer = st.checkbox("Show only cars with odometer below 250,000 miles", value=True)

vehicles_df_display = vehicles_df_cleaned.copy()
if filter_odometer:
    vehicles_df_display = vehicles_df_display[vehicles_df_display['odometer'] < 250000]

hover_cols = ['make', 'model', 'year', 'condition']
existing_hover_cols = [col for col in hover_cols if col in vehicles_df_display.columns]

fig_scatter_price_odometer = px.scatter(vehicles_df_display, x="odometer", y="price", title='Price vs Odometer Reading', hover_data=existing_hover_cols, color='year' if 'year' in vehicles_df_display.columns else None, labels={'odometer': 'Odometer (miles)', 'price': 'Price'})
st.plotly_chart(fig_scatter_price_odometer, use_container_width=True)

st.subheader("Price vs Manufacturing Year")
st.write("Analyze how car prices vary with their manufacturing year.")

if 'condition' in vehicles_df_cleaned.columns:
    fig_scatter_price_year = px.scatter(vehicles_df_cleaned, x="year", y="price", title='Price vs Manufacturing Year (by Condition)', hover_data=existing_hover_cols, color='condition', labels={'year': 'Manufacturing Year', 'price': 'Price ($)'})

else:
    fig_scatter_price_year = px.scatter(vehicles_df_cleaned, x='year', y='price', title='Price vs Manufacturing Year', hover_data=existing_hover_cols, labels={'year': 'Manufacturing Year', 'price': 'Price ($)'})

st.plotly_chart(fig_scatter_price_year, use_container_width=True)

if st.checkbox("Show raw data"):
    st.subheader("Raw Data Smaple")
    st.dataframe(vehicles_df_cleaned.head())
    
