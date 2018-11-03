import unittest

from question_b import check_strings


class TestStringComparison(unittest.TestCase):

    def test_equal_strings(self, nb_runs=10000):

        for item in range(nb_runs):
            str1 = str(item) + '.1'
            str2 = str(item) + '.1'

            result = check_strings(str1, str2)
            self.assertEqual(result, str1 + ' == ' + str2)

    def test_greater_strings(self, nb_runs=10000):

        for item in range(nb_runs):
            str1 = str(item) + '.2'
            str2 = str(item) + '.1'

            result = check_strings(str1, str2)
            self.assertEqual(result, str1 + ' > ' + str2)

    def test_smaller_strings(self, nb_runs=10000):
    
        for item in range(nb_runs):
            str1 = str(item) + '.1'
            str2 = str(item) + '.2'

            result = check_strings(str1, str2)
            self.assertEqual(result, str1 + ' < ' + str2)

    def test_input_error_strings(self, nb_runs=10000):
    
        for item in range(nb_runs):
            str1 = str(item) + '.a2'
            str2 = str(item) + '.1'

            result = check_strings(str1, str2)
            self.assertEqual(result, 'Invalid Input. Insert string with numbers')

if __name__ == '__main__':
    unittest.main()
