#GUSS THE NUMBER
import random
random=random.randint(0,5)
guss=int(input('enter the guss value: '))
while(random!=guss):
    if (random > guss):
        print('entered value is short')
        guss = int(input('enter the guss value: '))

    elif(random<guss):
        print('entered value is high')
        guss = int(input('enter the guss value: '))
    else:
        print("entered value is curect")

