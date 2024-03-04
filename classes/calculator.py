class Calculator():
    """
    Class to perform calculations
    on cart as set out in the 
    assignment tasks
    """

    def __init__(self, order):
        self.order = order

    # Calculating Small Order Surcharge
    def calculateSmallOrderFee(self):
        # Adding surcharge for cost < €10 and returning value
        if self.order.cart_value < 1000:
            self.order.small_order_fee = 1000 - self.order.cart_value
            return self.order.small_order_fee
        else:
            self.order.small_order_fee = 0
            return self.order.small_order_fee

    # Calculating Delivery Distance Fee
    def calculateDistanceFee(self):
        # Testing delivery distance and adding €1 for every additional
        # 500m travelled by courier past 1km base
        self.order.distance_fee = 200
        charging_distance = 1001
        while self.order.delivery_distance >= charging_distance:
            self.order.distance_fee += 100
            charging_distance += 500
        return self.order.distance_fee

    # Calculating Item Quantity Fee
    def calculateItemFee(self):
        self.order.item_quantity_fee = 0
        item_charge_check = 5
        # Adding 50c on for each item over 4
        for items in range(4, self.order.number_of_items):
            if items <= item_charge_check:
                self.order.item_quantity_fee += 50
                item_charge_check += 1
        # Adding €1.20 surcharge for over 12 items
        if self.order.number_of_items >= 13:
            self.order.item_quantity_fee += 120
        return self.order.item_quantity_fee

    # Calculating total amount of fees to be paid by customer
    def calculateAllFees(self):
        # Adding together all calculated fees
        self.order.delivery_fee = self.order.small_order_fee + self.order.distance_fee + self.order.item_quantity_fee
        # Call checkTime method to see if rush fee is to be applied
        if self.checkTime():
            self.order.delivery_fee = self.order.delivery_fee * 1.2
        # To a maximum of €15
        if self.order.delivery_fee >= 1500:
            self.order.delivery_fee = 1500
        # No fees if order is over €200
        if self.order.cart_value >= 20000:
            self.order.delivery_fee = 0
        return self.order.delivery_fee

    # Checking if current time is within rush hours
    def checkTime(self):
        # Parsing Order Datetime Info to return day & hour as string
        order_day = self.order.time.strftime('%a')
        order_hour = int(self.order.time.strftime('%H'))
        # Checking if order is placed on a Friday between 3pm & 7pm
        if order_day == 'Fri':
            if (order_hour >= 15) and (order_hour < 19):
                return True
        else:
            return False
        
        