package Server;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class VisaService {

    public static void main(String[] args) {
    	
        try (ServerSocket serverSocket = new ServerSocket(8901, 0, InetAddress.getByName("127.0.0.1"))) {
            System.out.println("Visa Payment Service iniciado na porta 8900.");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Cliente conectado: " + clientSocket.getInetAddress());

                try (PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
                        ObjectInputStream in = new ObjectInputStream(clientSocket.getInputStream());
                        ObjectOutputStream objectOut = new ObjectOutputStream(clientSocket.getOutputStream())) {

                       Map<String, Object> data = (Map<String, Object>) in.readObject();
                       System.out.println("Cliente: " + data);
                       
                       if("PAY".equals(data.get("servico"))) {
                    	   System.out.println(data);
                    	   String numeroCartao = (String) data.get("numeroCartao");
                    	   String nomeCartao = (String) data.get("nomeCartao");
                    	   String dataExpiracao = (String) data.get("dataExpiracao");
                    	   String valor = (String) data.get("valor");
                    	   
                    	   if(isCardNumberValid(numeroCartao) 
                    			   && isClientNameValid(nomeCartao)
                    			   && isExpirationDateValid(dataExpiracao)
                    			   && isTransactionValueValid(valor)) {
                    		   objectOut.writeObject("Fazer o pagamento aplicando a taxa comissao");
                       		}                 	
                       }
                       
                       objectOut.flush();
                       objectOut.close();
                       in.close();
                       
                   } catch (IOException | ClassNotFoundException e) {
                       System.out.println("Erro ao processar a requisição: " + e.getMessage());
                   }
            }
        } catch (IOException e) {
            System.out.println("Erro ao iniciar o servidor: " + e.getMessage());
        }
    }
    
    private static boolean isCardNumberValid(String cardNumber) {
        return cardNumber.matches("[4][0-9]{15}");
    }

    private static boolean isClientNameValid(String clientName) {
        return clientName.length() >= 2;
    }

    private static boolean isExpirationDateValid(String expirationDate) {
        Pattern pattern = Pattern.compile("(0[1-9]|1[0-2])/(20[0-9]{2})");
        Matcher matcher = pattern.matcher(expirationDate);
        return matcher.matches();
    }

    private static boolean isTransactionValueValid(String transactionValue) {
        try {
            double value = Double.parseDouble(transactionValue);
            return value > 0;
        } catch (NumberFormatException e) {
            return false;
        }
    }
    
}