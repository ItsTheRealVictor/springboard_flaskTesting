import doctests_demo
import unittest as ut

class AdditionTestCase(ut.TestCase):
    '''
    examples of unit tests
    
    Remember:
        1) The class with the tests must subclass TestCase

        2) test methods MUST start with test_
    '''

    def test_add(self):
        assert doctests_demo.add(2,2) == 4

    def test_add_2(self):
        self.assertEqual(doctests_demo.add(1,2), 3)

print(dir(ut.TestCase))


# if __name__ == '__main__':
#     ut.main(verbosity=3)
