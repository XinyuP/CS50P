class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
    
    def __str__(self):
        return self._size * "🍪"
    
    def deposit(self, n):
        if n < 0: raise ValueError
        self.size += n

    
    def withdraw(self, n):
        if n < 0: raise ValueError
        self.size -= n 


    @property
    def capacity(self):
        return self._capacity


    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity or size < 0:
            raise ValueError
        self._size = size
    



def main():
    jar = Jar()
    print(jar)
    jar.deposit(4)
    print(jar) 
    jar.deposit(8)
    print(jar) 
    jar.withdraw(5)
    print(jar) 

if __name__ == "__main__":
    main()