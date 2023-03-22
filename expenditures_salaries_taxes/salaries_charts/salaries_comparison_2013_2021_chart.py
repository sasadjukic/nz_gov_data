
import sys 
import matplotlib.pyplot as plt 

file_path = r'C:\Users\sasad\Desktop\github\nz_gov_data\expenditures_salaries_taxes'
sys.path.append(file_path)

from salaries_comparison_2013_2021 import sorted_salaries

def display_salaries_comparison(shi: list[tuple]) -> None:

    industry = [name[0] for name in shi]
    wages_2013 = [wage[1][1] for wage in shi]
    wages_2021 = [wage[1][0] for wage in shi]
    shorten_names = [
        'Order and Safety',
        'Mining',
        'Electricity, Gas, Water',
        'Education and Training',
        'Rental, Hiring, Real Estate',
        'Media and Telecommunications',
        'Arts, Recreation',
        'Agriculture',
        'Transport, Postal, Warehousing',
        'Financial, Insurance Services',
        'Wholesale Trade',
        'Healthcare',
        'Construction',
        'Retail Trade, Accommodation',
        'Manufacturing',
        'Professional, Scientific, Technical'
    ]

    industry[:] = [x for x in shorten_names]

    line_color = '#D83A56'
    bg_color = '#F9F3DF'
    text_color = '#8AC4D0'
    colors = ['#FF7878', '#28527A']

    fig, ax = plt.subplots()

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.barh(
        industry, 
        wages_2013,
        color = colors[0],
        label = '2013'
    )

    ax.barh(
        industry, 
        wages_2021,
        label = '2021',
        color = colors[1],
        left = wages_2013
    )

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    ax.set_xlabel(
        'SALARIES (in millions of NZ Dollars)',
        fontsize = 12.5,
        fontfamily = 'Bahnschrift',
        color = text_color
        )

    plt.suptitle(
        'NEW ZEALAND INDUSTRIES - TOTAL SALARIES COMPARISON (2013,2021)',
        fontsize = 18,
        fontfamily = 'Bahnschrift',
        color = text_color
    )

    plt.title(
        '*source https://www.data.govt.nz/', 
        color = text_color, 
        fontfamily = 'Bahnschrift'
    )

    plt.yticks(color = colors[1])
    plt.tick_params(
        bottom = False,
        labelbottom = False,
        left = False
    )

    for value in ax.patches[2:16]:
        ax.text(
            value.get_x() + value.get_width() / 2,
            value.get_height() + value.get_y() - 0.50,
            value.get_width(),
            ha = 'center',
            color = bg_color,
            fontweight = 'bold',
            fontsize = 12
        )

    for value in ax.patches[18:]:
        ax.text(
            value.get_x() + value.get_width() / 2,
            value.get_height() + value.get_y() - 0.50,
            value.get_width(),
            ha = 'center',
            color = bg_color,
            fontweight = 'bold',
            fontsize = 12
        )

    plt.legend(framealpha=0, facecolor=bg_color)
    plt.show()

display_salaries_comparison(sorted_salaries)


