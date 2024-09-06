"""Find Prime Faster"""
def find_primes_faster(number):
    """Finding the Prime Numbers in a faster way and optimized solution"""
    output = {2}
    result = [2]
    threshold = (int(number ** 0.5) + 1)
    for number in range(3, number):
        #print(int(number ** 0.5) + 1)
        for factor in output:
            if number % factor == 0:
                break
        else:
            if number < threshold:
                output.add(number)
            #print(f'{number} is prime!')
            result.append(number)
    return output, result

X = find_primes_faster(1000)
print('The efficient list of prime divisors', X[0])
print('The list of primes', X[1])
