
import sys 
import matplotlib.pyplot as plt 

abs_filepath = r'C:\Users\sasad\Desktop\github\nz_gov_data\government_subsidies'
sys.path.append(abs_filepath)

from gov_subsidies_2013 import (construction_subs_2013, retail_subs_2013,
                                agriculture_subs_2013, manufacturing_subs_2013,
                                wholesale_subs_2013)

from gov_subsidies_2021 import (construction_subs_2021, retail_subs_2021,
                                agriculture_subs_2021, manufacturing_subs_2021,
                                wholesale_subs_2021)

construction = int(round(construction_subs_2021 / construction_subs_2013))*100
retail = int(round(retail_subs_2021 / retail_subs_2013))*100
agriculture = int(round(agriculture_subs_2021 / agriculture_subs_2013))*100
manufacturing = int(round(manufacturing_subs_2021 / manufacturing_subs_2013))*100
wholesale = int(round(wholesale_subs_2021 / wholesale_subs_2013))*100


def display_construction_subsidies() -> None:
    labels = ['Construction', 'Retail', 'Wholesale trade', 'Agriculture', 'Manufacturing']
    values = [construction, retail, wholesale, agriculture, manufacturing]

    color = '#191825'
    bg_color = '#E4FBFF'

    fig, ax = plt.subplots()
    plt.bar(labels, values, color=color)

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['left'].set_color('lightgrey')

    plt.suptitle(
        'HIGHEST INCREASE IN NEW ZEALAND GOVERNMENT SUBSIDIES PER INDUSTRY 2013-2021',
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
        'TOTAL INCREASE (in percentage)',
        fontfamily = 'Bahnschrift',
        fontsize = 15,
        color = 'lightgrey'
    )

    ax.set_xlabel(
        'INDUSTRY NAME',
        fontfamily = 'Bahnschrift',
        fontsize = 15,
        color = 'lightgrey'
    )

    plt.xticks(color=color)
    plt.yticks(color='lightgrey')

    for index, value in enumerate(values):
        plt.text(
            index, 
            value,
            f'{value}%',
            ha = 'center',
            position = (index, value+1000)
        )

    plt.show()

display_construction_subsidies()