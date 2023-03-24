

import sys 
import matplotlib.pyplot as plt 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\liabilities_equities_assets'
sys.path.append(file_path)

from return_on_equity import sorted_roe

def display_salaries_comparison(roe: list[tuple]) -> None:

    industry = [name[0] for name in roe]
    roe_2013 = [wage[1][1] for wage in roe]
    roe_2021 = [wage[1][0] for wage in roe]
    shorten_names = [
        'Agriculture',
        'Electricity, Gas, Water',
        'Transport, Postal, Warehousing',
        'Financial, Insurance Services',
        'Rental, Hiring, Real Estate',
        'Education and Training',
        'Manufacturing',
        'Information and Telecommunications',
        'Arts, Recreation',
        'Public Order and Safety',
        'Mining',
        'Healthcare',
        'Wholesale Trade',
        'Professional, Scientific, Technical',
        'Retail Trade and Accommodation',
        'Construction'
    ]

    industry[:] = [x for x in shorten_names]

    line_color = '#D83A56'
    bg_color = '#C9EEFF'
    num_color = '#ffffff'
    text_color = '#0E185F'
    colors = ['#0E185F', '#FF5677']

    fig, ax = plt.subplots()

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.barh(
        industry, 
        roe_2013,
        color = colors[0],
        label = '2013'
    )

    ax.barh(
        industry, 
        roe_2021,
        label = '2021',
        color = colors[1],
        left = roe_2013
    )

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    ax.set_xlabel(
        'RETURN ON EQUITY (in percentage)',
        fontsize = 12.5,
        fontfamily = 'Bahnschrift',
        color = text_color
        )

    plt.suptitle(
        'NEW ZEALAND INDUSTRIES - RETURN ON EQUITY COMPARISON (2013,2021)',
        fontsize = 18,
        fontfamily = 'Bahnschrift',
        color = text_color
    )

    plt.title(
        '*source https://www.data.govt.nz/', 
        color = text_color, 
        fontfamily = 'Bahnschrift'
    )

    plt.yticks(color = colors[0])
    plt.tick_params(
        bottom = False,
        labelbottom = False,
        left = False
    )

    for value in ax.patches:
        ax.text(
            value.get_x() + value.get_width() / 2,
            value.get_height() + value.get_y() - 0.50,
            value.get_width(),
            ha = 'center',
            color = num_color,
            fontweight = 'bold',
            fontsize = 12
        )

    plt.legend(framealpha=0, facecolor=bg_color)
    plt.show()

display_salaries_comparison(sorted_roe)


