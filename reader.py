import sys
import pickle

class BitReader(object):
    def __init__(self, f):
        self.input = f
        self.accumulator = 0
        self.bcount = 0
        self.read = 0

    def _readbit(self):
        if not self.bcount:
            a = self.input.read(1)
            if a:
                self.accumulator = ord(a)
            self.bcount = 8
            self.read = len(a)
        rv = (self.accumulator & (1 << self.bcount-1)) >> self.bcount-1
        self.bcount -= 1
        return rv

    def readbits(self, n):
        v = 0
        while n > 0:
            v = (v << 1) | self._readbit()
            n -= 1
        return v

with open("coding.dat", "rb") as f:
    code = pickle.load(f)
    rcode = {y: x for x, y in code.items()}

with open(sys.argv[1], "rb") as f:
    reader = BitReader(f)
    s = ""
    while True:
        while s not in rcode:
            bit = str(reader.readbits(1))
            if not reader.read:
                break
            s += bit
        ch = rcode.get(s, '')
        if ch == 'END':
            break
        print(ch, flush=True, end="")
        if not reader.read:
            break
        s = ""
