
import sys 
import matplotlib.pyplot as plt 
import pandas as pd 

f_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\expenditures_salaries_taxes'
sys.path.append(f_path)

from construction_expenditure_growth_by_year import const_yearly_exp

def display_yearly_construction_expenditure_growth(c_expenditures: pd.DataFrame) -> None:

    year = c_expenditures['year'].tolist()
    exp = c_expenditures['value'].tolist()

    line_color = '#D83A56'
    color = '#FF7878'
    bg_color = '#F9F3DF'
    text_color = '#8AC4D0'
    n_color = '#28527A'

    fig, ax = plt.subplots()

    plt.plot(
        year, 
        exp,
        marker = 'o',
        linestyle = 'solid',
        color = line_color
    )

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(color)
    ax.spines['bottom'].set_color(color)

    plt.suptitle(
        'INCREASE IN NEW ZEALAND CONSTRUCTION EXPENDITURES 2013-2021',
        fontfamily = 'Bahnschrift',
        fontsize = 18,
        color = text_color
    )

    plt.title(
        '*source https://www.data.govt.nz/',
        fontfamily = 'Bahnschrift',
        color = text_color
    )

    plt.ylabel(
        'EXPENDITURES (in millions of NZ Dollars)',
        fontfamily = 'Bahnschrift',
        fontsize = 12.5,
        color = text_color
    )

    plt.xlabel(
        'YEAR',
        fontfamily = 'Bahnschrift',
        fontsize = 12.5,
        color = text_color
    )

    plt.xticks(color=color)
    plt.yticks(color=color)

    for index, value in enumerate(sorted(exp)):
        plt.text(
            index,
            value, 
            str(value),
            position = (index+2012.73, value+800),
            fontweight = 'bold',
            color = n_color,
            fontsize = 10
        )

    plt.show()

display_yearly_construction_expenditure_growth(const_yearly_exp)