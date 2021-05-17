# def isPerfect( n ):
#   def checkPerfectNumber(num: int) -> bool:
#        if num == 1:
#            return False
#        div = set([1]) 
#        for i in range(2, int(num**0.5)+1):
#            if (num % i)==0:
#                div.add(i)
#                div.add(num//i)
#        return sum(div) == num
	
#   count = 0
#   for i in range(n):
#     if checkPerfectNumber(i) == True:
#       count += 1
#   return count
  
# print(isPerfect(5))


import math as m

def isPerfect(N):
     
    import math
 
# Function to check
# Log base 2
    def Log2(x):
        if x == 0:
            return False
    
        return (math.log10(x) /
                math.log10(2))
    
    # Function to check
    # if x is power of 2
    def isPowerOfTwo(n):
        return (math.ceil(Log2(n)) ==
                math.floor(Log2(n)))

    count = 1
    for i in range(4,N):
        if isPowerOfTwo(i-1):
            count += 1
    return count


     
    # If sum of divisors is equal to
    # n, then n is a perfect number
     
    return count

print(isPerfect(5))