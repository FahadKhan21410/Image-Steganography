import PIL

from PIL import Image

def StegnoImg(input_path,message,output_path):

    img = Image.open(input_path)
    width , height = img.size
    encoded = img.copy()
    message += chr(0)  # Null character to signal end of message
    binary_msg = ''.join(format(ord(char),'08b') for char in message) #Converts each char of msg into binary 1 char = 1 byte = 8 bits

    data_index = 0

    for y in range(width):
        for x in range(height):
            pixel = list(img.getpixel((x,y)))
            for i in range(3):  #R, G, B
                if data_index < len(binary_msg):
                    pixel[i] = pixel[i] & ~1 | int(binary_msg[data_index])
                    data_index += 1
            encoded.putpixel((x,y),tuple(pixel))

            if data_index >= len(binary_msg):
                break
        if data_index >= len(binary_msg):
            break

    encoded.save(output_path)
    print("Message Successfully Embedded In Image")

def unStegnoImg(input_path):
    img =Image.open(input_path)
    width , height = img.size
    binary_msg= ''
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x,y)))
            for i in range(3): #R,G,B
                binary_msg += str(pixel[i] & 1)

    chars = [binary_msg[i:i+8] for i in range(0,len(binary_msg),8)]   #range(start,stop,step) --> [0:8] --> [8:16]
    message = ''
    for char in chars:
        if chr(int(char,2)) == chr(0):
            break
        message += chr(int(char,2))

    print(f"Message={message}")

def encryptMsg():
    pass
def decryptMsg():
    pass

while True:
    print("===Stegnography===")

    choice = input("Options:\n"
                    "1)Embed text into an image\n"
                    "2)Decode text in an image\n"
                    "3)Exit :_(\n"
                    "Choice(1/2/3): ")

    if choice == '1':
        input_path = input("Enter Image Path: ")
        Message = input("Message you want to embed: ")
        output_path = input("Where do you want to save the image Text-Embedded-Image: ")
        StegnoImg(input_path,Message,output_path)

    if choice == '2':
        input_path = input("Enter Text-Embedded-Image Path: ")
        unStegnoImg(input_path)

    if choice == '3':
        print("\nExiting...")
        break




