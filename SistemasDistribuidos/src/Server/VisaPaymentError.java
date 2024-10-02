package Server;

public class VisaPaymentError extends Exception {

    private int errorCode;

    public VisaPaymentError(int errorCode) {
        this.errorCode = errorCode;
    }

    public int getErrorCode() {
        return errorCode;
    }

    @Override
    public String getMessage() {
        switch (errorCode) {
            case 3000:
                return "Comando inválido";
            case 3001:
                return "Número de cartão de crédito inválido";
            case 3002:
                return "Cartão de crédito não é da bandeira Visa";
            case 3003:
                return "Nome da pessoa inválido";
            case 3004:
                return "Data de expiração do cartão de crédito inválida";
            case 3005:
                return "Valor da transação inválido";
            case 3006:
                return "Sistema indisponível";
            default:
                return "Erro desconhecido";
        }
    }
}