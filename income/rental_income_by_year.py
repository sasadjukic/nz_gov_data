
import sys 
import pandas as pd 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(file_path) 

from data import export_clean_data

nz_data = export_clean_data()

def find_yearly_rental_income(data: pd.DataFrame) -> dict[int:int]:

    rental = nz_data[nz_data['industry_name'] == 'Rental, Hiring and Real Estate Services']
    rental_income = {}

    for i in rental.index:
        year = rental.loc[i, 'year']
        income = rental.loc[i, 'value']
        if year not in rental_income:
            rental_income[year] = income 

    return rental_income

def sort_ascending(income: dict[int:int]) -> list[tuple]:

    sorted_income = sorted(income.items(), key = lambda x: x[1])
    return sorted_income

find_income = find_yearly_rental_income(nz_data)
rental_income = sort_ascending(find_income)

