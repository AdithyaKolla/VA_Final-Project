import plotly.express as px
import plotly.graph_objs as go
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt


def get_count_athletes_1_over_time(df,selected_country,selected_gender,year_range):
    if selected_country=='Overall':
        temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
        temp_df1=temp_df.groupby(['Year']).ID.nunique().reset_index()
        temp_df1.sort_values('Year')
        return temp_df1

    if selected_country!='Overall':
         temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
         temp_df1=temp_df[temp_df['region']== selected_country]
         temp_df2=temp_df1.groupby(['Year']).ID.nunique().reset_index()
         return temp_df2  

def get_count_athletes_1_over_time_categorized(df,selected_country,selected_gender,year_range):
    if selected_country=='Overall' and len(selected_gender)!=0:
        temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
        temp_df1=temp_df[temp_df['Sex'].isin(selected_gender)]
        temp_df2=temp_df1.groupby(['Year','Sex']).ID.nunique().reset_index()
        return temp_df2
    if  selected_country!='Overall' and len(selected_gender)!=0:
        temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
        temp_df1=temp_df[temp_df['region']== selected_country]
        temp_df2=temp_df1[temp_df1['Sex'].isin(selected_gender)]
        temp_df3=temp_df2.groupby(['Year','Sex']).ID.nunique().reset_index()
        return temp_df3   


def get_medal_count_total(df,selected_country,year_range):
    temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
    temp_df1=temp_df[temp_df['region'].isin(selected_country)]
    temp_df2=temp_df1.groupby(['region','Year']).sum()[['Gold', 'Silver', 'Bronze']].sort_values(
        'Year').reset_index()
    temp_df2['Gold'] = temp_df2['Gold'].astype('int')
    temp_df2['Silver'] = temp_df2['Silver'].astype('int')
    temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
    temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
    return temp_df2

def get_medal_tally(df,selected_country,selected_gender,year_range):
    if (selected_country=='Overall' and len(selected_gender)==0):
        temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
        temp_df2=temp_df.groupby(['region']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total','Gold','Silver','Bronze'],
        ascending=False).reset_index().drop(['index'],axis=1)
        return temp_df3
    if selected_country=='Overall' and len(selected_gender)!=0:
        temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
        temp_df1=temp_df[temp_df['Sex'].isin(selected_gender)]
        temp_df2=temp_df1.groupby(['region']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total','Gold','Silver','Bronze'],
        ascending=False).reset_index().drop(['index'],axis=1)
        return temp_df3
    if selected_country!='Overall' and len(selected_gender)==0:
        temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
        temp_df1=temp_df[temp_df['region']==selected_country]   
        temp_df2=temp_df1.groupby(['region']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total','Gold','Silver','Bronze'],
        ascending=False).reset_index().drop(['index'],axis=1)
        return temp_df3
    if  selected_country!='Overall' and len(selected_gender)!=0:
        temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
        temp_df1=temp_df[(temp_df['region']== selected_country)&(temp_df['Sex'].isin(selected_gender))]    
        temp_df2=temp_df1.groupby(['region']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total','Gold','Silver','Bronze'],
        ascending=False).reset_index().drop(['index'],axis=1)
        return temp_df3
        
    


def get_top_10_athletes_categorized(df,selected_country,selected_gender,year_range):
    if (selected_country=='Overall' and len(selected_gender)==0):
        temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
        temp_df2=temp_df.groupby(['Name','region','Sport']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total'],ascending=False)
        temp_df4=temp_df3[(temp_df3['Total']>0)]
        return temp_df4.head(10) 
    
    if selected_country=='Overall' and len(selected_gender)!=0:
        temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
        temp_df1=temp_df[temp_df['Sex'].isin(selected_gender)]
        temp_df2=temp_df1.groupby(['Name','region','Sport']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total'],ascending=False)
        temp_df4=temp_df3[(temp_df3['Total']>0)]
        return temp_df4.head(10)
    if selected_country!='Overall' and len(selected_gender)==0:
        temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
        temp_df1=temp_df[temp_df['region']==selected_country]
        temp_df2=temp_df1.groupby(['Name','region','Sport']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total'],ascending=False)
        temp_df4=temp_df3[(temp_df3['Total']>0)]
        return temp_df4.head(10)  

    if  selected_country!='Overall' and len(selected_gender)!=0:
        temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
        temp_df1=temp_df[(temp_df['region']== selected_country)&(temp_df['Sex'].isin(selected_gender))]
        temp_df2=temp_df1.groupby(['Name','region','Sport']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total'],ascending=False)
        temp_df4=temp_df3[(temp_df3['Total']>0)]
        return temp_df4.head(10)

def draw_map(dataset, title, colorscale):
        trace = go.Choropleth(
            locations=dataset["region"],
            locationmode="country names",
            z=dataset["ID"],
            text=dataset["region"],
            autocolorscale=False,
            reversescale=False,
            colorscale=colorscale,
            marker=dict(line=dict(color="rgb(0,0,0)", width=0.7)),
            colorbar=dict(title="Medals", tickprefix=""),
        )
        data = [trace]
        layout = go.Layout(
            title=title,
            geo=dict(
                showframe=True,
                showlakes=False,
                showcoastlines=True,
                projection=dict(type="mercator"),
            ),
        )
        fig = dict(data=data, layout=layout)
        return fig

def get_count_events_over_years(df,year_range,selected_country):
    temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
    if selected_country=='Overall':
        temp_df1=temp_df.groupby(['Year'])['Event'].nunique().reset_index()
        temp_df2=temp_df1.sort_values(by=['Year'])
        return temp_df2
    if selected_country!='Overall':
        temp_df1=temp_df[temp_df['region']==selected_country]
        temp_df2=temp_df1.groupby(['Year'])['Event'].nunique().reset_index()
        return temp_df2
def get_sport_medal_tally(df,year_range,selected_country,selected_sport):
    temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
    if selected_country=='Overall'and selected_sport=='Overall':
        temp_df2=temp_df.groupby(['Sport']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total','Gold','Silver','Bronze'],
        ascending=False).reset_index().drop(['index'],axis=1)
        return temp_df3
    if selected_country!='Overall'and selected_sport=='Overall':
        temp_df1=temp_df[temp_df['region']==selected_country]   
        temp_df2=temp_df1.groupby(['Sport']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total','Gold','Silver','Bronze'],
        ascending=False).reset_index().drop(['index'],axis=1)
        return temp_df3
    if selected_country=='Overall'and selected_sport!='Overall':
        temp_df1=temp_df[temp_df['Sport']==selected_sport]   
        temp_df2=temp_df1.groupby(['Sport']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total','Gold','Silver','Bronze'],
        ascending=False).reset_index().drop(['index'],axis=1)
        return temp_df3
    if selected_country!='Overall'and selected_sport!='Overall':
        temp_df1=temp_df[(temp_df['Sport']==selected_sport)&(temp_df['region']==selected_country)]
        temp_df2=temp_df1.groupby(['Sport']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total','Gold','Silver','Bronze'],
        ascending=False).reset_index().drop(['index'],axis=1)
        return temp_df3   
def get_top_10_ath_sport(df,year_range,selected_country,selected_sport):
    temp_df=df[(df['Year']>=year_range[0]) & (df['Year']<=year_range[1])]
    if selected_country=='Overall'and selected_sport=='Overall':
        temp_df2=temp_df.groupby(['Name','Sport','region']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total','Gold','Silver','Bronze'],
        ascending=False).reset_index().drop(['index'],axis=1)
        temp_df4=temp_df3.head(10)
        return temp_df4
    if selected_country!='Overall'and selected_sport=='Overall':
        temp_df1=temp_df[temp_df['region']==selected_country]   
        temp_df2=temp_df1.groupby(['Name','region','Sport']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total','Gold','Silver','Bronze'],
        ascending=False).reset_index().drop(['index'],axis=1)
        temp_df4=temp_df3[temp_df3['Total']>0].head(10)
        return temp_df4
    if selected_country=='Overall'and selected_sport!='Overall':
        temp_df1=temp_df[temp_df['Sport']==selected_sport]   
        temp_df2=temp_df1.groupby(['Name','region','Sport']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total','Gold','Silver','Bronze'],
        ascending=False).reset_index().drop(['index'],axis=1)
        temp_df4=temp_df3[temp_df3['Total']>0].head(10)
        return temp_df4    
    if selected_country!='Overall'and selected_sport!='Overall':
        temp_df1=temp_df[(temp_df['Sport']==selected_sport)&(temp_df['region']==selected_country)]
        temp_df2=temp_df1.groupby(['Name','region','Sport']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        temp_df2['Gold'] = temp_df2['Gold'].astype('int')
        temp_df2['Silver'] = temp_df2['Silver'].astype('int')
        temp_df2['Bronze'] = temp_df2['Bronze'].astype('int')
        temp_df2['Total']=temp_df2['Gold']+temp_df2['Silver']+temp_df2['Bronze']
        temp_df3=temp_df2.sort_values(by=['Total','Gold','Silver','Bronze'],
        ascending=False).reset_index().drop(['index'],axis=1)
        temp_df4=temp_df3[temp_df3['Total']>0].head(10)
        return temp_df4   





        

