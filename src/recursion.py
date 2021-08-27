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


if __name__ == '__main__':
    test_list = [1,2,3,5,6,7,8,9,12,14,45,78,89]

    result = rec_binary_search(test_list, 12, 0, len(test_list)-1)
    print(result)
