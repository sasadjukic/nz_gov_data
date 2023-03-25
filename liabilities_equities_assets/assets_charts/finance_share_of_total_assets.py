
import sys 
import matplotlib.pyplot as plt 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\liabilities_equities_assets'
sys.path.append(file_path)

from total_assets import financial_assets, total_assets

def display_finance_share_of_total_assets(finance: int, total: int) -> None:

    finance_share = round((finance / total) * 100, 2)
    rest = 100 - finance_share

    labels = ['Finances', 'Rest']
    colors = ['#0E185F', '#FF5677']
    bg_color = '#C9EEFF'
    text_color = '#0E185F'

    fig = plt.subplots()

    patches, texts, autotexts = plt.pie(
        [finance_share, rest],
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
        'FINANCIAL AND INSURANCE SHARE OF NEW ZEALAND TOTAL ASSETS 2013-2021',
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

display_finance_share_of_total_assets(financial_assets, total_assets)