from string import ascii_lowercase,ascii_uppercase,punctuation,digits
import random
length=int(input("tell me the lenght of password "))

def password_creator(lg):
   
    copy=lg
    numbers=[i for i in range(10)]
    chars=[ascii_lowercase,ascii_uppercase,punctuation,numbers]
    password=''
    


    while copy>0:
        random.shuffle(chars)
        password+=str(random.choice(random.choice(chars)))
        copy-=1
    
    return password


