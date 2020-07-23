'''
Input: an integer
Returns: an integer

# if n == 10: 274 possible ways
# if n == 9: 149 possible ways
# if n == 8: 81 possible ways
# if n == 7: 44 possible ways
# if n == 6: 24 possible ways
# if n == 5: 13 possible ways
# if n == 4: 7 possible ways
# if n == 3: 4 possible ways
# if n == 2: 2 possible ways
# if n == 1: 1 possible way

'''
def eating_cookies(n, cache=None):
    # Your code here
    # receives number of cookies (n)
    # can eat up to 3 cookies at once
    
    if n < 0:
        return 0

    if n == 1 or n == 0:
        return 1

    if cache and cache[n]:
        print(f'from cache {n}')
        return cache[n]
    elif not cache:
        cache = [0 for i in range(n+1)]

    print(f'computing {n}')
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        
    return cache[n]
    
    
    # return number of possible ways to eat all the cookies

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 30

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
