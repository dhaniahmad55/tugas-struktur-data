def minmax(data):
    smallest = largest = data[0]
    for entry in data:
        if smallest > entry:
            smallest = entry
        if largest < entry:
            largest = entry
    return (smallest, largest)


print(minmax([0,13,30,7,14,70,80,40,-1,60,4,-7,33,3,-3,-30]))