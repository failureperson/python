for i in [1,2]:
    print(i)
    for j in [1,2]:
        print(j)
        print(i+j)
    print(i)
print("done looping")

'''
with open('s.txt', "w+") as x:
    x.writelines(" th data is hidden data , data is data")


count =0
with open('s.txt', "r+") as x:
    s =x.read().split()
    for i in s:
        if i == "data":
            count += 1

print(count)


with open('s.txt', "r+") as x:
    s = x.readlines()
    print(s)
'''


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn 
import sklearn
import tensorflow
import keras 
