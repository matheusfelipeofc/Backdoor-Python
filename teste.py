import cryptography.fernet as fernet

with open('key.txt', 'w+') as key:
    key.write(fernet.Fernet.generate_key().decode())
    
chave = open('key.txt', 'r').read()

print(chave)

f = fernet.Fernet(chave)

token = 'Olá Mundo'.encode()

criptografar = f.encrypt(token)

print(criptografar)

print(f.decrypt(criptografar).decode())