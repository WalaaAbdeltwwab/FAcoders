s1=['Ahmad',18,17,19.5,8,25]
s2=['Sami',20,20,19,9,28]
s3=['Faris',14.5,16,13,7,23]
num=input('Enter Student\'s name: ')
if num==s1[0]:
    print(s1[0]+' '+str(sum(s1[1:])))
elif num==s2[0]:
    print(s2[0]+' '+str(sum(s2[1:])))
elif num==s3[0]:
    print(s3[0]+' '+str(sum(s3[1:])))
else :
    print('Student is not recorded 0')
