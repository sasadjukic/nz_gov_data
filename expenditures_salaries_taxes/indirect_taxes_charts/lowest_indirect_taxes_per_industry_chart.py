

import sys 
import matplotlib.pyplot as plt 
import pandas as pd 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\expenditures_salaries_taxes'
sys.path.append(file_path)

from indirect_taxes_2013_2021 import lowest_indirect_taxes

def display_highest_indirect_taxes_per_industry(l_taxes: pd.Series) -> None:
    
    names = l_taxes.index.tolist()
    taxes = l_taxes.values.tolist()

    line_color = '#D83A56'
    color = '#FF7878'
    bg_color = '#F9F3DF'
    text_color = '#8AC4D0'

    fig, ax = plt.subplots()
    plt.bar(names, taxes, color = color)

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color(color)
    ax.spines['left'].set_color(color)

    plt.suptitle(
        'LOWEST TOTAL INDIRECT TAXES PER INDUSTRY 2013-2021',
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
        'TAXES (in millions of NZ Dollars)',
        fontfamily = 'Bahnschrift',
        fontsize = 12.5,
        color = text_color
    )

    plt.xlabel(
        'INDUSTRY NAME',
        fontfamily = 'Bahnschrift',
        fontsize = 12.5,
        color = text_color
    )

    plt.xticks(color=color)
    plt.yticks(color=color)

    for index, value in enumerate(taxes):
        plt.text(
            index,
            value, 
            str(value),
            ha = 'center',
            position = (index, value-35),
            fontweight = 'bold',
            color = bg_color,
            fontsize = 15
        )

    plt.show()

display_highest_indirect_taxes_per_industry(lowest_indirect_taxes)