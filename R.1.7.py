def odd_squares_sum(n):
    return sum(a*a for a in range(0,n) if a%2==1)


print(odd_squares_sum(4))