import sys
import json
import socket
import argparse


def check_service(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((host, port)) == 0


def main():
    parser = argparse.ArgumentParser(description='Test if a service is up')
    parser.add_argument('config_file',
                        help='file path to config file')
    parser.add_argument('--host',
                        help='host name')
    args = parser.parse_args()

    config_file = args.config_file
    with open(config_file, 'r') as cf:
        config = json.load(cf)

    host = args.host
    for service in config['service_list']:
        port = service.get('port')
        if check_service(host, port):
            print("{0} is up".format(service.get('name')))
        else:
            print("{0} is down".format(service.get('name')))


if __name__ == '__main__':
    main()
