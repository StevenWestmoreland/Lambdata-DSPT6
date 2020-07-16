import unittest
import pandas as pd
from my_lambdata.ds_utilities import enlarge, My_Data_Splitter

class TestDsUtilities(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(3), 300)

    def test_date_divider(self):
        raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
                    'age': [20, 19, 22, 21],
                    'favorite_color': ['blue', 'red', 'yellow', "green"],
                    'grade': [88, 92, 95, 70],
                    'birth_date': ['01-1996', '08-05-1997', '04-28-1996', '12-16-1995']}
        df = pd.DataFrame(raw_data, index = ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'])
        date_col = 'birth_date'

        current_shape = df.shape[1]
        expected_shape = current_shape + 3

        # Create My_Data_Splitter object
        splitter = My_Data_Splitter(df, features=['age', 'favorite_color', 'birth_date'], target='grade')
        converted_df = splitter.date_divider(date_col)

        self.assertEqual(expected_shape, converted_df.shape[1])


if __name__ == '__main__':
    unittest.main()