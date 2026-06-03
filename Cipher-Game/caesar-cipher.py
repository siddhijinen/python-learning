logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"Y8bbdP"  `"8bbdP"Y8 88  
                                                      
                                                      
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             
"""

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction_shift, original_text, shift_amount):
    cipher_text = ""
    if direction_shift == "decode":
            shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            cipher_text += alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]
        else:
            cipher_text += letter
    print(f"Here is the {direction_shift}d result: {cipher_text}")

again = True

while again:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid Direction Error! Program Ended.")
        break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, direction_shift=direction)

    if input("Do you want to go again? Type 'yes' to continue. ").lower() == "yes" or "y":
        again = True
    else:
        again = False
        print("Program Ended")
