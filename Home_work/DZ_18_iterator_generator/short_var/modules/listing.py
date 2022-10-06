class MyRange:
    
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish
        
    def __iter__(self):
        self.cursor = self.start - 1
        return self
    
    def __next__(self):
        self.cursor  += 1
        if self.cursor >= self.finish:
            raise StopIteration
        return self.cursor
    
my_range = MyRange(1, 5)
for item in my_range:
    print(item)