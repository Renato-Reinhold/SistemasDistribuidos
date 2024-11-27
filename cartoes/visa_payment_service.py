from datetime import datetime
import socket
import re

#taxa vai ser de 5%
HOST = '127.0.0.1'
PORT = 8900

class VisaPaymentService():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f'Conectado por {addr}')
            while True:
                data = conn.recv(1024).decode('utf-8')
                print(f'Requisição recebida: {data}')

                if not data:
                    break

                if data == 'PAY':
                    conn.sendall('Solicita efetuacao de pagamento'.encode('utf-8'))
                    conn.sendall('N° do cartão'.encode('utf-8'))
                    conn.sendall('Nome do cartão'.encode('utf-8'))
                    conn.sendall('Data de expiração do cartão (MM/yyyy)'.encode('utf-8'))
                    conn.sendall('Valor da transação'.encode('utf-8'))
                    conn.sendall('Confirma a transação'.encode('utf-8'))

                    numero_cartao = conn.recv(1024).decode('utf-8')
                    nome_cartao = conn.recv(1024).decode('utf-8')
                    data_expiracao = conn.recv(1024).decode('utf-8')
                    valor_transacao = conn.recv(1024).decode('utf-8')
                    confirmacao = conn.recv(1024).decode('utf-8')

                    if confirmacao == 'COMMIT':
                        print('Transação aprovada!')
                        conn.sendall('OK (1ª linha)'.encode('utf-8'))
                        conn.sendall(f'Dados da transação* (2ª linha): {numero_cartao}:{nome_cartao}:{data_expiracao}:{valor_transacao}'.encode('utf-8'))
                    else:
                        print('Transação cancelada!')
                        conn.sendall('NOK'.encode('utf-8'))

                else:
                    conn.sendall('OK'.encode('utf-8'))

def valida_data_expiracao(data):
    data = datetime.strptime(data, "%m/%Y")
    now = datetime.now()
    if data > now:
        return DataExpiracaoError
    return True

def valida_nome(nome):
    regex_nome = r"^[A-Za-zÀ-ÖØ-öø-ÿ]+(?: [A-Za-zÀ-ÖØ-öø-ÿ]+)*$"
    if re.match(regex_nome, nome):
        return True
    return NomeError

def valida_visa(cartao):
    regex_cartao = r'^[0-9]{16}$'
    regex_visa = r'^4[0-9]{12}(?:[0-9]{3})?$'
    if re.match(regex_cartao, cartao):
        if re.match(regex_visa, cartao):
            return True
        else:
            return CartaoCreditoVisaError
    else:
        return NumeroCartaoInvalidoError

class ComandoInvalidoError(Exception):
        def __init__(self, message="Error 3000: Comando inválido"):
            self.message = message
            super().__init__(self.message)

class NumeroCartaoInvalidoError(Exception):
    def __init__(self, message="Error 3001: Número de Cartão de crédito inválido"):
        self.message = message
        super().__init__(self.message)

class CartaoCreditoVisaError(Exception):
    def __init__(self, message="Error 3002: Cartão de crédito não é da bandeira Visa"):
        self.message = message
        super().__init__(self.message)

class NomeError(Exception):
    def __init__(self, message="Error 3003: Nome da pessoa inválido"):
        self.message = message
        super().__init__(self.message)

class DataExpiracaoError(Exception):
    def __init__(self, message="Error 3004: Data Expiracao do cartão de crédito inválida"):
        self.message = message
        super().__init__(self.message)

class ValorTransError(Exception):
    def __init__(self, message="Error 3005: Valor da transação inválido"):
        self.message = message
        super().__init__(self.message)

class SistemaIndisponivelError(Exception):
    def __init__(self, message="Error 3006: Sistema indisponível"):
        self.message = message
        super().__init__(self.message)

if __name__ == "__main__":
    VisaPaymentService()