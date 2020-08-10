
import argparse
import asyncio
import signal
import sys

from hash_python import App


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

# Handles boolean command line arguments
def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


# Add CLI arguments to the parser
def add_cli_arguments(parser):
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
    parser.add_argument("--birthday", dest='enable_birthday', const=True, nargs='?',
                        default=None, help="--birthday <hex_value>")


# This 'nameguard' runs App.start() if this file is called directly from python
if __name__ == '__main__':
    # Parser allows the use of command line arguments and also generates help
    # when running the app with '-h' or '--help' flag
    parser = argparse.ArgumentParser(description='This app does stuff.')
    add_cli_arguments(parser)
    # Set the app to handle interrupt signal with our custom signal handler
    signal.signal(signal.SIGINT, signal_handler)
    # Initialize the app with the CLI arguments
    app = App(parser.parse_args())
    try:
        asyncio.run(app.start())
    except EOFError:
        # Handle presses of Ctrl^D gracefully
        print("^D")
