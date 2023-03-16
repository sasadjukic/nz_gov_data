
import sys 
import pandas as pd
import matplotlib.pyplot as plt 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\income'
sys.path.append(file_path)

from income_2013_2021 import highest_income

def display_highest_income(h_income: pd.Series) -> None:

    industry = h_income.index.tolist()
    income = h_income.values.tolist()

    color = '#2E4F4F'
    bg_color = '#EEEEEE'
    grey = '#B2B1B9'

    fig, ax = plt.subplots()
    plt.bar(industry, income, color=color)

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['left'].set_color('lightgrey')

    plt.suptitle(
        'HIGHEST TOTAL INCOME BY INDUSTRY 2013-2021',
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
        'INCOME (in millions of NZ Dollars)',
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
    plt.ylim(250_000, 1_000_000)

    for index, value in enumerate(income):
        plt.text(
            index,
            value,
            str(value),
            ha = 'center',
            position = (index, value-35_000),
            color = bg_color,
            fontweight = 'bold',
            fontsize = 15
        )

    plt.show()
    
display_highest_income(highest_income)