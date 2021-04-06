# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:05:57 2020

@author: johne
"""

def practice_7(no_one_liter_bottles, no_more_than_one_liter_bottles):
    # When you buy soda bottles, you deposit a small amount to encourage recycling. 
    # For one liter bottle the depost is $0.10.
    # For a bottle larger than one liter, the depost is $0.25.
    # Complete this function to print a refund message like follows:
    # The refund is $<amount>.
    # Round the refund to two decimal places. 
    
    # YOUR CODE HERE
    vv1 = float(no_one_liter_bottles)*0.10
    vv2 = float(no_more_than_one_liter_bottles)*0.25
    vsum = vv1 + vv2
    print(f'The refund is $',vsum,'.')
   
    return(practice_7)




def practice_8(a, b):
    # Complete this function to print the following given two numbers a and b
    
    #The sum of <a> and <b> is <result>.
    #The difference when <b> is substracted from <a> is <result>.
    #The product of <a> and <b> is <result>.
    #The quotient when <a> is divided by <b> is <result>.
    #The remainder when <a> is divided by <b> is <result>. 
    #The result of <a>^<b> is <result>. 
    """
    
    """
   # a = 10
   # b = 5
   # The sum of 10 and 5 is 15.
    #The difference when 5 is substracted from 10 is -5.
   # The product of 10 and 5 is 50.
    #The quotient when 10 is divided by 5 is 2.0.
   # The remainder when 10 is divided by 5 is 2.
   # The result of 10^5 is 100000.
    float(a)
    float(b)
    rsum = a + b
    rdif = a - b
    rpro = a * b
    rquo = a/b
    rrem = a%b
    rexp = pow(a,b)
    print(f'The sum of {a} and {b} is {rsum}.''\n'f'The difference when {b} is subtracted from {a} is {rdif}.''\n'f'The product of {a} and {b} is {rpro}.''\n'f'The quotient of when {a} is divided by {b} is {rquo}.''\n'f'The remainder when {a} is divided by {b} is {rrem}.''\n'f'The result of {a}^{b} is {rexp}.')

    return(practice_8)




























def practice_9(P, r, t):
    # The formula for simple interest is A = P(1+rt), where P is
    # the principle amount, r is the annual rate of interest,
    # t is the number of years the amount is invested, and A
    # is the amount at the end of the investment. 
    # Complete this function to print the following message:
    # After <t> years at <r>%, the investment will be worth $<A>.
    # Round the amount to two decimal places. 
    # Hint: rate is a percentage!
    float(P)
    float(r)
    r2 = r/100
    float(t)
    A = P*(1+(r2*t))
    round(A,2)
    print(f'After {t} years at {r}%, the investment will be worth ${A}.')
    return(practice_9)
    ###########################################
    ######################################
    
    
    
    
    
def practice_10(P, r, t, n):
    # The formula for compound interest is 
    # A = P(1 + r/n)^nt
    # where:
    # P is the principle amount.
    # r is the annual rate of interest.
    # t is the number of years the amount is invested. 
    # n is the number of times the interest is compounded per year.
    # A is the amount at the end of the investment. 
    # Complete this function to print the following:
    # $<P> invested at <r>% for <t> years compounded <n> times per year is $<A>.
    float(P)
    float(r)
    float(t)
    float(n)
    vexp = n*t
    r2 = r/100
    A =  P*(1 + (r2/n))**vexp
    print(f'${P} invested at {r}% for {t} years compounded {n} times per year is ${round(A,2)}.')
    return(practice_10)
    
    