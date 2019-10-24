list=[]
x = int(input())
word1 = "insert"
word2 = "remove"
word3 = "append"
word4 = "pop"
word5 = "reverse"
word6 = "sort"
word7 = "print"
for i in range(x):
    y = input().split()
    if(y[0]==word1):
        list.insert(int(y[1]), int(y[2]))
    elif(y[0]==word2):
        list.remove(int(y[1]))
    elif(y[0]==word3):
        list.append(int(y[1]))
    elif (y[0] == word5):
        list.reverse()
    elif (y[0] == word6):
        list.sort()
    elif (y[0] == word4):
        list.pop()
    elif (y[0] == word7):
        print(list)