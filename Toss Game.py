import random
option=('head','tail')
userchoice=str(input("Choose Head or Tail:"))
computerchoice=random.choice(option)
print("Userchoice is:",userchoice)
print("Computerchoice:",computerchoice)

if(userchoice==computerchoice):
    print("You won the toss!")
else:
    print("You lose the toss!")