package RMI;
import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class Server {

    public static void main(String[] args) {
        try {
            LocateRegistry.createRegistry(11099);

            TaxaComissaoImpl taxaComissaoImpl = new TaxaComissaoImpl();

            Naming.rebind("rmi://127.0.0.1:11099/calculadoraTaxa", taxaComissaoImpl);

            System.out.println("Servidor RMI iniciado com sucesso!");
        } catch (Exception e) {
            System.err.println("Erro ao iniciar o servidor RMI: " + e.getMessage());
            e.printStackTrace();
        }
    }
}