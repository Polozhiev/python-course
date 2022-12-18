# Matrix

+ [Diagonal sum](#diagonal-sum)

## Diagonal sum

Возвращает сумму диагональных элементов

```python

def DiagSum(mat):
    sum=0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end=' ')
            if i==j:
                sum+=mat[i][j]
        print()
    return(sum)     
    
```