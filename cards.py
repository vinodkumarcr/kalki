from random import shuffle
J=11
Q=12
K=13
A=14
D=10
a=23456789
e=[D,J,Q,K,A]
b=str(a)
c=b*4
d=list(c)
#print(d)
f=e*4
#print(f)
card=''
for g in d:
	card+=g
cards=list(card)
cards.extend(f)
#print(cards)
shuffle(cards)
#print(cards)

com=cards[len(cards)/2:]
player=cards[:len(cards)/2]
print(com)
print(player)
	
