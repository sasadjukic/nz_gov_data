
import sys
import pandas as pd 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(file_path)

from data import export_clean_data, find_major_industries

nz_data = export_clean_data()
major_industries = find_major_industries()

def find_total_incomes(data: pd.DataFrame, industries: set) -> pd.DataFrame:
    income_code = data[data['variable_code'] == 'H01']
    total_income = income_code[income_code['industry_code'].isin(industries)]
    return total_income

def find_total_income_per_industry(all_income: pd.DataFrame) -> dict[str: int]:

    industries_income = {}

    for i in all_income.index:
        industry = all_income.loc[i, 'industry_name']
        income = all_income.loc[i, 'value']
        if industry.capitalize() not in industries_income:
            industries_income[industry.capitalize()] = income
        else:
            industries_income[industry.capitalize()] += income

    return industries_income

def find_highest_income(industries_income: dict[str: int]) -> pd.Series:

    sort_highest = pd.Series(industries_income).nlargest(5)
    return sort_highest 

def find_lowest_income(industries_income: dict[str: int]) -> pd.Series:

    sort_lowest = pd.Series(industries_income).nsmallest(5)
    return sort_lowest

total_income = find_total_incomes(nz_data, major_industries)
all_incomes = find_total_income_per_industry(total_income)
highest_income = find_highest_income(all_incomes)
lowest_income = find_lowest_income(all_incomes)



