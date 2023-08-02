class Observer:
    def update(self, observable, *args, **kwargs):
        pass

class Observable:
    def __init__(self):
        self.observers = []

    def addObserver(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def removeObserver(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notifyObservers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(self, *args, **kwargs)

class AmericanStockMarket(Observer):
    def update(self, observable, *args, **kwargs):
        print('American stock market received: {0}\n{1}'.format(args, kwargs))

class EuropeanStockMarket(Observer):
    def update(self, observable, *args, **kwargs):
        print('European stock market received: {0}\n{1}'.format(args, kwargs))

class StockMarket(Observable):
    def setStocks(self, stocks):
        self.stocks = stocks
        self.notifyObservers(stocks)

def main():
    nyse = AmericanStockMarket()
    nasdaq = AmericanStockMarket()
    lse = EuropeanStockMarket()
    stockMarket = StockMarket()
    stockMarket.addObserver(nyse)
    stockMarket.addObserver(nasdaq)
    stockMarket.addObserver(lse)
    stockMarket.setStocks({'NYSE': 'American Stock Exchange', 'NASDAQ': 'National Association of Securities Dealers Automated Quotations', 'LSE': 'London Stock Exchange'})

if __name__ == '__main__':
    main()