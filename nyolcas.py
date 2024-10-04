def nyolc(n):
    fibonacci_sorozat = [0, 1]
    for i in range(2, n):
     fibonacci_sorozat.append(fibonacci_sorozat[i - 1] + fibonacci_sorozat[i - 2])
    return fibonacci_sorozat[:n]
print(nyolc(80))

