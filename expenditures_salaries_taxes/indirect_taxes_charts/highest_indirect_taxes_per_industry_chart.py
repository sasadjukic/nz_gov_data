
import sys 
import matplotlib.pyplot as plt 
import pandas as pd 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\expenditures_salaries_taxes'
sys.path.append(file_path)

from indirect_taxes_2013_2021 import highest_indirect_taxes

def display_highest_indirect_taxes_per_industry(h_taxes: pd.Series) -> None:
    
    names = h_taxes.index.tolist()
    taxes = h_taxes.values.tolist()
    shorten_names = [
        'Manufacturing',
        'Rental, hiring, real estate',
        'Transport, postal, warehousing',
        'Agriculture, forestry, fishing',
        'Wholesale trade'
    ]
    names[:] = [x for x in shorten_names]

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
        'HIGHEST TOTAL INDIRECT TAXES PER INDUSTRY 2013-2021',
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
            position = (index, value-1800),
            fontweight = 'bold',
            color = bg_color,
            fontsize = 15
        )

    plt.show()

display_highest_indirect_taxes_per_industry(highest_indirect_taxes)