def highest_even(li):
    highest = 0
    for i in range(len(li)):
        if (li[i]%2 == 0):
            if (li[i] > highest):
                highest = li[i]
    return highest

print(highest_even([4,2,8,29,20,35,34,12]))