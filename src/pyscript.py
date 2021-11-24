import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
pd.set_option('display.max_columns', None)
import datetime as dt
import seaborn as sns
import matplotlib.dates as mdates

#Read dataset and create dataframes
crimes_2016_2019_df = pd.read_csv('data/COBRA-2016-2019.csv')
crimes_2020_1_df = pd.read_csv('data/COBRA-2020-OldRMS-09292020.csv')
crimes_2020_2_df = pd.read_csv('data/COBRA-2020(NEW RMS 9-30 12-31).csv')
crimes_2021_df = pd.read_csv('data/COBRA-2021.csv')
covid19_2020_df = pd.read_csv('data/epicurve_rpt_date.csv')

#convert dtype for resolve dtypewarning
def convert_dtype(x):
    if not x:
        return ''
    try:
        return str(x)   
    except:        
        return ''

#Concatenate two or more dataframes
def concat_df(df1,df2,df3=pd.DataFrame(),df4=pd.DataFrame()):
    df = pd.concat([df1, df2, df3, df4], axis=0)
    return df

#Display all columns on dataframe
def lst_columns(df):
    df = list(df.columns)
    return df

#Drop columns that won't be used
def drop_columns(df):
    df = df.drop(columns=[col for col in df if col not in lst_keep_column], axis=1)
    return df

#Drop null and nan values in column
def dropna_df(df,col):
    df = df.dropna(subset=[col])
    return df

#Show sorted list of unique values
def unique_vals(df, col):
    return sorted(df[col].unique())

#Convert date column to datetime
def date_time(df, col):
    df[col] = pd.to_datetime(df[col], errors='coerce')
    return df[col] 

#Create new column of "Year" from Date column
def col_year(df, col1, col2):
    df[col1] = pd.DatetimeIndex(df[col2]).year
    return df
#Create new column of "Month" from Date column
def col_month(df, col1, col2):
    df[col1] = pd.DatetimeIndex(df[col2]).month
    return df
#Create new column of "YYYY-mm" from Date column
def col_year_month(df, date_col):
    df['YYYY-mm'] = pd.to_datetime(df[date_col]).dt.strftime('%Y-%m')

#Create new column of Month as String format mmm
def col_mmm(df, col1, col2):
    df[col1] = df[col2].dt.strftime('%b')
    return df
    
#Create new column of "Day of Week"
def col_year(df, col1, col2):
    df[col1] = df[col2].dt.day_name()
    return df

#Select filter by year format as yyyy
def filter_year(df, col, year):
    df = df[df[col] == int(year)]
    return df

#Select date range with date format as 'yyyy-mm-dd'
def range_df(df, col, start_date, end_date):
    mask = (df[col] >= start_date) & (df[col] < end_date)
    return df.loc[mask]

#Creating New crime categories column by merging crime subcategories
new_type_name = [
'LARCENY_FROM_VEHICLE',
'LARCENY_NON_VEHICLE',
'AUTO_THEFT',
'BURGLARY',
'AGG_ASSAULT',
'ROBBERY',
'HOMICIDE',
'MANSLAUGHTER']

HOMICIDE =  ['HOMICIDE']
AGG_ASSAULT = ['AGG ASSAULT']
MANSLAUGHTER = ['MANSLAUGHTER']
AUTO_THEFT = ['AUTO THEFT']
LARCENY_FROM_VEHICLE = ['LARCENY-FROM VEHICLE']
LARCENY_NON_VEHICLE = ['LARCENY-NON VEHICLE']
BURGLARY = ['BURGLARY-RESIDENCE', 'BURGLARY-NONRES', 'BURGLARY']
ROBBERY = ['ROBBERY', 'ROBBERY-PEDESTRIAN', 'ROBBERY-COMMERCIAL', 'ROBBERY-RESIDENCE']

new_type_cat = [
LARCENY_FROM_VEHICLE,
LARCENY_NON_VEHICLE,
AUTO_THEFT,
BURGLARY,
AGG_ASSAULT,
ROBBERY,
HOMICIDE,
MANSLAUGHTER]

def new_crime_cat(df):
# Here is the process of re-categorize the type of crime
    new_dic = {}
    for old_cat, str_name in zip(new_type_cat, new_type_name):
        for a, b in zip(old_cat, [str_name]*len(old_cat)):
            new_dic.update([(a, b)])
#Apply the dict to to df to create new categorial column and variable
    new_dic
    df['Crime Categories'] = None
    df['Crime Categories'] = df['UCR Literal'].map(new_dic)

#Filter column
def filt_column(df, col, value):
    df = df[df[col] == value]
    return df

#Bar Plot of Total Crimes Per "Year"
def plot_bar_total_crimes_year(df, col):
    fig, ax = plt.subplots(figsize=[7,6])
    ax = sns.barplot(x=df[col].value_counts().index.tolist(), y=df[col].value_counts().values)
    plt.title(input('Fig Title: '), fontsize = 20)
    plt.ylabel('Number of Crimes', fontsize = 15)
    plt.xlabel(col, fontsize = 15)
    plt.xticks(fontsize = 13)
    plt.yticks(fontsize = 13)
    plt.bar_label(ax.containers[0],size=13)
    fig.tight_layout()
#plt.savefig('images/', dpi=100)

#Bar Plot of Crime categories
def plot_count_crimes_cat_year(df):
    fig, ax = plt.subplots(figsize=[8.5, 6])
    ax = sns.countplot(y = df['Crime Categories'], data = df, order = df['Crime Categories'].value_counts().index)
    plt.title(input('Fig Title: '), fontsize = 20)
    plt.xlabel('Number of Crimes', fontsize = 15)
    plt.ylabel('Crime Categories', fontsize = 15)
    plt.xticks(fontsize = 9)
    plt.yticks(fontsize = 9)
    plt.bar_label(ax.containers[0],size=8)
    fig.tight_layout()
#plt.savefig('images/', dpi=100, bbox_inches = "tight")

#Count Plot of Total Crimes in each Month
def plot_count_total_crimes_monthly(df):
    fig, ax = plt.subplots(figsize=[8, 6])
    ax = sns.countplot(x=df['MMM'])
    plt.title(input('Fig Title: '), fontsize = 20)
    plt.ylabel('Number of Crimes', fontsize = 15)
    plt.xlabel('Month', fontsize = 15)
    plt.xticks(fontsize = 13)
    plt.yticks(fontsize = 13)
    plt.bar_label(ax.containers[0],size=13)
    fig.tight_layout()
#plt.savefig('images/', dpi=100)

#Count Plot of Total Crimes in each Month
def plot_line_graph(df,colx,coly):
    fig, ax = plt.subplots(figsize = (8,6))
    ax = sns.lineplot(x = df[colx], y = df[coly])
    ax.set_ylabel('Daily Reported Cases', fontsize = 15)
    ax.set_xlabel('Month (2020)', fontsize = 15)
    ax.set_title(input('Fig Title: '), fontsize = 20)
    plt.xticks(fontsize = 11)
    plt.yticks(fontsize = 13)
    plt.grid()
    fig.tight_layout()
#plt.savefig('images/', dpi=100)

#Bar Plot of Covid Cases in each Month (2020)
def plot_bar_graph(df,colx,coly):
    fig, ax = plt.subplots(figsize=[8, 6])
    ax = sns.barplot(x=df[colx], y = df[coly])
    ax.set_ylabel('Monthly Reported Cases', fontsize = 15)
    ax.set_xlabel('Month (2020)', fontsize = 15)
    ax.set_title(input('Fig Title: '), fontsize = 20)
    plt.xticks(fontsize = 13)
    plt.yticks(fontsize = 13)
    fig.tight_layout()
#plt.savefig('images/', dpi=100)

#Grab total count for each category by Month
def
type_crimes_df = crimes_2020_df.groupby(["Month","Crime Categories"])["Report Number"].count().reset_index(name="count")

if __name__ == "__main__":

#all columns from crimes dataset
    ['Report Number',
    'Report Date',
    'Occur Date',
    'Occur Time',
    'Possible Date',
    'Possible Time',
    'Beat',
    'Apartment Office Prefix',
    'Apartment Number',
    'Location',
    'Shift occurence',
    'Location Type',
    'UCR Literal',
    'UCR #',
    'Neighborhood',
    'NPU',
    'Latitude',
    'Longitude']

#Columns to keep
lst_keep_column = ['Occur Date', 'UCR Literal']