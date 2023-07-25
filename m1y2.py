import random

live = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_len = int(input("Длинна пароля: "))
password = ""

for i in range(pass_len):
    password += random.choice(live)

print(password)    