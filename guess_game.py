fav="banana"
guess=""
count=0
while guess!=fav and count<4:
	guess=input("Enter my favourite fruit:")
	if(count<4 and guess==fav):
	    print("you win bladdy fucker!!")
	count=count+1
if(count>=5):
   print("you lose! your attempts is over idiot!")