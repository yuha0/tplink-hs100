import sys
import getpass
import logging
from logging.handlers import RotatingFileHandler
from contextlib import closing
from socket import socket, AF_INET, SOCK_STREAM


if sys.platform.startswith('linux'):
    log_path = '/var/log/tplinkswitch.log'
else:
    log_path = '/usr/local/var/log/tplinkswitch.log'
file_handler = RotatingFileHandler(
    log_path, maxBytes=10485760, backupCount=5)
logging.basicConfig(format="[%(asctime)s] %(message)s",
                    datefmt="%Y%m%d %H:%M:%S %Z",
                    level=logging.INFO,
                    handlers=[logging.StreamHandler(), file_handler])

msg = "user '%s' issued '%s' command to '%s:%s'"


class Switch(object):
    on_cmd = [
        '0000002ad0f281f88bff9af7d5ef94b6c5a0d48bf99cf091e8b7c4b0d1a5c0e2d8a381f286e793f6d4eedfa2dfa2',
        '00000025d0f281e28aef8bfe92f7d5ef94b6d1b4c09ff194ec98c7a6c5b1d8b7d9fbc1afdab6daa7da'
    ]
    off_cmd = [
        '0000002ad0f281f88bff9af7d5ef94b6c5a0d48bf99cf091e8b7c4b0d1a5c0e2d8a381f286e793f6d4eedea3dea3',
        '0000002dd0f281f88bff9af7d5ef94b6c5a0d48bf99cf091e8b7c4b0d1a5c0e2d8a381e496e4bbd8b7d3b694ae9ee39ee3'
    ]

    def __init__(self, ip, port=9999):
        self.ip = ip
        self.port = port

    def send_data(self, data):
        with closing(socket(AF_INET, SOCK_STREAM)) as s:
            s.connect((self.ip, self.port))
            for d in data:
                if sys.version_info[0] < 3:
                    s.send(d.decode('hex'))
                else:
                    s.send(bytes.fromhex(d))

    def turn_on(self):
        logging.info(msg, getpass.getuser(), 'on', self.ip, self.port)
        self.send_data(Switch.on_cmd)

    def turn_off(self):
        logging.info(msg, getpass.getuser(), 'off', self.ip, self.port)
        self.send_data(Switch.off_cmd)


def main():

    switch = Switch(sys.argv[1])
    cmd = {
        'on': switch.turn_on,
        'off': switch.turn_off
    }
    cmd[sys.argv[2]]()


if __name__ == '__main__':
    main()
