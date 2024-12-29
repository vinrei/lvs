from datetime import datetime
import unittest
from unittest.mock import patch

from storage import EventStorage

class TestStringMethods(unittest.TestCase):

    @patch('storage.datetime')
    def test_saving_events(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 12, 25, 10, 30, 0)
        event_storage = EventStorage()
        event_storage.save_to_file('event1', 'abc.jpg', 'tests/test_output.json')
        with open('tests/test_output.json', 'r') as f:
            data = f.read()
            with open('tests/benchmark1.json', 'r') as f:
                benchmark = f.read()
                self.assertEqual(data, benchmark)

    @patch('storage.datetime')
    def test_reading_appending_and_saving_happy_path(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 12, 25, 10, 30, 0)
        event_storage = EventStorage()
        event_storage.read_existing_events('tests/benchmark1.json')
        event_storage.save_to_file('event2', 'xyz.jpg', 'tests/test_output2.json')
        with open('tests/test_output2.json', 'r') as f:
            data = f.read()
            with open('tests/benchmark2.json', 'r') as f:
                benchmark = f.read()
                self.assertEqual(data, benchmark)
    
    def test_reading_bad_events_file(self):
        with self.assertRaises(SystemExit):
            event_storage = EventStorage()
            event_storage.read_existing_events('tests/benchmark3.json')

if __name__ == '__main__':
    unittest.main()