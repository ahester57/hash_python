# Python SHA256
## Austin Hester
## CS 5732
## UMSL 2020

import asyncio
import hashlib
import secrets


class SHA256(object):
    def __init__(self, seed):
        self.seed = seed.encode()
        self.hashed_seed = None

    def sha256(self):
        """Hash"""
        self.hashed_seed = hashlib.sha256(self.seed)
        print(self.hashed_hex)
    
    async def async_sha256(self):
        """Hash"""
        self.hashed_seed = hashlib.sha256(self.seed)
        print(self.hashed_hex)

    @property
    def hashed_hex(self):
        return self.hashed_seed.hexdigest()
    
    @staticmethod
    def SMALL_SEED():
        while True:
            yield "t"

    @staticmethod
    def LARGE_SEED():
        while True:
            yield "t"*10000

    @staticmethod
    def LEGIT_SEED():
        while True:
            yield secrets.token_hex(16)