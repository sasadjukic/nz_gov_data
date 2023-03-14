
import sys 
import matplotlib.pyplot as plt

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\income'
sys.path.append(file_path)

from construction_income_by_year import construction_income

def display_construction_income(c_income: list[tuple]) -> None:
    
    years = [x[0] for x in c_income]
    income = [x[1] for x in c_income]

    color = '#2E4F4F'
    bg_color = '#EEEEEE'
    grey = '#B2B1B9'

    fig, ax = plt.subplots()
    plt.plot(
        years, 
        income, 
        color=color, 
        marker='o', 
        linestyle='solid'
        )

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('lightgrey')
    ax.spines['bottom'].set_color('lightgrey')

    plt.suptitle(
        'CONSTRUCTION INCOME BY YEAR 2013-2021',
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
        'YEARS',
        fontfamily = 'Bahnschrift',
        color = grey
    )

    plt.xticks(color = 'lightgrey')
    plt.yticks(color = 'lightgrey')

    for i, v in enumerate(income):
        plt.text(
            i, 
            v, 
            str(v),
            ha = 'center',
            position = (i+2012.90, v+800)
        )

    plt.show()

display_construction_income(construction_income)
