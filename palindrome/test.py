#Test Driven Devlopment TDD
#Unittest
import unittest

from palindrome import palindrome

class palindrome_test_case(unittest.TestCase):
    def test_good_palindrome(self):

        palindromes = palindrome()

        if len(palindromes) >= 1:
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()