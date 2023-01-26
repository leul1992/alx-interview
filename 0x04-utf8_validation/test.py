j = 0
arr = [1,2,3,4,5]
for i in range(len(arr)):
    if j > len(arr):
        break
    if arr[j] == 3:
        j += 1
    print(arr[j], end=',')
    j+=1