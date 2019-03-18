import zmq, time, pickle, sys

context = zmq.Context()
r = context.socket(zmq.PULL)

p1 = "tcp://127.0.0.1:7777"
p2 = "tcp://127.0.0.1:7778"
r.connect(p1)
r.connect(p2)

while True:
    work = pickle.loads(r.recv()) # receive work from a source
    print(work)
    time.sleep(work[1]*0.01)
