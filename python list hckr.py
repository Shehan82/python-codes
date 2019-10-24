x = int(input())
y = int(input())
z = int(input())
n = int(input())
count=0
large_list=[]
for i in range(x + 1):
    for j in range( y + 1):
        for k in range(z+1):
            if(i+j+k!=n):
                large_list.append([i,j,k])
print(large_list)