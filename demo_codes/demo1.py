t=[1,5,-6,-4]
ans=max(t, key=lambda k:abs(k))
print(ans)

dd = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": -4,
}

def func1(k):
    return abs(dd[k])


func2 = lambda k: abs(dd[k])


r2 = max(dd, key=func2)


print(r2)
