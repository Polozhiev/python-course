# Arrays

+ [Compress string](#compress-string)

## Compress string

Возвращение сжатую строку.
["a","b","b","c","c","c"] -> "ab2c3"

```python

def compress(chrs):  
    res = ""
    i, j = 0, 0
    while i < len(chrs):
        count=0
        while j < len(chrs) and chrs[i] == chrs[j]:
            count+=1
            j+=1
        if count==1:
            res=res+chrs[i]
        else:        
            res = res+chrs[i]+str(count)
        i+=count
    return res
```
