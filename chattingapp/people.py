import socket
import threading
import time
from colorama import Fore,Style
PORT=5050
ADD=socket.gethostbyname(socket.gethostname())
FORMATE="utf-8"
# print("hello")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ADD,PORT))

def get_msg():
    while True:
        msg_lenght = client.recv(64).decode(FORMATE)
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            msg = client.recv(msg_lenght).decode(FORMATE)
            print(msg)
            # print(f"{Fore.BLUE} hey {Style.RESET_ALL}")

thread=threading.Thread(target=get_msg)
thread.start()

def send(msg):
    msg = msg.encode(FORMATE)
    msg_lenght = len(msg)
    send_lenght = str(msg_lenght).encode()
    send_lenght += b' ' * (64 - len(send_lenght))
    client.send(send_lenght)
    client.send(msg)

if __name__ == '__main__':

    while True:
        time.sleep(0.2)
        msg=input()
        send(msg)

