class Hashtable:

    def __init__(self):
        self.MAX = 10
        #self.arr = [None for i in range(self.MAX)]
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
t = Hashtable()
print(t.get_hash("M"))
t.__setitem__("dec 12", 190)
t.__setitem__("March 17", 190)

print(t.arr)
