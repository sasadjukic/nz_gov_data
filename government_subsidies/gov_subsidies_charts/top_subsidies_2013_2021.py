
import sys 
import pandas as pd 
import matplotlib.pyplot as plt

abs_filepath = r'C:\Users\sasad\Desktop\github\nz_gov_data\government_subsidies'
sys.path.append(abs_filepath)

from gov_subsidies_2013_2021 import highest_subsidies

def display_highest_gov_subsidies(h_subs: pd.Series) -> None:

    industries = h_subs.index.tolist()
    subsidies = h_subs.values.tolist()
    industry_labels = [
        'Healthcare', 
        'Education and training', 
        'Transport and warehousing',
        'Administrative services',
        'Retail and accommodation'
        ]
        
    color = '#191825'
    bg_color = '#E4FBFF' 

    industries[:] = [x for x in industry_labels]

    fig, ax = plt.subplots()

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.barh(
        industries,
        subsidies,
        color = color
    )

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['left'].set_color('lightgrey')

    ax.set_ylabel(
        'INDUSTRIES',
        fontname = 'Bahnschrift', 
        fontsize = 15,
        color = 'lightgrey'
    )

    ax.set_xlabel(
        'TOTAL SUBSIDIES (in millions of NZ Dollars)',
        fontname = 'Bahnschrift', 
        fontsize = 15,
        color = 'lightgrey'
    )

    plt.xticks(color = 'lightgrey')
    plt.yticks(color = '#191825')

    plt.suptitle(
        'TOP RECIPIENTS OF NEW ZEALAND GOVERNMENT SUBSIDIES 2013-2021',
        fontname = 'Bahnschrift', 
        fontsize = 18,
        color = 'lightgrey'
    )

    plt.title(
        '*source https://www.data.govt.nz/', 
        fontname = 'Bahnschrift',
        color = 'lightgrey'
    )

    for index, value in enumerate(subsidies):
        plt.text(
            value, 
            index, 
            str(value),
            position = (value + 500, index)
        )

    plt.show()

display_highest_gov_subsidies(highest_subsidies)