val=['6','7','8', '9','1', 'J','Q','K','A']
card1,card2=input().split()
koz=input()
dictVal=dict(zip(val,range(9)))
if(card1[len(card1)-1]==card2[len(card2)-1]):
    if(dictVal.get(card1[0])>dictVal.get(card2[0])):
        print('First')
    else:
        print('Second')
elif(card1[len(card1)-1]==koz):
    print('First')
elif(card2[len(card2)-1]==koz):
    print('Second')
else:
    print('Error')