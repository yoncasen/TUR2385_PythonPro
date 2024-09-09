import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola_uzunlugu = int(input("Parolanız kaç haneli olsun?"))

parola = ""

for i in range(parola_uzunlugu):
  parola += random.choice(karakterler)

print(parola)