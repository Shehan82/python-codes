x = int(input())
y = int(input())
z = int(input())
n = int(input())
count=-1
large_list=[]
for i in range(x + 1):
    for j in range( y + 1):
        for k in range(z+1):
            if(i+j+k!=n):
                count=count+1
                print(i,j,k)
                print(count)
                #large_list[count].append(i,j,k)
#print(large_list)