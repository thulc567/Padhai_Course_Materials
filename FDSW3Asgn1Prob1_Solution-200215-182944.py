#!/usr/bin/env python
# coding: utf-8

# # Assignment 1 problems 1 

# Exercise 1: 
# 
# 
# ---
# 
# 
# 1.   Prompt the user "Enter your weight (in kgs)" and record weight
# 2.   Prompt the user "What is your preferred unit of height? Type "F" for feet and "M" for meters" and record the preference
# 3.   If user says "F" then prompt user "You will enter your height given as feet and inches. First enter feet" and record feet and then prompt user "Now enter inches" and record inches
# 4.   If user says "M" then prompt user "What is your height in meters" and record height in meters
# 5.   If user had chosen "F" then convert height into meters
# 6.   Compute BMI using the following formula $$\mbox{BMI} = \dfrac{\mbox{Weight (in kgs)}}{\mbox{Height }^2\mbox{(in m)}}$$
# 7.   Depending on the value of BMI, report the user's type given by the following table: 
# > *   $\mbox{BMI} < 18.5$: UNDERWEIGHT
# > *   $18.5 \leq \mbox{BMI} < 25$: NORMAL
# > *   $25 \leq \mbox{BMI} < 30$: OVERWEIGHT
# > *   $\mbox{BMI} \geq 30$: VERY-OVERWEIGHT
# 

# # Solution to problem 1

# In[ ]:


weight = input("Enter your weight in kgs ")
height_unit = input('What is your preferred unit of height "F" of feet and "M" for meters ')

if height_unit == "F":
    print("I am in the F block. TODO")
else:
    print("I am in the M block. TODO")


# In[ ]:


weight = input("Enter your weight in kgs ")
height_unit = input('What is your preferred unit of height "F" of feet and "M" for meters ')

if height_unit == "F":
    feet = input("Please enter both feet and inches. Now enter feet ")
    inches = input("Now enter inches ")
else:
    meters = input("Please enter your height in meters ")


# In[ ]:


weight = input("Enter your weight in kgs ")
height_unit = input('What is your preferred unit of height "F" of feet and "M" for meters ')

if height_unit == "F":
    feet = input("Please enter both feet and inches. Now enter feet ")
    inches = input("Now enter inches ")
    meters = (feet + inches/12) * 0.3048
else:
    meters = input("Please enter your height in meters ")

height = meters


# In[ ]:


def input_single_integer(prompt):
    ret = int(input(prompt))
    return ret


# In[ ]:


weight = input("Enter your weight in kgs ")
height_unit = input('What is your preferred unit of height "F" of feet and "M" for meters ')

if height_unit == "F":
    feet = input_single_integer("Please enter both feet and inches. Now enter feet ")
    inches = input_single_integer("Now enter inches ")
    meters = (feet + inches/12) * 0.3048
else:
    meters = input("Please enter your height in meters ")

height = meters


# In[ ]:


print(meters)


# In[ ]:


def input_single_float(prompt):
    ret = float(input(prompt))
    return ret


# In[ ]:


weight = input_single_float("Enter your weight in kgs ")
height_unit = input('What is your preferred unit of height "F" of feet and "M" for meters ')

if height_unit == "F":
    feet = input_single_integer("Please enter both feet and inches. Now enter feet ")
    inches = input_single_integer("Now enter inches ")
    meters = (feet + inches/12) * 0.3048
else:
    meters = input_single_float("Please enter your height in meters ")

height = meters

bmi = weight / height**2

print("Your BMI is", bmi)


# In[ ]:


weight = input_single_float("Enter your weight in kgs ")
height_unit = input('What is your preferred unit of height "F" of feet and "M" for meters ')

if height_unit == "F":
    feet = input_single_integer("Please enter both feet and inches. Now enter feet ")
    inches = input_single_integer("Now enter inches ")
    meters = (feet + inches/12) * 0.3048
else:
    meters = input_single_float("Please enter your height in meters ")

height = meters

bmi = weight / height**2

print("Your BMI is", bmi)

if bmi < 18.5:
    print("You are UNDERWEIGHT. Please consult doctor")
elif bmi < 25:
    print("You are NORMAL. Great going.")
elif bmi < 30:
    print("You are OVERWEIGHT. Watch out.")
else:
    print("You are VERY OVERWEIGHT. Please consult doctor")

