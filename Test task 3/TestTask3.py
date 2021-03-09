import sys
import hashlib
from importlib import reload

class IntegrityChecker:
    inputFilename = ""
    dirname = ""
    isproper = False

    hashAlgorithms = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256
    }

    def __init__(self, filename = "file.txt", dirname = "C:\Program Files"):
        self.inputFilename = filename
        self.dirname = dirname

        if not (self.dirname[-1] in ['\\', '/']):
            self.dirname += '\\'
            print("new one: ", self.dirname)

        try:
            open(filename)
        except FileNotFoundError:
            print("ERROR: cannot open input file: ", FileNotFoundError.errno)
            return

        try:
            open(filename)
        except FileNotFoundError:
            print("ERROR: cannot open input file: ", FileNotFoundError.errno)
            return

        self.isproper = True

    def UpdateFiles(self, filename, dirname):
        self.inputFilename = filename
        self.dirname = dirname

        self.isproper = False

        try:
            open(filename)
        except FileNotFoundError:
            print("ERROR: cannot open input file: ", FileNotFoundError.errno)
            return

        try:
            open(filename)
        except FileNotFoundError:
            print("ERROR: cannot open input file: ", FileNotFoundError.errno)
            return

        self.isproper = True

    def __checkFile(self, filename, properHash, algorithm):
        if not self.isproper:

            return
        hash = self.hashAlgorithms[algorithm]()

        with open(self.dirname + filename, "rb") as reader:
            for chunk in iter(lambda: reader.read(4096), b''):
                hash.update(chunk)

        return hash.hexdigest() == properHash


    def CheckIntegrity(self):
        with open(self.inputFilename) as reader:
            while True:
                input = reader.readline()

                if input == '':
                    break

                input = input.split()

                try:
                    open(self.dirname + input[0])
                except FileNotFoundError:
                    print(input[0], "NOT FOUND")
                    continue


                print(input[0], end=' ')

                if self.__checkFile(input[0], input[2], input[1]):
                    print("OK")
                else:
                    print("FAIL")

if __name__ == "__main__":
    filename = sys.argv[1]
    dirname = sys.argv[2]

    checker = IntegrityChecker(filename, dirname)
    checker.CheckIntegrity()
