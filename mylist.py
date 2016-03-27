'''
Created on Feb 21, 2013

@author: Fig Newton
'''
'''
Created on Feb 16, 2013

@author: Your Name
'''

def match_ends(words):
    count = 0
    for p in range(0,len(words)):
        word = words[p]
        if(word is not ''):
            last = word[-1]
        if(len(word) >= 2):
            if(word[0] == last):
                count += 1
    return count

def front_x(words):
    listx = []
    listsort = []
    p = 0
    while(p < len(words)):
        tester = words[p]
        if(tester[0]=='x'):
            listx.append(words[p])
            p += 1
        else:
            listsort.append(words[p])   
            p += 1 
    listx.sort()
    listsort.sort()
    final = (listx + listsort)
    return(final)    

def get_Last(t):
    return t[-1]

def sort_last(tuples):
    
    return sorted(tuples,key=get_Last)

def remove_adjacent(nums):
    numList = nums
    p = 0
    while(p < (len(nums)-1)):
        if(numList[p] == numList[p-1]):
                numList.remove(nums[p-1])
                p = 0
        elif(numList[p] < (len(nums))+1):
            if(numList[p] == numList[p+1]):
                numList.remove(nums[p+1])
                p = 0
        p += 1         
    return numList    

#def check(cellBlock):
    #if(nums[p] == nums[p-1]):
    #nums[p] == nums[p+1]
def linear_merge(list1, list2):
    orderedList = []
    p = 0
    k = 0
    total = (len(list1) + len(list2))
    """
    while (len(orderedList) < total):
       
        if(p == len(list1)):
            orderedList.extend(list2[k:])
        if(k == len(list2)):
            orderedList.extend(list1[p:]) 
                     
        if(list1[p] <= list2[k]):
            orderedList.append(list1[p])
            if(p < (len(list1))):
                p += 1
        if(list2[k] <= list1[p]):
            orderedList.append(list2[k])
            if(k < (len(list2))):
                k += 1
        
            
    return orderedList    
"""
   
    while len(orderedList) != total:
        if len(list1) == p:
            orderedList += list2[k:]
            break
        elif len(list2) == k:
            orderedList += list1[p:]
            break
        elif list1[p] < list2[k]:
            orderedList.append(list1[p])
            p += 1
        else:
            orderedList.append(list2[k])
            k += 1
    return orderedList
 
