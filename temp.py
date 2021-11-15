# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
sales =int(input("Total Sales"))
if (sales < 3000): print("You only get 10% commision!")

elif (sales < 7000): print("You only get 15% commision! and 500 bonus")

elif(sales<10000):print("You only get commision of 15% and no bonus!")
elif(sales>10000):print("commision of 25% and 1000 bonus")