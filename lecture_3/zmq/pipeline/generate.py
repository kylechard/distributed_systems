import zmq, time, pickle, sys, random

context = zmq.Context()
me = str(sys.argv[1])

s = context.socket(zmq.PUSH)
prt = 7777 if me == '1' else 7778
p = "tcp://127.0.0.1: %s" % prt
s.bind(p)

for i in range(10):
    time.sleep(2)
    workload = random.randint(1, 100)
    s.send(pickle.dumps((me,workload)))
