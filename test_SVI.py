import unittest
from main2 import validate_symbol, validate_chart_type, validate_time_series, validate_date

class TestStockVisualizerInputs(unittest.TestCase):

    def test_validate_symbol(self):
        self.assertTrue(validate_symbol("AAPL"))
        self.assertTrue(validate_symbol("GOOG"))

        self.assertFalse(validate_symbol("apple"))  
        self.assertFalse(validate_symbol("12345"))  
        self.assertFalse(validate_symbol("BLACKROCK"))  


    def test_validate_chart_type(self):
        # Valid chart types
        self.assertTrue(validate_chart_type('1'))
        self.assertTrue(validate_chart_type('2'))

        # Invalid chart types
        self.assertFalse(validate_chart_type('3'))
        self.assertFalse(validate_chart_type('a'))
    
    def test_validate_time_series(self):
        # Valid time series
        for i in ['1', '2', '3', '4']:
            self.assertTrue(validate_time_series(i))

        # Invalid time series
        self.assertFalse(validate_time_series('5'))
        self.assertFalse(validate_time_series('0'))
        self.assertFalse(validate_time_series('a'))

    def test_validate_start_date(self):
        # Valid dates
        self.assertTrue(validate_date('2020-01-01'))
        self.assertTrue(validate_date('2021-12-31'))

        # Invalid dates
        self.assertFalse(validate_date('01-01-2020'))
        self.assertFalse(validate_date('2020/01/01'))
        self.assertFalse(validate_date('20200101'))
    

    def test_validate_end_date(self):
        self.assertTrue(validate_date('2020-01-01'))
        self.assertTrue(validate_date('2021-12-31'))

        # Invalid dates
        self.assertFalse(validate_date('01-01-2020'))
        self.assertFalse(validate_date('2020/01/01'))
        self.assertFalse(validate_date('20200101'))

        



if __name__ == '__main__':
    unittest.main()

