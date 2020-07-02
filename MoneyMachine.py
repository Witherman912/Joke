import random
#Begin
print ("Welcome to Money Printer Program")
print ("How much money do you need?")
Need=int(input(">>") )

#Why you need money printer when you have enough money?
if Need == 0:
	print ("If you dont need money, why you are here?")

#Time to BRRRR	
if Need > 0:
    Brr = random.randint(1, Need)	
    print ("Money print go ")
    while Brr != 0:
    	print ("BRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    	Brr = Brr - 1
    print ("Here is your", Need,"$")
#BTW, BITCOIN and other Cryptocurrency still gg