class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Wrong capacity')
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size *'🍪'

    def deposit(self, n):
        if n > self._capacity:
            raise ValueError("Exceed capacity")
        if self._size + n > self._capacity:
            raise ValueError("Exceed capacity")
        self._size += n

    def withdraw(self, n):
        if self._size < n:
            raise ValueError("There are less cookies than asked to remove")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar=Jar()
jar.deposit(4)
jar.withdraw(3)
jar.deposit(6)
print(jar)
