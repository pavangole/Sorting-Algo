#!/usr/bin/env python
# coding: utf-8

#Simplest sorting algorithm , comparatively swaps the unsorted data
#Space Complexity: O(n)
#Time Complexity : O(n^2)
def Bubble_Sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i -1):
            if a[j] > a [j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
                

b = []
for i in range(int(input())):
        b.append(input()) 
Bubble_Sort(b)





