# The purpose of this file is to create an encryption and decryption program that will take a file inputted by the user and convert it to an encrypted message in a new file. 
# This program will also take that file with the encrypted message and convert it back to the original message.

def open_file(input_path, output_path):
    try:

        with open(input_path, 'r') as input_file: 
            content = input_file.read()
            
        encrypt_data = ''.join(chr(ord(char) + 10) for char in content)

        with open(output_path, 'w') as output_file:
            output_path.write(content)

        print("File has been encoded! ")
    except FileNotFoundError:
        print(f"Error: File '{input_path}' was not found!")
    except IOError:
        print(f"Error: I/O error has occured!")
    except Exception as e:
        print (f"An unexpected error has occured!")

    