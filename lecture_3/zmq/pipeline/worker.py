import zmq, time, pickle, sys

context = zmq.Context()
r = context.socket(zmq.PULL)

r.connect("tcp://127.0.0.1:7777")
r.connect("tcp://127.0.0.1:7778")

while True:
    work = pickle.loads(r.recv())
    print(work)
    time.sleep(work[1]*0.01)
