import socket
import threading

PORT=5050
HOST=socket.gethostbyname(socket.gethostname())
FORMATE="utf-8"
HADDER=64
ADDR=(HOST,PORT)

sever=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sever.bind(ADDR)
late=[]

person1=False
person2=False

def handle_client(conn,add,no):
    # print(f"{name} entered")
    global person2,person1
    send_msg(conn,"ENTER YOUR NAME:")
    while True:
        msg_lenght=conn.recv(HADDER).decode(FORMATE)
        if msg_lenght:
            msg_lenght=int(msg_lenght)
            msg=conn.recv(msg_lenght).decode(FORMATE)
            if not person1:
                person1=(msg,conn,no)
                print(f"{msg} ENTERD")
            elif not person2 and no!=1:
                person2=(msg,conn,no)
                print(f"{msg} ENTERD")
                if late:
                    for l in late:
                        send_msg(person2[1],l,person1[0])
            else:
                if msg == "!disconnect":
                    break

                if not person2:
                    send_msg(person1[1],"sorry another person is not online yet!","FROM SERVER")
                    late.append(msg)
                else:
                    if person1[2] != no:
                        send_msg(person1[1], msg, person2[0])
                    if person2[2] != no:
                        send_msg(person2[1], msg, person1[0])

            print(no,"massge is :",msg)
    conn.close()

def send_msg(conn,msg,name=None):
    if name:
        msg=f"{name}:{msg}"
    msg=msg.encode(FORMATE)
    msg_lenght=len(msg)
    send_lenght=str(msg_lenght).encode()
    send_lenght+=b' '*(64-len(send_lenght))
    conn.send(send_lenght)
    conn.send(msg)

no=0
def start():
    sever.listen()
    global no
    while True:
        conn,add=sever.accept()
        no+=1
        thread_client=threading.Thread(target=handle_client,args=(conn,add,no))
        print(f"ACTIVE PEOPLE:{threading.activeCount()}")
        thread_client.start()



print("SEVER STARTED.........")

if __name__ == '__main__':
    start()
