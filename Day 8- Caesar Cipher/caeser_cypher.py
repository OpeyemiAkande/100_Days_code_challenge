# Let the show begin!

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text, shift, direction):
        
        if direction == 'encode':
            conv_text = ''
            for char in text:
                if char in alphabet:
                
                    position = alphabet.index(char)
                    conv_text += (alphabet[position + shift%26])
                else:
                    conv_text += char

        elif direction == 'decode':
            conv_text = ''
            for char in text:
                
                if char in alphabet:
                    position = alphabet.index(char)
                    conv_text += (alphabet[position - shift%26])
                else:
                    conv_text += char
        else:
            print('You entered a wrong input')
        
        print(f'You {direction}d message is {conv_text}')
    # conv_text = ''
    # for letter in text:
    #     position = alphabet.index(letter)
    #     if direction == 'decode':
    #         shift *= -1
        


from art import logo
print(logo)


print('Welcome to the caeser cypher')
response = 'yes'

while response == 'yes':

    direction = input("Type 'encode' to encrypt, type decode to decrypt: \n")
    text = input("Type your message:\n").lower()
    shift = int(input('Type the shift number:\n'))

    
        

    caesar(text=text, shift=shift, direction=direction)
    response = input('To continue, type "yes". To end type "No".')

print('Goodbye')

 

