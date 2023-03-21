
import sys 
import matplotlib.pyplot as plt
import pandas as pd 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\expenditures_salaries_taxes'
sys.path.append(file_path)

from indirect_taxes_2013_2021 import highest_indirect_taxes, total_indirect_taxes

def display_manufacturing_share_of_indirect_taxes(hit: pd.Series, tit: int) -> None:

    manufacturing = hit.values.tolist()[0]
    rest = tit - manufacturing

    labels = ['Manufacturing', 'Rest']
    colors = ['#FF7878', '#28527A']
    bg_color = '#F9F3DF'
    text_color = '#8AC4D0'

    fig = plt.subplots()

    patches, texts, autotexts = plt.pie(
        [manufacturing, rest],
        labels = labels,
        colors = colors,
        autopct = '%.2f %%',
        startangle = 45,
        pctdistance = 0.85
    )

    center_circle = plt.Circle((0, 0), 0.70, fc=bg_color)
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)

    texts[0].fontfamily = 'Bahnschrift'
    texts[0].set_color(colors[0])
    texts[1].fontfamily = 'Bahnschrift'
    texts[1].set_color(colors[1])

    for autotext in autotexts:
        autotext.set_color(bg_color)

    fig.set_facecolor(bg_color)

    plt.suptitle(
        'MANUFACTURING SHARE OF NEW ZEALAND INDIRECT TAXES 2013-2021',
        fontsize = 18,
        fontfamily = 'Bahnschrift',
        color = text_color
    ) 

    plt.title(
        '*source https://www.data.govt.nz/', 
        color = text_color, 
        fontfamily = 'Bahnschrift'
    )

    plt.show()

display_manufacturing_share_of_indirect_taxes(highest_indirect_taxes, total_indirect_taxes)
