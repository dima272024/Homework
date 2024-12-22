numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for figure in numbers:
    if figure == 1:
        continue
    is_prime = True
    for i in range(2, figure):
        if figure % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(figure)
    else:
        not_primes.append(figure)
print('primes', primes)
print('nom_primes', not_primes)


