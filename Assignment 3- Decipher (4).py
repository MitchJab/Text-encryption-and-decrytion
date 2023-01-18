# Function and Variables
def code ():
    encode_text=input("text to enccode:")
    encoder_text=""
    key=4
    for i in encode_text:
        ascii_value=ord(i)+key
        encoder_text=encoder_text+chr(ascii_value)
    return encoder_text

def decode():
    decode_text=input("text to decode:")
    decoder_text=""
    key=-4
    for i in decode_text:
        ascii_value2=ord(i)+key
        decoder_text=decoder_text+chr(ascii_value2)
    return decoder_text


#welcome
print ("Welcome to the Decipher 3.0 \n")

#User Instructions
print("**This Program Deciphers any given text**\n ")

print (" 1 - Encrypt text given\n")
print (" 2- Decrypt text given\n")
print ("3- Exit the Program\n")

input_1=True

while (input_1):
    
     #initial prompt
    option = input("Please enter your shift (1 - 3) : ")
    if option.isnumeric():
        option=int(option)
    #Option 1
        if option==1:
            print("the encoded message:",code())
        #Option 2
        elif option==2:
            print("the decoded messge:" ,decode())
        #Option 3
        elif option==3:
            input_1=False
            exit
    #Validation statement 
        else:    # Remember, print is a function in 3.x
            print ("That wasn't an integer from 1-3")
    else:
        print("Value should be a whole number")


       
