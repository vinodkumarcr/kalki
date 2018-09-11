from random import shuffle
D=10
J=11
Q=12
K=13
A=14
a=[2,3,4,5,6,7,8,9]
b=[D,J,Q,K,A]
cards=a*4
#print(c)
d=b*4
#print(d)
cards.extend(d)
#print(cards)
shuffle(cards)
com = cards[int(len(cards)/2):]
player=cards[:int(len(cards)/2)]
playdata=[]
comdata=[]
#print(com)


def call():
            for x,y in zip(com,player):
                if x==10:
                    print('x: ',10)
                if y==10:
                    print('y: ',10)
                if x==11:
                    print('x: J')
                if y==11:
                    print('y: J')
                if x==12:
                    print('x: Q')
                if y==12:
                    print('y: Q')
                if x==13:
                    print('x: K')
                if y==13:
                    print('y: K')
                if x==14:
                    print('x: A')
                if y==14:
                    print('x: A')
                else:
                    print('x: ',x)
                    print('y: ',y)
              
              #character()
                com.remove(x)
                player.remove(y)
                if x<y:
                    playdata.extend([x,y])
                    print('Player Data: ',playdata)
                    break

                elif x>y:
                    comdata.extend([x,y])
                    print('ComData:' ,comdata)
                    break

                else:
                      for r in range(2):
                          com.remove(x)
                          player.remove(y)
                      
                  

'''def character():
    if x==10:
        print('x: ',10)
    if y==10:
        print('y: ',10)
    if x==11:
        print('x: J')
    if y==11:
        print('y: J')
    if x==12:
        print('x: Q')
    if y==12:
        print('y: Q')
    if x==13:
        print('x: K')
    if y==13:
        print('y: K')
    if x==14:
        print('x: A')
    if y==14:
        print('x: A')
    else:
        print('x: ',x)
        print('y: ',y)'''
        
    
            

run=True
while run:
    n=input()
    call()
    com=com
    player=player
    




            


