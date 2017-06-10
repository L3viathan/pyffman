import pickle
import sys

class BitWriter(object):
    """from: https://stackoverflow.com/a/10691412/1016216"""
    def __init__(self, f):
        self.accumulator = 0
        self.bcount = 0
        self.out = f

    def __del__(self):
        try:
            self.flush()
        except ValueError:   # I/O operation on closed file
            pass

    def _writebit(self, bit):
        if self.bcount == 8:
            self.flush()
        if bit > 0:
            self.accumulator |= 1 << 7-self.bcount
        self.bcount += 1

    def writebits(self, bits, n):
        while n > 0:
            self._writebit(bits & 1 << n-1)
            n -= 1

    def flush(self):
        self.out.write(bytearray([self.accumulator]))
        self.accumulator = 0
        self.bcount = 0

with open("coding.dat", "rb") as f:
    code = pickle.load(f)

with open(sys.argv[1]) as f:
    payload = f.read()

with open("output.dat", "wb") as f:
    writer = BitWriter(f)
    while payload:
        token = max((tkn for tkn in code if payload.startswith(tkn)), key=len)
        for bit in code[token]:
            writer.writebits(int(bit), 1)
        payload = payload[len(token):]
    for bit in code["END"]:
        writer.writebits(int(bit), 1)
    writer.flush()
