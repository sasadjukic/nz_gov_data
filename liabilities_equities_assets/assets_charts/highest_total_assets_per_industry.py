
import sys 
import matplotlib.pyplot as plt
import pandas as pd  

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\liabilities_equities_assets'
sys.path.append(file_path)

from total_assets import highest_api 

def display_highest_total_assets(hpi: pd.Series) -> None:
    
    industry = hpi.index.tolist()
    assets = hpi.values.tolist()

    shorten_names = [
        'Financial and Insurance',
        'Rental, Hiring, Real Estate',
        'Agriculture, Forestry, Fishing',
        'Manufacturing',
        'Professional, Scientific, Technical'
    ]
    industry[:] = [x for x in shorten_names]

    line_color = '#D83A56'
    color = '#0E185F'
    bg_color = '#C9EEFF'
    text_color = '#FF5677'

    fig, ax = plt.subplots()
    plt.bar(industry, assets, color = color)

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color(color)
    ax.spines['left'].set_color(color)

    plt.suptitle(
        'NEW ZEALAND HIGHEST TOTAL ASSETS PER INDUSTRY 2013-2021',
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
        'ASSETS (in millions of NZ Dollars)',
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

    for index, value in enumerate(assets):
        plt.text(
            index,
            value, 
            str(value),
            ha = 'center',
            position = (index, value-500_000),
            fontweight = 'bold',
            color = 'w',
            fontsize = 15
        )

    plt.show()

display_highest_total_assets(highest_api)

