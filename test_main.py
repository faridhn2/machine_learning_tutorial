from main import ma3
import unittest
class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass
    def test_query1(self):
        ma3_list = ma3([1,4,3,2,5,7,0,9])
        self.assertEqual(ma3_list,[0,0,2.7,3,3.3,4.7,4,5.3])
        
    
    
if __name__ == '__main__':
    unittest.main()

#python -m unittest discover