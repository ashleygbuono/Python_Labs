'''
List twin primes < a given number

p1 and p2 are twin primes if both are prime and p1 + 2 = p2


Need a function that determines if a candidate number is prime
Iterate over numbers between 2 and the candidate
If any iterated number evenly divides the candidate then the candidate is not prime ==> function returns False
If the loop extends to completion (without returning False) return True

'''

def is_prime(candidate):
    for num in range(2, candidate):
        if candidate % num == 0:
            return False
        
    return True




'''
Write a function that accepts a single integer param to serve as the upper bound for the 
twin prime table (find twin primes < upper bound)
The function should SAVE AND RETURN the twin primes in an appropriate structure 

Iterate over numbers 2 to upper bound
Inside the loop, add 2 to the loop iterate variable
Check if both numbers are prime -- if so, we have a pair of twins
Add them to the structure
When the loop terminates, return the structure containing the twin primes

'''

def find_twin_primes(upper_bound):
    '''
    twin_primes = []
    for num in range(2, upper_bound):
        second_num = num + 2
        if is_prime(num) and is_prime(second_num):
            twin_primes.append((num, second_num))
    '''
    twin_primes = [(num, num + 2) for num in range(2, upper_bound) if is_prime(num) and is_prime(num + 2)]

    return twin_primes

bound = 1000
twin_primes = find_twin_primes(bound)
for pair in twin_primes:
    print(f'{pair[0]} and {pair[1]} are twin primes')