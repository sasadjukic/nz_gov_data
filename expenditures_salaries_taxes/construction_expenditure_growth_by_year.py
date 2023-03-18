
import sys 
import pandas as pd 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\gov_data'
sys.path.append(file_path)

from data import export_clean_data

nz_data = export_clean_data()

def find_construction_cost_per_year(data: pd.DataFrame) -> pd.DataFrame:

    construction = data[data['industry_name'] == 'Construction']
    const_expenditure = construction[construction['variable_code'] == 'H08']
    yearly_c_exp = const_expenditure[['year', 'value']]

    return yearly_c_exp

const_yearly_exp = find_construction_cost_per_year(nz_data)