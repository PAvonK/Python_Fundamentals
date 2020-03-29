# Generators - 9000



def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
#
#
#def genPrimes():
#    p = 2
#    n = 2
#    primes = []
#    while True:
#        while n < 10:
#            if ((n**p - n) % p) != 0:
#                return False
#            elif ((n**p - n) % p) == 0:
#                n += 1
#            primes.append(p)
#            yield next
#        p = (p + 1)
#        p = next
#        print(primes)
        
        
                
                    


#def prime(p):
#    n = 2
#    while n <= 10:
#        if ((n**p - n) % p) == 0:
#            print('True')
#            n += 1
#            print(p)
#            print(n)
#        else:
#            break
#            print('Nope, this number is not prime')
            
#prime(3)

#print()
#p = 3
#print(p)
#n = 2
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#print()
#p += 1
#print(p)
#n = 2
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#print()
#p += 1
#print(p)
#n = 2
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#print()
#p += 1
#print(p)
#n = 2
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#print()
#p += 1
#print(p)
#n = 2
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#print()
#p += 1
#print(p)
#n = 2
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#print()
#p += 1
#print(p)
#n = 2
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)
#n += 1
#print((n**p - n) % p)