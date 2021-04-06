# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 18:17:49 2020

@author: johne
"""

# 1 ---------------------
# Write a program to prompt the user for temperature in Celsius, convert 
# the temperature to Fahrenheit, and print temperature in Fahrenheit. 

celsius = float(input('Please Enter temperature in Celsius: '))

f = celsius *9/5 + 32
output_string = f'The temperature in Celsius {celsius} converted to Farenheit is {f}.'
print(output_string)

print('hello')