- 👋 Hi, I’m Robert from North Carolina currently residing in Baltimore, MD
- 👀 I’m interested in learning everything that data science a has to offer me.
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me by my email. robertalston89@icloud.com

- Explanation of my project: Explanation and How it Addresses Requirements:

app.py in root: The file is created directly in the root of your project directory.

Imports: streamlit, pandas, and plotly.express are imported at the top.

Read CSV:

DATA_PATH = 'data/car_advertisement_data.csv' sets the expected path. You MUST verify this path is correct for your project structure. If your car_advertisement_data.csv is directly in the root, change it to 'car_advertisement_data.csv'. If it's in a different subfolder, adjust accordingly.

pd.read_csv(DATA_PATH) reads the data.

Basic error handling for FileNotFoundError is included to make it more robust.

Data Cleaning/Preparation: A basic data cleaning step is included to drop rows with NaNs in 'price', 'odometer', and 'year', and convert 'year' to integer. This should ideally mirror the cleaning steps you finalized in your EDA.ipynb.

st.header: st.header("Car Advertisement Data Explorer") creates a prominent title.

Plotly Express Histograms:

fig_hist_price = px.histogram(...) creates the first histogram for price.

fig_hist_odometer = px.histogram(...) creates the second histogram for odometer.

st.plotly_chart(fig, use_container_width=True) is used to display the Plotly figures in Streamlit. use_container_width=True makes the plots responsive.

Plotly Express Scatter Plots:

fig_scatter_price_odometer = px.scatter(...) creates the scatter plot for price vs. odometer.

fig_scatter_price_year = px.scatter(...) creates the scatter plot for price vs. year.

hover_data is used to show more details when hovering over points.

color is used to add another dimension to the plots (e.g., coloring by year or condition).

st.checkbox:

filter_odometer = st.checkbox("Show only cars with odometer below 250,000 miles", value=True) creates a checkbox.

An if filter_odometer: block then conditionally filters the df_display DataFrame used for the price_odometer scatter plot. This changes the behavior of the component (the scatter plot) based on the checkbox state.

<!---
Fatrat28338/Fatrat28338 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
