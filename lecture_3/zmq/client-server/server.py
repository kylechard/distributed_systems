import zmq
context = zmq.Context()

p1 = 'tcp://127.0.0.1:7777'
p2 = 'tcp://127.0.0.1:7778'

s = context.socket(zmq.REP)

s.bind(p1) # bind socket to address
s.bind(p2) # bind socket to address
while True:
    message = s.recv_string() # wait for incoming message
    if not "STOP" in message: # if not to stop...
         s.send_string(message + "*") # append "*" to message
    else: # else...
         break # break out of loop and end
