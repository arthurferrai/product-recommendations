# coding=utf-8
from argparse import ArgumentParser

from FlaskServer import FlaskServer
from model import SQLiteModel


def main(host, port):
    model = SQLiteModel()

    FlaskServer(model, host, port).run()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('host', help='host used to bind to the server')
    parser.add_argument('port', help='port used by the server', type=int)
    args = parser.parse_args()
    main(args.host, args.port)
