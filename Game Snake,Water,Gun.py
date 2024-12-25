import random
print("!!!!!WELCOME TO SNAKE,WATER,GUN GAME!!!C")
print("you want play online with friends press (F) otherwise press (C) for computer")
x=input()
if x=='f':
    #k=input("enter first letter of your name in capital letter")
    #y=input("enter first letter for another user/friends in capital letter")
    print("!!!Welcome to Play With friends/user!!!" )
    User1=input("user1 enter your choice : ")
    user2=input("user2 enter your choice : ")
    dictt={"s":1,'w':-1,"g":0}
    dictt2={1:"snake",-1:"water",0:"gun"}
    you=dictt[user2]
    you2=dictt[User1]
    print("user1 choose",{dictt2[you2]})
    print("user2 choose",{dictt2[you]})
    if(you==you2):
        print("draw")
    else:
        if(you==1 and you2==-1):
            print("Congratulation User2 Win")    
        elif(you==1 and you2==0) :
            print,("Congratulation User1 Win")   
        elif(you==-1 and you2==1):
            print("Congratulation User1 Win")    
        elif(you==-1 and you2==0):
            print("Congratulation User2 Win")    
        elif(you==0 and you2==-1):
            print("Congratulation User1 Win")   
        elif(you==0 and you2==1):
            print("Congratulation User2 Win")  
        else:
            print("something went wrongs")

                 #SNAKE,WATER,GUN PLAY WITH COMPUTER 

elif x=='c':
    print("!!!Welcome to play with computer!!!")
    computer=random.choice([0,-1,1])
    user2=input("Enter your choice : ")
    dictt={"s":1,'w':-1,"g":0}
    dictt2={1:"Snake",-1:"Water",0:"Gun"}
    you=dictt[user2]
    print("Computer Choose -",{dictt2[computer]})
    print("You Choose -",{dictt2[you]})
    if(you==computer):
        print(" Draw,Wow!! What a Coincidence ")
    else:
        if(you==1 and computer==-1):
            print("!!!Congratulation You Win!!!")    
        elif(you==1 and computer==0) :
            print,("Congratulation Computer Win")   
        elif(you==-1 and computer==1):
            print("Congratulation Computer Win")    
        elif(you==-1 and computer==0):
            print("!!!Congratulation You Win!!!")    
        elif(you==0 and computer==-1):
            print("Congratulation Computer Win")   
        elif(you==0 and computer==1):
            print("!!!Congratulation You Win!!!")  
        else:
            print("something went wrongs")
    
                      
        


