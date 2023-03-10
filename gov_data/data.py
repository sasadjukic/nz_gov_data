
import pandas as pd 
from pathlib import Path 

directory = Path(__file__).parents[1]
file = directory / 'annual-enterprise-survey-2021-financial-year-provisional-csv.csv'

nz_data = pd.read_csv(file)

# Change column names
nz_data.rename(columns = {
    'Year' :  'year',
    'Industry_aggregation_NZSIOC' : 'industry_aggregation',
    'Industry_code_NZSIOC' : 'industry_code',
    'Industry_name_NZSIOC' : 'industry_name',
    'Units' : 'units',
    'Variable_code' : 'variable_code',
    'Variable_name' : 'variable_name',
    'Variable_category' : 'variable_category',
    'Value' : 'value',
    'Industry_code_ANZSIC06' : 'industry_code_06'
}, inplace=True)

# fix 'value' column and turn values into integers
nz_data['value'] = nz_data['value'].str.replace(r'C', '0', regex=True)
nz_data['value'] = nz_data['value'].str.replace(r'S', '0', regex=True)
nz_data['value'] = nz_data['value'].str.replace(r',', '', regex=True).astype('int64')


def export_clean_data() -> pd.DataFrame:
    return nz_data

def find_major_industries() -> set:
    major_industries = set([x for x in nz_data['industry_code'].to_list() if len(x) == 2])
    return major_industries

def get_year_2013_data() -> pd.DataFrame:
    
    data_2013 = nz_data[nz_data['year'] == 2013]
    return data_2013

def get_year_2014_data() -> pd.DataFrame:

    data_2014 = nz_data[nz_data['year'] == 2014]
    return data_2014 

def get_year_2015_data() -> pd.DataFrame:

    data_2015 = nz_data[nz_data['year'] == 2015]
    return data_2015

def get_year_2016_data() -> pd.DataFrame:

    data_2016 = nz_data[nz_data['year'] == 2016]
    return data_2016 

def get_year_2017_data() -> pd.DataFrame:

    data_2017 = nz_data[nz_data['year'] == 2017]
    return data_2017

def get_year_2018_data() -> pd.DataFrame:

    data_2018 = nz_data[nz_data['year'] == 2018]
    return data_2018

def get_year_2019_data() -> pd.DataFrame:

    data_2019 = nz_data[nz_data['year'] == 2019]
    return data_2019 

def get_year_2020_data() -> pd.DataFrame:

    data_2020 = nz_data[nz_data['year'] == 2020]
    return data_2020 

def get_year_2021_data() -> pd.DataFrame:

    data_2021 = nz_data[nz_data['year'] == 2021]
    return data_2021