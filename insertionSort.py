# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 22:02:55 2018

@author: MarcAngelo
"""

def insertionSort(arr):
    print(arr)
    #for each element
    for i in range (len(arr)):
        print('--------------')
        print('current element:' , arr[i])
        #look at element j after it
        j = i
        #keep comparing element j to j--
        while (j > 0 and arr[j] < arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            print('new array: ', arr)
            j-=1;
        #if j < j-1, swap
        
my_arr = [10, 9, 8, 5, 6]
insertionSort(my_arr)

    
