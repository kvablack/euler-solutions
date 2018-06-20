def computeOddTotients(n):
    m = (n - 1) // 2 # length of list, since only storing odd values

    # phi[i] corresponds to phi(i * 2 + 1), since we only care about odd values
    # start by marking each phi[i] as the number it's supposed to represent
    phi = [i * 2 + 1 for i in range(m + 1)]

    for i in range(1, m + 1):
        p = i * 2 + 1 # the actual odd number that phi[i] represents
        if (phi[i] == p):
            # phi[i] still has its initial value, so p is prime

            print(p)
            phi[i] = p - 1 # phi of a prime number p is p-1
  
            # update phi values of all multiples of p
            for j in range(i + p, m + 1 , p):
                # add contribution of p to its multiple i by multiplying by (1 - 1/p)
                phi[j] = (phi[j]//p) * (p-1)

    return phi

print(sum(computeOddTotients(5 * (10**8))))
