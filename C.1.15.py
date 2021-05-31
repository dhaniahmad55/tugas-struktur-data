def has_distinct_elements(data):
    s = set(data)
    if len(data) != len(s):
        return False
    else:
        return True

def has_distinct_elements_1(data):
    s=[]
    for d in data:
        if d in s:
            return False
        else:
            s.append(d)
    return True

print(has_distinct_elements([4,5,6,7,8,10,13,14]))
print(has_distinct_elements_1([3,4,5,6,7,8,9,10]))