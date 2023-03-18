
import sys
import matplotlib.pyplot as plt
import pandas as pd 

f_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\expenditures_salaries_taxes'
sys.path.append(f_path)

from expenditures_2013_2021 import top_expenditures

def display_top_expenditures_by_industry(i_expenditures: pd.Series) -> None:

    names = i_expenditures.index.tolist()
    expenditures = i_expenditures.values.tolist()

    bar_color = '#D83A56'
    color = '#FF7878'
    bg_color = '#F9F3DF'
    text_color = '#8AC4D0'

    fig, ax = plt.subplots()
    plt.bar(names, expenditures, color=color)

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(color)
    ax.spines['bottom'].set_color(color)

    plt.suptitle(
        'NEW ZEALAND HIGHEST EXPENDITURES PER INDUSTRY 2013-2021',
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
        'TOTAL EXPENDITURES (in millions of NZ Dollars)',
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

    for index, value in enumerate(expenditures):
        plt.text(
            index,
            value,
            str(value),
            ha = 'center',
            position = (index, value-45_000),
            color = bg_color,
            fontweight = 'bold',
            fontsize = 15
        )

    plt.show()

display_top_expenditures_by_industry(top_expenditures)