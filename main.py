# The purpose of this file is to create an encryption and decryption program that will take a file inputted by the user and convert it to an encrypted message in a new file. 
# This program will also take that file with the encrypted message and convert it back to the original message.
import string
from PIL import Image

def open_file(input_path, output_path):
    try:

        with open(input_path, 'r') as input_file:   #Opens the selected file and reads the contents
            content = input_file.read()
            
        encrypt_data = ''.join(chr(ord(char) + 10) for char in content) #Basic encryption function that shifts the value of ASCII characters by 10

        with open(output_path, 'w') as output_file:  #Writes encrypted message to outputfile
            output_path.write(content)

        print("File has been encoded! ")
    except FileNotFoundError:
        print(f"Error: File '{input_path}' was not found!")
    except IOError:
        print(f"Error: I/O error has occured!")
    except Exception as e:
        print (f"An unexpected error has occured!")

#Functions for character mapping and generating images
def image_map():
#Creates dictionary for range of character values image will generate from
    char_map = { 
        range(65, 81): '', 
        range(81, 97):'', 
        range(97, 123):'', 
        range(48,58):'',
        range(32,48):''
    }
    return char_map

#Takes the ascii value of the character and compares it to the ranges from image_map function
    def image_for_char(char, char_mapping):     
        ascii_val = ord(char)
        for ascii_range m image_path in char_mapping.items():
            if ascii_val in ascii_range:
                return Image.open(image_path)

        return None
    
    def text_to_image(text, char_mapping):
        images = [image_for_char(char,char_mapping) for char in text if image_for_char(char, char_mapping)]

        imageWidth = sum(img.width for img in images)
        imageHeight = max(img.height for img in images)

        result = Image.new('RGB', imageWidth, imageHeight)

#Function to paste images together
        x_offset = 0
        for img in images: 
            result.paste(img,(x_offset, 0))
            x_offset += img.width

        return result

def image_to_text(text, char_mapping):
    char_map_inv = {v: k for k, v in char_mapping.items()}
    tect = ''
    x_offset = 0

    while x_offset < text.width:
        for image_path, char in char_map_inv.items():
            if text.crop((x_offset, 0, x_offset + image_path.width, image_path.height)) == image_path:
                text += char
                x_offset += image_path.width
                break
    return text