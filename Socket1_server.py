import socket

# 서버 IP 주소와 포트 번호
SERVER_IP = '172.31.37.199'
SERVER_PORT = 8080

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 소켓을 주소에 바인딩
server_socket.bind((SERVER_IP, SERVER_PORT))

# 클라이언트의 연결을 기다림
server_socket.listen(1)
print('서버가 시작되었습니다. 클라이언트의 연결을 기다립니다...')

# 클라이언트와의 연결 수락
client_socket, client_address = server_socket.accept()
print('클라이언트가 연결되었습니다:', client_address)

while True:
    # 클라이언트로부터 데이터 수신
    data = client_socket.recv(1024).decode()

    if not data:
        # 클라이언트가 연결을 종료한 경우
        print('클라이언트가 연결을 종료했습니다.')
        break

    # 문자를 ASCII 코드로 변환
    ascii_codes = [str(ord(c)) for c in data]

    # ASCII 코드들을 공백으로 구분하여 문자열로 변환
    response = ' '.join(ascii_codes)

    # 변환된 ASCII 코드를 클라이언트에게 전송
    client_socket.send(response.encode())

# 연결 종료
client_socket.close()
server_socket.close()
