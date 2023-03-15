
import sys 
import pandas as pd 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(file_path)

from data import export_clean_data, find_major_industries

nz_data = export_clean_data()
major_industries = find_major_industries()

def find_income_per_employee_count(data: pd.DataFrame, industries: set) -> pd.DataFrame:
    
    income_data = data[data['variable_code'] == 'H34']
    income_per_employee = income_data[income_data['industry_code'].isin(industries)]
    return income_per_employee

def find_total_income_per_employee_count(ipe: pd.DataFrame) -> dict[str:int]:

    industry_income_employee = {}

    for i in ipe.index:
        industry = ipe.loc[i, 'industry_name']
        income_per_employee = ipe.loc[i, 'value']
        if industry.capitalize() not in industry_income_employee:
            industry_income_employee[industry.capitalize()] = income_per_employee
        else: 
            industry_income_employee[industry.capitalize()] += income_per_employee

    return industry_income_employee 

def get_yearly_average_income_per_employee_count(total_ipe: dict[str:int]) -> dict[str:int]:

    for key, value in total_ipe.items():
        total_ipe[key] = int(round(value / 9))

    return total_ipe

def get_highest_average_income_per_employee_count(avg_ipe: dict[str:int]) -> pd.Series:

    highest_avg_income = pd.Series(avg_ipe).nlargest(n=5)
    return highest_avg_income

def get_lowest_average_income_per_employee_count(avg_ipe: dict[str:int]) -> pd.Series:

    lowest_avg_income = pd.Series(avg_ipe).nsmallest(n=5)
    return lowest_avg_income

income_per_employee_count = find_income_per_employee_count(nz_data, major_industries)
total_income_per_employee_count = find_total_income_per_employee_count(income_per_employee_count)
average_income_per_employee_count = get_yearly_average_income_per_employee_count(total_income_per_employee_count)
highest_avg_income_per_employee_count = get_highest_average_income_per_employee_count(average_income_per_employee_count)
lowest_avg_income_per_employee_count = get_lowest_average_income_per_employee_count(average_income_per_employee_count)