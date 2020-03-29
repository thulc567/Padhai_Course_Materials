#!/usr/bin/env python
# coding: utf-8

# # Printing basic types

# In[ ]:


print("Hello World!") 


# In[ ]:


print("Hello World!")
print("Namaskar from PadhAI")


# In[ ]:


print("PadhAI")
print("Padh" + "AI")


# In[ ]:


print(1729)


# In[ ]:


print(1000 + 729)  # Check this with Ramanujan's entry


# In[ ]:


print(55/34)   # check golden ratio


# In[ ]:


print(1.618)


# In[ ]:


print(True)


# In[ ]:


print(False)


# In[ ]:


print(True or False)


# In[ ]:


print(True and False)


# # Variables and inputs

# In[ ]:


school = "PadhAI"


# In[ ]:


print(school)


# In[ ]:


print(type(school))


# In[ ]:


print(id(school))


# In[ ]:


another_school = "PadhAI"


# In[ ]:


print(another_school)


# In[ ]:


print(id(another_school))


# In[ ]:


another_school = "IIT Madras"


# In[ ]:


print(id(another_school))


# In[ ]:


print("I am studying at " + school)


# In[ ]:


r_no = 1729


# In[ ]:


print(type(r_no))


# In[ ]:


golden_ratio = 55/34


# In[ ]:


print(type(golden_ratio))


# In[ ]:


is_good = True


# In[ ]:


print(type(is_good))


# In[ ]:


my_name = input("What is your name ")


# In[ ]:


print(my_name, type(my_name))


# In[ ]:


print(my_name + " is studying at " + school)


# In[ ]:


hours_per_day = input("How many hours per day do you study ")


# In[ ]:


print(my_name + " studies for " + hours_per_day + " hours")


# In[ ]:


hours_per_week = hours_per_day * 7


# In[ ]:


print(my_name + " studies for " + hours_per_week + " hours")


# In[ ]:


print(type(hours_per_day))


# In[ ]:


hours_per_day_int = float(hours_per_day)


# In[ ]:


print(hours_per_day_int, type(hours_per_day_int))


# In[ ]:


hours_per_week = hours_per_day_int * 7


# In[ ]:


print(my_name + " studies for " + hours_per_week + " hours")


# In[ ]:


print(my_name + " studies for " + str(hours_per_week) + " hours")


# # String Processing

# In[ ]:


topic = "Foundations of Data Science"


# In[ ]:


print(topic)


# In[ ]:


print(topic[0])


# In[ ]:


print(topic[1])


# In[ ]:


print(topic[10])


# In[ ]:


print(topic[-1])


# In[ ]:


print(topic[-2])


# In[ ]:


print(topic[0:10])


# In[ ]:


print(topic[12:16])


# In[ ]:


print(topic.lower())


# In[ ]:


print(topic)


# In[ ]:


topic = topic.lower()


# In[ ]:


print(topic.upper())


# In[ ]:


print(topic.islower())


# In[ ]:


topic = topic.upper()


# In[ ]:


print(topic.islower())


# In[ ]:


print(topic.isupper())


# In[ ]:


print(topic.find("DATA"))


# In[ ]:


print(topic[15])


# In[ ]:


print(topic.find("AI"))


# In[ ]:


print(topic.replace("SCIENCE", "ENGINEERING"))


# In[ ]:


print(55/34)


# In[ ]:


golden_ratio = 55/34


# In[ ]:


print(type(golden_ratio))


# In[ ]:


print(golden_ratio.is_integer())


# In[ ]:


print(golden_ratio.as_integer_ratio())


# In[ ]:


print(3642617345667313/2251799813685248)


# In[ ]:


print(55 // 34, 55/34)


# In[ ]:


print(55 % 34)


# In[ ]:


print(2 ** 3)


# # If, For, While Blocks

# In[ ]:


hours_per_week = 5


# In[ ]:


if hours_per_week > 10:
    print(my_name + " you are doing well")


# In[ ]:


if hours_per_week > 10:
    print(my_name + " you are doing well")
print("Outside If")


# In[ ]:


if hours_per_week > 10:
    print(my_name + " you are doing well")
else:
    print(my_name + " you need to study more")


# In[ ]:


for i in range(5):
    print(i)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'range')


# In[ ]:


for i in range(2, 5):
    print(i, i**2)


# In[ ]:


a = 1
b = 1
print(a)
print(b)
for i in range(10):
    temp = a + b
    a = b
    b = temp
    print(temp)


# In[ ]:


a = 1
b = 1
print(a)
print(b)
i = 2
while b < 1729:
    temp = a + b
    i += 1
    a = b
    b = temp
    print(temp)
print("Printed", i, "numbers")


# # Functions

# In[ ]:


def fibonacci(pos):
    a = 1
    b = 1
    for i in range(pos):
        temp = a + b
        a = b
        b = temp
    return temp


# In[ ]:


print(fibonacci(3))


# In[ ]:


print(fibonacci(8), fibonacci(7))


# In[ ]:


for i in range(2, 20):
    ratio = fibonacci(i) / fibonacci(i - 1)
    print(i, ratio)


# In[ ]:


def fibonacci_relative(pos, a, b):
    for i in range(pos):
        temp = a + b
        a = b
        b = temp
    return temp


# In[ ]:


print(fibonacci_relative(3, 34, 55))


# In[ ]:


def fibonacci_ol(pos, a = 1, b = 1):
    for i in range(pos):
        temp = a + b
        a = b
        b = temp
    return temp


# In[ ]:


print(fibonacci_ol(3, 34, 55))


# In[ ]:


print(fibonacci_relative(3))


# In[ ]:


def fibonacci_recursive(n, a = 1, b = 1):
    if n > 1:
        return fibonacci_recursive(n - 1, b, a + b)
    else:
        return a + b


# In[ ]:


print(fibonacci_recursive(3, 34, 55))


# In[ ]:


def fibonacci(pos):
    a = 1
    b = 1
    for i in range(pos):
        temp = a + b
        a = b
        b = temp
    return temp


# In[ ]:


print(fibonacci(3))


# In[ ]:


print(fibonacci(8), fibonacci(7))


# In[ ]:


for i in range(2, 20):
    ratio = fibonacci(i) / fibonacci(i - 1)
    print(i, ratio)


# In[ ]:


def fibonacci_relative(pos, a, b):
    for i in range(pos):
        temp = a + b
        a = b
        b = temp
    return temp


# In[ ]:


print(fibonacci_relative(3, 34, 55))


# In[ ]:


def fibonacci_ol(pos, a = 1, b = 1):
    for i in range(pos):
        temp = a + b
        a = b
        b = temp
    return temp


# In[ ]:


print(fibonacci_ol(3, 34, 55))


# In[ ]:


print(fibonacci_relative(3))


# In[ ]:


def fibonacci_recursive(n, a = 1, b = 1):
    if n > 1:
        return fibonacci_recursive(n - 1, b, a + b)
    else:
        return a + b


# In[ ]:


print(fibonacci_recursive(3, 34, 55))

