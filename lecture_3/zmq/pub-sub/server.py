import zmq, time

context = zmq.Context()
s = context.socket(zmq.PUB) 
s.bind('tcp://127.0.0.1:7777')

while True:
    time.sleep(5)
    print("sending")
    s.send_string("TIME " + time.asctime())
