import unittest
import os
import sys

# Add src to path so we can import our modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.validate_data import run_integrity_check

class TestDataPipeline(unittest.TestCase):
    
    def test_file_existence_check(self):
        """Test if the validator correctly handles a missing file."""
        result = run_integrity_check('data/raw/non_existent_file.csv')
        self.assertFalse(result)

    def test_processed_data_path(self):
        """Verify the processed data directory exists."""
        self.assertTrue(os.path.exists('data/processed/'))

if __name__ == '__main__':
    unittest.main()