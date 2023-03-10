
import sys 
from pathlib import Path
import pandas as pd 

abs_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(abs_path)

from data import get_year_2014_data, find_major_industries

nz_2014_data = get_year_2014_data()
major_industries = find_major_industries()

def find_all_2014_subsidies() -> pd.DataFrame:  
    gov_funding = nz_2014_data[nz_2014_data['variable_code'] == 'H06']
    subsidies = gov_funding[gov_funding['industry_code'].isin(major_industries)]
    return subsidies

def find_highest_2014_subsidies(subs_2014: pd.DataFrame) -> pd.DataFrame:
    largest_subsidies = subs_2014[['industry_name', 'value', 'units']].nlargest(n=5, columns='value')
    return largest_subsidies

def find_total_2014_subsidies(subs_2014: pd.DataFrame) -> int:
    total_subs = subs_2014['value'].sum()
    return total_subs

def find_2014_healthcare_subsidies(largest_subsidies: pd.DataFrame) -> int:
    healthcare_subs = largest_subsidies['value'].tolist()[0]
    return healthcare_subs

def find_2014_retail_subsidies(all_subs: pd.DataFrame) -> int:
    retail_subs = all_subs[all_subs['industry_name'] == 'Retail Trade and Accommodation']
    return retail_subs['value'].values[0]

def find_2014_construction_subsidies(all_subs: pd.DataFrame) -> int:
    construction_subs = all_subs[all_subs['industry_name'] == 'Construction']
    return construction_subs['value'].values[0]

all_subs_2014 = find_all_2014_subsidies()
highest_subs_2014 = find_highest_2014_subsidies(all_subs_2014)
total_subs_2014 = find_total_2014_subsidies(all_subs_2014)
healthcare_subs_2014 = find_2014_healthcare_subsidies(highest_subs_2014)
retail_subs_2014 = find_2014_retail_subsidies(all_subs_2014)
construction_subs_2014 = find_2014_construction_subsidies(all_subs_2014)
