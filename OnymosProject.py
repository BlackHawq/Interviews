import random
import time

# Constants to keep track of
TICKERMAX = 1024
BUY = 'BUY' = 'buy' = 'Buy'
SELL = 'SELL' = 'sell' = 'Sell'

# Defining what an order contains based on description
class Order:
    def __init__(self, orderType, tickerName, price, quantity):
        self.orderType = orderType
        self.ticker = tickerName
        self.price = price
        self.quantity = quantity

# Since we can't import I wanted to define a double Queue, a hash map or dictionary would have taken a bit longer to implement and I was short on time 
class doubleQueue:
    def __init__(self):
        self.elements = []

    def add_front(self, item):
        self.elements.insert(0, item)

    def add_rear(self, item):
        self.elements.append(item)
    
    def get_Len(self):
        return len(self.elements)
    
    def is_Empty(self):
        return len(self.elements) == 0
    
    def pop_Front(self):
        if self.is_Empty():
            print("Looks like it's Empty")
            return None
        else:
            return self.elements.pop(0)
    
    def pop_Rear(self):
        if self.is_Empty():
            print("Looks like it's Empty")
            return None
        else:
            return self.elements.pop()
    
    def peek_Front(self):
        if self.is_Empty():
            print("Looks like it's Empty")
            return
        else:
            return self.elements[0]
    
    def peek_Rear(self):
        if self.is_Empty():
            print("Looks like it's Empty")
            return
        else:
            return self.elements[0]
    
#Class for tracking orders that will contain the underlying functions for adding and matching orders
class StockOrderTracker:
    def __init__(self):
        self.buys = doubleQueue()
        self.sells = doubleQueue()
    
    #Adds orders to the queues 
    def add_Order(self, order):
        if order.orderType == BUY:
            self.buys.add_front(order)
        elif order.orderType == SELL:
            self.sells.add_front(order)
        else:
            print("Seems like there's an error with the order, check the type")
            return None
    
    # Matches orders via buy and sell prices
    def match_Orders(self):
        isMatched = False
        while self.buys and self.sells:
            current_Buy = self.buys.peek_Front
            current_Sell = self.sells.peek_Front
            if current_Buy.price >= current_Sell.price:
                quantityCheck = min(current_Buy.quantity,current_Sell.quantity)
                current_Buy.quantity -=quantityCheck
                current_Sell.quantity -=quantityCheck
                isMatched = True
                if current_Buy.quantity == 0:
                    self.buys.pop_Rear()
                if current_Sell.quantity == 0:
                    self.sells.pop_Rear()
                print("A match was made! " + quantityCheck + " stocks were matched of" + current_Buy.ticker)
                print("The price was " + current_Buy.price)
            else:
                break
        print("Match completed!")
        return isMatched
    

class TradeWrapper:
    def __init__(self):
        self.Trackers = []
        for i in range(TICKERMAX):
            self.Trackers[i] = StockOrderTracker()

    def add_Order(self,order_type, ticker, price, quantiy):
        order = Order(orderType=order_type, tickerName=ticker, price=price, quantity=quantiy)
        index = hash(ticker) % TICKERMAX
        self.Trackers[index].add_Order(order)
    
    def match_Order(self):
        for tracker in self.Trackers:
            tracker.match_Orders()
    
    def getOrderIndex(self,order):
        return hash(order.ticker) % TICKERMAX

#Just grabbed a bunch of stock tickers from online  
def generate_random_Orders(TradeWrapper):
    ticker = random.choice(["AAPL","GOOG","MSFT", "AMZN", "NVDA","KO","WMT","MCD", "PEP", "GS", "CSCO", "IBM", "ORCL", "AMD"])
    order_type = random.choice([BUY, SELL])
    quantity = random.randint(1, 100000)
    price = random.randint(50, 200000)

    TradeWrapper.addOrder(order_type,ticker,price,quantity)
    
def tradeSimulator(TradeWrapper, duration=10):
    start_time = time.time()
    while time.time() - start_time < duration:
        generate_random_Orders(market)
        TradeWrapper.match_orders()
        time.sleep(random.uniform(0.1, 0.5))  # Simulate random time interval between orders

if __name__ == "__main__":
    stockmarket = TradeWrapper()
    tradeSimulator(stockmarket)

