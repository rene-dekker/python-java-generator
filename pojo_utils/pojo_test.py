'''
Created on May 27, 2016

@author: dekkerr
'''
import unittest
from pojo import Pojo

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_sim_user_table(self):
        print 'prints sim user pojo: \n\n\n'
        filename = '../resources/pojo/sim_user_list'
        with open(filename, 'rb') as f:
            l = f.read().split('\n')
            pj = Pojo(json_properties = l)
            print pj

    def test_sim_address_table(self):
        print 'prints sim address pojo: \n\n\n'
        filename = '../resources/pojo/sim_address'
        with open(filename, 'rb') as f:
            l = f.read().split('\n')
            pj = Pojo(json_properties = l)
            print pj
 
    def test_sim_optin_table(self):
        print 'prints sim optin pojo: \n\n\n'
        filename = '../resources/pojo/sim_optin'
        with open(filename, 'rb') as f:
            l = f.read().split('\n')
            pj = Pojo(json_properties = l)
            print pj
 
    def test_sim_products_table(self):
        print 'prints sim products pojo: \n\n\n'
        filename = '../resources/pojo/sim_product'
        with open(filename, 'rb') as f:
            l = f.read().split('\n')
            pj = Pojo(json_properties = l)
            print pj
 
    def test_sim_campaign_table(self):
        print 'prints sim campaign pojo: \n\n\n'
        filename = '../resources/pojo/sim_campaign'
        with open(filename, 'rb') as f:
            l = f.read().split('\n')
            pj = Pojo(json_properties = l)
            print pj

#     def test_sim_garbage(self):
#         filename = '../resources/pojo/USERS_CUSTOMER_2016_05_27_10_51.csv'
#         with open(filename, 'rb') as f:
#             for i in f.readlines():
#                 if len(i.split(';')) != 26:
#                     print i.strip()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSimUserTable']
    unittest.main()
    