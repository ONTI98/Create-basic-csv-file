#Programme asks for user input
#uses loops for different parts
#one part-for loop,another while loop
#while the user has not entered a certain word, it will keep prompting for a name
#this loop will stop when the original condition is no longer true
#the names included in the while loop will be added to a list
#the list will then be arranged in alphabetical order

#create empty list and declare variables
guests=[]
names=""
answer= ""

#for user-friendliness
print("Please enter names when asked to add name.To stop adding ,type 'stop'\n ")

#while loop
while names.upper() != "STOP".upper():
    names=input("Add name of guest: ")
    guests.append(names)

#for  loop. I used this to print the list once,hence the range argument
for name in range (1):
    print(guests)
    answer=input("Would you like to rearrange in alphabetical order? y/n: " )

#conditional statemement. If answer is Y(yes)
    if answer.upper() == "Y".upper():
        guests.sort()
        print(guests)
    else:
        break
#since 'stop' keeps appearing in the list.Let us simply remove it
guests.remove("stop")
print(guests)





  


