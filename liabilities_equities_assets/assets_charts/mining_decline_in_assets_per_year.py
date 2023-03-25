
import sys 
import matplotlib.pyplot as plt 
import pandas as pd

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\liabilities_equities_assets'
sys.path.append(file_path)

from total_assets import mining_decline

def display_decline_of_mining_assets(m_decline: pd.DataFrame) -> None:

    m_values = m_decline['value'].tolist()
    m_years = m_decline['year'].tolist()

    m_values.reverse()
    m_years.reverse()

    line_color = '#D83A56'
    color = '#0E185F'
    bg_color = '#C9EEFF'
    text_color = '#FF5677'

    fig, ax = plt.subplots()

    plt.plot(
        m_years, 
        m_values,
        marker = 'o',
        linestyle = 'solid',
        color = color
    )

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(color)
    ax.spines['bottom'].set_color(color)

    plt.suptitle(
        'DECREASE IN NEW ZEALAND MINING ASSETS 2013-2021',
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
        'YEAR',
        fontfamily = 'Bahnschrift',
        fontsize = 12.5,
        color = text_color
    )

    plt.xticks(color=color)
    plt.yticks(color=color)

    for index, value in enumerate(m_values[:5]):
        plt.text(
            index,
            value, 
            str(value),
            position = (index+2012.73, value+800),
            fontweight = 'bold',
            color = text_color,
            fontsize = 10
        )

    for index, value in enumerate(m_values[5:]):
        plt.text(
            index,
            value, 
            str(value),
            position = (index+2018, value+800),
            fontweight = 'bold',
            color = text_color,
            fontsize = 10
        )

    plt.show()

display_decline_of_mining_assets(mining_decline)