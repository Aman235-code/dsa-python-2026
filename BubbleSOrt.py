def bubbleSort(a):
    n = len(a)

    for i in range(n):
        for j in range(0, n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

a = [64,32,25,15,45,40,51,2]
bubbleSort(a)
print(a)