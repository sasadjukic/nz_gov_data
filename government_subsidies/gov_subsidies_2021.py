
import sys 
from pathlib import Path
import pandas as pd 

abs_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(abs_path)

from data import get_year_2021_data, find_major_industries

nz_2021_data = get_year_2021_data()
major_industries = find_major_industries()

def find_all_2021_subsidies() -> pd.DataFrame:  
    gov_funding = nz_2021_data[nz_2021_data['variable_code'] == 'H06']
    subsidies = gov_funding[gov_funding['industry_code'].isin(major_industries)]
    return subsidies

def find_highest_2021_subsidies(subs_2021: pd.DataFrame) -> pd.DataFrame:
    largest_subsidies = subs_2021[['industry_name', 'value', 'units']].nlargest(n=5, columns='value')
    return largest_subsidies

def find_total_2021_subsidies(subs_2021: pd.DataFrame) -> int:
    total_subs = subs_2021['value'].sum()
    return total_subs

def find_2021_healthcare_subsidies(largest_subsidies: pd.DataFrame) -> int:
    healthcare_subs = largest_subsidies['value'].tolist()[0]
    return healthcare_subs

def find_2021_retail_subsidies(all_subs: pd.DataFrame) -> int:
    retail_subs = all_subs[all_subs['industry_name'] == 'Retail Trade and Accommodation']
    return retail_subs['value'].values[0]

def find_2021_construction_subsidies(all_subs: pd.DataFrame) -> int:
    construction_subs = all_subs[all_subs['industry_name'] == 'Construction']
    return construction_subs['value'].values[0]

def find_2021_agriculture_subsidies(all_subs: pd.DataFrame) -> int:
    agriculture_subs = all_subs[all_subs['industry_name'] == 'Agriculture, Forestry and Fishing']
    return agriculture_subs['value'].values[0]

def find_2021_manufacturing_subsidies(all_subs: pd.DataFrame) -> int:
    manufacturing_subs = all_subs[all_subs['industry_name'] == 'Manufacturing']
    return manufacturing_subs['value'].values[0]

def find_2021_wholesale_subsidies(all_subs: pd.DataFrame) -> int:
    wholesale_subs = all_subs[all_subs['industry_name'] == 'Wholesale Trade']
    return wholesale_subs['value'].values[0]

all_subs_2021 = find_all_2021_subsidies()
highest_subs_2021 = find_highest_2021_subsidies(all_subs_2021)
total_subs_2021 = find_total_2021_subsidies(all_subs_2021)
healthcare_subs_2021 = find_2021_healthcare_subsidies(highest_subs_2021)
retail_subs_2021 = find_2021_retail_subsidies(all_subs_2021)
construction_subs_2021 = find_2021_construction_subsidies(all_subs_2021)
agriculture_subs_2021 = find_2021_agriculture_subsidies(all_subs_2021)
manufacturing_subs_2021 = find_2021_manufacturing_subsidies(all_subs_2021)
wholesale_subs_2021 = find_2021_wholesale_subsidies(all_subs_2021)

