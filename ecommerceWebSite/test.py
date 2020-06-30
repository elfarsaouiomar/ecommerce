import unittest
from weShop.Controllers.views import shop
from django.urls import reverse
from django.test import Client

class MyTestCase(unittest.TestCase):

    client = Client()
    
    
    

    def test_something(self):
        pass
        #self.assertEqual(True, False)


    def test_whatever_list_view(self):
        #w = self.test_something()
        url = reverse(shop)
        resp = self.client.get(url)

        print(url)
        print(resp)


        self.assertEqual(resp.status_code, 200)
        #self.assertIn('django', resp.content)


if __name__ == '__main__':
    unittest.main()
