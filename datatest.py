import random
import time



def unique(arr):
    unique_elements = []
    for x in arr:
        if x not in unique_elements:
            unique_elements.append(x)
    return len(unique_elements)

def maxBiValue(A):
    subArrays = [A[i:i+j]
                 for i in range(0, len(A)) for j in range(1, len(A)-i+1)]
    maxBiValueSubArray = []
    for subArray in subArrays:
        if unique(subArray) == 1 or unique(subArray) == 2:
            if len(subArray) > len(maxBiValueSubArray):
                maxBiValueSubArray = subArray
    return maxBiValueSubArray


def nonNegativeSum(A):
    subArrays = [A[i:i+j]
                 for i in range(0, len(A)) for j in range(1, len(A)-i+1)]
    newSubArrays = []
    maxSum= 0
    for s in subArrays:
        if not any(n < 0 for n in s):
            newSubArrays.append(s)
    if newSubArrays == []:
        return -1
    for s in newSubArrays:
        m = sum(s)
        if m > maxSum:
            maxSum = m
    print(maxSum)
            

# print(maxBiValue(A))
B = [1,2,-3,4,5,-6]
B1 = [-8, 3,0,5,-3,12]
B2 = [-1,2, 1 ,2,0,2,1,-3,4,3,0,-1]
B3 = [-1,-2,-4]
# nonNegativeSum(B)  
# nonNegativeSum(B3)


# L = range(1000)
# while(1):
#     amount = 100
#     print(maxBiValue([random.choice(L) for _ in range(amount)]))
# [31, 91, 52, 18, 92, 17, 70, 97, 17, 56]
        
def maxSubArrayNonNegative(A):
    maxSum = 0
    current_max = 0
    noNonNegatives = True
    for i in A:
        if i < 0:
            current_max = 0
        else:
            noNonNegatives = False
            current_max += i
        if current_max > maxSum:
            maxSum = current_max
    if noNonNegatives:
        return -1
    return maxSum

nums = [-2,1,-3,7,-2,2,1,-5,4]

A = [4, 2, 2, 4, 2]
A1 = [1, 2, 3, 2]
A2 = [0, 5, 4, 4, 5, 12]
A3 = [4, 4]

def maxSubArrayBiValued(A):
    maxSum = 0
    current_max = 0
    
    
    unique_vals = [A[0], A[1]]
    maxLen = 0
    currLen = 0
    subArrays = []
    tmp = []
    for index, i in enumerate(A):
        if i in unique_vals:
            tmp.append(i)
            currLen += 1
        else:
            subArrays.append(tmp)
            tmp = []
            tmp.append(i)
            unique_vals = [i, A[index+1]]
            
        if i < 0:
            current_max = 0
        else:
            noNonNegatives = False
            current_max += i
        if current_max > maxSum:
            maxSum = current_max
    if noNonNegatives:
        return -1
    return maxSum


print(maxSubArrayNonNegative(B3))      
                    
    


def nonNegativeSum(A):
    subArrays = [A[i:i+j]
                 for i in range(0, len(A)) for j in range(1, len(A)-i+1)]

    maxSum = sum(subArrays[0])
    maxArr = subArrays[0]
    print(subArrays)
    for s in subArrays:
        m = sum(s)
        if m >= 0:
            if len(s) > len(maxArr):
                maxArr = s
                print("max ", maxArr)
    print(maxSum)
    return len(maxArr)


# print(nonNegativeSum([-1, -1, 1, -1, 1, 0, 1, -1, -1]))
