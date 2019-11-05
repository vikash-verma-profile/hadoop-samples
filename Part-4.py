def calculate(choice):
	Number1=int(input("enter number 1:"))
	Number2=int(input("enter number 2:"))
	if(choice==1):
		print(Number1+Number2)
	if(choice==2):
		print(Number1-Number2)	
			
	
	
if __name__== "__main__":
	msg = ''
	while msg != 'quit':     
		msg = input("Please enter your choice \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n enter quit for quit \n") 
		if(msg!="quit"):
			calculate(msg)	
		
		
		