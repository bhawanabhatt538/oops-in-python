
#dunder method: They have double underscore at the beginning and end of their names.
# they allow you to define custom behaviours for built in operations and make your objects more pythonic and user friendly.

from enum import Enum

class condition(Enum):
    NEW = 0
    GOOD = 1
    OKAY = 2
    BAD = 3
    

class MethodNotAllowed(Exception):
    pass

class Bike(object):
    count = 0
    num_wheels = 2
    def __init__(self,description, condition, sale_price,cost=0):
        self.description = description
        self.condition = condition 
        self.sale_price = sale_price
        self.cost = cost
        
        self.sold = False
        
        Bike.count+=1
        
        print(f'new bike:{self}')
        
    def __del__(self):
        Bike.count -=1

    def update_sale_price(self,new_sale_price):
        if self.sold:
            raise MethodNotAllowed("you can't update the sale price of a bike that has been sold")
        self.sale_price = new_sale_price
        
    def sell(self):
        """Mark as sold and determine the profit received from selling the bike"""
        self.sold = True
        profit = self.sale_price -self.cost
        return profit
    
    def service(self,cost, new_sale_price = None , new_condition = None):
        """service the bike and update attributes"""
        self.cost += cost
        if new_sale_price :
            self.update_sale_price(new_sale_price)
        if new_condition:
            self.condition  = new_condition
            
    def __repr__(self):
        sold_or_price = 'sold' if self.sold else f"${self.sale_price}"
        return f'Bike : {self.description}({sold_or_price})'

class tricycle(Bike):
    num_wheels = 3
            
if __name__ == '__main__':
    
    bike = Bike('univega Alpina,orange',condition.OKAY,500,100)
    trike = tricycle('Releigh Talus 2',condition.BAD, sale_price = 20)
    
    print(trike.num_wheels)
    print(trike)
    
    print(bike.num_wheels)
    
    print(bike.count)
    print('tricycle:', tricycle.count)
    
    del bike
    print(Bike.count) 
    