import bluetooth
 
while True:

	server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

	port = 1
	server_sock.bind(("", port))
	server_sock.listen(1)

	client_sock,address = server_sock.accept()
	print ("Accepted connection from ", address)

	while True:
	 
	 	try:

	 		data = client_sock.recv(10*1024)
	 		print ("received [%s]" % data)

			if (data == ""):
				print ("Exit")
				break 		

	 	except Exception, e:
	 		print (e)
	 		break
		
	 
	client_sock.close()
	server_sock.close()