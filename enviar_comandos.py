import socket
import tkinter as tk

UDP_IP = "192.168.4.1"
UDP_PORT = 12340

sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)

def andar(mover):
    if mover == "frente":
        MESSAGE = b"motorfrenteservo80"
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        print("frente")
    elif mover == "tras":
        MESSAGE = b"motortrasservo80"
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        print("tras")
    elif mover == "direita":
        MESSAGE = b"girad200"
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        print("gira direita")
    elif mover == "esquerda":
        MESSAGE = b"girae200"
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        print("gira esquerda")

window = tk.Tk()

button1 = tk.Button(text="Frente!", width=5,  height=2, command=lambda: (andar("frente"))).pack()
button2 = tk.Button(text="Tras!", width=5,  height=2, command=lambda: (andar("tras"))).pack()
button3 = tk.Button(text="Direita!", width=5,  height=2, command=lambda: (andar("direita"))).pack()
button4 = tk.Button(text="Esquerda!", width=5,  height=2, command=lambda: (andar("esquerda"))).pack()

window.mainloop()