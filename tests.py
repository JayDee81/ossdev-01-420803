import unittest
import importlib
from prime import eratosthenes


class TestEratosthenesSieve(unittest.TestCase):
    def test_basic(self):
        arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
               103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
        self.assertEqual(eratosthenes(0, 200), arr)

    def test_negative(self):
        with self.assertRaises(Exception):
            eratosthenes(-20, -5)
        with self.assertRaises(Exception):
            eratosthenes(-5, 5)
        with self.assertRaises(Exception):
            eratosthenes(5, -5)

if __name__ == '__main__':
    unittest.main()
