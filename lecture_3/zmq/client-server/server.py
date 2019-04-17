import zmq
context = zmq.Context()

s = context.socket(zmq.REP)

s.bind('tcp://127.0.0.1:7777') 

while True:
    message = s.recv_string()
    if not "STOP" in message:
         s.send_string(message + " pong")
    else:
         break
