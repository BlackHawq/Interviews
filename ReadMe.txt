This document describes the thought process behind the Onymos Programming interview solution.
Initially I had wanted to scrape the prices and ticker names from online but I found I had to import quite a few additional files given the problem wanted us to limit imports I decided against it.

The imports I did need to simulate the random Nature of the problem were
import random
import time
Random to use the random choice function and generate randints
Time to create a random interval at which trades and matches would occur.

The initial Class Declaration is as per instruction but in order to prevent issues with concurrency I set a flag in it which would deterine whether the current order is in use or not which is set during the matching phase of the project
class Order:
    def __init__(self, orderType, tickerName, price, quantity):
        self.orderType = orderType
        self.ticker = tickerName
        self.price = price
        self.quantity = quantity
        self.inUseFlag = False
    
    def toggle_Flag(self):
        if self.inUseFlag == False:
            self.inUseFlag = True
        elif self.inUseFlag == True:
            self.inUseFlag = False
        return self.inUseFlag
    
    def get_Flag(self):
        return self.inUseFlag

As we were not allowed to use any imports and dictionaries I went ahead and created a data structure for a double ended Queue
This would allow me to add and remove any elements from either side of the queue depending on the use case.
class doubleQueue:
    def __init__(self):
        self.elements = []

#Accessing elements via index
    def __getitem__(self, index):
        return self.elements[index]

#Removing an element from the front. Checks whether the list is empty prior to trying to remove
    def pop_Front(self):
        if self.is_Empty():
            print("Looks like it's Empty")
            return None
        else:
            return self.elements.pop(0)

#Removing an element from the back. Also checks for list capacity
    def pop_Rear(self):
        if self.is_Empty():
            print("Looks like it's Empty")
            return None
        else:
            return self.elements.pop()

# Class for tracking orders that will contain the functions for adding and matching orders uses the Double queue above to store sells and buys in seperate lists
class StockOrderTracker:

# Matches orders via buy and sell prices and checks the flags on the current item in the list. It will pop items that are in use in other threads
    def match_Orders(self):

# Is a wrapper class that runs the underlying functions of the Stock Order tracker
class TradeWrapper:

# Uses the hash function to create the index value for the order which is the modulo'd against the max number of orders
    def add_Order(self,order_type, ticker, price, quantiy):

# I just grabbed a bunch of stock tickers from online for companies I know and used random function
def generate_random_Orders(TradeWrapper):

# I have assigned a fixed duration over which the simulator runs to save time while testing and debugging but this can be changed   
def tradeSimulator(TradeWrapper, duration=5):
