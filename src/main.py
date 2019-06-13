# coding=utf-8
from FlaskServer import FlaskServer
from model import DBModelBase


def main():
    model = DBModelBase()

    FlaskServer(model).run()


if __name__ == '__main__':
    main()
