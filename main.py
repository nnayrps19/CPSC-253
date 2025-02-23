import encryption

def main():
    input_path = 'message.txt'
    output_path = 'encoded_message.txt'
    encryption.encrypt_file(input_path, output_path)
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            input_path = input("Enter the path of the file to encrypt: ")
            output_path = input("Enter the path of the encrypted file: ")
            encryption.encrypt_file(input_path, output_path)
        elif choice == '2':
            input_path = input("Enter the path of the file to decrypt: ")
            output_path = input("Enter the path of the decrypted file: ")
            encryption.decrypt_file(input_path, output_path)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def menu():
    print(** Welcome to the Encryption Program **)
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Exit")

def encyrpt_to_image(input_path, encrypted_path):
    content = encryption.open_file(input_path, encrypted_path)
    if content: 
        char_mapping = image_map()
        encrypted_image = text_to_image(content, char_mapping)
        encrypted_image.save(encrypted_path)
        print(f"Encrypted image saved to '{encrypted_path}'")

decrypt_to_text(input_path, decrypted_path):
    encrypted_image = Image.open(input_path)
    char_mapping = image_map()
    decrypted_text = image_to_text(encrypted_image, char_mapping)
    with open(decrypted_path, 'w') as decrypted_file:
        decrypted_file.write(decrypted_text)
    print(f"Decrypted text saved to '{decrypted_path}'")

if __name__ == '__main__':
    main()