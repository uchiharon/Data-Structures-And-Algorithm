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
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
        
########################### Test Session #######################        
test = hash_map()
test["march 6"] = 500
print(test.arr)
print(test["march 6"])
del test["march 6"]
print(test.arr)
    