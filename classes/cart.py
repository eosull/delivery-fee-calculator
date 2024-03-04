import json
import datetime

class Cart():
    """
    Class to create cart from
    JSON payload and return
    as Python object for
    calculations to be performed
    """
     
    def __init__(self, payload):
        self.cart_value = payload["cart_value"]
        self.delivery_distance = payload["delivery_distance"]
        self.number_of_items =  payload["number_of_items"]
        # Calculating time
        self.time = self.order_time()


    # Return current UTC time for order timestamp
    def order_time(self):
        return datetime.datetime.now(datetime.timezone.utc)
    
    # Update order JSON payload
    def update_order(self, payload, live):
        # Adding current time to order
        payload["time"] = self.time.strftime("%Y-%m-%d %H:%M:%S")
        # Adding delivery_fee to response payload
        payload["delivery_fee"] = self.delivery_fee
        if live:
            return payload
        else:
            # Add updated order info to JSON file
            with open('sample_orders/order1_incl_fees.json', 'w', encoding='utf-8') as f:
                json.dump(payload, f, ensure_ascii=False, indent=4)