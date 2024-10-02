import rmi
from rmi import Server, Client, RemoteException


class TaxaComissaoInterface(rmi.Remote):
    def calcularValorComComissao(self, valor: float) -> float:
        raise NotImplementedError()


# Implementa o servidor
class TaxaComissaoImpl(TaxaComissaoInterface, rmi.server.UnicastRemoteObject):
    def __init__(self):
        rmi.server.UnicastRemoteObject.__init__(self)

    def calcularValorComComissao(self, valor: float) -> float:
        taxaComissao = 0.1
        valorComComissao = valor + (valor * taxaComissao)
        return valorComComissao


# Código do servidor
if __name__ == "__main__":
    try:
        # Cria o registro RMI (se necessário)
        rmi.registry.Registry.createRegistry(1099)

        # Cria a implementação do servidor
        taxaComissaoImpl = TaxaComissaoImpl()

        # Registra a implementação no registro RMI
        rmi.Naming.rebind("rmi://127.0.0.1:1099/calculadoraTaxa", taxaComissaoImpl)

        print("Servidor RMI iniciado com sucesso!")
    except RemoteException as e:
        print(f"Erro ao iniciar o servidor RMI: {e}")

# Código do cliente
if __name__ == "__main__":
    try:
        # Obtém a referência remota para o servidor
        taxaComissao = rmi.Naming.lookup("rmi://127.0.0.1:1099/calculadoraTaxa")

        # Chama o método remoto para calcular a taxa de comissão
        valor = 100.0
        valorComComissao = taxaComissao.calcularValorComComissao(valor)

        # Exibe o resultado
        print(f"Valor com comissão: {valorComComissao}")
    except RemoteException as e:
        print(f"Erro ao conectar ao servidor RMI: {e}")