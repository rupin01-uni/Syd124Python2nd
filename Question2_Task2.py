# https://github.com/rupin01-uni/Syd124Python2nd.git

def separate_and_convert(s):
    Number_String = ''.join([c for c in s if c.isdigit()])
    Letter_String = ''.join([c for c in s if c.isalpha()])
    
    even_numbers = [int(num) for num in Number_String if int(num) % 2 == 0]
    Ascii_Values_Numbers = [ord(str(num)) for num in even_numbers]
    
    Ascii_Values_Letters = [ord(letter) for letter in Letter_String if letter.isupper()]
    
    return {
        "Number_String": Number_String,
        "Letter_String": Letter_String,
        "Even_numbers_ascii_values": Ascii_Values_Numbers,
        "Upper_case_letters_ascii_values": Ascii_Values_Letters
    }


Input_String = '56aAww1984sktr235270aYmn145ss785fsq31D0'
result = separate_and_convert(Input_String)
print(result)


def decrypt_cryptogram(cryptogram):
    for shift in range(16):
        decrypted_text = ''.join([decrypt_char(char, shift) for char in cryptogram])
        print(f"Shift {shift}: {decrypted_text}")

def decrypt_char(char, shift):
    if char.isalpha():
        Ascii_offset = ord('A') if char.isupper() else ord('a')
        Decrypted_char = chr((ord(char) - Ascii_offset - shift) % 26 + Ascii_offset)
        return Decrypted_char
    else:
        return char


cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
decrypt_cryptogram(cryptogram)