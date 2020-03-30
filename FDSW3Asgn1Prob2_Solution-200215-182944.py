#!/usr/bin/env python
# coding: utf-8

# # Assignment 1 Problem 2 

# Exercise 2
# 
# ---
# 
# 1.   Write an iterative function to compute the factorial of a natural number
# 2.   Write a recursive function to compute the factorial of a natural number.
# 3.   Write a function to compute $\frac{x^n}{n!}$ given a float $x$ and natural number $n$ as arguments
# 4.   Write a function to iteratively sum up the value $\frac{x^n}{n!}$ from $n = 1$ to a given $N$ for a given $x$, i.e., 
# $$ F(x, N) = 1 + \sum_{i = 1}^N \dfrac{x^n}{n!}$$
# 5.   Write a function to iteratively sum up the value $\frac{x^n}{n!}$ from $n = 1$ to a chosen value of $N'$ such that $$F(x, N') - F(x, N' - 1) < \epsilon$$ for given real number $x$ and positive small number $\epsilon$
# 6.   Choose two real numbers $p$ and $q$ and compute the following two values
# $$ v_1 = F(p, 100) * F(q, 100) $$
# $$ v_2 = F(p + q, 100) $$
# Compute the difference $v_1 - v_2$ and comment on what you see.

# # Solution to Problem 2

# In[ ]:


def factorial(n):
    product = 1
    for i in range(n):
        # print(i, product)
        product *= (i + 1)
    return product


# In[2]:


print(factorial(3))


# In[ ]:


def factorial_recursive(n):
    if n > 1:
        return n * factorial_recursive(n - 1)
    else:
        return 1


# In[4]:


print(factorial_recursive(3))


# In[ ]:


def compute_ratio(x, n):
    ratio = x**n / factorial(n)
    return ratio


# In[6]:


compute_ratio(2, 3)


# In[ ]:


def compute_sum(x, N):
    sum = 1
    for i in range(N):
        sum += compute_ratio(x, i + 1)
    return sum


# In[8]:


print(compute_sum(2, 3))


# In[ ]:


def compute_sum_epsilon(x, epsilon):
    sum = 1
    var = epsilon
    i = 1
    while var >= epsilon:
        var = compute_ratio(x, i)
        sum += var
        i += 1
    return sum


# In[10]:


print(compute_sum_epsilon(2, 0.01))


# In[11]:


print(compute_sum(2, 100))


# In[ ]:


def compute_sum_epsilon(x, epsilon):
    sum = 1
    i = 1
    while True: 
        var = compute_ratio(x, i)
        sum += var
        i += 1
        if var < epsilon:
            break
    return sum


# In[13]:


print(compute_sum_epsilon(2, 0.01))


# In[14]:


p = -1.5
q = 7.1

v1 = compute_sum(p, 100) * compute_sum(q, 100)
v2 = compute_sum(p + q, 100)

print(v1, v2, v2 - v1)


# In[15]:


for i in range(10):
    print(i, compute_sum(i, 100))


# In[ ]:




