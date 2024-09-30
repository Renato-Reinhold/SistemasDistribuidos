import socket
from datetime import datetime
import pickle

regex_mastercard = r'^5[1-5][0-9]{14}$'
def MasterPaymentService():
    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind(('127.0.0.1', 8901))
        servidor.listen(5)
        print("Servidor ouvindo a porta 8900")

        while True:

            cliente, endereco = servidor.accept()
            print(f"Cliente conectado: {endereco[0]}")

            dados_recebidos = cliente.recv(4096)
            parametros = pickle.loads(dados_recebidos)
            print(parametros['nome'])
            print(f"Parâmetros recebidos: {parametros}")

            cliente.sendall(b"Dados complexos recebidos com sucesso!")
            cliente.close()

            cliente.close()

    except Exception as e:
        print("Erro:", str(e))


if __name__ == "__main__":
    MasterPaymentService()