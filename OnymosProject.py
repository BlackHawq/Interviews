import random
import time

# Constants to keep track of
TICKERMAX = 1024
BUY = 'BUY'
SELL = 'SELL'

# Defining what an order contains based on description
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

# Since we can't import or use dictionaries I wanted to define a double Queue. A hash map or dictionary would have taken a bit longer to implement and I was short on time 
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
    
    def __getitem__(self, index):
        return self.elements[index]

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
        while not self.buys.is_Empty() and not self.sells.is_Empty():
            current_Buy = self.buys[0]
            current_Sell = self.sells[0]
            if current_Buy.price >= current_Sell.price and current_Buy.get_Flag() == False and current_Sell.get_Flag() == False:
                self.buys[0].toggle_Flag()
                self.sells[0].toggle_Flag()
                quantityCheck = min(current_Buy.quantity,current_Sell.quantity)
                current_Buy.quantity -=quantityCheck
                current_Sell.quantity -=quantityCheck
                isMatched = True
                self.buys[0].toggle_Flag()
                self.sells[0].toggle_Flag()
                if current_Buy.quantity == 0:
                    self.buys.pop_Rear()
                if current_Sell.quantity == 0:
                    self.sells.pop_Rear()
                
                print("A match was made! " + str(quantityCheck) + " stocks were matched of " + str(current_Buy.ticker))
                print("The price was " + str(current_Buy.price))
            else:
                break
        return isMatched
    

class TradeWrapper:
    def __init__(self):
        self.Trackers = []
        for i in range(TICKERMAX):
            self.Trackers.append(StockOrderTracker())

    def add_Order(self,order_type, ticker, price, quantiy):
        order = Order(orderType=order_type, tickerName=ticker, price=price, quantity=quantiy)
        index = hash(ticker) % TICKERMAX
        self.Trackers[index].add_Order(order)
        print("Created order of type " + str(order_type) + " for ticker " + str(ticker) + " in quantity of " + str(quantiy) + " for the price of " + str(price))
    
    def match_Orders(self):
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

    TradeWrapper.add_Order(order_type,ticker,price,quantity)
    
def tradeSimulator(TradeWrapper, duration=5):
    start_time = time.time()
    while time.time() - start_time < duration:
        generate_random_Orders(TradeWrapper)
        TradeWrapper.match_Orders()
        # Simulate random time interval between orders
        time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    stockmarket = TradeWrapper()
    print("Trading time starts now!")
    tradeSimulator(stockmarket)

