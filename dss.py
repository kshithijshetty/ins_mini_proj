import random
import hashlib
from Crypto.Util.number import getPrime

class SimpleDSA:
    def __init__(self):
        # Fixed 1024-bit parameters for simplicity
        self.p = 0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1
        self.q = 0xf4f47f05794b256174bba6e9b396a7707e563c5b
        self.g = 0x5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291
        self.x = random.randint(1, self.q - 1)  # private key
        self.y = pow(self.g, self.x, self.p)    # public key

    def sign(self, message):
        h = int(hashlib.sha1(message.encode()).hexdigest(), 16)
        
        while True:
            k = random.randint(1, self.q - 1)
            r = pow(self.g, k, self.p) % self.q
            if r == 0:
                continue
            
            try:
                s = (pow(k, -1, self.q) * (h + self.x * r)) % self.q
            except ValueError:
                continue
            
            if s != 0:
                break
        
        return (r, s)

    def verify(self, message, r, s):
        if not (0 < r < self.q and 0 < s < self.q):
            return False
        
        h = int(hashlib.sha1(message.encode()).hexdigest(), 16)
        w = pow(s, -1, self.q)
        u1 = (h * w) % self.q
        u2 = (r * w) % self.q
        v = (pow(self.g, u1, self.p) * pow(self.y, u2, self.p)) % self.p % self.q
        
        return v == r