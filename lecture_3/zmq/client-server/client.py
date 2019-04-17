import zmq
context = zmq.Context()

s = context.socket(zmq.REQ)

s.connect('tcp://127.0.0.1:7777')

s.send_string("Ping")

message = s.recv_string()
s.send_string("STOP")
print(message)
