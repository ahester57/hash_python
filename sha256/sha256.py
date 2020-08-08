# Python SHA256
## Austin Hester
## CS 5732
## UMSL 2020

import asyncio
import hashlib
import secrets


class SHA256(object):

    @staticmethod
    def sha256(what):
        """Hash"""
        return hashlib.sha256(what)
        # print(hashlib.sha256(what).hexdigest())
    
    @staticmethod
    async def async_sha256(what):
        """Hash"""
        return hashlib.sha256(what)
        # print(hashlib.sha256(what).hexdigest())
    
    @staticmethod
    def infinite_hashes():
        while True:
            seed = next(SHA256.LEGIT_SEED())
            hashval = SHA256.sha256(seed)
            yield seed, hashval
    
    @staticmethod
    def SMALL_SEED():
        value = "t".encode()
        while True:
            yield value

    @staticmethod
    def LARGE_SEED():
        value = 10000*"t".encode()
        while True:
            yield value

    @staticmethod
    def LEGIT_SEED():
        while True:
            yield secrets.token_bytes(16)
