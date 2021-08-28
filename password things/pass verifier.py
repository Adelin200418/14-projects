from pass_gen import password_creator,length
length
psswrds=[]


def pass_check(lg):
    global psswrds
    pct,upper,lower,number,symbol=0,0,0,0,0
    a=password_creator(lg)
    for i in a:
        if i.islower():
            pct+=1
            lower+=1
        elif i.isupper():
            pct+=1
            upper+=1
        elif i.isdigit():
            pct+=1
            number+=1
        else:
            pct+=1
            symbol+=1
    if lower<1:
        print('password require at least 1 lowercase char')
        print('generating new password...................')
        pass_check(lg)
    if upper<1:
        print('password require at least 1 upercase char')
        print('generating new password.................')
        pass_check(lg)
    if number<1:
        print('password require at least 1 number')
        print('generating new password.....................')
        pass_check(lg)
    if symbol<1:
        print('password require at least 1 special symbol')
        print('generating new password.............')
        pass_check(lg)
    psswrds.append(a)

pass_check(length)
print(f'Your newly created password is {psswrds[0]}')




   
