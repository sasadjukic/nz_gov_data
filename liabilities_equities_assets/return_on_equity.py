
import sys 
import pandas as pd 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(file_path)

from data import export_clean_data, find_major_industries

nz_data = export_clean_data()
major_industries = find_major_industries()
roe_code = nz_data[nz_data['variable_code'] == 'H39']

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

def find_major_industry_roe(roe: pd.DataFrame, industries: set) -> pd.DataFrame:

    mi_roe = roe[roe['industry_code'].isin(industries)]
    return mi_roe 

def parse_industry_roe(roe: pd.DataFrame, industry_d: dict[str:list]) -> dict[str:list]:
    
    edge_years = roe[(roe['year'] == 2013) | (roe['year'] == 2021)]

    for i in edge_years.index:
        industry = edge_years.loc[i, 'industry_name']
        i_roe = edge_years.loc[i, 'value']
        industry_d[industry].append(i_roe)
        
    return industry_d

def sort_roe(h_roe: dict[str:list]) -> list[tuple]:

    return sorted(h_roe.items(), key = lambda x: sum(x[1]))

roe = find_major_industry_roe(roe_code, major_industries)
parsed_roe = parse_industry_roe(roe, industry_dict)
sorted_roe = sort_roe(parsed_roe)