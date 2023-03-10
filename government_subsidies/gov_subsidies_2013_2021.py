
import sys 
from pathlib import Path 
import pandas as pd 

abs_filepath = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(abs_filepath)

from data import export_clean_data, find_major_industries

nz_data = export_clean_data()
major_industries = find_major_industries()

def find_government_subsidies_per_industry(data: pd.DataFrame, industries: set) -> pd.DataFrame:

    gov_funding = data[data['variable_code'] == 'H06']
    subsidies = gov_funding[gov_funding['industry_code'].isin(industries)]
    return subsidies 

def assign_subsidies_to_industries(subsidies: pd.DataFrame) -> dict[str:int]:

    industry_subsidies = {}

    for i in subsidies.index:
        industry = subsidies.loc[i, 'industry_name']
        subsidy = subsidies.loc[i, 'value']
        if industry.capitalize() not in industry_subsidies:
            industry_subsidies[industry.capitalize()] = subsidy
        else:
            industry_subsidies[industry.capitalize()] += subsidy

    return industry_subsidies

def find_total_subsidies(subsidies: pd.DataFrame) -> dict[str:int]:
    
    total_subsidies = {'all_industries' : 0}

    for i in subsidies.index:
        subsidy = subsidies.loc[i, 'value']
        total_subsidies['all_industries'] += subsidy

    return total_subsidies

def get_highest_industry_subsidies(industries: dict[str:int]) -> pd.Series:

    sort_highest = pd.Series(industries).nlargest(n=5)
    return sort_highest 

def get_lowest_industry_subsidies(industry: dict[str:int]) -> pd.Series:

    sort_lowest = pd.Series(industry).nsmallest(n=5)
    return sort_lowest

gov_subsidies = find_government_subsidies_per_industry(nz_data, major_industries)
all_industries = assign_subsidies_to_industries(gov_subsidies)
total_subsidies = find_total_subsidies(gov_subsidies)
highest_subsidies = get_highest_industry_subsidies(all_industries)
lowest_subsidies = get_lowest_industry_subsidies(all_industries)

