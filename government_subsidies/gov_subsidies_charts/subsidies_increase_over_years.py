
import sys 
import matplotlib.pyplot as plt

abs_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\government_subsidies'
sys.path.append(abs_path)

from gov_subsidies_2013 import total_subs_2013
from gov_subsidies_2014 import total_subs_2014
from gov_subsidies_2015 import total_subs_2015
from gov_subsidies_2016 import total_subs_2016
from gov_subsidies_2017 import total_subs_2017
from gov_subsidies_2018 import total_subs_2018
from gov_subsidies_2019 import total_subs_2019
from gov_subsidies_2020 import total_subs_2020
from gov_subsidies_2021 import total_subs_2021

def display_gov_subsidies() -> None:

    years = [
        2013, 2014, 2015, 2016, 2017, 
        2018, 2019, 2020, 2021
        ]

    subsidies = [
        total_subs_2013, total_subs_2014, total_subs_2015,
        total_subs_2016, total_subs_2017, total_subs_2018,
        total_subs_2019, total_subs_2020, total_subs_2021
        ]

    

    color = '#191825'
    bg_color = '#E4FBFF' 

    fig, ax = plt.subplots()
    plt.plot(years, subsidies, 'k-o')

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['left'].set_color('lightgrey')

    plt.suptitle(
        'INCREASE IN NEW ZEALAND GOVERNMENT SUBSIDIES 2013-2021',
        fontfamily = 'Bahnschrift',
        fontsize = 18,
        color = 'lightgrey'
    )

    plt.title(
        '*source https://www.data.govt.nz/',
        fontfamily = 'Bahnschrift',
        color = 'lightgrey'
    )

    ax.set_ylabel(
        'Subsidies in NZD (in millions)',
        fontfamily = 'Bahnschrift',
        fontsize = 15,
        color = 'lightgrey'
    )

    ax.set_xlabel(
        'Years',
        fontfamily = 'Bahnschrift',
        fontsize = 15,
        color = 'lightgrey'
    )

    plt.xticks(color='lightgrey')
    plt.yticks(color='lightgrey')

    for index, value in enumerate(subsidies):
        plt.text(
            index,
            value,
            str(value),
            ha = 'center',
            position = (index+2012.90, value+350),
            color = '#37306B'
        )

    plt.show()

display_gov_subsidies()
