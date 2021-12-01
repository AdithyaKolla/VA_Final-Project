import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
from vega_datasets import data
import plotly.express as px
import plotly.graph_objs as go
import altair as alt


df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df_1896 = preprocessor.preprocess(df, region_df)


read_file_1986_athelte_events = pd.read_csv('athlete_events.csv')
read_file_1986_noc_regions = pd.read_csv('noc_regions.csv')
read_file_2020_technical_official = pd.read_csv('technical_officials.csv')
read_file_2020_medals = pd.read_csv('medals.csv')
read_file_2020_coaches = pd.read_csv('coaches.csv')
read_file_2020_medals_total = pd.read_csv('medals_total.csv')
read_file_2020_athletes = pd.read_csv('athletes.csv')


source = alt.topo_feature(data.world_110m.url, "countries")

st.sidebar.title(" Olympics Dashboard")
st.sidebar.image('https://stillmed.olympics.com/media/Images/Olympic-Games/Tokyo-2020/Banner/Tokyo-2020-page-banner-02.jpg?im=Resize=(1400,720),aspect=fill;Crop,size=(1400,720),gravity=Center')
user_menu= st.sidebar.radio(
    'Select a Dashboard to dispaly',
    ('Athletes Count Dashboard', 'Medal Tally Comparsion','Medal Tally and Top 10 Athletes',
    'choropleth map','Event and Sport wise Dashboard','Olympics 2021 Visualization')
)  
           
if user_menu == 'Athletes Count Dashboard':
        st.sidebar.title('Filtering Options')
        cols=df_1896['region'].dropna().unique().tolist()
        cols.sort()
        cols_OA=['Overall']
        cols_OA.extend(cols)       
        selected_country=st.sidebar.selectbox('select a country',cols_OA)
        cols2=['M','F']
        year_range=st.sidebar.slider('select a year range  you want to visualize',1896,2016,(1896,2016))  
        selected_gender=st.sidebar.multiselect('Select one or more Categories',cols2)
        count_athletes_overall= helper.get_count_athletes_1_over_time(df_1896,selected_country,selected_gender,year_range)
        #print(count_athletes_overall)
        st.title("Total Athletes participated from" +" "+ selected_country)
        map5= alt.Chart(count_athletes_overall).mark_bar().encode(
            x ='Year:O',
            y =alt.Y('ID:Q',title='Total  No of athletes'),
            tooltip=['Year:Q',alt.Tooltip('ID:Q', title=" Total No of athletes")]
        ).properties(
        width=700,
        height=400).interactive()
        st.altair_chart(map5)

        count_athletes_categorized=helper.get_count_athletes_1_over_time_categorized(df_1896,selected_country,selected_gender,year_range)
        st.title("Comparsion between Male and Female for"+"  "+selected_country)
        map6= alt.Chart(count_athletes_categorized).mark_bar().encode(
            x ='Year:O',
            y =alt.Y('ID:Q',title='No of Athletes'),
            color='Sex:N',
            tooltip=['Year:Q',alt.Tooltip('ID:Q', title="No of athletes"),alt.Tooltip('Sex:N',title="Gender")]
            ).properties(
            width=700,
            height=400).interactive()
        st.altair_chart(map6)

if user_menu == 'Medal Tally Comparsion':
        st.sidebar.title('Filtering Options')
        cols=df_1896['region'].dropna().unique().tolist()      
        selected_country=st.sidebar.multiselect('select one or more state(s):',cols,default=['USA'])
        year_range=st.sidebar.slider('select a year range  you want to visualize',1896,2016,(1896,2016))  
        medal_count_total= helper.get_medal_count_total(df_1896,selected_country,year_range)
        map9= alt.Chart(medal_count_total).mark_line().encode(
            x ='Year:O',
            y =alt.Y('Total:Q',title='Total Medals count'),
            color='region:N',
            tooltip=['Year:Q',alt.Tooltip('Total:Q', title=" Total Medals")]
            ).properties(
            width=700,
            height=400,title="Total Medals").interactive()
        st.altair_chart(map9)
        
        map10= alt.Chart(medal_count_total).mark_line().encode(
            x ='Year:O',
            y =alt.Y('Gold:Q',title='Gold Medals count'),
            color='region:N',
            tooltip=['Year:Q',alt.Tooltip('Gold:Q', title="Gold Medals")]
            ).properties(
            width=700,
            height=400,title="Gold Medal").interactive()
        st.altair_chart(map10)
        
        map11= (alt.Chart(medal_count_total).mark_line().encode(
            x ='Year:O',
            y =alt.Y('Silver:Q',title='Silver Medals count'),
            color='region:N',
            tooltip=['Year:Q',alt.Tooltip('Silver:Q', title="Silver Medals")]
            ).properties(
            width=700,
            height=400,title="Silver Medal").interactive())
        st.altair_chart(map11)

        map12= (alt.Chart(medal_count_total).mark_line().encode(
            x ='Year:O',
            y =alt.Y('Bronze:Q',title='Bronze Medals count'),
            color='region:N',
            tooltip=['Year:Q',alt.Tooltip('Bronze:Q', title="Bronze Medals")]
            ).properties(
            width=700,
            height=400,
            title='Bronze Medal').interactive())
        st.altair_chart(map12)

if user_menu=='Medal Tally and Top 10 Athletes':
    st.sidebar.title('Filtering Options')
    cols=df_1896['region'].dropna().unique().tolist()
    cols.sort()
    cols_OA=['Overall']
    cols_OA.extend(cols)       
    selected_country=st.sidebar.selectbox('select a country',cols_OA)
    cols2=['M','F']
    year_range=st.sidebar.slider('select a year range  you want to visualize',1896,2016,(1896,2016)) 
    selected_gender=st.sidebar.multiselect('Select one or more Categories',cols2)
    medal_tally=helper.get_medal_tally(df_1896,selected_country,selected_gender,year_range)
    st.title(selected_country+' '+'Medal tally'+' '+'between'+' '+ str(year_range[0]) +' '+'and'+' '+str(year_range[1]))
    st.table(medal_tally)

    top_10_categorized= helper.get_top_10_athletes_categorized(df_1896,selected_country,selected_gender,year_range)
    st.title('Top 10 Athletes'+' '+ 'for'+ " "+selected_country+' '+'between'+' '+ str(year_range[0]) +' '+'and'+' '+str(year_range[1]))
    st.table( top_10_categorized)

if user_menu=='choropleth map':
    df_medal = df_1896.groupby(["region", "Medal"])["ID"].agg("count").dropna()
    df_1 = pd.DataFrame(df_medal).reset_index()
    gold = df_1[df_1["Medal"] == "Gold"]
    silver = df_1[df_1["Medal"] == "Silver"]
    bronze = df_1[df_1["Medal"] == "Bronze"]
    
    chor_map=helper.draw_map(gold, "Countries that Won Gold Medals", "OrRd")
    chor_map_S=helper.draw_map(silver, "Countries that Won Silver Medals", "Greys")
    chor_map2=helper.draw_map(bronze, "Countries that Won Bronze Medals", "turbid")
    st.plotly_chart(chor_map)
    st.plotly_chart(chor_map_S)
    st.plotly_chart(chor_map2)

if user_menu=='Event and Sport wise Dashboard':
    st.sidebar.title("Visualizations based on Events/Sports")
    event_spec=st.sidebar.radio('Select One',('Total Event Count','Sport wise medal Tally'))
    cols_Sp=df_1896['Sport'].dropna().unique().tolist()
    cols=df_1896['region'].dropna().unique().tolist()
    cols.sort()
    cols_OA=['Overall']
    cols_OA.extend(cols)  
    cols_Sp.sort()
    cols_Sp_OA=['Overall']
    cols_Sp_OA.extend(cols_Sp)        
    if event_spec=='Total Event Count':
        selected_country=st.sidebar.selectbox('select a country',cols_OA) 
        year_range=st.sidebar.slider('select a year range  you want to visualize',1896,2016,(1896,2016))
        event_total=helper.get_count_events_over_years(df_1896,year_range,selected_country)
        map13= alt.Chart(event_total).mark_bar().encode(
            x ='Year:O',
            y =alt.Y('Event:Q',title='Total Event count'),
            tooltip=['Year:Q',alt.Tooltip('Event:Q', title=" Total Events")]
            ).properties(
            width=700,
            height=400,title="Total Events").interactive()
        st.altair_chart(map13)
    if event_spec=='Sport wise medal Tally':
        year_range=st.sidebar.slider('select a year range  you want to visualize',1896,2016,(1896,2016))
        selected_country=st.sidebar.selectbox('select a Country',cols_OA)
        selected_sport=st.sidebar.selectbox('select a Sport',cols_Sp_OA)
        sport_medal_tally=helper.get_sport_medal_tally(df_1896,year_range,selected_country,selected_sport)
        st.title('Sport wise Medal Tally')
        st.table(sport_medal_tally)
        top_10_ath_sp=helper.get_top_10_ath_sport(df_1896,year_range,selected_country,selected_sport)
        st.title('Top 10 Athletes')
        st.table(top_10_ath_sp)


if user_menu=='Olympics 2021 Visualization':
    st.title("Total Medal Count display for the Countries")
    country_map = go.Figure(data=go.Choropleth(
        locations = read_file_2020_medals_total['Country Code'],
        z = read_file_2020_medals_total['Total'],
        text = read_file_2020_medals_total['Country Code'],
        colorscale = 'Blues',
        autocolorscale=True,
        reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        # colorbar_tickprefix = 'Total Medal Count : ',
        colorbar_title = 'Total Medal Count',
        ))
        
    st.plotly_chart(country_map)
    st.title("Top 10 Countries with most number of Medals")
    st.table(read_file_2020_medals_total)
    
    countries_medal_graph= alt.Chart(read_file_2020_medals_total).mark_line().encode(
            x ='Country Code:O',
            y =alt.Y('Total:Q',title='Total Medals count'),
            tooltip=[alt.Tooltip('Total:Q', title=" Total Medals")]
            ).properties(
            width = 800,
            height = 400,
            title="Graph of total medals won by different countries").interactive()
    st.altair_chart(countries_medal_graph)
    st.title('Graph of Total Number of Gold, Silver and Bronze medals won by top 10 Countries')
    top10_countries_gold= (alt.Chart(read_file_2020_medals_total.head(10)).mark_line().encode(
            x ='Country Code:O',
            y =alt.Y('Gold Medal:Q',title='Gold Medals count'),
            tooltip=[alt.Tooltip('Gold Medal:Q', title="Gold Medals")]
            ).properties(
            width=700,
            height=400,
            title='Gold Medal').interactive())
    
    top10_countries_silver= (alt.Chart(read_file_2020_medals_total.head(10)).mark_line().encode(
            x ='Country Code:O',
            y =alt.Y('Silver Medal:Q',title='Silver Medals count'),
            tooltip=[alt.Tooltip('Silver Medal:Q', title="Silver Medals")]
            ).properties(
            width=700,
            height=400,
            title='Silver Medal').interactive())
    
    top10_countries_bronze= (alt.Chart(read_file_2020_medals_total.head(10)).mark_line().encode(
            x ='Country Code:O',
            y =alt.Y('Bronze Medal:Q',title='Bronze Medals count'),
            tooltip=[alt.Tooltip('Bronze Medal:Q', title="Bronze Medals")]
            ).properties(
            width=700,
            height=400,
            title='Bronze Medal').interactive())
    
    
    st.altair_chart(top10_countries_gold)
    st.altair_chart(top10_countries_silver)
    st.altair_chart(top10_countries_bronze)
    
    st.title('Top Players ')
    df_medals = pd.DataFrame(data =read_file_2020_medals , columns = ['medal_type' , 'medal_code' , 'athlete_name' , 'athlete_sex' , 'country_code' , 'discipline' , 'event' , 'country' ])
    # display(df_medals)
    df_medals =df_medals.groupby(['athlete_name','country_code'])['medal_type'].count()
    # df_medals=df_medals.sort_values(by=['medal_type'],ascending=False)
    df_medals = pd.DataFrame(data=df_medals)
    df_medals=df_medals.sort_values(by=['medal_type'],ascending=False)

  
    
    st.table(df_medals.head(34))
    
#     df_gender = pd.DataFrame(data = read_file_2020_athletes, columns=['gender', 'country' , 'discipline'] )
#     df_gender  = df_gender.groupby(['discipline' , 'gender'])['gender'].count()
#     st.write(df_gender)

    
    

    









