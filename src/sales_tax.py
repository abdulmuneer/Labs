'''
Created on May 13, 2012

@author: MUNEER
'''
class Item(object):
    '''contains the information and methods of a particular item'''
    def __init__(self, name, shelf_price, sales_tax=10, import_duty=0):
        self.name, self.shelf_price = name, shelf_price
        self.sales_tax_rate, self.is_import_rate = sales_tax, import_duty
        
    def get_sale_tax(self):
        #rounding to .05 precision
        sales_tax = self.__myround(self.shelf_price*self.sales_tax_rate)/100.0
        return sales_tax
    
    def get_import_duty(self):
        #rounding to .05 precision
        import_duty = self.__myround(self.shelf_price*self.import_rate)/100.0
        return import_duty
        
    def __myround(self,x, base=5):
        return int(base * round(float(x)/base))
    
class MyStore(object):
    '''stores the items in a dictionary. 
    Describes methods to add or remove a product from store.'''
    def __init__(self):
        self.store_items = {}
    #set items in the store
    def enter_item(self,name,shelf_price, sales_tax=10, import_duty=0):
        self.store_items[name] = Item(name,shelf_price, sales_tax, import_duty)
        
    def delete_item(self,name):
        try:
            del self.store_items[name]
            return True
        except:
            return False

class BillDesk(object):
    def __init__(self):
        super(self.__class__).__init__()
        self.purchased_items = {}

    def get_bill_input(self):
        next_input = raw_input()
        self.bill_entry = []
        while(next_input):
            self.bill_entry.append(next_input)
            next_input = raw_input()
        for items in self.bill_entry:
            quantity, name, sale_price, description = self.__item_parser(items)
            
    
        
    def __item_parser(self,bill_input):
        '''
        parses the input strings to return product name, quantity, 
        sale_price and tax rates.
        '''
        entry = bill_input.strip().split()
        quantity, sale_price = int(entry.pop(0)), int(entry.pop())
        #remove the "at" that comes before the rate
        entry.pop()
        description, product = entry[0], '_'.join(entry[1:]) \
                    if entry[0]=='imported' else None, '_'.join(entry)
    