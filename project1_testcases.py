class TestPenguinStats(unittest.TestCase):
    
    def setUp(self):
        """Create small fake penguin data for testing."""
        self.sample_data = [
            {"island": "Biscoe", "flipper_length": 190.0, "body_mass": 3800.0},
            {"island": "Biscoe", "flipper_length": 200.0, "body_mass": 4000.0},
            {"island": "Biscoe", "flipper_length": 210.0, "body_mass": 4200.0},
            {"island": "Biscoe", "flipper_length": None, "body_mass": 3900.0},
        ]
        self.empty_data = []  # represents case where no penguins exist
        self.missing_data = [
            {"island": "Dream", "flipper_length": None, "body_mass": None},
            {"island": "Dream", "flipper_length": None, "body_mass": None},
        ]

    def test_avg_calculator_general_flipper_length(self):
        """General: Calculates average flipper length correctly."""
        data = [
            {"flipper_length": 190, "body_mass": 3000},
            {"flipper_length": 200, "body_mass": 3200},
            {"flipper_length": 210, "body_mass": 3100}
        ]
        result = avg_calculator("Adelie", "Biscoe", "flipper_length", data)
        self.assertEqual(result, 200.0)

    def test_avg_calculator_general_body_mass(self):
        """General: Calculates average body mass correctly."""
        data = [
            {"flipper_length": 190, "body_mass": 3000},
            {"flipper_length": 200, "body_mass": 3200},
            {"flipper_length": 210, "body_mass": 3100}
        ]
        result = avg_calculator("Adelie", "Biscoe", "body_mass", data)
        self.assertEqual(result, 3100.0)

    def test_avg_calculator_edge_some_missing(self):
        """Edge: Ignores None values and still averages correctly."""
        data = [
            {"flipper_length": None, "body_mass": 3000},
            {"flipper_length": 200, "body_mass": None},
            {"flipper_length": 210, "body_mass": 3100}
        ]
        result = avg_calculator("Adelie", "Biscoe", "flipper_length", data)
        self.assertEqual(result, 205.0)  # average of 200 and 210
