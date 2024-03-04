# Backend Challenge for Wolt Software Engineer Intern 2024
# Completed by Eoin O'Sullivan on 30.01.24

from flask import Flask, request
import json

from classes.cart import Cart
from classes.calculator import Calculator

# Set live to True for API server functionality
# Set to False for local functionality
# See readme.md for further details
live = False

# Handle Payload, trigger calculations & return response
def handle_payload(request_payload, live):
    # Creating new cart object with order info
    order = Cart(request_payload)
    # Creating new calculator object using order info
    calculator = Calculator(order)
    # Calling calculator methods to calculate fees
    calculator.calculateSmallOrderFee()
    calculator.calculateDistanceFee()
    calculator.calculateItemFee()
    calculator.calculateAllFees()
    # Returning updated order info to be sent as HTTP response
    if live:
        return order.update_order(request_payload, live)
    # Sending updated order info to local JSON file
    else:
        order.update_order(request_payload, live)

if live:
    # Loading Order info from HTTP POST request
    app = Flask(__name__)
    @app.route("/orders/", methods=['GET', 'POST'])
    def handle_request():
        request_payload = request.get_json()
        # Returning response payload to server
        return handle_payload(request_payload, live)
    
else:
    # Loading Order info from JSON file
    with open ('sample_orders/order1.json') as f:
        request_payload = json.load(f)
    handle_payload(request_payload, live)