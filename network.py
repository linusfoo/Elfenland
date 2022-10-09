import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # self.server= "10.0.0.202" #"10.122.191.41"
        self.server = "10.121.120.252"
        # self.server = "10.121.181.187"
        self.port = 6000
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048*256))
        except:
            pass

    def send(self, data):
        
        try:
            self.client.send(pickle.dumps(data))
            a =   self.client.recv(2048*256)
            if a!= None:
                m=pickle.loads(a)
                return m
            else:
                return None
        except Exception as e:
            return None

# data = b""
# while True:
#     packet = s.recv(4096)
#     if not packet: break
#     data += packet

# data_arr = pickle.loads(data)
# print (data_arr)
# s.close()