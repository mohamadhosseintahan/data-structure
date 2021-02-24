l = [1,2,4,1,2,5,23,756,43,674,23,7,137,1,123]
def merge(l):
    if len(l)<2:
        return l
        

    mid = len(l) // 2
    a = l[:mid]
    b = l[mid:]
    # print(f'a is{a}' , f'b is {b}')
    a = merge(a)
    b = merge(b)

    i = j = 0
    
    l = []
    # print(l)
    while i < len(a) and j<len(b):
        if a[i] <= b[j]:
            l += [a[i]]
            i += 1
        else:
            l += [b[j]]
            j += 1
    l += a[i:] + b[j:]
    return l
merge(l)
print(merge(l))