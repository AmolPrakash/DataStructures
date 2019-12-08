class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.buckets = [None] * self.size
        self.values = [None] * self.size
    def get(self, key):
        bucket = self.hashfunction(key)
        c = -1
        if self.buckets[bucket] == None:
            return None
        while self.buckets[bucket] != None and self.buckets[bucket] != key and c != bucket:
            bucket = self.linearProbe(bucket)
            c += 1
        if self.buckets[bucket] == key:
            return self.values[bucket]
        return None
    def put(self, key, value):        
        bucket = self.hashfunction(key)
        if self.buckets[bucket] == None:
            self.buckets[bucket] = key
            self.values[bucket] = value
            return
        if self.buckets[bucket] == key and self.buckets[bucket] != None:
            self.values[bucket] = value
            return
        while self.buckets[bucket] != None and self.buckets[bucket] != key:
            bucket = self.linearProbe(bucket)
        if self.buckets[bucket] == None:
            self.buckets[bucket] = key
            self.values[bucket] = value
            return
        if self.buckets[bucket] == key and self.buckets[bucket] != None:
            self.values[bucket] = value
            return                    
    def hashfunction(self, key):
        return key%self.size
    def linearProbe(self, previousBucket):
        return previousBucket+1%self.size
    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, value):
        return self.put(key, value)        
ht = HashTable(7)
ht[15] = "abce"
ht[22] = "xyz"
ht[11] = "spj"
ht[18] = 'datascience'
print (ht.buckets)
print (ht.values)
print (ht[17])
print (ht[11])
