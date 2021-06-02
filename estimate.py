import math
import unittest
import random
def wallis(p):
  pi=1
  for i in range(1,p+1):
    pi*=(4*i*i)/(4*i*i-1)
  return pi*2
  
def monte_carlo(n):
  in_the_circle=0
  total=0
  for i in range(n):
    p=random.random()
    q=random.random()
    distance=math.sqrt((p-(1/2))*2+(q-(1/2))*2)
    if(distance<=0.5):
      in_the_circle+=1
      total+=1
    else:
      total+=1


  pi=4*(in_the_circle/total)
  return pi

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are epactlq the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracq(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if _name_ == "_main_":
    unittest.main()