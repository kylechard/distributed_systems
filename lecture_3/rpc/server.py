import rpyc
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
    value = []

    def exposed_append(self, data):
        self.value = self.value + [data] 
        return self.value

    def exposed_value(self):
        return self.value

if __name__ == "__main__":
    server = ThreadedServer(DBList, port = 7777)
    server.start()
