import numpy as np
import pandas as pd 



def medal_tally(df, df_1):
    # merge two dataset in basis of NOC
    df = df.merge(df_1, on='NOC', how='left')
    # drop duplicate values
    df = df.drop_duplicates()
    # create binary representation of medal field
    pd.get_dummies(df['Medal'])
    # add to the main df 
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    # drop duplicates values
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    # group by sum on noc, regions have null value, so use noc
    medal_tally = medal_tally.groupby('region')[['Gold', 'Bronze', 'Silver']].sum()
    # rest index
    medal_tally = medal_tally.sort_values('Gold', ascending=False).reset_index()
    # add total
    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Bronze'] + medal_tally['Silver']

    return medal_tally


# drop down list for year & country
def country_year_list(df, df_1):
    # merge two dataset in basis of NOC
    df = df.merge(df_1, on='NOC', how='left')
    # year list
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')



    countries = np.unique(df['region'].dropna().values).tolist()
    countries.sort()
    countries.insert(0, 'Overall')

    return years, countries


def fetch_medal_tally(year, country, df, df_1):

    if year == 'Overall' and country == 'Overall':
        # merge two dataset in basis of NOC
        df = df.merge(df_1, on='NOC', how='left')
        # drop duplicate values
        df = df.drop_duplicates()
        # create binary representation of medal field
        pd.get_dummies(df['Medal'])
        # add to the main df 
        df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
        # drop duplicates values
        medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
        # group by sum on noc, regions have null value, so use noc
        medal_tally = medal_tally.groupby('region')[['Gold', 'Bronze', 'Silver']].sum()
        # rest index
        medal_tally = medal_tally.sort_values('Gold', ascending=False).reset_index()
        # add total
        medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Bronze'] + medal_tally['Silver']


        return medal_tally, 'Overall analysis'

        
        
    if year == 'Overall' and country != 'Overall':
        # merge two dataset in basis of NOC
        df = df.merge(df_1, on='NOC', how='left')
        # drop duplicate values
        df = df.drop_duplicates()
        # create binary representation of medal field
        pd.get_dummies(df['Medal'])
        # add to the main df 
        df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
        # drop duplicates values
        medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
        # filter out data
        medal_tally = medal_tally[medal_tally['region'] == country]
        # group by sum on noc, regions have null value, so use noc
        medal_tally = medal_tally.groupby('region')[['Gold', 'Bronze', 'Silver']].sum()
        # rest index
        medal_tally = medal_tally.sort_values('Gold', ascending=False).reset_index()
        # add total
        medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Bronze'] + medal_tally['Silver']

        title = f'Analysis by Country {country}'
        return medal_tally,title
                                                                                         
        
    if country == 'Overall' and year != 'Overall':
        # merge two dataset in basis of NOC
        df = df.merge(df_1, on='NOC', how='left')
        # drop duplicate values
        df = df.drop_duplicates()
        # create binary representation of medal field
        pd.get_dummies(df['Medal'])
        # add to the main df 
        df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
        # drop duplicates values
        medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
        # filter out data
        medal_tally = medal_tally[medal_tally['Year'] == year]
        # group by sum on noc, regions have null value, so use noc
        medal_tally = medal_tally.groupby('region')[['Gold', 'Bronze', 'Silver']].sum()
        # rest index
        medal_tally = medal_tally.sort_values('Gold', ascending=False).reset_index()
        # add total
        medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Bronze'] + medal_tally['Silver']


        title = f'Analysis by year {year}'
        return medal_tally, title


    if country != 'Overall' and year != 'Overall':
        # merge two dataset in basis of NOC
        df = df.merge(df_1, on='NOC', how='left')
        # drop duplicate values
        df = df.drop_duplicates()
        # create binary representation of medal field
        pd.get_dummies(df['Medal'])
        # add to the main df 
        df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
        # drop duplicates values
        medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
        # filter out data
        medal_tally = medal_tally[medal_tally['Year'] == year]
        medal_tally = medal_tally[medal_tally['region'] == country]
        # group by sum on noc, regions have null value, so use noc
        medal_tally = medal_tally.groupby('region')[['Gold', 'Bronze', 'Silver']].sum()
        # rest index
        medal_tally = medal_tally.sort_values('Gold', ascending=False).reset_index()
        # add total
        medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Bronze'] + medal_tally['Silver']
        
        
        title = f'Analysis of {country} on year {year}'
        return medal_tally, title

    


## over analysis custom functions
def overall_analysis(df, df_1):
    # merge both data set
    df_ = df.merge(df_1, on='NOC', how='left')
    # remove duplicates
    df_ = df_.drop_duplicates()
    # summer olympics filter
    df_ = df_[df_['Season'] == 'Summer']

    
    # calculate 
    # number of cities 
    cities = df_['City'].unique().tolist()
    len_cities = len(cities)

    # no of countries
    country = np.unique(df_['region'].dropna().values).tolist()
    len_countries = len(country)

    # no of events
    events = df_['Event'].unique().tolist()
    len_of_events = len(events)

    # no of sports
    sports = df_['Sport'].unique().tolist()
    len_of_sports = len(sports)

    # no of years
    year =  df_['Year'].unique().tolist()
    len_of_year = len(year)

    # no of athletes
    athletes = df_['Name'].unique().tolist()
    len_of_athletes = len(athletes)

    return cities, len_cities, country, len_countries, events, len_of_events, sports, len_of_sports, year, len_of_year, athletes, len_of_athletes


def graph_1(df, df_1):
    # merge both data set
    df_ = df.merge(df_1, on='NOC', how='left')
    # remove duplicates
    df_ = df_.drop_duplicates()
    # summer olympics filter
    df_ = df_[df_['Season'] == 'Summer']

    # drop duplicates values
    df_10 = df_.drop_duplicates(['Year','NOC'])['Year'].value_counts().reset_index()
    # rename column
    df_10.rename(columns = {'index':'Year', 'Year':'Count'}, inplace = True)
    # sort 
    df_10 = df_10.sort_values(by='Year')

    return df_10

def graph_2(df, df_1):
    # merge both data set
    df_ = df.merge(df_1, on='NOC', how='left')
    # remove duplicates
    df_ = df_.drop_duplicates()
    # summer olympics filter
    df_ = df_[df_['Season'] == 'Summer']

    # sport / year count
    df_11 = df_.drop_duplicates(['Year','Sport'])['Year'].value_counts().reset_index()
    # rename column
    df_11.rename(columns = {'index':'Year', 'Year':'Count'}, inplace = True)
    # sort 
    df_11 = df_11.sort_values(by='Year')

    return df_11

def graph_3(df, df_1):
    # merge both data set
    df_ = df.merge(df_1, on='NOC', how='left')
    # remove duplicates
    df_ = df_.drop_duplicates()
    # summer olympics filter
    df_ = df_[df_['Season'] == 'Summer']

    # count events in each year
    df_12 = df_.drop_duplicates(['Year','Event'])['Year'].value_counts().reset_index()
    # rename column
    df_12.rename(columns = {'index':'Year', 'Year':'Count'}, inplace = True)
    # sort 
    df_12 = df_12.sort_values(by='Year')

    return df_12

def graph_4(df, df_1):
    # merge both data set
    df_ = df.merge(df_1, on='NOC', how='left')
    # remove duplicates
    df_ = df_.drop_duplicates()
    # summer olympics filter
    df_ = df_[df_['Season'] == 'Summer']

    x = df_.drop_duplicates(['Year','Event', 'Sport'])
    x_1 = x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype(int)

    return x_1



def table_2(df, df_1):
    # merge both data set
    df_ = df.merge(df_1, on='NOC', how='left')
    # remove duplicates
    df_ = df_.drop_duplicates()
    # summer olympics filter
    df_ = df_[df_['Season'] == 'Summer']

    # count medals and add to df
    df_30 = pd.concat([df_, pd.get_dummies(df['Medal'])], axis=1)

    # group by sum on noc, regions have null value, so use noc
    player_tally = df_30.groupby('Name')[['Gold', 'Bronze', 'Silver']].sum()

    # total medal
    player_tally['Total'] = player_tally['Gold'] + player_tally['Bronze'] + player_tally['Silver']
    # sort 
    player_tally = player_tally.sort_values(by='Total', ascending=False)
    

    return player_tally





############### Country wise analysis ###############

def countries(df, df_1):
    # merge two dataset in basis of NOC
    df_12 = df.merge(df_1, on='NOC', how='left')
    # summer filter
    df_12 = df_12[df_12['Season'] == 'Summer']
    # remove duplicates
    df_12 = df_12.drop_duplicates()

    # countries
    countries = df_12['region'].unique().tolist()

    return countries


### country wise medal tally / year (line plot)
def country_wise_analysis(df, df_1, country):
    # merge two dataset in basis of NOC
    df_12 = df.merge(df_1, on='NOC', how='left')
    # summer filter
    df_12 = df_12[df_12['Season'] == 'Summer']
    # remove duplicates
    df_12 = df_12.drop_duplicates()
    


    # remove nan in medals 
    df_13 = df_12.dropna(subset=['Medal'])
    # drop duplicates
    df_13 = df_13.drop_duplicates(subset=['Team', 'Medal', 'Sport', 'Games'])

    # country filter
    df_13 = df_13[df_13['region'] == country]
    # count year wise : Group by with count
    df_13 = df_13.groupby(['Year']).count()['Medal'].reset_index()

    return df_13



def countries_good_at(df, df_1, country):
    # merge two dataset in basis of NOC
    df_12 = df.merge(df_1, on='NOC', how='left')
    # summer filter
    df_12 = df_12[df_12['Season'] == 'Summer']
    # remove duplicates
    df_12 = df_12.drop_duplicates()


    # drop duplicates
    df_12 = df_12.drop_duplicates(subset=['Team', 'Medal', 'Sport', 'Games'])
    # count 
    df_20 = df_12.groupby(['region', 'Sport']).count()['Medal'].reset_index()
    # sort 
    df_20 = df_20.sort_values(by='Medal', ascending=False)

    # country filter
    df_20 = df_20[df_20['region'] == country]


    return df_20



def player_good_at_by_countries(df, df_1, country):
    # merge two dataset in basis of NOC
    df_12 = df.merge(df_1, on='NOC', how='left')
    # summer filter
    df_12 = df_12[df_12['Season'] == 'Summer']
    # remove duplicates
    df_12 = df_12.drop_duplicates()


    # drop duplicates
    df_12 = df_12.drop_duplicates(subset=['Team', 'Medal', 'Sport', 'Games'])
    # count
    df_30 = df_12.groupby(['region', 'Name']).count()['Medal'].reset_index()
    # sort
    df_30 = df_30.sort_values(by='Medal', ascending=False)
    # filter
    df_30 = df_30[df_30['region'] == country]



    return df_30





###################### athlete wise analytics ######################

# histogram (PDF) of age 
def pdf_histogram(df):

    # drop duplicates
    df_50 = df.drop_duplicates(subset=['Team', 'Medal', 'Sport', 'Games', 'Name'])


    # filter data
    df_51 = df_50[df_50['Medal'] == 'Gold']
    df_52 = df_50[df_50['Medal'] == 'Silver']
    df_53 = df_50[df_50['Medal'] == 'Bronze']

    # clean out nan values
    x1 = df_51["Age"].dropna()
    x2 = df_52["Age"].dropna()
    x3 = df_53["Age"].dropna()

    # over all age
    x4 = df_50["Age"].dropna()

    return x1, x2, x3, x4


# age histogram in various sports
def age_histogram_sports(df, sports):

    # drop duplicates
    df_50 = df.drop_duplicates(subset=['Team', 'Medal', 'Sport', 'Games', 'Name'])


    # sports filter
    df_60 = df_50[df_50['Sport'] == sports]
    # gold filter
    df_61 = df_60[df_60['Medal'] == 'Gold']
    y1 = df_61["Age"].dropna()


    return y1


# Player who won gold ( weight and height scatter plot )
def Player_who_won_gold(df):

    # drop duplicates
    df_50 = df.drop_duplicates(subset=['Team', 'Medal', 'Sport', 'Games', 'Name'])

    df_70 = df_50.dropna(subset = ["Medal"]) 
    df_70 = df_70.dropna(subset = ["Height"]) 
    df_70 = df_70.dropna(subset = ["Weight"]) 


    
    x1= df_70[df_70['Medal'] == 'Gold']
    height_gold = x1['Height'].tolist()
    weight_gold = x1['Weight'].tolist()

    x2 = df_70[df_70['Medal'] == 'Silver']
    height_silver = x2['Height'].tolist()
    weight_silver = x2['Weight'].tolist()

    x3 = df_70[df_70['Medal'] == 'Bronze']
    height_bronze = x3['Height'].tolist()
    weight_bronze = x3['Weight'].tolist()


    return height_gold, weight_gold, height_silver,weight_silver, height_bronze,weight_bronze 


## Men vs Women participation over the years
def Men_Women_participation(df):

    df= df[df['Season'] == 'Summer']
    # drop duplicates
    df_50 = df.drop_duplicates(subset=['Team', 'Medal', 'Sport', 'Games', 'Name'])

    df_70 = df_50.dropna(subset = ["Medal"]) 
    df_70 = df_70.dropna(subset = ["Height"]) 
    df_70 = df_70.dropna(subset = ["Weight"]) 


    x1= df_70[df_70['Medal'] == 'Gold']

    # male and female filter 
    df_71 = x1[x1['Sex'] == 'M']
    df_72 = x1[x1['Sex'] == 'F']


    # count 
    df_73 = df_71.groupby(['Year']).count()['Sex'].reset_index()
    df_74 = df_72.groupby(['Year']).count()['Sex'].reset_index()

    return df_73, df_74




