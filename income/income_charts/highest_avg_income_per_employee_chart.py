
import sys 
import matplotlib.pyplot as plt 
import pandas as pd  

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\income'
sys.path.append(file_path)

from income_per_employee_count import highest_avg_income_per_employee_count

def display_highest_average_income_per_employee(hai: pd.Series) -> None:

    industry = hai.index.tolist()
    avg_income_per_employee = hai.values.tolist()
    short_names = [
        'Financial and Insurance Services',
        'Mining',
        'Electricity, Gas, Water and Waste',
        'Rental, Hiring and Real Estate',
        'Wholesale Trade'
        ]

    industry[:] = [x for x in short_names]
    
    color = '#2E4F4F'
    bg_color = '#EEEEEE'
    grey = '#B2B1B9'

    fig, ax = plt.subplots()
    plt.bar(industry, avg_income_per_employee, color=color)

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['left'].set_color('lightgrey')

    plt.suptitle(
        'HIGHEST AVERAGE INCOME PER EMPLOYEE COUNT 2013-2021',
        fontfamily = 'Bahnschrift',
        fontsize = 18,
        color = grey
    )

    plt.title(
        '*source https://www.data.govt.nz/',
        fontfamily = 'Bahnschrift',
        color = grey
    )

    ax.set_ylabel(
        'AVERAGE INCOME PER EMPLOYEE COUNT(NZ Dollars)',
        fontfamily = 'Bahnschrift',
        color = grey
    )

    ax.set_xlabel(
        'INDUSTRY NAME',
        fontfamily = 'Bahnschrift',
        color = grey
    )

    plt.xticks(color='#2E4F4F')
    plt.yticks(color='lightgrey')

    for index, value in enumerate(avg_income_per_employee):
        plt.text(
            index,
            value,
            str(value),
            ha = 'center',
            position = (index, value-60_000),
            color = bg_color,
            fontweight = 'bold',
            fontsize = 15
        )

    plt.show()

display_highest_average_income_per_employee(highest_avg_income_per_employee_count)