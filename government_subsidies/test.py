
import unittest 
import pandas as pd 
from gov_subsidies_2013_2021 import (
                                    find_government_subsidies_per_industry,
                                    assign_subsidies_to_industries,
                                    find_total_subsidies,
                                    get_highest_industry_subsidies,
                                    get_lowest_industry_subsidies
                                    )

# testing all functions in gov_subsidies_2013_2021 module
class Subsidies_Per_Industry_2013_2021(unittest.TestCase):

    # set up fake data
    def setUp(self):

        self.fake_data = {
            'variable_code' : ['H06', 'H06', 'H06', 'H06', 'H06'],
            'industry_name' : ['Construction', 'Healthcare', 'Retail', 'Wholesale Trade', 'Rental'],
            'industry_code' : ['EE', 'QQ', 'GH', 'RR', 'TF'],
            'value' : [3000, 4000, 5000, 3500, 6000]
        }

        self.df = pd.DataFrame(self.fake_data)
        self.fake_industries = set({'EE', 'QQ', 'GH', 'PP', 'TF','RR'})
        self.fake_dict = {
                            'Construction' : 4000, 
                            'Healthcare' : 5000,
                            'Retail' : 10000,
                            'Security' : 2000,
                            'Education' : 9000
                         }
    
    # test for correct output type
    def test_1_subsidies_per_industry(self):

        self.assertEqual(type(find_government_subsidies_per_industry(self.df, self.fake_industries)), pd.DataFrame)

    # test for correct output type and the output itself
    def test_2_assign_subsidies_to_industries(self):

        self.assertEqual(type(assign_subsidies_to_industries(self.df)), dict)
        self.assertEqual(
                        assign_subsidies_to_industries(self.df), 
                        {
                            'Construction' : 3000,
                            'Healthcare' : 4000,
                            'Retail' : 5000,
                            'Wholesale trade' : 3500,
                            'Rental' : 6000
                        })

    # test for correct output type and the output itself
    def test_3_find_total_subsidies(self):

        self.assertEqual(type(find_total_subsidies(self.df)), dict)
        self.assertEqual(find_total_subsidies(self.df), {'all_industries' : 21500})

    # test for correct output type 
    def test_4_get_highest_industry_subsidies(self):

        self.assertEqual(type(get_highest_industry_subsidies(self.fake_dict)), pd.Series)
    
    # test for correct output type
    def test_5_get_lowest_industry_subsidies(self):

        self.assertEqual(type(get_lowest_industry_subsidies(self.fake_dict)), pd.Series)

if __name__ == '__main__':
    unittest.main()


