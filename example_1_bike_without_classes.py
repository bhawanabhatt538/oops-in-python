def update_sale_price(bike, sale_price):
    if bike['sold'] is True:
        raise Exception('Action not allowed. Bike has already been sold')
    bike['sale_price']= sale_price

  
def create_bike(description, cost, sale_price, condition):
    return{'description': description,
           'cost':cost,
           'sale_price':sale_price,
           'condition': condition,
           'sold':False,
           
           }
    
def sell(bike,sold_for = None):
    if sold_for:
        update_sale_price(bike, sold_for)
    bike['sold'] = True
    profit = bike['sale_price']-bike['cost']
    return profit

if __name__ == '__main__':
    bike1= create_bike('univega Alpine,orange',cost=100,sale_price=500,condition=0.5)
    
    update_sale_price(bike1,350)
    
    print(sell(bike1))
    