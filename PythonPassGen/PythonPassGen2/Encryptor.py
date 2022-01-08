from cryptography.fernet import Fernet



class Encryptor():
    
    def key_creation(self):
        key = Fernet.generate_key()
        return key
    
    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)
            
    def key_load(self, key_name):
        with open(key_name,'r') as mykey:
            key = mykey.read()
        return key
    
    def file_encrypt(self, key, original_file, encrypted_file):
        f = Fernet(key)
        
        with open(original_file,  'rb') as file:
            original = file.read()
        
        encrypted = f.encrypt(original)
        
        with open (encrypted_file, 'wb') as file:
            file.write(encrypted)
            
    def file_decrypt(self, key, encrypted_file, decrypted_file):
        f = Fernet(key)
        
        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()
            
            
        print(encrypted) #Test to see if its pulling encrypted data.            
        decrypted = f.decrypt(encrypted)
        print(decrypted) #Why is data lost here
        
        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)