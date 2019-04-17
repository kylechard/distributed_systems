import zmq

context = zmq.Context()
s = context.socket(zmq.SUB)
s.connect('tcp://127.0.0.1:7778')
s.setsockopt_string(zmq.SUBSCRIBE, '')

print("GETTING")
for i in range(5):
    time = s.recv_string()
    print (time)
