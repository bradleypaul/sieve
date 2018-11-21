class Sieve:
    def __init__(self, maxValue=1000000):
        self.sieve = [None for i in range(maxValue + 1)]
        self.populate()

    def populate(self):
        p = 2
        size = len(self.sieve)
        while p < size:
            if self.sieve[p] == None:
                self.sieve[p] = True
                for i in range(p * 2, size, p):
                    self.sieve[i] = False
            p += 1

    def isPrime(self, index):
        return False if (index < 2) else self.sieve[index]

    def isComposite(self, index):
        return False if (index < 2) else not self.isPrime(index)


if __name__ == '__main__':
    s = Sieve(10)
    s1 = Sieve()
    print(s.isPrime(5))
    print(s.isPrime(1))
    print(s1.isComposite(990))
