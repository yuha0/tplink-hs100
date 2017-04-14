from contextlib import closing
from socket import socket, AF_INET, SOCK_STREAM


class Plug(object):
    on_cmd = [
        '0000002ad0f281f88bff9af7d5ef94b6c5a0d48bf99cf091e8b7c4b0d1a5c0e2d8a381f286e793f6d4eedfa2dfa2'.decode('hex'),
        '00000025d0f281e28aef8bfe92f7d5ef94b6d1b4c09ff194ec98c7a6c5b1d8b7d9fbc1afdab6daa7da'.decode('hex')
    ]
    off_cmd = [
        '0000002ad0f281f88bff9af7d5ef94b6c5a0d48bf99cf091e8b7c4b0d1a5c0e2d8a381f286e793f6d4eedea3dea3'.decode('hex'),
        '0000002dd0f281f88bff9af7d5ef94b6c5a0d48bf99cf091e8b7c4b0d1a5c0e2d8a381e496e4bbd8b7d3b694ae9ee39ee3'.decode('hex')
    ]

    def __init__(self, ip, port=9999):
        self.addr = (ip, port)

    def send_data(self, data):
        with closing(socket(AF_INET, SOCK_STREAM)) as s:
            s.connect(self.addr)
            for d in data:
                s.send(d)

    def turn_on(self):
        self.send_data(Plug.on_cmd)
        print "on"

    def turn_off(self):
        self.send_data(Plug.off_cmd)
        print "off"

