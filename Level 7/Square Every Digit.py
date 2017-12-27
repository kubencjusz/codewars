def square_digits(num):
    return int(''.join([str(int(k)**2) for k in str(num)]))