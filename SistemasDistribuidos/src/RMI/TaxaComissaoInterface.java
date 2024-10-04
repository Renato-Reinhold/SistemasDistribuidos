package RMI;
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface TaxaComissaoInterface extends Remote {
    float calcularValorComComissao(float valor) throws RemoteException;
}