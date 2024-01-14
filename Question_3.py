# https://github.com/rupin01-uni/Syd124Python2nd

# Encrypted code 

encrypted_code = """
tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xr12': 'inyhr2', 'xr13': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref= [1, 2, 3, 4, 5]
    
    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inevnoyr) 
        ybpny_inevnoyr -= 1
    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref (ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xr14'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    V += 1
vs zl_frg vf abg Abar naq zl_qvpg['xr14'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""

# decrypted_code

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)  # Use chr() to convert ASCII value back to a character
        else:
            decrypted_text += char
    return decrypted_text


# First Find Key Using Below Code 
total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i - j

counter = 0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2
key = total
print("Final key:", key)


original_code = decrypt(encrypted_code, key)
print("Decrypted Code:\n", original_code)

# Below code is corrected from given code. written comment for each correction in the same line.

global_variable = 100
my_dict = {'key1': 'value1', 'ke12': 'value2', 'ke13': 'value3'}

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]
    
    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable) 
        local_variable -= 1
    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers()  # Corrected: Removed the unnecessary argument

def modify_dict():
    local_variable = 10
    my_dict['ke14'] = local_variable

modify_dict()  # Corrected: Removed the unnecessary argument

def update_global():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)
    # Corrected: Variable name should be lowercase 'i' instead of uppercase 'I'
    # I += 1  # This line is unnecessary

if my_set is not None and my_dict['ke14'] == 10:
    print("Condition met!")

if 5 not in my_dict: # Corrected: Changed the my_set to my_dict
    print("5 not found in the dictionary!")  

print(global_variable)
print(my_dict)
print(my_set)