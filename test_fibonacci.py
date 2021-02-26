import fibonacci
import unittest
import pytest


print("This is a testing program that will test the functionality of fibonacci.py\n"
      "Errors will be printed as they happen, so a test succeeds if no errors are printed\n\n")
def test_answer():
    assert fibonacci.nth_num(5)==3
    

class TestCase(unittest.TestCase):
      def testfib(self):
            self.assertEqual(fibonacci.nth_num(5),3)

if __name__ == '__main__':
      test_answer()
      unittest.main(verbosity=2)
      