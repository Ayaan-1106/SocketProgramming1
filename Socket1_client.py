import socket

# DNS 서버 정보
dns_host = '172.31.37.199'  # DNS 서버 IP 주소
dns_port = 8080         # DNS 서버 포트 번호

# DNS 서버에 연결
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((dns_host, dns_port))

print("문자 -> ASCII 변환 프로그램. 종료하려면 'quit' 를 입력하세요")

while True:
    # DNS 쿼리 요청 입력
    
    user_input = input("문자 입력: ")
    
    if user_input == 'quit':
        print("프로그램 종료")
        break

    if isinstance(user_input, str):
         client_socket.send(user_input.encode())
        
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")
        continue

    # DNS 응답 수신
    response = client_socket.recv(1024).decode()

    # 응답 출력
    print(response)

# 연결 종료
client_socket.close()
