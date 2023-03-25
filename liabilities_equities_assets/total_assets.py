
import sys 
import pandas as pd 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(file_path)

from data import export_clean_data, find_major_industries

nz_data = export_clean_data()
major_industries = find_major_industries()
assets = nz_data[nz_data['variable_code'] == 'H24']

def find_major_industry_assets(assets: pd.DataFrame, industry: set) -> pd.DataFrame:

    mi_assets = assets[assets['industry_code'].isin(industry)]
    return mi_assets 

def get_total_assets(assets: pd.DataFrame) -> int:

    all_assets = assets[assets['industry_name'] == 'All industries']
    total_assets = all_assets['value'].sum()
    return total_assets

def get_financial_total_assets(assets: pd.DataFrame) -> int:

    finances = assets[assets['industry_name'] == 'Financial and Insurance Services']
    f_assets = finances['value'].sum()
    return f_assets 

def find_total_assets_per_industry(all: pd.DataFrame) -> dict[str:int]:
    
    assets_per_industry = {}

    for i in all.index:
        industry = all.loc[i, 'industry_name']
        value = all.loc[i, 'value']
        if industry not in assets_per_industry:
            assets_per_industry[industry] = value 
        else:
            assets_per_industry[industry] += value

    return assets_per_industry

def find_highest_total_assets(total: dict[str:int]) -> pd.Series:

    highest_assets = pd.Series(total).nlargest(n=5)
    return highest_assets

def find_lowest_total_assets(total: dict[str:int]) -> pd.Series:
    
    lowest_assets = pd.Series(total).nsmallest(n=5)
    return lowest_assets

def decline_of_mining_assets_per_year(assets: pd.DataFrame) -> pd.DataFrame:

    mining = assets[assets['industry_name'] == 'Mining']
    return mining[['year', 'value']]

all_assets = find_major_industry_assets(assets, major_industries)
total_assets = get_total_assets(assets)
financial_assets = get_financial_total_assets(assets)
assets_pi = find_total_assets_per_industry(all_assets)
highest_api = find_highest_total_assets(assets_pi)
lowest_api = find_lowest_total_assets(assets_pi)
mining_decline = decline_of_mining_assets_per_year(all_assets)




