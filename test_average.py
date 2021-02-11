import unittest
import average


class TestAverage(unittest.TestCase):
    def test_average(self):
        result = average.avg(4,4,6,6)
        self.assertEqual(result, 5)

    def test_average1(self):
        result = average.avg(1,1,1,1)
        self.assertEqual(result, 1)

    def test_average2(self):
        result = average.avg(.5,1.5,2.5,3.5)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
