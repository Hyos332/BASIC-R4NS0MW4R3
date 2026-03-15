import os
import sys
from cryptography.fernet import Fernet

key = sys.argv[1].encode()
cipher = Fernet(key)

for root, _, files in os.walk("#RUTA DONDE SE ENCUENTRAN LOS ARCHIVOS CIFRADOS"):
    for file in files:
       if file.endswith(".locked"):
            file_path = os.path.join(root, file)
        
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()

                decrypted = cipher.decrypt(data)
                original = file_path.replace('.locked', '')

                with open(original, 'wb') as f:
                    f.write(decrypted)

                os.remove(file_path)
            except:
                pass
 
print(f"\n[!] Todos los archivos .locked han sido descifrados.\n")
print(f"\n[+] La has descifrado con esta key: {key.decode()}\n")

