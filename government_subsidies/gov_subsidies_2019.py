
import sys 
import pandas as pd 

abs_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(abs_path)

from data import get_year_2019_data, find_major_industries

nz_2019_data = get_year_2019_data()
major_industries = find_major_industries()

def find_all_2019_subsidies() -> pd.DataFrame:  
    gov_funding = nz_2019_data[nz_2019_data['variable_code'] == 'H06']
    subsidies = gov_funding[gov_funding['industry_code'].isin(major_industries)]
    return subsidies

def find_highest_2019_subsidies(subs_2019: pd.DataFrame) -> pd.DataFrame:
    largest_subsidies = subs_2019[['industry_name', 'value', 'units']].nlargest(n=5, columns='value')
    return largest_subsidies

def find_total_2019_subsidies(subs_2019: pd.DataFrame) -> int:
    total_subs = subs_2019['value'].sum()
    return total_subs

def find_2019_healthcare_subsidies(largest_subsidies: pd.DataFrame) -> int:
    healthcare_subs = largest_subsidies['value'].tolist()[0]
    return healthcare_subs

def find_2019_retail_subsidies(all_subs: pd.DataFrame) -> int:
    retail_subs = all_subs[all_subs['industry_name'] == 'Retail Trade and Accommodation']
    return retail_subs['value'].values[0]

def find_2019_construction_subsidies(all_subs: pd.DataFrame) -> int:
    construction_subs = all_subs[all_subs['industry_name'] == 'Construction']
    return construction_subs['value'].values[0]

all_subs_2019 = find_all_2019_subsidies()
highest_subs_2019 = find_highest_2019_subsidies(all_subs_2019)
total_subs_2019 = find_total_2019_subsidies(all_subs_2019)
healthcare_subs_2019 = find_2019_healthcare_subsidies(highest_subs_2019)
retail_subs_2019 = find_2019_retail_subsidies(all_subs_2019)
construction_subs_2019 = find_2019_construction_subsidies(all_subs_2019)
