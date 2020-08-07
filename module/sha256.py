import hashlib
import asyncio

class SHA256(object):
    def __init__(self, seed):
        self.seed = seed.encode()
        self.hashed_seed = None

    def sha256(self):
        """Hash"""
        self.hashed_seed = hashlib.sha256(self.seed)
        # print(self.hashed_hex)
    
    async def async_sha256(self):
        """Hash"""
        self.hashed_seed = hashlib.sha256(self.seed)
        # print(self.hashed_hex)

    @property
    def hashed_hex(self):
        return self.hashed_seed.hexdigest()