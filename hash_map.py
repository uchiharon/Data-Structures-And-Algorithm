class hash_map():
    def __init__(self):
        self.space = 10
        self.arr = [None for i in range(self.space)]
        
    def change_space(self, size):
        self.space = size
        
    def get_hash(self,key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.space
    
    def add_value(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
        
    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]
        
########################### Test Session #######################        
test = hash_map()
test.add_value("march 6",500)
print(test.arr)
print(test.get("march 6"))
    