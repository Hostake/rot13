def rot13(text): 
    rot13ed = ''
    for letter in text:
        byte = ord(letter)
        capital = (byte & 32) 
        byte &= ~capital
        if ord('A') <= byte <= ord('Z'):
            byte -= ord('A')
            byte += 13
            byte %= 26
            byte += ord('A')
        byte |= capital
        rot13ed += chr(byte)
    print(rot13ed)    
    return rot13ed

enter = input("input:")
print("")
rot13(enter)
