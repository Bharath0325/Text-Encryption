def encrypt(text, shift):
    result = ""
    
    # Traverse the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Encrypt digits
        elif char.isdigit():
            result += chr((ord(char) + shift - 48) % 10 + 48)
        
        # Leave other characters unchanged
        else:
            result += char
    
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Example usage
if __name__ == "__main__":
    print("Welcome to the Text Encryption Tool!")
    
    # Get user input for text and shift value
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    
    # Encrypt the text
    encrypted_text = encrypt(text, shift)
    print(f"Encrypted text: {encrypted_text}")
    
    # Decrypt the text
    decrypted_text = decrypt(encrypted_text, shift)
    print(f"Decrypted text: {decrypted_text}")
