#Rot13 is a special case of caeser cipher encryption

#Type ur message and hit enter to encrypt


alph="abcdefghijklmnopqrstuvwxyz"

letts=input().lower()
resl=""
for let in letts:
    if let in alph:
        i=alph.index(let)
        k=i+13
        if k<=25:
            resl=resl+alph[k]
        else:
            resl=resl+alph[k-26]
    else:
        resl=resl+let
print(resl)
