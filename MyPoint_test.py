
import math
import unittest
from MyPoint import MyPoint

class TestMyPoints(unittest.TestCase):
    def test_chkDistance(self): # test case must start with test_
        p1=MyPoint(1,2) # mypy doesn't warn it (implicit int->float conversion), why?
        p2=MyPoint(3,4)
        dist=p1.distance_of(p2)
        reference= math.sqrt(2) * 2.0
        self.assertAlmostEqual(dist, reference, places=7)

if __name__ == '__main__':
    unittest.main()