#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
a = random.randint(1,9)
print ("random integer generated")
found = True
n = 1
while found == True:
  x = input("please guess a number between 1 and 9 (or enter exit to end game) ---- ")
  y = "ajsd"
  if y == "exit":
    break
  else:
    x = int(x)
    z = x - a
  if z > 0 :
    print("too high")
    n+=1
  elif z < 0 :
    print("too low")
    n+=1
  elif z == 0:
    print("Exactly RIGHT, GJ")
    found = False
  elif z == "exit":
    found = False
  else:
    print ("please enter only whole numbers")

print(n)

if y != "exit":
  if n == 1:
    print ("You took " + str(n) + " try")
  else:
    print ("You took " + str(n) + " tries")



