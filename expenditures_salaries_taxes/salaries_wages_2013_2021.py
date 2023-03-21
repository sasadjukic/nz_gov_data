
import sys 
import pandas as pd 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(file_path)

from data import export_clean_data, find_major_industries

nz_data = export_clean_data()
major_industries = find_major_industries()

def get_salaries(data: pd.DataFrame, industries: set) -> pd.DataFrame:

    salaries = nz_data[nz_data['variable_code'] == 'H12']
    all_salaries = salaries[salaries['industry_code'].isin(industries)]
    return all_salaries

def get_total_salaries_per_industry(salaries: pd.DataFrame) -> dict[str:int]:

    industry_salaries = {}

    for i in salaries.index:
        industry = salaries.loc[i, 'industry_name']
        wages = salaries.loc[i, 'value']
        if industry.capitalize() not in industry_salaries:
            industry_salaries[industry.capitalize()] = wages
        else:
            industry_salaries[industry.capitalize()] += wages

    return industry_salaries 

def get_highest_total_salaries_per_industry(i_salaries: dict[str:int]) -> pd.Series:

    highest_salaries = pd.Series(i_salaries).nlargest(n=5)
    return highest_salaries

def get_lowest_total_salaries_per_industry(i_salaries: dict[str:int]) -> pd.Series:

    lowest_salaries = pd.Series(i_salaries).nsmallest(n=5)
    return lowest_salaries

all_salaries = get_salaries(nz_data, major_industries)
industry_salaries = get_total_salaries_per_industry(all_salaries)
highest_salaries = get_highest_total_salaries_per_industry(industry_salaries)
lowest_salaries = get_lowest_total_salaries_per_industry(industry_salaries)

