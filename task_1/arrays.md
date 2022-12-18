# Arrays

+ [Squares of sorted array](#squares-of-sorted-array)
+ [Merge two sorted arrays](#merge-two-sorted-arrays)

## Squares of sorted array

Возвращение отсортированного массива, состоящего из элементов начального массива, возведенных в квадрат за O(n)

```python
def merge(first, second):
    l,r=0,0
    ans=[]
    while l<len(first) and r<len(second):
        if first[l]<=second[r]:
            ans.append(first[l])
            l+=1
        else:
            ans.append(second[r])
            r+=1           
    while l<len(first):
        ans.append(first[l])
        l+=1
    while r<len(second):
        ans.append(second[r])
        r+=1
    return ans

def squares(s):
    i=0
    while s[i]<0:
        i+=1
    l=[j**2 for j in s[:i]]
    l.reverse()
    r=[j**2 for j in s[i:]]
    return merge(l, r)    
```

## Merge two sorted arrays

```python 
def merge(left, right):
    len_left = len(left)
    len_right = len(right)
    result = [0] * (len_left + len_right)
    pA = pB = pC = 0

    while pA != len_left and pB != len_right:

        if left[pA] <= right[pB]:
            result[pC] = left[pA]
            pC += 1
            pA += 1
        else:
            result[pC] = right[pB]
            pC += 1
            pB += 1

    while pA != len_left:
        result[pC] = left[pA]
        pC += 1
        pA += 1

    while pB != len_right:
        result[pC] = right[pB]
        pC += 1
        pB += 1

    return 
```
