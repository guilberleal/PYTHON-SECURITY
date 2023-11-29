import hashlib

arquivo1 = "a.txt"
arquivo2 = "b.txt"

hash1 = hashlib.new("ripemd160") #tipo do hash
hash2 = hashlib.new("ripemd160") #tipo do hash

hash1.update(open(arquivo1, "rb").read()) #compara o hash

hash2.update(open(arquivo2, "rb").read()) #compara o hash

if hash1.digest() != hash2.digest(): #compara os hashs forem diferentes
    print(f"O arquivo: {arquivo1} é diferente do arquuivo: {arquivo2}")
    print("O hash do arquivo a.txt é: ",hash1.hexdigest())
    print("O hash do arquivo b.txt é: ",hash2.hexdigest())
else:
    print(f"O arquivo: {arquivo1} é igual ao arquivo {arquivo2}")
    print("O hash do arquivo a.txt é: ",hash1.hexdigest())
    print("O hash do arquivo b.txt é: ",hash2.hexdigest())