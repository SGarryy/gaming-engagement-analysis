import unittest
import os
import sys
import pandas as pd
from pathlib import Path

# Add src to path so we can import our modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.validate_data import run_integrity_check, REQUIRED_COLUMNS

class TestDataPipeline(unittest.TestCase):
    """Unit tests for the gaming engagement analysis pipeline."""
    
    def test_file_existence_check(self):
        """Test if the validator correctly handles a missing file."""
        result = run_integrity_check('data/raw/non_existent_file.csv')
        self.assertFalse(result)

    def test_processed_data_directory_exists(self):
        """Verify the processed data directory exists."""
        self.assertTrue(os.path.exists('data/processed/'))
    
    def test_raw_data_directory_exists(self):
        """Verify the raw data directory exists."""
        self.assertTrue(os.path.exists('data/raw/'))
    
    def test_source_files_exist(self):
        """Verify all required source modules are present."""
        required_files = [
            'src/data_loader.py',
            'src/feature_engineering.py',
            'src/validate_data.py',
            'src/cluster_model.py',
            'src/summary_stats.py',
            'src/visualize_trends.py',
            'src/check_env.py'
        ]
        for file_path in required_files:
            self.assertTrue(os.path.exists(file_path), f"Missing: {file_path}")
    
    def test_reports_directory_exists(self):
        """Verify the reports directory can be created."""
        reports_dir = 'reports'
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)
        self.assertTrue(os.path.exists(reports_dir))
    
    def test_models_directory_can_be_created(self):
        """Verify the models directory can be created for storing pickled models."""
        models_dir = 'models'
        if not os.path.exists(models_dir):
            os.makedirs(models_dir)
        self.assertTrue(os.path.exists(models_dir))
    
    def test_required_columns_defined(self):
        """Verify that required columns are properly defined."""
        self.assertIn('session_duration_hr', REQUIRED_COLUMNS)
        self.assertIn('weekly_frequency', REQUIRED_COLUMNS)
        self.assertIn('milestones_reached', REQUIRED_COLUMNS)

if __name__ == '__main__':
    unittest.main()