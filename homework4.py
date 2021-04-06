# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:28:40 2020

@author: johne
"""

def list_comp1(lst):
    # Complete this function to use list comprehension to return all values from `lst`
    # that are a multiple of 3 or 4. Just complete the list comprehension below.
    # input: `lst` of numbers
    # output: a list of numbers
    
    # complete the following line!
#     return [for ele in lst] #complete this line!
    
    # YOUR CODE HERE
    output_list = []
    for ele in lst:
        if ele % 3 == 0:
            output_list.append(ele)
        elif ele % 4 == 0:
            output_list.append(ele)
    return output_list

def list_comp2(lst):
    # Complete this function to use list comprehension to multiple all numbers
    # in the list by 3 if it is even or 5 if its odd
    # input: `lst` of numbers
    # output: a list of numbers

    # complete the following line!
#     return [for ele in lst] #complete this line!
   
    
    # YOUR CODE HERE
    list_2 = []
    for ele in lst:
        if ele % 2 == 0:
            ele = ele * 3
            list_2.append(ele)
        else:
            ele = ele * 5
            list_2.append(ele)
    return(list_2)  
    
  
