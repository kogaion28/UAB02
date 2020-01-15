# Parte clientului 



#Librari
import socket 
import argparse #Pentru linile de comanda si subcomenzi

parser = argparse.ArgumentParser(description = "Acest client este pe server!")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname())
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 9999)
args = parser.parse_args()

print(f"Conectare la server cu hostul: {args.host} si portul: {args.port}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
	try:
		sck.connect((args.host, args.port))
	except Exception as e:
		raise SystemExit(f"A esuat sa se conecteze la host: {args.host} pe portul: {args.port}, din cauza: {e}")

	while True:
		msg = input("Ce mesaj vrei sa trimiti pe server?: ")
		sck.sendall(msg.encode('utf-8'))
		if msg =='iesi':
			print("Clientul zice PA!")
			break
		data = sck.recv(1024)
		print(f"Raspunsul servarului a fost: {data.decode()}")