import socket
import pickle

def cliente(parametros):
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(('127.0.0.1', 8900))

        dados = pickle.dumps(parametros)
        cliente.sendall(dados)

        resposta = cliente.recv(1024).decode('utf-8')
        print(f"Resposta do servidor: {resposta}")

        cliente.close()
        print("Conexão encerrada")

    except Exception as e:
        print("Erro:", str(e))

if __name__ == "__main__":
    parametros = {'nome': 'Cliente 1', 'idade': 30, 'mensagem': 'Olá, servidor!'}
    cliente(parametros)