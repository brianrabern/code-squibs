def checksum(message):
    s=0

    for letter in message:
        s+=ord(letter)
    rem=s%26
    rem +=97

    return chr(rem)


print(checksum("cat"))
print(checksum("bat"))
print(checksum("hack reactor"))
