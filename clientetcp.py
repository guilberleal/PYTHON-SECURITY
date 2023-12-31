import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexao falhou")
        print("Erro: {}".format(e))
        sys.exit()
        
    print ("Socket criado com sucesso")
    
    HostAlvo = input("Digite o Hosto ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")
    
    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com Sucesso no host: " + HostAlvo + " e na Porta: " + PortaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("Nao foi possivel conectar no Host: " + HostAlvo + " - Porta "+ PortaAlvo)
        print("Erro: {}".format(e))
        sys.exit()
if __name__ == "__main__":
    main()