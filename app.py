import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt

st.set_page_config(
    page_title="Video games analysis",
    layout="wide",
)

st.title("Video Games Analysis Dashboard")

DATA_PATH = "game_sales.csv"

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_PATH, nrows=nrows)
    return data


selected = False


with st.sidebar:
    st.title("Options")
    st.write("")

    overall_insights = st.checkbox("Overall insights and conclusions")

    st.write("")
    st.header("Data")

    show_raw_data = st.checkbox("Show data", value=True)
    nrows = st.number_input("Number of rows", 0, 16600, 10000, 500)
    year_range = st.slider("Year range", 1980, 2020, (1980, 2020), 1)

    st.markdown("---")

    st.header("Plots")


    st.subheader("Based on number of games")
    add_publishers_ngames = st.checkbox("Publishers", key=0)
    add_genres_ngames = st.checkbox("Genres", key=1)
    add_platforms_ngames = st.checkbox("Platforms", key=2)
    add_year_ngames = st.checkbox("Year", key=3, value=True)

    st.subheader("Based on game sales")
    add_publisher_sales = st.checkbox("Publishers", key=4, value=True)
    add_genre_sales = st.checkbox("Genres", key=5)
    add_platform_sales = st.checkbox("Platforms", key=6)
    add_year_sales = st.checkbox("Year", key=7)

    st.write("")
    st.write("")
    st.write("")


if overall_insights:
    st.header("Overall Insights and Conclusions")

    st.markdown("""
- 2009 was a popular year for video games, with the most number of games released.
- While in other regions, action is the most popular genre, in Japan it is role-playing.
- The number of games released per year has decreased exponentially since 2009, with a small increase in 2015. This could be due to the rise of mobile gaming.
    
    """)

    st.write("")
    st.write("")

    # st.write("2008 was a popular year for video games, with the most number of games released.")
    # st.write("While in other regions, action is the most popular genre, in Japan it is role-playing.")
    # st.write("The number of games released per year has decreased exponentially since 2008. This could be due to the rise of mobile gaming.")
    


# Load nrows of data (from number input)
data = load_data(nrows)
# Only use data from the entered year range (from slider)
data = data[(data['Year'] >= year_range[0]) & (data['Year'] <= year_range[1])]

charts = {}



if add_publisher_sales:
    heading5 = st.selectbox("Choose a publisher (for pie chart)", data['Publisher'].unique(), key=99)

    titleee = "Region-wise sales for " + heading5 + " (in millions)"

    NA_sales = data[data['Publisher'] == heading5]['NA_Sales'].sum()
    EU_sales = data[data['Publisher'] == heading5]['EU_Sales'].sum()
    JP_sales = data[data['Publisher'] == heading5]['JP_Sales'].sum()
    Other_sales = data[data['Publisher'] == heading5]['Other_Sales'].sum()

    # Create altair pie chart

    df = pd.DataFrame({'Region': ['North America', 'Europe', 'Japan', 'Other'], 'Sales': [NA_sales, EU_sales, JP_sales, Other_sales]})

    chart5 = alt.Chart(df).mark_arc().encode(
        theta=alt.Theta(field='Sales', type='quantitative'),
        color=alt.Color('Region', type="nominal", legend=alt.Legend(title="Region", labelFontSize=16)),
    )

    conclusion_card_0 = f"For the {heading5} publisher, maximum sales are {max(NA_sales, EU_sales, JP_sales, Other_sales)} million from the region {'North America' if max(NA_sales, EU_sales, JP_sales, Other_sales) == NA_sales else 'Europe' if max(NA_sales, EU_sales, JP_sales, Other_sales) == EU_sales else 'Japan' if max(NA_sales, EU_sales, JP_sales, Other_sales) == JP_sales else 'Other'}."

    charts[titleee] = [chart5, conclusion_card_0]

    # print(NA_sales)


if add_genre_sales:
    heading6 = st.selectbox("Choose a genre (for pie chart)", data['Genre'].unique(), key=98)

    titleee2 = "Region-wise sales for " + heading6 + " (in millions)"


    NA_sales = data[data['Genre'] == heading6]['NA_Sales'].sum()
    EU_sales = data[data['Genre'] == heading6]['EU_Sales'].sum()
    JP_sales = data[data['Genre'] == heading6]['JP_Sales'].sum()
    Other_sales = data[data['Genre'] == heading6]['Other_Sales'].sum()

    # Create altair pie chart

    df = pd.DataFrame({'Region': ['North America', 'Europe', 'Japan', 'Other'], 'Sales': [NA_sales, EU_sales, JP_sales, Other_sales]})

    chart6 = alt.Chart(df).mark_arc().encode(
        theta=alt.Theta(field='Sales', type='quantitative'),
        color=alt.Color('Region', type="nominal", legend=alt.Legend(title="Region", labelFontSize=16)),
    )

    conclusion_card_1 = f"In the {heading6} genre, maximum sales are {max(NA_sales, EU_sales, JP_sales, Other_sales)} million from the region {'North America' if max(NA_sales, EU_sales, JP_sales, Other_sales) == NA_sales else 'Europe' if max(NA_sales, EU_sales, JP_sales, Other_sales) == EU_sales else 'Japan' if max(NA_sales, EU_sales, JP_sales, Other_sales) == JP_sales else 'Other'}."


    charts[titleee2] = [chart6, conclusion_card_1]


if add_platform_sales:
    heading7 = st.selectbox("Choose a platform (for pie chart)", data['Platform'].unique(), key=97)

    titleee3 = "Region-wise sales for " + heading7 + " (in millions)"


    NA_sales = data[data['Platform'] == heading7]['NA_Sales'].sum()
    EU_sales = data[data['Platform'] == heading7]['EU_Sales'].sum()
    JP_sales = data[data['Platform'] == heading7]['JP_Sales'].sum()
    Other_sales = data[data['Platform'] == heading7]['Other_Sales'].sum()

    # Create altair pie chart

    df = pd.DataFrame({'Region': ['North America', 'Europe', 'Japan', 'Other'], 'Sales': [NA_sales, EU_sales, JP_sales, Other_sales]})

    chart7 = alt.Chart(df).mark_arc().encode(
        theta=alt.Theta(field='Sales', type='quantitative'),
        color=alt.Color('Region', type="nominal", legend=alt.Legend(title="Region", labelFontSize=16)),
    )

    conclusion_card_2 = f"On the {heading7} platform, maximum sales are {max(NA_sales, EU_sales, JP_sales, Other_sales)} million from the region {'North America' if max(NA_sales, EU_sales, JP_sales, Other_sales) == NA_sales else 'Europe' if max(NA_sales, EU_sales, JP_sales, Other_sales) == EU_sales else 'Japan' if max(NA_sales, EU_sales, JP_sales, Other_sales) == JP_sales else 'Other'}."

    charts[titleee3] = [chart7, conclusion_card_2]


if add_year_sales:
    heading8 = st.selectbox("Choose a year (for pie chart)", [int(i) for i in data['Year'].unique()], key=96)

    titleee4 = "Region-wise sales in " + str(heading8) + " (in millions)"

    NA_sales = data[data['Year'] == heading8]['NA_Sales'].sum()
    EU_sales = data[data['Year'] == heading8]['EU_Sales'].sum()
    JP_sales = data[data['Year'] == heading8]['JP_Sales'].sum()
    Other_sales = data[data['Year'] == heading8]['Other_Sales'].sum()

    # Create altair pie chart

    df = pd.DataFrame({'Region': ['North America', 'Europe', 'Japan', 'Other'], 'Sales': [NA_sales, EU_sales, JP_sales, Other_sales]})

    chart8 = alt.Chart(df).mark_arc().encode(
        theta=alt.Theta(field='Sales', type='quantitative'),
        color=alt.Color('Region', type="nominal", legend=alt.Legend(title="Region", labelFontSize=16)),
    )

    conclusion_card_3 = f"In the year {heading8}, maximum sales are {max(NA_sales, EU_sales, JP_sales, Other_sales)} million from the region {'North America' if max(NA_sales, EU_sales, JP_sales, Other_sales) == NA_sales else 'Europe' if max(NA_sales, EU_sales, JP_sales, Other_sales) == EU_sales else 'Japan' if max(NA_sales, EU_sales, JP_sales, Other_sales) == JP_sales else 'Other'}."

    charts[titleee4] = [chart8, conclusion_card_3]




if add_publishers_ngames:
    heading1 = "Top 10 Publishers"

    # Get top 10 publishers
    games_per_publisher = data['Publisher'].value_counts().head(10)

    # Create dataframe for altair
    df = pd.DataFrame({'Publisher': games_per_publisher.index, 'Number of Games': games_per_publisher.values})

    # Create altair chart
    chart1 = alt.Chart(df).mark_bar().encode(
        x=alt.X('Publisher', sort='-y', axis=alt.Axis(labelFontSize=16)), # Sort descending
        y=alt.Y('Number of Games', axis=alt.Axis(labelFontSize=16)),
        tooltip=['Publisher', 'Number of Games']
    )

    conclusion_card_4 = f"The top publisher is {games_per_publisher.index[0]} with {games_per_publisher.values[0]} games."

    charts[heading1] = [chart1, conclusion_card_4]

if add_genres_ngames:
    heading2 = "Top 10 Genres"

    # Get top 10 genres
    games_per_genre = data['Genre'].value_counts().head(10)

    # Create dataframe for altair
    df = pd.DataFrame({'Genre': games_per_genre.index, 'Number of Games': games_per_genre.values})

    # Create altair chart
    chart2 = alt.Chart(df).mark_bar().encode(
        x=alt.X('Genre', sort='-y', axis=alt.Axis(labelFontSize=16)), # Sort descending
        y=alt.Y('Number of Games', axis=alt.Axis(labelFontSize=16)),
        tooltip=['Genre', 'Number of Games']
    )

    conclusion_card_5 = f"The top genre is {games_per_genre.index[0]} with {games_per_genre.values[0]} games."

    charts[heading2] = [chart2, conclusion_card_5]


if add_platforms_ngames:
    heading3 = "Top 10 Platforms"

    # Get top 10 platforms
    games_per_platform = data['Platform'].value_counts().head(10)

    # Create dataframe for altair
    df = pd.DataFrame({'Platform': games_per_platform.index, 'Number of Games': games_per_platform.values})

    # Create altair chart
    chart3 = alt.Chart(df).mark_bar().encode(
        x=alt.X('Platform', sort='-y', axis=alt.Axis(labelFontSize=16)), # Sort descending
        y=alt.Y('Number of Games', axis=alt.Axis(labelFontSize=16)),
        tooltip=['Platform', 'Number of Games']
    )

    conclusion_card_6 = f"The top platform is {games_per_platform.index[0]} with {games_per_platform.values[0]} games."

    charts[heading3] = [chart3, conclusion_card_6]


if add_year_ngames:
    heading4 = "Number of Games per Year"

    # Get number of games per year
    games_per_year = data['Year'].value_counts()

    # Create dataframe for altair
    df = pd.DataFrame({'Year': games_per_year.index, 'Number of Games': games_per_year.values})

    # Create altair chart
    chart4 = alt.Chart(df).mark_bar().encode(
        x=alt.X('Year', axis=alt.Axis(labelFontSize=16)),
        y=alt.Y('Number of Games', axis=alt.Axis(labelFontSize=16)),
        tooltip=['Year', 'Number of Games']
    )

    conclusion_card_7 = f"The year with the most number of games is {int(games_per_year.index[0])} with {games_per_year.values[0]} games."

    charts[heading4] = [chart4, conclusion_card_7]





# charts_keys = list(charts.keys())
# num_charts = len(charts_keys)

# with st.container():
#     num_cols = min(2, num_charts)  # Maximum of 2 columns
#     cols = st.columns(num_cols)

#     for i in range(num_charts):
#         with cols[i % num_cols]:

#             st.write(charts_keys[i])
#             st.altair_chart(charts[charts_keys[i]], use_container_width=True)


# Display all the plots with their conclusion cards next to them. (2 columns)

charts_keys = list(charts.keys())
num_charts = len(charts_keys)

with st.container():
    num_cols = min(2, num_charts)  # Maximum of 2 columns
    cols = st.columns(2)

    for i in range(num_charts):
        with cols[i % num_cols]:

            st.write(charts_keys[i])
            st.altair_chart(charts[charts_keys[i]][0], use_container_width=True)
            st.caption("Conclusion: " + charts[charts_keys[i]][1])


if show_raw_data or add_publishers_ngames or add_genres_ngames or add_platforms_ngames or add_year_ngames or add_publisher_sales or add_genre_sales or add_platform_sales or add_year_sales:
    selected = True


if selected == False:
    st.subheader("Use this dashboard to analyse data regarding video game sales from 1980 to 2020.")
    st.caption("Please select one or more options from the sidebar to start")


if show_raw_data:
    st.subheader("Detailed data view")
    st.dataframe(data, use_container_width=True)
