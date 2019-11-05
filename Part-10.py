arr=[1,1,2,3,2,4]
counter={}
for item in arr:
	if(item in counter):
	  counter.update({item:(int(counter.get(item))+1)})
	else:
	  counter.update({item:1})
	 
for item1 in counter:
	print(str(item1)+"\t"+str(counter.get(item1)))
	

	

