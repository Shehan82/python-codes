import array
print("Enter 5 numbers")
arr=array.array("i",[])
for i in range(0,5):
    x=int(input())
    arr.append(x)
for i in range(0,len(arr)):
    print(arr[i],end=' ')

list=[1,2,3,4]
for i in range(len(list)):
    print(list[i])
print("shehan")