# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 23:04:14 2018

@author: MarcAngelo
"""

import numpy as np

def merge_sort(array):
    if (len(array)>=2):
        iM = len(array)//2
        
        left = array[:iM].copy()
        right = array[iM:].copy()
        
        merge_sort(left)
        merge_sort(right)
        
        iA = 0
        iB = 0
        iC = 0
        
        while(iA<len(left) and iB<len(right)):
            if left[iA]<right[iB]:
                array[iC]=left[iA]
                iA+=1
            else:
                array[iC]=right[iB]
                iB+=1
            iC+=1
            
        while(iA<len(left)):
            array[iC]=left[iA]
            iA+=1
            iC+=1
            
        while(iB<len(right)):
            array[iC]=right[iB]
            iB+=1
            iC+=1

ar_size = 20
ar = np.random.randint(10, size=ar_size)
ar = np.arange(ar_size)
np.random.shuffle(ar)

myArr = [10, 6, 2, 5, 7, 9]
print(ar)
merge_sort(ar)
print(ar)  