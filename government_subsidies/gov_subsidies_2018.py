
import sys 
from pathlib import Path
import pandas as pd 

abs_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(abs_path)

from data import get_year_2018_data, find_major_industries

nz_2018_data = get_year_2018_data()
major_industries = find_major_industries()

def find_all_2018_subsidies() -> pd.DataFrame:  
    gov_funding = nz_2018_data[nz_2018_data['variable_code'] == 'H06']
    subsidies = gov_funding[gov_funding['industry_code'].isin(major_industries)]
    return subsidies

def find_highest_2018_subsidies(subs_2018: pd.DataFrame) -> pd.DataFrame:
    largest_subsidies = subs_2018[['industry_name', 'value', 'units']].nlargest(n=5, columns='value')
    return largest_subsidies

def find_total_2018_subsidies(subs_2018: pd.DataFrame) -> int:
    total_subs = subs_2018['value'].sum()
    return total_subs

def find_2018_healthcare_subsidies(largest_subsidies: pd.DataFrame) -> int:
    healthcare_subs = largest_subsidies['value'].tolist()[0]
    return healthcare_subs

def find_2018_retail_subsidies(all_subs: pd.DataFrame) -> int:
    retail_subs = all_subs[all_subs['industry_name'] == 'Retail Trade and Accommodation']
    return retail_subs['value'].values[0]

def find_2018_construction_subsidies(all_subs: pd.DataFrame) -> int:
    construction_subs = all_subs[all_subs['industry_name'] == 'Construction']
    return construction_subs['value'].values[0]

all_subs_2018 = find_all_2018_subsidies()
highest_subs_2018 = find_highest_2018_subsidies(all_subs_2018)
total_subs_2018 = find_total_2018_subsidies(all_subs_2018)
healthcare_subs_2018 = find_2018_healthcare_subsidies(highest_subs_2018)
retail_subs_2018 = find_2018_retail_subsidies(all_subs_2018)
construction_subs_2018 = find_2018_construction_subsidies(all_subs_2018)

