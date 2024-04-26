import unittest
from unittest.mock import patch, mock_open
import battery_notify

class TestBatteryNotify(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="50")
    def test_read_battery_capacity(self, mock_file):
        self.assertEqual(battery_notify.read_battery_capacity(), 50)

    @patch("builtins.open", new_callable=mock_open, read_data="1")
    def test_read_ac_status(self, mock_file):
        self.assertEqual(battery_notify.read_ac_status(), 1)

    @patch("subprocess.Popen")
    def test_send_notification(self, mock_subprocess):
        battery_notify.send_notification("Test message")
        mock_subprocess.assert_any_call(['notify-send', '--urgency=normal', '--icon=dialog-information', '\'Battery Notification\'', "Test message"])
        mock_subprocess.assert_any_call(['paplay', "/home/stryder/Music/sfx/normal.ogg"])

if __name__ == "__main__":
    unittest.main()