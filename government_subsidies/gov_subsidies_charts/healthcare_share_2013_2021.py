
import sys 
from pathlib import Path 
import pandas as pd 
import matplotlib.pyplot as plt 

abs_filepath = r'C:\Users\sasad\Desktop\github\nz_gov_data\government_subsidies'
sys.path.append(abs_filepath)

from gov_subsidies_2013_2021 import total_subsidies, highest_subsidies

def get_healthcare_share_in_total_subsidies(t_s: dict[str:int], h_s: pd.Series) -> float:
    
    healthcare_subsidies = h_s.values[0]
    total_subsidies = t_s['all_industries']

    return round((healthcare_subsidies / total_subsidies)*100, 2)

def display_healthcare_share_of_gov_subs(h_share: float) -> None:

    rest = 100 - h_share
    labels = ['HEALTHCARE', 'REST']
    colors = ['#7868E6', '#191825']

    explode = (0.1, 0)
    fig, ax = plt.subplots()

    #  create a pie chart
    patches, texts, autotexts = ax.pie(
        [h_share, rest],
        labels = labels,
        colors = colors,
        autopct = '%.2f %%',
        startangle = 45,
        pctdistance = 0.85
    )

    # draw a circle to make it a doughnut pie chart
    center_circle = plt.Circle((0, 0), 0.70, fc='#E4FBFF')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)

    # customize pie chart labels
    texts[0].fontfamily = 'Bahnschrift'
    texts[0].set_color('#7868E6')
    texts[1].fontfamily = 'Bahnschrift'
    texts[1].set_color('#191825')

    # change pie chart label color
    for autotext in autotexts:
        autotext.set_color('#FFEA20')

    # set BG color
    fig.set_facecolor('#E4FBFF')

    # create title
    plt.suptitle(
        'HEALTHCARE SHARE OF NEW ZEALAND GOVERNMENT SUBSIDIES 2013-2021',
        fontsize = 18,
        fontfamily = 'Bahnschrift',
        color = 'lightgrey'
    ) 

    # create sub title
    plt.title(
        '*source https://www.data.govt.nz/', 
        color = 'lightgrey', 
        fontfamily = 'Bahnschrift'
    )

    plt.show()

healthcare_share = get_healthcare_share_in_total_subsidies(total_subsidies, highest_subsidies)
display_healthcare_share_of_gov_subs(healthcare_share)