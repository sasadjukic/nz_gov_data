
import sys 
import pandas as pd 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(file_path)

from data import export_clean_data, find_major_industries

nz_data = export_clean_data()
major_industries = find_major_industries()
ls_code = nz_data[nz_data['variable_code'] == 'H41']

def find_major_industries_ls(ls: pd.DataFrame, industries: set) -> pd.DataFrame:
    
    mi_ls = ls[ls['industry_code'].isin(industries)]
    return mi_ls

def get_highest_liability_structure_of_2021(ls_2021: pd.DataFrame) -> pd.DataFrame:
    
    highest_ls = ls_2021[['industry_name','value']].nlargest(n=5, columns='value')
    return highest_ls

def get_lowest_liability_structure_of_2021(ls_2021: pd.DataFrame) -> pd.DataFrame:
    
    lowest_ls = ls_2021[['industry_name', 'value']].nsmallest(n=5, columns='value')
    return lowest_ls

m_ls = find_major_industries_ls(ls_code, major_industries)
highest_ls_2021 = get_highest_liability_structure_of_2021(m_ls[m_ls['year'] == 2021])
lowest_ls_2021 = get_lowest_liability_structure_of_2021(m_ls[m_ls['year'] == 2021])
