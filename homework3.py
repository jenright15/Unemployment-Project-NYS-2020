# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:15:03 2020

@author: johne
"""

def is_date_valid(month, day, year):
    # Complete this function to check if a data is valid, given month, day, and year.  
    # For example, 5/24/1962 is valid, but 9/31/2000 is not
    # Inputs: month, day, year
    # Output: True or False (Boolean)
    # Hint: Use is leap year function

    # YOUR CODE HERE
   
    import datetime  
    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False

    if(isValidDate) :
        return True
    else :
        return False
        
        
        
        
        
        

    # Complete this function to calculate the day_number given month, day, and year.
    # Information: The days of the year are often numbered from 1 through 365 (or 366).
    # This number can be computed in three steps using int arithmetic:
    # (a) - day_num = 31 * (month - 1) + day
    # (b) - if the month is after February subtract (4*(month)+23)//10
    # (c) - if it's a leap year and after February 29, add 1
    # Hint: First verify the input date is valid, return False if it is not valid; use is_date_valid
    # Hint: Also use the is_leap function
    # Inputs: month, day, year
    # Output: the day number or False (boolean) if the date is invalid. 

    # YOUR CODE HERE
 
    
 
    
 
    
def years_to_double_investment(apr):
    # Complete this function to use a while loop to determine how long it takes for an investment 
    # to double at a given interest rate. The input to this function, apr, is the annualized interest rate
    # and the output is the number of years it takes an investment to double. Note: The amount of the initial 
    # investment (principal) does not matter; you can use $1. 
    # Hint: principal is the amount of money being invested. 
    # apr is the annual percentage rate expressed as a decimal number.  
    # Relationship: value after one year is given by principal * (1+ apr)

    # YOUR CODE HERE
    principal = 1
    balance = principal 
    year = 0
    while balance < 2*principal:
        balance = balance*(1 + apr)
        year += 1
        
    return(year)
    
def stopping_time(n):
    # Complete this function to return the number of steps taken to reach 1 in
    # the Collatz sequence (https://en.wikipedia.org/wiki/Collatz_conjecture)

    # YOUR CODE HERE
    num_seq = [n]
    if n < 1:
       return []
    while n > 1:
       if n % 2 == 0:
         n = n / 2
       else:
         n = 3 * n + 1
       num_seq.append(n)
    return(len(num_seq) - 1)





##################
def is_prime(n):
    # A positive whole number > 2 is prime if no number between 2 and sqrt(n)
    # (include) evenly divides n. Write a program that accepts a value of n as
    # input and determine if the value is prime. If n is not prime, your program should
    # return False (boolean) as soon as it finds a value that evenly divides n.
    # Hint: if number is 2, return False

    import math
    from math import sqrt 
    
    # YOUR CODE HERE
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
#######################
def all_primes(n):
    plist = []
    for i in range(3, n + 1):
        if is_prime(i):
            plist.append(i)
    return plist

#######
##################
def gcd(m,n):
    # Complete this function to determine the greatest common divisor (GCD). 
    # The GCD of two values can be computed using Euclid's algorithm. Starting with the values
    # m and n, we repeatedly apply the formula: n, m = m, n%m until m is 0. At this point, n is the GCD
    # of the original m and n. 
    # Inputs: m and n which are both natural numbers
    # Output: gcd

    # YOUR CODE HERE
    while n != 0:
        (m, n) = (n, m % n)
    return m
    






def is_magic_date(date):
    # A magic date is a date where the day multiplied by the month is equal 
    # to the two digit year. For example, June 10, 1960 is a magic date because
    # June is the sixth month, and 6 times 10 is 60, which is equal to the two
    # digit year. Complete this function to determine whether or not a date is
    # a magic date.

    # input: date (str -- month/day/year)
    # output: True or False (bool)


    # YOUR CODE HERE
    from datetime import datetime
    my_date = datetime.strptime(date, "%m/%d/%Y")
    month = my_date.month
    day = my_date.day
    year = my_date.year - 1900
    day_month_year = day * month
    if day_month_year == year:
        return True
    else:
        return False
    
def xyz(date):
    from datetime import datetime 
    mdate = datetime.strptime(date,"%m/%d/%Y") 
    year = mdate.year - 1900
    print(year)
    
    
    






def remove_duplicates(words):
    # Complete this function to remove duplicates from the words list using a loop
    # input: words (list)
    # output: a list without duplicates

    # YOUR CODE HERE
    my_list = set(words)
    return(my_list)





def proper_divisors(n):
    # A proper divisor of a positive integer, n, is a positive integer less than n which divides
    # evenly into n. Complete this function to compute all the proper divisors of a positive
    # integer. The integer is passed to this function as the only parameter. The function will
    # return a list of containing all of the proper divisors as its only reult. 
    # input: n (int)
    # output: list

    # YOUR CODE HERE
    lt = []
    i = 1
    while i <= n:
        if (n % i == 0):
                lt.append(i)
        i = i + 1
    return (lt)




def isPerfect(n): 
      
    # To store sum of divisors 
    sum = 1
      
    # Find all divisors and add them 
    i = 2
    while i * i <= n: 
        if n % i == 0: 
            sum = sum + i + n/i 
        i += 1
      
    # If sum of divisors is equal to 
    # n, then n is a perfect number 
    if sum == n and n!=1:
        return True
    else:
        return False
    
    
    
    
def best_line(points):
    import statistics
    X = []
    Y = []
    for coord in points:
        X.append(coord[0])
        Y.append(coord[1])
    meany = statistics.mean(Y)
    meanz = statistics.mean(X)
    sumx = 0
    sumy = 0
    for x,y in points:
        sumx = sumx + (x-meanz) * (y-meany)
        sumy = sumy + (x-meanz) * (x-meanz)
    z = sumx / sumy
    b = meany - z * meanz
    z = round(z,2)
    b = round(b,2)
    return(z,b)
        
from datetime import datetime
day_of_year = datetime.now().timetuple().tm_yday
print(day_of_year)        