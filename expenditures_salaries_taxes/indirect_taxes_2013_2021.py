
import sys 
import pandas as pd 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(file_path)

from data import export_clean_data, find_major_industries

nz_data = export_clean_data()
major_industries = find_major_industries()

def get_indirect_taxes(data: pd.DataFrame, industries: set) -> pd.DataFrame:

    taxes = data[data['variable_code'] == 'H10']
    all_taxes = taxes[taxes['industry_code'].isin(industries)]
    return all_taxes 

def get_total_taxes_per_industry(taxes: pd.DataFrame) -> dict[str: int]:

    industry_taxes = {}

    for i in taxes.index:
        industry = taxes.loc[i, 'industry_name']
        in_taxes = taxes.loc[i, 'value']
        if industry.capitalize() not in industry_taxes:
            industry_taxes[industry.capitalize()] = in_taxes 
        else:
            industry_taxes[industry.capitalize()] += in_taxes 

    return industry_taxes

def get_highest_indirect_taxes_per_industry(i_taxes: dict[str:int]) -> pd.Series:

    highest_in_taxes = pd.Series(i_taxes).nlargest(n=5)
    return highest_in_taxes

def get_lowest_indirect_taxes_per_industry(i_taxes: dict[str:int]) -> pd.Series:

    lowest_in_taxes = pd.Series(i_taxes).nsmallest(n=5)
    return lowest_in_taxes

def get_total_indirect_taxes(i_taxes: dict[str:int]) -> int:

    total_taxes = pd.Series(i_taxes).sum()
    return total_taxes

all_taxes = get_indirect_taxes(nz_data, major_industries)
industry_taxes = get_total_taxes_per_industry(all_taxes)
highest_indirect_taxes = get_highest_indirect_taxes_per_industry(industry_taxes)
lowest_indirect_taxes = get_lowest_indirect_taxes_per_industry(industry_taxes)
total_indirect_taxes = get_total_indirect_taxes(industry_taxes)
