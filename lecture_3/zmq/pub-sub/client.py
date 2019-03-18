import zmq

context = zmq.Context()
s = context.socket(zmq.SUB)
p = 'tcp://127.0.0.1:7778'
s.connect(p)
s.setsockopt(zmq.SUBSCRIBE, b'TIME')

for i in range(5):
    time = s.recv_string()
    print (time)
