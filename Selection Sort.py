
def Selection_Sort(a):
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a) ):
            if a[min] > a[j]:
                min = j
        a[i],a[min] = a[min],a[i]
    return a


flag = True
print("Enter Numbers you want to Sort")
b = []
while(flag):
        a = input()
        if a == "Over":
            break 
        else :
            b.append(int(a))
a = Selection_Sort(b)
print(a)




