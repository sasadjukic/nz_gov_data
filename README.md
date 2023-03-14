
*THIS REPO WILL RECEIVE FURTHER UPDATES!

<strong>ABOUT</strong><br>
<br>

Analyzing New Zealand government data with Python, Pandas and MatplotLib. The data covers a nine year period from 2013-2021. At the moment, analysis includes government subsidies but will grow as time goes by. The code is divided into packages to make navigation easier. 

The data sheet picked up from https://www.data.govt.nz/

Due to the size of this project, the analysis covers trends in major industries. This means I did not explore trends of rental, hiring and real estate separately but as part of what NZ government labeled as 'Rental, Hiring and Real Estate Services' (a major industry branch). To be fair to this datasheet, you can do that if you want to focus on something in particular.

In addition to Matplotlib, I added a few touches to my charts in Photoshop to make them more interesting. Granted,
a few of these details may have been added with Matplotlib but I have felt that the PS had given me more tools to achieve the results I was after. 

<strong>HOW TO NAVIGATE THIS REPO?</strong><br>

In short, there are a lot of packages, modules, and imports<br>
<br>
There's a main data package named 'gov_data' and all other packages import from module 'data.py' that is inside of that package.<br>
<br> 
The other major packages are named after the subject they explore (for ex. 'government_subsidies', 'income') and contain modules that deal with and make charts only for that type of data. Inside of the major packages there's the chart subpackage that imports from main modules to create charts.

<strong>GOVERNMENT SUBSIDIES</strong><br>

Lots of interesting findings in this section that contains 6 charts dissecting New Zealand government subsidies to the major industries. Healthcare subsidies are dominating but declined in the last few years, while construction and retail subsidies have skyrocketed. Construction subsidies have grown 854 times in nine years that this data covers. Retail have managed a whopping 229 times increase and cracked the top 5 recipients of the subsidies. 

Included is a sample unittest module that test for functions in gov_subsidies_2013_2021.py module. Similar functions can be found in modules across the subsidies package so I didn't post them. 

<strong>INCOME</strong><br>

Construction and Rental/Real Estate recorded highest growth in income over this nine year period, and that growth is recorded in separate charts. In addition, this section features industries that recorded highest total income as well as highest average income per employee. IMO, there aren't many surprises there as well as in industries that recorded the lowest average income per employee. To sum it up; work in finances not in arts.

<strong>NOTES</strong><br>
<br>
All charts are in the assets folder

<strong>SCREENSHOTS</strong>
<img src="./assets/gov_subsidies_charts/healthcare_share_of_subsidies_2013_2021.png" />
<img src="./assets/income_charts/construction_income_by_year.png" />



