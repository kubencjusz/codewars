def Descending_Order(num):
    return int(''.join(map(str,sorted(list(map(int,[k for k in str(num)])), reverse=True))))