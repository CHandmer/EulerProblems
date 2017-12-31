######################

# Question source: https://projecteuler.net/problem=1

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

######################

# There are two obvious ways to solve this problem. One is to list all the multiples of 3 or 5 and add them, the other is to add all the multiples of 3 and 5 then subtract the multiples of 15. Since this is coding oriented, let's do it the coding way.

# This function creates a list and sets all numbers that aren't multiples of 3 or 5 to zero, then performs the sum.

N=1000

print(sum([i if i%3==0 or i%5==0 else 0 for i in range(N)]))

# A more explicit way of doing this would be

total=0
for i in range(N):
    # exclude the non multiples, then perform progressive sum in place
    if i%3==0 or i%5==0:
        total +=i 
print(total)

