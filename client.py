#Librari


import socket 
import argparse #Pentru linile de comanda si subcomenzi

parser = argparse.ArgumentParser(description = "Acest client este pe server!")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname()) 		# vom da la host o metavariabila'host' va avea tipul string vom da un nr de argumente "?"" si ca default este socket
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 9999)					#vom da un argument la port de tip integer vom da un  nr de argumente "?"" iar ca default val 9999
args = parser.parse_args()

print(f"Conectare la server cu hostul: {args.host} si portul: {args.port}") ##printez urmatorele  f stringuri pe scurt am specificat ca vreau sa retin tot ce a trecut de --host intro metavariabila host si as vrea sa fie string iar asi vrea sa am "?"( 0 sau 1) nr de argumente 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
	try: 
		sck.connect((args.host, args.port))
	except Exception as e: # ca excepti am esuat sa ne conectam
		raise SystemExit(f"A esuat sa se conecteze la host: {args.host} pe portul: {args.port}, din cauza: {e}")

	while True: #initere infint loop
		msg = input("Ce mesaj vrei sa trimiti pe server?: ") #mesaj
		sck.sendall(msg.encode('utf-8')) #functia are asteptari de biti nu string de aia punem encode 
		if msg =='iesi':
			print("Clientul Iese!")
			break # vrem sa iesim din loop 
		data = sck.recv(1024) #raspuns de la server
		print(f"Raspunsul servarului a fost: {data.decode()}")