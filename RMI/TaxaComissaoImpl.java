package RMI;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class TaxaComissaoImpl extends UnicastRemoteObject implements TaxaComissaoInterface {

    private static final long serialVersionUID = 1L;

    public TaxaComissaoImpl() throws RemoteException {
        super();
    }

    @Override
    public float calcularValorComComissao(float valor) throws RemoteException {
        float taxaComissao = 0.05f;
        float valorComComissao = valor + (valor * taxaComissao);
        return valorComComissao;
    }
}