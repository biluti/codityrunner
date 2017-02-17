# -*- coding: UTF-8 -*-



import unittest

import codity



def demo0():
    pass

def demo1(a):
    return 0

def demo2(a, b):
    return 0



class TestCodityRunner(unittest.TestCase):
    
    def setUp(self):
        pass
 
 
    def test_0(self):
        cr = codity.CodityRunner()
        self.assertEqual(cr.solution, None)

        cr = codity.CodityRunner(demo0)
        self.assertEqual(cr.solution, demo0)
        
        
    def test_1(self):
        cr = codity.CodityRunner(demo1)
        ret = cr.run(1)
        self.assertEqual(ret, 0)                

    def test_2(self):
        cr = codity.CodityRunner(demo2)
        ret = cr.run(2, 2)
        self.assertEqual(ret, 0)                
        
        
    def test_3(self):
        cr = codity.CodityRunner(demo2)
        cr.add_vector(0, 0, 0)
        cr.add_vector(1, 0, 0)
        cr.run_test()

        
        
        
        
        
        
        
        




if __name__ == "__main__":
    unittest.main()
    



