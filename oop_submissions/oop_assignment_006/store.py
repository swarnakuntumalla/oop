class Item:
    def __init__(self, name, price, category):
        self._name = name
        self._category = category
        if price <= 0:
            raise ValueError(f'Invalid value for price, got {price}')
        else:
            self._price = price
            
    def __str__(self):
        return f'{self._name}@{self._price}-{self._category}'
    
    @property
    def name(self): return self._name
    @property
    def category(self): return self._category
    @property
    def price(self): return self._price

class Query:
    def __init__(self, field, operation, value):
        self._field = field
        self._value = value
        operation_list=['IN', 'EQ', 'GT', 'LT', 'GTE', 'LTE', 'STARTS_WITH', 'ENDS_WITH', 'CONTAINS']
        if operation in operation_list:
            self._operation = operation
        else:
            raise ValueError(f'Invalid value for operation, got {operation}')
            
    def __str__(self):
        return f'{self._field} {self._operation} {self._value}'
    
    @property
    def field(self): return self._field
    @property
    def value(self): return self._value
    @property
    def operation(self): return self._operation
    
class Store:
    store_list =[]
    
    def add_item(self,item):
        self.store_list.append(item)
        
    def filter(self,*args):
        for query in args:
            store_filter_list = Store()
            for compare_item in self.store_list:
                key = getattr(compare_item,query.field)
                #print(key)
                if query.operation == 'IN' and key in query.value:
                    store_filter_list.add_item(compare_item)
                
                elif query.operation == 'EQ' and key == query.value:
                    store_filter_list.add_item(compare_item)
            
                elif query.operation == 'GT' and key > query.value:
                    store_filter_list.add_item(compare_item)
            
                elif query.operation == 'GTE' and key >= query.value:
                    store_filter_list.add_item(compare_item)
                
                elif query.operation == 'LT' and key < query.value:
                    store_filter_list.add_item(compare_item)
    
                elif query.operation == 'LTE' and key <= query.value:
                    store_filter_list.add_item(compare_item)
                
                elif query.operation == 'STARTS_WITH' and key.startswith(query.value):
                    store_filter_list.add_item(compare_item)
            
                elif query.operation == 'ENDS_WITH' and key.endswith(query.value):
                    store_filter_list.add_item(compare_item)
            
                elif query.operation == 'CONTAINS' and query.value in key :
                    store_filter_list.add_item(compare_item)
        return store_filter_list
        #return '\n'.join([str(x) for x in store_result_list])
    
    def exclude(self,*args):
        store_exclude_list = Store()
        for query in args:
            filtered_list = self.filter(query)
            [store_exclude_list.add_item(compare_item) for compare_item in self.store_list if compare_item not in filtered_list.store_list]
            return store_exclude_list
         
    def count(self):
        return len(self.store_list)
       
    def __str__(self):
        if len(self.store_list) == 0:
            return 'No items'
        else:
            return '\n'.join(map(str,self.store_list))
            
    def __add__(self, other):
        results = []
        add_list =Store()
        results = self.store_list + other.store_list
        [add_list.add_item(item) for item in results if item not in add_list.store_list]
        return add_list

'''store = Store()
item = Item(name="Oreo Biscuits", price=30, category="Food")
store.add_item(item)
item = Item(name="Boost Biscuits", price=20, category="Food")
store.add_item(item)
item = Item(name="ParleG Biscuits", price=10, category="Food")
store.add_item(item)

#print(store)
#query = Query(field="price", operation="GT", value=15)
#results = store.exclude(query) + store.filter(query)
query = Query(field="name", operation="CONTAINS", value="oo")
query = Query(field="price", operation="LT", value=15)
#results = store.filter(query)
results = store.filter(query, query)
print(results)'''