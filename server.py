
#Librari

import socket
import argparse
import threading 

parser = argparse.ArgumentParser(description = "This is the server for the multithreaded socket demo!")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname())
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 9999)
args = parser.parse_args()

print(f"Ruleaza servarul pe hostul: {args.host} si portul: {args.port}")

sck = socket.socket()
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try: 
	sck.bind((args.host, args.port))
	sck.listen(5)
except Exception as e:
	raise SystemExit(f"Nu am putut face conexiunea dintre server si hostul: {args.host} la  portul: {args.port}, din cauza: {e}")


def on_new_client(client, connection):
	ip = connection[0]
	port = connection[1]
	print(f"Noua conexiune a fost facuta de la  {ip}, si portul: {port}!")
	while True:
		msg = client.recv(1024)
		if msg.decode() == 'exit':
			break
		print(f"Clientul a spus: {msg.decode()}")
		reply = f"Tu ai spus: {msg.decode()}"
		client.sendall(reply.encode('utf-8'))
	print(f"Clientul de la ip-ul : {ip}, si portul: {port}, sa deconectat!")
	client.close()

while True:
	try: 
		client, ip = sck.accept()
		threading._start_new_thread(on_new_client,(client, ip))
	except KeyboardInterrupt:
		print(f"Inchidere server!")
	except Exception as e:
		print(f"Nu am aticipat asta: {e}")

sck.close()