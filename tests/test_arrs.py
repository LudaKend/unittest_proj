import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
#        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 3)
#ошибка в тесте должно быть 2, а не 3
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
#еще новенький:
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")
#        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
#еще новенький:
        self.assertEqual(arrs.my_slice([1, 2, 3], -1, -1), [])
        self.assertEqual(arrs.my_slice([]), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -5), [1, 2, 3, 4])
