import sys 
import pandas as pd 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(file_path)

from data import export_clean_data, find_major_industries

nz_data = export_clean_data()
major_industries = find_major_industries()

industry_dict = {
    'Agriculture, Forestry and Fishing' : [],
    'Mining' : [],
    'Manufacturing' : [],
    'Electricity, Gas, Water and Waste Services' : [],
    'Construction' : [],
    'Wholesale Trade' : [],
    'Retail Trade and Accommodation' : [],
    'Transport, Postal and Warehousing' : [],
    'Information Media and Telecommunications' : [],
    'Financial and Insurance Services' : [],
    'Rental, Hiring and Real Estate Services' : [],
    'Professional, Scientific, Technical, Administrative and Support Services' : [],
    'Public Order, Safety and Regulatory Services' : [],
    'Education and Training' : [],
    'Health Care and Social Assistance' : [],
    'Arts, Recreation and Other Services' : []
}

def get_salaries(data: pd.DataFrame, industries: set) -> pd.DataFrame:

    salaries = nz_data[nz_data['variable_code'] == 'H12']
    all_salaries = salaries[salaries['industry_code'].isin(industries)]
    return all_salaries

def parse_salaries(a_salaries: pd.DataFrame, i_dict: dict[str:list]) -> dict[str:list]:

    edge_years = a_salaries[(a_salaries['year'] == 2013) | (a_salaries['year'] == 2021)]

    for i in edge_years.index:
        industry = edge_years.loc[i, 'industry_name']
        wage = edge_years.loc[i, 'value']
        i_dict[industry].append(wage)
        
    return i_dict

def sort_salaries(h_increase: dict[str:list]) -> list[tuple]:

    return sorted(h_increase.items(), key = lambda x: sum(x[1]))

all_salaries = get_salaries(nz_data, major_industries)
wages = parse_salaries(all_salaries, industry_dict)
sorted_salaries = sort_salaries(wages)