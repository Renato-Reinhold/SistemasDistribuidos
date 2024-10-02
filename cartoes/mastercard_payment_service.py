import socket


HOST = '127.0.0.1'
PORT = 8901
regex_mastercard = r'^5[1-5][0-9]{14}$'

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

            if data == 'PAYMENT':
                conn.sendall('Solicita efetuacao de pagamento'.encode('utf-8'))
                conn.sendall('Primeira parte do n do cartão'.encode('utf-8'))
                conn.sendall('Segunda parte do n do cartão'.encode('utf-8'))
                conn.sendall('Terceira parte do n do cartão'.encode('utf-8'))
                conn.sendall('Quarta parte do n do cartão'.encode('utf-8'))
                conn.sendall('Nome do cartão'.encode('utf-8'))
                conn.sendall('Data de expiração do cartão (MM/yyyy)'.encode('utf-8'))
                conn.sendall('Valor da transação'.encode('utf-8'))
                conn.sendall('Confirma a transação'.encode('utf-8'))

                primeira_parte_cartao = conn.recv(1024).decode('utf-8')
                segunda_parte_cartao = conn.recv(1024).decode('utf-8')
                terceira_parte_cartao = conn.recv(1024).decode('utf-8')
                quarta_parte_cartao = conn.recv(1024).decode('utf-8')
                nome_cartao = conn.recv(1024).decode('utf-8')
                data_expiracao = conn.recv(1024).decode('utf-8')
                valor_transacao = conn.recv(1024).decode('utf-8')
                confirmacao = conn.recv(1024).decode('utf-8')

                if confirmacao == 'COMMIT':
                    print('Transação aprovada!')
                    conn.sendall('OK (1ª linha)'.encode('utf-8'))
                    conn.sendall(f'Dados da transação* (2ª linha): {primeira_parte_cartao}:{segunda_parte_cartao}:{terceira_parte_cartao}:{quarta_parte_cartao}:{nome_cartao}:{data_expiracao}:{valor_transacao}'.encode('utf-8'))
                else:
                    print('Transação cancelada!')
                    conn.sendall('NOK'.encode('utf-8'))

            else:
                conn.sendall('OK'.encode('utf-8'))