#we should write a code to store the data in key:data format,by indexing them
#a prime number that is associated with the key mod size
#1 2 3 5 7 11 13 17 19 . . . . .  are the prime numbers

hashtable = [[]] * 10

def Insertdata(key,data):
    index = HashTable(key)
    hashtable[index] = [key, data]

def Removedata(key):
    index = HashTable(key)
    hashtable[index] = []

def HashTable(key):
    capacity = GetPrime(10)
    return key % capacity

def CheckPrime(num):
    if num == 0 or num == 1:
        return False

    for i in range(2,(num//2)):
        if num % i == 0:
            return False

    return True

def GetPrime(num):
    if num%2 == 0:
        num+=1
    flag = CheckPrime(num)
    while not flag:
        num = num+2
        flag = CheckPrime(num)
    return num

Insertdata(123, "apple")
Insertdata(432, "mango")
Insertdata(213, "banana")
Insertdata(654, "guava")
print(hashtable)
Removedata(123)
print(hashtable)
