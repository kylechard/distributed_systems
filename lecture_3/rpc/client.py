import rpyc

class Client:
    conn = rpyc.connect('localhost', 7777)

    conn.root.exposed_append(2)
    conn.root.exposed_append(4)
    conn.root.exposed_append(6)

    print(conn.root.exposed_value())
