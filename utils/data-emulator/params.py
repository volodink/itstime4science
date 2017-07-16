import sys
import argparse


class Parser:
    def createParser(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-i', '--ip', default="localhost")
        self.parser.add_argument('-p', '--port', default=5000, type=int)

        return self.parser


if __name__ == "__main__":
    parser = Parser()
    argv = parser.createParser()
    namespace = argv.parse_args(sys.argv[1:])

    print(namespace.ip)
    print(namespace.port)
