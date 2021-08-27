def fakt(n):
    if(n > 0):
        return n * fakt(n -1)
    else:
        return 1

def fibonacci(n):
    if(n > 1):
        return fibonacci(n -1) + fibonacci(n - 2)
    else:
        return n

def rec_binary_search(list, data, e, u):
    k = 0
    if(e > u):
        return False
    else:
        k = (e + u) // 2
        if(list[k] > data):
            return rec_binary_search(list, data, e, k - 1)
        elif(list[k] < data):
            return rec_binary_search(list, data, k + 1, u)
        else:
            return k

def hanoi(n, r1,r3,r2):
    if(n > 0):
        hanoi(n-1, r1,r2,r3)
        print(str(n) + '. korong átrakása:', r1, '->', r3)
        hanoi(n-1, r2,r3,r1)

if __name__ == '__main__':
    hanoi(5, 'a', 'b', 'c')
