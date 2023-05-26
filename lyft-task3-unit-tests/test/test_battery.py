import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestBattery(unittest.TestLoader):
    def test_nubbin_needs_service_true(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        battery = NubbinBattery(last_service_date, current_date)
        result = battery.needs_service()
        self.assertTrue(result)

    def test_nubbin_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = NubbinBattery(last_service_date, current_date)
        result = battery.needs_service()
        self.assertFalse(result)

    def test_spindler_needs_service_true(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        battery = SpindlerBattery(last_service_date, current_date)
        result = battery.needs_service()
        self.assertTrue(result)

    def test_spindler_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = SpindlerBattery(last_service_date, current_date)
        result = battery.needs_service()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()


