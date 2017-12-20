def high_and_low(numbers):
    k=list(map(int, numbers.split()))
    return str(max(k))+" "+ str(min(k))