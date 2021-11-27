import streamlit as st 
import pandas as pd

import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

import preprocessor, helper




#df2 = pd.read_csv("athlete_events.csv")
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')
process_data = preprocessor.preprocess(df, region_df)


st.sidebar.image("https://i.ibb.co/mDH38WV/olympics-logo.png")
st.sidebar.title("Olympics Analysis")
user_menu = st.sidebar.radio(
    'Select an option ',
    ('Overall Analysis','Medal Tally','country-wise-analysis','athlete-wise-analysis' )
)

st.sidebar.write(' ##### Developed by Somnath Paul')



# default home page display
# if user_menu radio button is 
if user_menu == 'Medal Tally':
    
    # year & country 
    year, country = helper.country_year_list(df,region_df)
    # check box for year selection
    selected_year = st.sidebar.selectbox("select year", year)
    selected_country = st.sidebar.selectbox("select country", country)

    # fetch dataframe for selected options 
    medal_df, title = helper.fetch_medal_tally(selected_year, selected_country, df, region_df,)
    # display dataframe
    st.title(title)
    st.dataframe(medal_df)

elif user_menu == 'Overall Analysis':
    cities, len_cities, country, len_countries, events, len_of_events, sports, len_of_sports, year, len_of_year, athletes, len_of_athletes = helper.overall_analysis(df, region_df)

    st.title("STATISTICS :")
    # first column
    col1, col2= st.columns(2)
    with col1:
        st.write(""" ### Hosted Counties""")
        st.title(len_cities)
    with col2:
        st.write(""" ### Counties Participated """)
        st.title(len_countries)


    # second columns
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("""### Sports""")
        st.title(len_of_sports)
    with col2:
        st.write(""" ### Events""")
        st.title(len_of_events)
    with col3:
        st.write(""" ### Editions""")
        st.title(len_of_year)
    with col4:
        st.write(""" ### Athletes""")
        st.title(len_of_athletes)



    # graph 1
    # number of countries participated
    df_10 = helper.graph_1(df, region_df)
    fig = px.line(df_10, x="Year", y="Count")
    st.title("Countries participated in each year")
    st.plotly_chart(fig)



    # graph 2
    # number of sports played in each year
    df_11 = helper.graph_2(df, region_df)
    fig = px.line(df_11, x="Year", y="Count")
    st.title("Sports played in each year")
    st.plotly_chart(fig)



    # graph 3
    # number of events played in each year
    # events has many under one sport
    df_12 = helper.graph_3(df, region_df)
    fig = px.line(df_12, x="Year", y="Count")
    st.title("Events played in each year")
    st.plotly_chart(fig)



    # graph 4 : heatmap
    
    x_1 = helper.graph_4(df, region_df)
    
    fig = px.imshow(x_1)
    st.title("Over the year how many events played / sports")
    st.plotly_chart(fig)


    # table 2:
    top_players = helper.table_2(df, region_df)
    st.title("Top 10 player won medals")
    st.dataframe(top_players.head(10))



elif user_menu == 'country-wise-analysis': 

    countries = helper.countries(df, region_df)
    countries.insert(0, 'Not Selected')
    options = st.selectbox("Select country",countries)
    

    if options == 'Not Selected':
        st.error('Please select country')
    else:
        df_13= helper.country_wise_analysis(df, region_df, options)
        # line chart
        fig = px.line(df_13, x='Year', y='Medal')
        st.subheader(f'Number of medals won by {options} over the year')
        st.plotly_chart(fig)


        df_20 = helper.countries_good_at(df, region_df, options)
        st.subheader(f'Medals won by {options} under different sports')
        st.dataframe(df_20)


        df_30 = helper.player_good_at_by_countries(df, region_df, options)
        st.subheader(f'Medals won by players for {options}')
        st.dataframe(df_30)
        

    

else:
    # athletics wise analysis
    x1, x2, x3, x4 = helper.pdf_histogram(process_data)

    # histogram (PDF) of age in plotly
    import plotly.figure_factory as ff

    gl=['Gold player age', 'Silver player age', 'Bronze player age', 'Overall player age']
    fig = ff.create_distplot([x1, x2, x3, x4], show_hist=False, show_rug=False, group_labels=gl)


    st.title("Athlete Wise Analysis")
    st.write(""" #### Age - Medals wise analysis :""")
    st.plotly_chart(fig)


    st.write(""" #### Player who won gold  [ weight - height ]:""")
    height_gold, weight_gold, height_silver,weight_silver, height_bronze,weight_bronze = helper.Player_who_won_gold(process_data)
    

    plt.scatter(height_gold,weight_gold,color='gold')
    plt.scatter(height_silver,weight_silver  ,color='lightsteelblue')
    plt.scatter(height_bronze,weight_bronze  ,color='lavender')
    plt.legend(["Gold" , "Silver", "Bronze"], bbox_to_anchor = (1 , 1))
    st.pyplot(plt)


    # Men vs Women participation over the years plot
    df_73, df_74 = helper.Men_Women_participation(process_data)
    st.write("### Men vs Women participation over the years")
    plt.figure(figsize=(8,5))
    plt.plot( df_73['Year'], df_73['Sex'], color='olive')
    plt.plot( df_74['Year'], df_74['Sex'])

    plt.legend(["Male" , "Female"], bbox_to_anchor = (1 , 1))
    st.pyplot(plt)
    


    # athletics age sport wise analysis
    sports = process_data['Sport'].unique().tolist()
    sports.insert(0, 'Not Selected')
    sport = st.selectbox("Select a sport",sports)


    if sport == 'Not Selected':
        st.error('Please select sport')
    else:
        y1 = helper.age_histogram_sports(process_data, sport)

        # labels
        gl=[sport]
        st.write(""" #### Age - sport wise analysis :""")
        fig = ff.create_distplot([y1], show_hist=False, show_rug=False, group_labels=gl)
        st.plotly_chart(fig)


        




    

















hide_st_style = """
                <style>
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)