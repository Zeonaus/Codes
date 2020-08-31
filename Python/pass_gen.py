# Random Password gen
import string
import random

def pass_gen():
    n = int(input("How many Character you want in Password : "))
    ran = string.ascii_lowercase + string.punctuation + string.ascii_uppercase + string.digits
    password = ''.join(random.choice(ran) for i in range (0, n))
    print("Your random password is :", password)

if __name__ == "__main__":
    while True:
        pass_gen()
        u = input("Enter q to exit and p for another password : ").upper()
        if u == 'P':
            continue
        elif u == 'Q':
            break
        else:
            print("You have given wrong input")
            break