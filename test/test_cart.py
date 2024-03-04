# Testing functionality of the Cart Class and creation
# of cart object from JSON payload

import unittest
import datetime

from classes.cart import Cart

# Using sample payload from assignment repo
sample_payload = {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4}

class TestCartBuild(unittest.TestCase):

    # Set up a test cart object
    def setUp(self):
        self.test_cart = Cart(sample_payload)

    # Testing successful addition of Cart Value to object
    def testCartValue(self):
        self.assertEqual(self.test_cart.cart_value, sample_payload["cart_value"])

    # Testing successful addition of Delivery Distance to object
    def testDeliveryDistance(self):
        self.assertEqual(self.test_cart.delivery_distance, sample_payload["delivery_distance"])

    # Testing successful addition of Item Number to object
    def testNumberOfItems(self):
        self.assertEqual(self.test_cart.number_of_items, sample_payload["number_of_items"])    
    
    # Testing successful addition of UTC time to order object
    def testTime(self):
        self.assertEqual(self.test_cart.time.replace(microsecond=0).isoformat(' '),
                        datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(' '))
