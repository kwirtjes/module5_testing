import unittest
from my_sum import my_sum


class TestMySum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(my_sum([1, 2, 3]), 6)


if __name__ == '__main__':
    unittest.main()
"""
The test passed successfully. It checked that the my_sum
function correctly adds numbers together. The result was 6,
which matched the expected answer. This means the function
is working correctly for this test.
"""