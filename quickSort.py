# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:04:25 2018

@author: MarcAngelo
"""

import time
import random
#sortedArr=[]
#use array.append(pivot) for this
#print(arr)
def quickSort(arr, low, high):
    if (low + 7 < high):
        pivot_pointer = partition(arr, low, high)
        quickSort(arr, low, pivot_pointer)
        quickSort(arr, pivot_pointer + 1, high)
    else:
        insertionSort(arr, low, high)

def insertionSort(arr, low, high):
    #print(arr)
    #for each element
    for i in range (low, high):
       # print('--------------')
        #print('current element:' , arr[i])
        #look at element j after it
        j = i
        #keep comparing element j to j--
        while (j > low and arr[j] < arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            #print('new array: ', arr)
            j-=1;
        #if j < j-1, swap
        
def partition(arr, low, high):
    pivot = arr[low]
    border_pointer = low 
    
    for i in range(low + 1, high):
        #print('-----------')
        #print(arr)
        #print('border: ', arr[border_pointer])
        #print(arr[i] , ' < ' , pivot , '?')
        
        if (arr[i] < pivot):
            #print('SWAP!')
            arr[i], arr[border_pointer+1]  = arr[border_pointer+1], arr[i]
            border_pointer += 1
            #print('new array: ', arr)
    
    #print('fwei', pivot, arr[border_pointer])
    #arr[low] = pivot
    #pivot, arr[border_pointer] = arr[border_pointer], pivot
    arr[low], arr[border_pointer] = arr[border_pointer], arr[low]
    #print('swap pivot w/ border: ', arr)
    #print('index of border: ', border_pointer)
    return border_pointer        

def main():
#    arr = [20, 90, 2, 15, 68, 22]
    arr=random.sample(range(10), 10)
    print(arr)
    start_time = time.clock()
    quickSort(arr, 0, len(arr))
    print(arr)
    print (time.clock() - start_time, "seconds")
   
    
if __name__ == '__main__':
    main()
    
'''def partition(arr, low, high):
    print(arr)
    mid = len(arr)//2
    pivot = arr[mid]
#    leftside=arr[:mid]
#    rightside=arr[mid+1:]
    for x in arr[:mid]:
        if pivot<=x:
            arr[mid+1:].append(x)
            arr[:mid].remove(x)
    
    for x in arr[mid+1:]:
        if pivot >=x:
            arr[:mid].append(x)
            arr[mid+1:].remove(x)
            
    print('left-', arr[:mid])
    print('pivot-', pivot)
    print('right-', arr[mid+1:])
    print(arr)
    '''

'''for i in range(high):
        print('------------------------------')
        print(i , 'th iteration:')
        print('comparing ', arr[i], pivot)
        if arr[i] < pivot:
            print('yes, they need swap')
            #print('swap ' , arr[i], ' and ' , pivot)
            arr[i], increment=increment, arr[i]
            print('array with swapped: ', arr)
            left_side += 1
        pivot, increment = increment, pivot
    return left_side
    '''
    
''' mid = len(arr)//2
    pivot = arr[mid]
    leftside=arr[:mid]
    rightside=arr[mid+1:]

    while x in leftside:
        if x>=pivot:
                 
    print('left-', leftside)
    print('pivot-', pivot)
    print('right-', rightside)
    print(arr)'''
    
    
'''    for x in leftside:
        if pivot<=x:
            x[pivot:].append(x)
            leftside.remove(x)
            if pivot>=x:
                break
    
    for x in rightside:
        if pivot >=x:
            leftside.append(x)
            rightside.remove(x)
            '''
    
#    for i in range():