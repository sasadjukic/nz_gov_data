
import sys 
import pandas as pd 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(file_path)

from data import export_clean_data, find_major_industries

nz_data = export_clean_data()
major_industries = find_major_industries()

def find_total_expenditure(data: pd.DataFrame, industries: set) -> pd.DataFrame:

    expenditures = data[data['variable_code'] == 'H08']
    industry_expenditures = expenditures[expenditures['industry_code'].isin(industries)]
    return industry_expenditures

def find_total_expenditures_per_industry(all_expenditures: pd.DataFrame) -> dict[str:int]:
    
    industry_expenditure = {}

    for i in all_expenditures.index:
        industry = all_expenditures.loc[i, 'industry_name']
        expenditure = all_expenditures.loc[i, 'value']
        if industry.capitalize() not in industry_expenditure:
            industry_expenditure[industry.capitalize()] = expenditure
        else:
            industry_expenditure[industry.capitalize()] += expenditure

    return industry_expenditure

def find_top_expenditures_per_industry(epi: dict[str:int]) -> pd.Series:

    top_expenditures = pd.Series(epi).nlargest(n=5)
    return top_expenditures

def find_lowest_expenditures_per_industry(epi: dict[str:int]) -> pd.Series:

    lowest_expenditures = pd.Series(epi).nsmallest(n=5)
    return lowest_expenditures

total_expenditures = find_total_expenditure(nz_data, major_industries)
exp_per_industry = find_total_expenditures_per_industry(total_expenditures)
top_expenditures = find_top_expenditures_per_industry(exp_per_industry)
lowest_expenditures = find_lowest_expenditures_per_industry(exp_per_industry)