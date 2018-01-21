
import  socket
import  sys
import  netifaces

from proto import referee_pb2


class Multicast(object):
    def __init__(self, group_addr, port):
        bind_addr = '0.0.0.0'

        # Create a IPv4/UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Avoid error 'Address already in use'.
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Construct a membership_request
        membership_request = socket.inet_aton(group_addr) + socket.inet_aton(bind_addr)

        # Send add membership request to socket
        self.sock.setsockopt(socket.IPPROTO_IP, 
                socket.IP_ADD_MEMBERSHIP, membership_request)

        # Bind the socket to an interfaces
        self.sock.bind((bind_addr, port))

        # Set non-blocking receiving mode
        self.sock.setblocking(False)


    def recv(self, buf_length)->str:
        try:
            buf = self.sock.recv(buf_length)
        except:
            return  None

        return  buf


class Listener(object):
    def __init__(self, addr, port):

        self._sock = Multicast(addr, port)
        self._protobuf = referee_pb2.SSL_Referee()
        self._ref_statge = None
        self._ref_command = None


    def receive(self):
        buf = self._sock.recv(1024)

        if buf == None:
            return False

        self._protobuf.ParseFromString(buf)
        self._ref_stage = self._protobuf.stage
        self._ref_command = self._protobuf.command
            
        return True


    def get_stage(self):
        return self._ref_stage


    def get_command(self):
        return self._ref_command


def add_two(value)->int:
    return value + 2
