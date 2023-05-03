import requests
import unittest

class TestCalculator(unittest.TestCase):
  def test_acceuil(self):
    self.assertEqual(requests.get('http://localhost:4999').status_code, 200)
