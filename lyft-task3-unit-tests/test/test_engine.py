import unittest

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestEngine(unittest.TestLoader):
    def test_capulet_needs_service_true(self):
        engine = CapuletEngine(current_mileage=30001, last_service_mileage=0)
        result = engine.capulet_needs_service()
        self.assertTrue(result)
    
    def test_capulet_needs_service_false(self):
        engine = CapuletEngine(current_mileage=30000, last_service_mileage=0)
        result = engine.needs_service()
        self.assertFalse(result)

    def test_sternman_needs_service_true(self):
        engine = SternmanEngine(warning_light_is_on=True)
        result = engine.needs_service()
        self.assertTrue(result)

    def test_sternman_needs_service_false(self):
        engine = SternmanEngine(warning_light_is_on=False)
        result = engine.needs_service()
        self.assertFalse(result)

    def test_willoughbyengine_needs_service_true(self):
        engine = WilloughbyEngine(current_mileage=60001, last_service_mileage=0)
        result = engine.capulet_needs_service()
        self.assertTrue(result)
    
    def test_willoughbyengine_needs_service_false(self):
        engine = WilloughbyEngine(current_mileage=60000, last_service_mileage=0)
        result = engine.needs_service()
        self.assertFalse(result)
    
if __name__ == '__main__':
    unittest.main()
