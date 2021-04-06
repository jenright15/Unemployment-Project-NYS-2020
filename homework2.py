# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:21:06 2020

@author: johne
"""

# Exercise 1
def total_wages_for_the_week(hours, wage):
    # Many companies pay time-and-a-half for any hours worked above 40 in a given week.
    # Complete this function whose inputs are hours worked (hours) and the hourly rate (wage) to
    # calculate the total wages for the week. 
    # YOUR CODE HERE
    weekwage = hours * wage
    timehalf = wage * 1.5
    timedwage =((hours - 40) * timehalf) + (40*wage)
    if hours >40:
        return(timedwage)
        
    elif hours <= 40:
        return(weekwage)
    
    

# Exercise 2
def convert_quiz_score_to_letter_grade(score):
    # A certain CS professor gives five-point quizzes that are graded on the scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F.
    # Complete this function which accepts a quiz score as an input and uses a decision structure to calculate the corresponding
    # grade. 
    # YOUR CODE HERE
    
    if score == 5:
       grade = 'A'
    elif score == 4:
        grade = 'B'
    elif score == 3:
        grade = 'C'
    elif score == 2:
        grade = 'D'
    elif score <=1:
        grade = 'F'
        
    return(grade)



# Exercise 3 
def convert_exam_score_to_letter_grade(score):
    # A certain CS professor gives 100-point exams that are graded on the scale 90-100: A, 80-89: B, 70-79: C,
    # 69-69: D, < 60: F. Complete this function which accepts an exam score as input and uses a decision structure 
    # to calculate the corresponding grade. 
    # YOUR CODE HERE
    if score >= 90:
        grade = 'A'
    elif score >=80:
        grade = 'B'
    elif score >=70:
        grade = 'C'

    elif score >=60:
        grade = 'D'
    elif score <60:
        grade = 'F'
    return(grade)




def calculate_class_standing_from_credits(credits):
    # A certain college classifies students according to credits earned. A student with less than 7 credits is a Freshman.
    # At least 7 credits are required to be a Sophomore, 16 to be a Junior and 26 to be classifed as Senior. 
    # Complete this function which calculates the class standing from the number of credits earned. 
    # YOUR CODE HERE
    if credits >= 26:
        return('Senior')
    elif credits >= 16:
        return('Junior')
    elif credits >= 7:
        return('Sophmore')
    elif credits < 7:
        return('Freshman')
    
def is_palindrome(input_string):
    # Complete this function which determines if the input_string is a palindrome. Return True or False
    # Use square brackets to reverse the input_string! Make sure to lower the input string before testing!
    
    # YOUR CODE HERE
    if input_string.lower() == input_string.lower()[::-1]:
        return(True)
    else:
        return(False)    
        
        
        