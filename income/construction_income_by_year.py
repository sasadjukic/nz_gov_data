
import sys
import pandas as pd 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(file_path)

from data import export_clean_data
                  
nz_data = export_clean_data()

def find_construction_income_by_year(data: pd.DataFrame) -> dict[int:int]:

    construction = data[data['industry_name'] == 'Construction'] 
    construction_income = {}

    for i in construction.index:
        year = construction.loc[i, 'year']
        income = construction.loc[i, 'value']
        if year not in construction_income:
            construction_income[year] = income
    
    return construction_income

def sort_ascending(income: dict[int:int]) -> list[tuple]:

    sorted_income = sorted(income.items(), key = lambda x: x[1])
    return sorted_income

find_income = find_construction_income_by_year(nz_data)
construction_income = sort_ascending(find_income)