# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 20:29:39 2016
Calculate the number times each character occurs in the given string s.
@author: ceciliaLee
"""

s = """
Write a program that prints the numbers from 1 to 100.
But for multiples of three print 'Fizz' instead of the number and f
or the multiples of five print 'Buzz'. For numbers which are
multiples of both three and five print 'FizzBuzz'
"""

# Approach 1
print s.lower().count('a')

# Approach 2
counter1 = {}
for _ in s.lower():
    counter1[_] = counter1.get(_, 0) + 1
print counter1['a']

# Approach 3
from collections import defaultdict
counter2 = defaultdict(int)
for _ in s.lower():
    counter2[_] += 1
print counter2['a']

# Approach 4
from collections import Counter
counter3 = Counter(s.lower())
print counter3['a']