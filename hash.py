# Python SHA256
## Austin Hester
## CS 5732
## UMSL 2020

import argparse
import asyncio
import signal
import sys
import time

from sha256 import sha256


class App(object):

    def __init__(self, args):
        """
        Initialize variables used by the app
        :param args: command line arguments
        :type args: argparse.Namespace
        """
        self.args = args
    
    @staticmethod
    def find_birthday(birthday="03011030"):
        # find the birthday
        birthday_length = len(birthday)
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
        print("About to do {} thing(s).".format(how_many_things))
        # Get the seed
        seed = sha256.SHA256.LEGIT_SEED()

        
        if self.args.enable_birthday:
            App.find_birthday("0202020202020202020202020202020202")
        else:
            if self.args.enable_small_value:
                seed = sha256.SHA256.SMALL_SEED()
            elif self.args.enable_large_value:
                seed = sha256.SHA256.LARGE_SEED()
            tasks_list = []
            if (self.args.enable_async):
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
        try:
            c = int(self.args.count)
        except ValueError:
            return False
        if c >= 0:
            return True
        return False

    async def start(self):
        """
        Entry point of the App
        """
        print()
        # Validate the CLI input
        if not self.validate_input_args():
            print("'count' must be a number greater than or equal to 0.")
            sys.exit(1)
        # Proceed if validated
        how_many = int(self.args.count)
        await self.do_a_few_things_at_once(how_many_things=how_many)
        print()


# This global variable is to keep track of multiple presses of Ctrl^C
handling_sigint = False


# This function handles the interrupt signal when Ctrl^C is pressed
def signal_handler(signal_num=None, frame=None):
    """Gracefully handle a SIGINT - triggered by Ctrl+c"""
    def flush():
        sys.stderr.write("\n")
        sys.stderr.flush()
    try:
        global handling_sigint
        if handling_sigint:
            # If they give another interrupt signal during handling, exit
            flush()
            sys.exit()
        else:
            handling_sigint = True
        flush()
        ans = '.'
        while ans and ans not in 'nN':
            sys.stderr.write("Do you want to quit? (y/N): ")
            sys.stderr.flush()
            try:
                ans = sys.stdin.readline().strip()
            except RuntimeError:
                # avoid crashing due to standard out collisions
                pass
            if ans and ans in 'yY':
                sys.exit()
        handling_sigint = False
        flush()
    except RuntimeError:
        handling_sigint = False
        pass

# Handles command line arguments
def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


# This 'nameguard' runs App.start() if this file is called directly from python
if __name__ == '__main__':
    # Parser allows the use of command line arguments and also generates help
    # when running the app with '-h' or '--help' flag
    parser = argparse.ArgumentParser(description='This app does stuff.')
    # The count argument is optional and defaults to 5
    parser.add_argument('-c', '--count', dest='count', default=5, const=True, nargs='?',
                        help='How many things to do at once.')
    parser.add_argument("--async", dest='enable_async', type=str2bool, nargs='?',
                        const=True, default=False,
                        help="--async [true|FALSE]")
    parser.add_argument("--small", dest='enable_small_value', type=str2bool, nargs='?',
                        const=True, default=False,
                        help="--single [true|FALSE]")
    parser.add_argument("--large", dest='enable_large_value', type=str2bool, nargs='?',
                        const=True, default=False,
                        help="--large [true|FALSE]")
    parser.add_argument("--birthday", dest='enable_birthday', type=str2bool, nargs='?',
                        const=True, default=False,
                        help="--birthday [true|FALSE]")                        
    # Set the app to handle interrupt signal with our custom signal handler
    signal.signal(signal.SIGINT, signal_handler)
    # Initialize the app with the CLI arguments
    app = App(parser.parse_args())
    try:
        asyncio.run(app.start())
    except EOFError:
        # Handle presses of Ctrl^D gracefully
        print("^D")