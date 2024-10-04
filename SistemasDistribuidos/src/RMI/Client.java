package RMI;

import java.rmi.Naming;

public class Client {

    public static void main(String[] args) {
        try {

            TaxaComissaoInterface taxaComissao = (TaxaComissaoInterface) Naming.lookup("rmi://127.0.0.1:11099/calculadoraTaxa");

            float valor = 100.0f;
            float valorComComissao = taxaComissao.calcularValorComComissao(valor);

            System.out.println("Valor com comissão: " + valorComComissao);
        } catch (Exception e) {
            System.err.println("Erro ao conectar ao servidor RMI: " + e.getMessage());
            e.printStackTrace();
        }
    }
}