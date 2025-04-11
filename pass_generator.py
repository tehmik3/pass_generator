import random

print('Welcome To Your Password Generator')

chars = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.!@#$%^&*(),.?0123456789')

number = int(input('Amount of password to generate: '))

length = int(input('Input your password length: '))


for pwd in range(number):
    passwords = " "
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)