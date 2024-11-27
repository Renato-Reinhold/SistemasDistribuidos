package Client;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.HashMap;
import java.util.Map;

public class VisaClient {

    public static void main(String[] args) {
        try (Socket socket = new Socket("127.0.0.1", 8901)) {
            ObjectOutputStream out = new ObjectOutputStream(socket.getOutputStream());
            ObjectInputStream in = new ObjectInputStream(socket.getInputStream());

            Map<String, Object> data = new HashMap<>();
            data.put("servico", "PAYMENT");
            data.put("numeroCartao", "4234567890123456");
            data.put("nomeCartao", "ROQUE BEZERRA");
            data.put("dataExpiracao", "12/2025");
            data.put("valor", "252.43");

            out.writeObject(data);
            out.flush();

            String response = (String) in.readObject();
            System.out.println("Resposta do servidor: " + response);

        } catch (IOException | ClassNotFoundException e) {
            System.err.println("Erro na conexão com o servidor: " + e.getMessage());
        }
    }
}