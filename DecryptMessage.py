from cryptography.fernet import Fernet
def load_k():
    keyholder = open("PasswordKey.key", 'rb')  # Passwordkey is a file stroing the key which is being generated as a password
    return keyholder.read();

def Decrypt_Content(enc_msg):
    keytkn = load_k();
    f = Fernet(keytkn);
    #decrypted_content = f.encrypt(enc_msg);
    decoded_content = f.decrypt(enc_msg);
    print(decoded_content.decode());
    print("Testing");

if __name__ == "__main__":
    Decrypt_Content(b'gAAAAABf5jrDYfOTUQgmWd0vDrBluSk2b_QBlsF3PyVIiFlXOLKHREFAaYQNIxjlPRkPHq7bja-4eEs8zOq8p96dKexBX7wrIw==');
