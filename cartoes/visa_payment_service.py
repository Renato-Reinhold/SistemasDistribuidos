from datetime import datetime
import socket
import pickle
import re

#taxa vai ser de 5%
def VisaPaymentService():
    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind(('127.0.0.1', 8900))
        servidor.listen(5)
        print("Servidor ouvindo a porta 8900")

        while True:

            cliente, endereco = servidor.accept()
            print(f"Cliente conectado: {endereco[0]}")

            dados_recebidos = cliente.recv(4096)
            parametros = pickle.loads(dados_recebidos)
            num_cartao = parametros['num_cartao']
            valida_visa(num_cartao)
            valida_nome(parametros['nome'])
            valida_data_expiracao(parametros['data_expiracao'])
            valor_trans = parametros['valor_trans']

            print(f"Parâmetros recebidos: {parametros}")

            cliente.sendall(b"Dados complexos recebidos com sucesso!")
            cliente.close()

            cliente.close()

    except Exception as e:
        print("Erro:", str(e))

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