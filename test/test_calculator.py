# Testing functionality of the Calculator Class and operations 
# completed on the order data to achieve response

import unittest
import json
from datetime import datetime

from classes.cart import Cart
from classes.calculator import Calculator

# Using sample payload from assignment repo
with open ('sample_orders/order1.json') as f:
    payload = json.load(f)


class TestCalculations(unittest.TestCase):

    # Set up a test cart & calculator object
    def setUp(self):
        self.test_cart = Cart(payload)
        self.calculator = Calculator(self.test_cart)

    # Testing small order calculation
    def testCalculateSmallOrder(self):
        # Surcharge will equal €10 - Cart Total
        self.assertEqual(self.calculator.calculateSmallOrderFee(),
                          (1000 - self.test_cart.cart_value))
        # If the cart value is €8.90, the surcharge will be €1.10
        self.test_cart.cart_value = 890
        self.assertEqual(self.calculator.calculateSmallOrderFee(),
                          110)
    # Testing delivery distance calculation    
    def testCalculateDistanceFee(self):
        # Delivery for 1000m = €2
        self.test_cart.delivery_distance = 1000
        self.assertEqual(self.calculator.calculateDistanceFee(),
                        200)
        # Delivery for 1499m = €3
        self.test_cart.delivery_distance = 1499
        self.assertEqual(self.calculator.calculateDistanceFee(),
                        300)
        # Delivery for 1500m = €3
        self.test_cart.delivery_distance = 1500
        self.assertEqual(self.calculator.calculateDistanceFee(),
                        300)
        # Delivery for 1501m = €4
        self.test_cart.delivery_distance = 1501
        self.assertEqual(self.calculator.calculateDistanceFee(),
                        400)
        
    # Testing item surcharge calculation      
    def testCalculateItemFee(self):
        # Charge for 4 Items = €0
        self.assertEqual(self.calculator.calculateItemFee(),
                         0)
        # Charge for 5 Items = €0.50
        self.test_cart.number_of_items = 5
        self.assertEqual(self.calculator.calculateItemFee(),
                         50)
        # Charge for 10 Items = €3
        self.test_cart.number_of_items = 10
        self.assertEqual(self.calculator.calculateItemFee(),
                         300)
        # Charge for 13 Items = €5.70
        self.test_cart.number_of_items = 13
        self.assertEqual(self.calculator.calculateItemFee(),
                         570)
        # Charge for 14 Items = €6.20
        self.test_cart.number_of_items = 14
        self.assertEqual(self.calculator.calculateItemFee(),
                         620)

    # Testing summing of all fees incl. rush hour fees & upper limits
    def testCalculateAllFees(self):
        base_total = (self.calculator.calculateSmallOrderFee() +
                     self.calculator.calculateDistanceFee() +
                     self.calculator.calculateItemFee())
        # All fees outside rush hours = total fees
        self.test_cart.time = datetime(2024,1,26,14,59,0) 
        self.assertEqual(self.calculator.calculateAllFees(),
                             base_total)
        # All fees inside rush hours = total fees * 1.2
        self.test_cart.time = datetime(2024,1,26,15,00,0) 
        self.assertEqual(self.calculator.calculateAllFees(),
                             base_total*1.2)
        # Edge Case Order to test max €15 delivery
        self.test_cart.delivery_distance = 5000
        self.test_cart.number_of_items = 20
        self.calculator.calculateDistanceFee()
        self.calculator.calculateItemFee()
        self.assertEqual(self.calculator.calculateAllFees(),
                             1500)
        # Free delivery for cart value >= €200
        self.test_cart.cart_value = 20000
        self.assertEqual(self.calculator.calculateAllFees(),
                             0)
