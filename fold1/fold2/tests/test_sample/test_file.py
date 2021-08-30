from unittest.case import TestCase
from unittest import main

class TestNothing(TestCase):
    def test_it(self):
        self.assertTrue(True)
        # self.assertTrue(False)

if __name__=="__main__":
    main()
