
import sys 
import pandas as pd 

abs_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(abs_path)

from data import get_year_2016_data, find_major_industries

nz_2016_data = get_year_2016_data()
major_industries = find_major_industries()

def find_all_2016_subsidies() -> pd.DataFrame:  
    gov_funding = nz_2016_data[nz_2016_data['variable_code'] == 'H06']
    subsidies = gov_funding[gov_funding['industry_code'].isin(major_industries)]
    return subsidies

def find_highest_2016_subsidies(subs_2016: pd.DataFrame) -> pd.DataFrame:
    largest_subsidies = subs_2016[['industry_name', 'value', 'units']].nlargest(n=5, columns='value')
    return largest_subsidies

def find_total_2016_subsidies(subs_2016: pd.DataFrame) -> int:
    total_subs = subs_2016['value'].sum()
    return total_subs

def find_2016_healthcare_subsidies(largest_subsidies: pd.DataFrame) -> int:
    healthcare_subs = largest_subsidies['value'].tolist()[0]
    return healthcare_subs

def find_2016_retail_subsidies(all_subs: pd.DataFrame) -> int:
    retail_subs = all_subs[all_subs['industry_name'] == 'Retail Trade and Accommodation']
    return retail_subs['value'].values[0]

def find_2016_construction_subsidies(all_subs: pd.DataFrame) -> int:
    construction_subs = all_subs[all_subs['industry_name'] == 'Construction']
    return construction_subs['value'].values[0]

all_subs_2016 = find_all_2016_subsidies()
highest_subs_2016 = find_highest_2016_subsidies(all_subs_2016)
total_subs_2016 = find_total_2016_subsidies(all_subs_2016)
healthcare_subs_2016 = find_2016_healthcare_subsidies(highest_subs_2016)
retail_subs_2016 = find_2016_retail_subsidies(all_subs_2016)
construction_subs_2016 = find_2016_construction_subsidies(all_subs_2016)
