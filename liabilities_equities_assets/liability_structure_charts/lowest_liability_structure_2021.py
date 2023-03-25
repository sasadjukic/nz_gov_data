

import sys 
import pandas as pd 
import matplotlib.pyplot as plt 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\liabilities_equities_assets'
sys.path.append(file_path)

from liability_structure import lowest_ls_2021

def display_highest_ls_of_2021(lls_2021: pd.DataFrame) -> None:

    industry = lls_2021['industry_name'].tolist()
    ls = lls_2021['value'].tolist()
    shorten_names = [
        'Financial and Insurance Services',
        'Mining',
        'Professional, Scientific Services',
        'Construction',
        'Retail Trade and Accommodation'
    ]

    industry[:] = [x for x in shorten_names]

    num_color = '#FFFFFF'
    color = '#0E185F'
    bg_color = '#C9EEFF'
    text_color = '#FF5677'

    fig, ax = plt.subplots()
    plt.barh(industry, ls, color=color)

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(color)
    ax.spines['bottom'].set_color(color)

    plt.suptitle(
        'NEW ZEALAND - LOWEST LIABILITY STRUCTURE PER INDUSTRY 2021',
        fontfamily = 'Bahnschrift',
        fontsize = 18,
        color = text_color
    )

    plt.title(
        '*source https://www.data.govt.nz/',
        fontfamily = 'Bahnschrift',
        color = text_color
    )

    plt.xlabel(
        'LIABILITY STRUCTURE (in percentage)',
        fontfamily = 'Bahnschrift',
        fontsize = 12.5,
        color = text_color
    )

    plt.xticks(color=text_color)
    plt.yticks(color=color)

    for index, value in enumerate(ls):
        plt.text(
            value,
            index, 
            f'{str(value)}%',
            ha = 'center',
            position = (value-1.5, index-0.05),
            fontweight = 'bold',
            color = num_color,
            fontsize = 15
        )

    plt.show() 

display_highest_ls_of_2021(lowest_ls_2021)