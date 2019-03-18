import zmq
context = zmq.Context()

php = "tcp://localhost:7777"
s = context.socket(zmq.REQ)

s.connect(php)
s.send_string("Hello World")

message = s.recv_string()
s.send_string("STOP")
print(message)
