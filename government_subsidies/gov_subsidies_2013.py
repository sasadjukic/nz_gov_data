
import sys 
import pandas as pd 

abs_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(abs_path)

from data import get_year_2013_data, find_major_industries

nz_2013_data = get_year_2013_data()
major_industries = find_major_industries()

def find_all_2013_subsidies() -> pd.DataFrame:  
    gov_funding = nz_2013_data[nz_2013_data['variable_code'] == 'H06']
    subsidies = gov_funding[gov_funding['industry_code'].isin(major_industries)]
    return subsidies

def find_highest_2013_subsidies(subs_2013: pd.DataFrame) -> pd.DataFrame:
    largest_subsidies = subs_2013[['industry_name', 'value', 'units']].nlargest(n=5, columns='value')
    return largest_subsidies

def find_total_2013_subsidies(subs_2013: pd.DataFrame) -> int:
    total_subs = subs_2013['value'].sum()
    return total_subs

def find_2013_healthcare_subsidies(largest_subsidies: pd.DataFrame) -> int:
    healthcare_subs = largest_subsidies['value'].tolist()[0]
    return healthcare_subs

def find_2013_retail_subsidies(all_subs: pd.DataFrame) -> int:
    retail_subs = all_subs[all_subs['industry_name'] == 'Retail Trade and Accommodation']
    return retail_subs['value'].values[0]

def find_2013_construction_subsidies(all_subs: pd.DataFrame) -> int:
    construction_subs = all_subs[all_subs['industry_name'] == 'Construction']
    return construction_subs['value'].values[0]

def find_2013_agriculture_subsidies(all_subs: pd.DataFrame) -> int:
    agriculture_subs = all_subs[all_subs['industry_name'] == 'Agriculture, Forestry and Fishing']
    return agriculture_subs['value'].values[0]

def find_2013_manufacturing_subsidies(all_subs: pd.DataFrame) -> int:
    manufacturing_subs = all_subs[all_subs['industry_name'] == 'Manufacturing']
    return manufacturing_subs['value'].values[0]

def find_2013_wholesale_subsidies(all_subs: pd.DataFrame) -> int:
    wholesale_subs = all_subs[all_subs['industry_name'] == 'Wholesale Trade']
    return wholesale_subs['value'].values[0]

all_subs_2013 = find_all_2013_subsidies()
highest_subs_2013 = find_highest_2013_subsidies(all_subs_2013)
total_subs_2013 = find_total_2013_subsidies(all_subs_2013)
healthcare_subs_2013 = find_2013_healthcare_subsidies(highest_subs_2013)
retail_subs_2013 = find_2013_retail_subsidies(all_subs_2013)
construction_subs_2013 = find_2013_construction_subsidies(all_subs_2013)
agriculture_subs_2013 = find_2013_agriculture_subsidies(all_subs_2013)
manufacturing_subs_2013 = find_2013_manufacturing_subsidies(all_subs_2013)
wholesale_subs_2013 = find_2013_wholesale_subsidies(all_subs_2013)


