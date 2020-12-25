#first task or goal is to generate a key using cryptography library
from cryptography.fernet import Fernet
def Generate_PassKey():
    pkey = Fernet.generate_key();
    keyholder = open("PasswordKey.key", 'wb');
    keyholder.write(pkey);
    keyholder.close();

def Load_key():
    keyholder = open("PasswordKey.key", 'rb')#Passwordkey is a file stroing the key which is being generated as a password
    return keyholder.read();

def Get_Content():
    e_msg = input("Enter the content you want to encrypt:");
    return e_msg;

def Encrypt_Content(nm_cnt):
    Generate_PassKey();
    keytkn = Load_key();
    f = Fernet(keytkn);
    nm_cnt = Get_Content();
    encoded_content = nm_cnt.encode();
    encrypted_content = f.encrypt(encoded_content);
    print(encrypted_content);

if __name__ == "__main__":
    Encrypt_Content("encrypt this message");





