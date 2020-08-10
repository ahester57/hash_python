# Python SHA256
## Austin Hester
## CS 5732
## UMSL 2020

import asyncio
import sys
import time

from hash_python import sha256


class App(object):

    def __init__(self, args):
        """
        Initialize variables used by the app
        :param args: command line arguments
        :type args: argparse.Namespace
        """
        self.args = args
    
    @staticmethod
    def find_birthday(birthday):
        # find the birthday
        birthday_length = len(birthday)
        print("Looking for hashes beginning with '{}'".format(birthday))
        start = time.time()
        while True:
            seed, hash = next(sha256.SHA256.infinite_hashes())
            hashhex = hash.hexdigest()
            for b in range(birthday_length, 4, -1):
                if hashhex[0:b] == birthday[0:b]:
                    print("WAMOO:\t{}".format(b))
                    print("Seed:\t{}".format(seed.hex()))
                    print("Hash:\t{}".format(hash.hexdigest()))
                    end = time.time()
                    print("Time:\t{}".format(end - start))

    async def do_a_few_things_at_once(self, how_many_things=5):
        """
        :param how_many_things: How many things to do
        :type how_many_things: int
        :return: None
        """
        # Get the seed
        seed = sha256.SHA256.LEGIT_SEED()

        if self.args.enable_birthday:
            App.find_birthday(self.args.enable_birthday)
        else:
            if self.args.enable_small_value:
                seed = sha256.SHA256.SMALL_SEED()
            elif self.args.enable_large_value:
                seed = sha256.SHA256.LARGE_SEED()
            print("About to do {} thing(s).".format(how_many_things))
            if (self.args.enable_async):
                tasks_list = []
                loop = asyncio.get_event_loop()
                print('async')
                tasks_list = (sha256.SHA256.async_sha256(next(seed)) for o in range(how_many_things))
                asyncio.gather(*tasks_list)
            else:
                print('sync')
                for o in range(how_many_things):
                    sha256.SHA256.sha256(next(seed))
            print("Done with {} thing(s).".format(how_many_things))

    def validate_input_args(self):
        """
        Validate whether the command line arg 'count' is a number >= 0
        :return: True or False
        :rtype: bool
        """
        count_valid = False
        try:
            c = int(self.args.count)
            if c >= 0:
                count_valid = True
            else:
                print("'count' must be greater than or equal to 0.")
        except ValueError:
            print("'count' must be a number.")
        birthday_valid = False
        try:
            birthday = self.args.enable_birthday
            if birthday is not None:
                int(birthday, 16)
                if len(birthday) < 5:
                    print("Birthday must be at least 5 characters.")
                elif len(birthday) > 64:
                    print("Birthday must be at most 64 characters.")
                else:
                    birthday_valid = True
            else:
                birthday_valid = True
        except ValueError:
            print("'birthday' must be hexadecimal.")
        except TypeError:
            print("'birthday' must be provided.")
        return count_valid and birthday_valid

    async def start(self):
        """
        Entry point of the App
        """
        print()
        # Validate the CLI input
        if not self.validate_input_args():
            sys.exit(1)
        # Proceed if validated
        how_many = int(self.args.count)
        await self.do_a_few_things_at_once(how_many_things=how_many)
        print()


if __name__ == '__main__':
    print("This class cannot be called directly.")
    sys.exit(1)

