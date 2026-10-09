import unittest
from game import Clicker,SUBJECT
class Tests(unittest.TestCase):
 def test_subject(self):self.assertEqual(SUBJECT,'🫪')
 def test_click(self):
  g=Clicker();g.click();self.assertEqual(g.points,1)
 def test_no_credit(self):
  g=Clicker();self.assertFalse(g.buy(1));self.assertEqual(g.power,1)
 def test_upgrade(self):
  g=Clicker();g.points=10;self.assertTrue(g.buy(1));g.click();self.assertEqual(g.points,2)
 def test_worker(self):
  g=Clicker();g.points=25;g.buy(2);g.tick(.5);self.assertEqual(g.points,.5)
 def test_cost_grows(self):
  g=Clicker();g.points=100;g.buy(1);self.assertEqual(g.cost(1),20)
if __name__=='__main__':unittest.main()
