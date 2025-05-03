# Tests for Timer.py
import unittest
import time
from Timer import format_time # Assuming Timer.py is in the same directory or accessible in PYTHONPATH

class TestTimerFunctions(unittest.TestCase):

    def test_format_time_zero(self):
        """Test formatting zero seconds."""
        self.assertEqual(format_time(0), "00:00:00")

    def test_format_time_seconds(self):
        """Test formatting only seconds."""
        self.assertEqual(format_time(30), "00:00:30")

    def test_format_time_minutes_seconds(self):
        """Test formatting minutes and seconds."""
        self.assertEqual(format_time(150), "00:02:30") # 2 minutes, 30 seconds

    def test_format_time_hours_minutes_seconds(self):
        """Test formatting hours, minutes, and seconds."""
        self.assertEqual(format_time(3725), "01:02:05") # 1 hour, 2 minutes, 5 seconds

    def test_format_time_large(self):
        """Test formatting a large number of seconds (more than 24 hours)."""
        # time.strftime with %H wraps around after 23 hours
        # Let's test a value within 24 hours first
        self.assertEqual(format_time(86399), "23:59:59") # 23 hours, 59 minutes, 59 seconds
        # Testing a value slightly over 24 hours to see the wrap-around behavior
        self.assertEqual(format_time(86401), "00:00:01") # Should wrap around to 1 second past midnight


if __name__ == '__main__':
    unittest.main()
