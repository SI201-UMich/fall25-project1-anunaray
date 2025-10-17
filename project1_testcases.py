import unittest
from project1_code_anunaray import avg_calculator, largest_penguins_percent, get_island_penguins

class TestPenguinStats(unittest.TestCase):

    '''AVG CALCULATOR TEST CASES'''

    def test_avg_basic(self):
        # test if the output is the actual average
        data = [
            {"island": "Dream", "flipper_length": 180.0, "body_mass": 3700.0,
             "bill_length": 39.1, "bill_depth": 18.7, "sex": "MALE", "year": 2008},
            {"island": "Dream", "flipper_length": 200.0, "body_mass": 3900.0,
             "bill_length": 40.3, "bill_depth": 18.5, "sex": "FEMALE", "year": 2008},
        ]
        result = avg_calculator("Adelie", "Dream", "flipper_length", data)
        self.assertEqual(result, 190.0)

    def test_avg_different_attribute(self):
        # test case for a different attribute other than flipper_length
        data = [
            {"island": "Dream", "flipper_length": 180.0, "body_mass": 3700.0,
             "bill_length": 39.1, "bill_depth": 18.7, "sex": "MALE", "year": 2008},
            {"island": "Dream", "flipper_length": 200.0, "body_mass": 3900.0,
             "bill_length": 40.3, "bill_depth": 18.5, "sex": "FEMALE", "year": 2008},
        ]
        result = avg_calculator("Adelie", "Dream", "body_mass", data)
        self.assertEqual(result, 3800.0)


    def test_avg_island_empty(self):
        # test case for when there are no penguins of the specified type on the island
        data = []  # no penguins
        result = avg_calculator("Adelie", "Dream", "flipper_length", data)
        self.assertIsNone(result)

    def test_avg_missing_values(self):
        # test case for when some penguins have missing values for the specified attribute
        # while this is not really the case in this dataset, it is good to test for robustness
        data = [
            {"island": "Dream", "flipper_length": 180.0, "body_mass": 3700.0,
             "bill_length": None, "bill_depth": 18.7, "sex": "MALE", "year": 2008},
            {"island": "Dream", "flipper_length": None, "body_mass": 4000.0,
             "bill_length": 40.0, "bill_depth": 18.5, "sex": "FEMALE", "year": 2008},
            {"island": "Dream", "flipper_length": 190.0, "body_mass": 3800.0,
             "bill_length": 39.5, "bill_depth": None, "sex": "MALE", "year": 2009},
        ]
        result = avg_calculator("Adelie", "Dream", "bill_length", data)
        self.assertEqual(result, 39.75) 

    ''''LARGEST PENGUINS PERCENT TEST CASES'''

    def test_largest_percent_basic(self):
        # basic test case for when there are some penguins larger than the threshold
        data = [
            {"island": "Dream", "bill_length": 38.9, "bill_depth": 18.8,
             "flipper_length": 180.0, "body_mass": 3700.0, "sex": "MALE", "year": 2008},
            {"island": "Dream", "bill_length": 39.2, "bill_depth": 18.1,
             "flipper_length": 200.0, "body_mass": 3900.0, "sex": "FEMALE", "year": 2008},
            {"island": "Dream", "bill_length": 37.8, "bill_depth": 17.6,
             "flipper_length": 190.0, "body_mass": 3800.0, "sex": "MALE", "year": 2009},
            {"island": "Dream", "bill_length": 40.0, "bill_depth": 18.3,
             "flipper_length": 205.0, "body_mass": 4000.0, "sex": "FEMALE", "year": 2009},
        ]
        result = largest_penguins_percent("Adelie", "Dream", data)
        self.assertEqual(result, 50.0)

    def test_percent_island_empty(self):
        # test case for when there are no penguins of the specified type on the island
        data = []  # no penguins
        result = largest_penguins_percent("Adelie", "Dream", data)
        self.assertEqual(result, None)

    def test_percent_missing_values(self):
        # test case for when some penguins have missing values for body_mass or
        data = [
            {"island": "Biscoe", "bill_length": 45.1, "bill_depth": 14.8,
             "flipper_length": 210.0, "body_mass": 5000.0, "sex": "MALE", "year": 2007},
            {"island": "Biscoe", "bill_length": 44.0, "bill_depth": 15.0,
             "flipper_length": None, "body_mass": 5900.0, "sex": "FEMALE", "year": 2008},
            {"island": "Biscoe", "bill_length": 46.2, "bill_depth": 15.5,
             "flipper_length": 220.0, "body_mass": None, "sex": "MALE", "year": 2008},
            {"island": "Biscoe", "bill_length": 47.0, "bill_depth": 14.9,
             "flipper_length": 230.0, "body_mass": 5200.0, "sex": "FEMALE", "year": 2009},
        ]
        result = largest_penguins_percent("Gentoo", "Biscoe", data)
        self.assertEqual(result, 25.0)

    def test_percent_all_equal(self):
        # test case where all penguins have the same measurements (none larger than average)
        data = [
            {"island": "Dream", "bill_length": 39.0, "bill_depth": 18.7,
             "flipper_length": 200.0, "body_mass": 4000.0, "sex": "MALE", "year": 2007},
            {"island": "Dream", "bill_length": 39.0, "bill_depth": 18.7,
             "flipper_length": 200.0, "body_mass": 4000.0, "sex": "FEMALE", "year": 2008},
            {"island": "Dream", "bill_length": 39.0, "bill_depth": 18.7,
            "flipper_length": 200.0, "body_mass": 4000.0, "sex": "MALE", "year": 2009},
                ]
        result = largest_penguins_percent("Adelie", "Dream", data)
        self.assertEqual(result, 0.0)    

if __name__ == "__main__":
    unittest.main()