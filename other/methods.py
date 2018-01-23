# << Swami Shreeji >>
# Below is a group of functions implemented for some
#  purpose a while back

print "heloo world"
helo = [2, 8, 16, 5]

# Filter out dups 
def deduplicate(input):
    noDups = []
    for item in input:
        if item in noDups:
            continue
        else:
            noDups.append(item)
    return noDups


# Find the greatest and least differences
def difference(input):
    preResult = sorted(input)
    result = []
    leastDiff = preResult[-1] - preResult[0]
    greatestDiff = preResult[2] - preResult[1]
    
    result.append(greatestDiff)
    result.append(leastDiff)
    return result


# Print every third word from the list
def third( input):
    preResult = input.split()
    result = []
    i = 2
    while (i < len(preResult)):
        result.append(preResult[i])
        i += 3
        
    return result

