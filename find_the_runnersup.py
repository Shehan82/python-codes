n = int(input())
arr = list(map(int, input().split()))
max=arr[0]
for i in range(1,n):
    if(arr[i]>max):
        max=arr[i]

arr.remove(max)

for j in range(len(arr)):
    if(max==arr[j]):
        arr.remove(arr[j])
        arr.insert(j,0)

max2=arr[0]
for k in range(len(arr)):
    if(arr[k]>max2):
        max2=arr[k]
print(max2)

