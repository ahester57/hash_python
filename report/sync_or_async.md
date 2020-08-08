
## Asynchronous vs. Synchronous Decision



Little noticable difference in smaller task pools.

#### Synchronous 10,000 hashes
```
$ time python hash.py -c 10000 --small

About to do 10000 thing(s).
sync
Done with 10000 thing(s).

real    0m0.162s
user    0m0.015s
sys     0m0.000s

---------------------

$ time python hash.py -c 10000 --small

About to do 10000 thing(s).
sync
Done with 10000 thing(s).

real    0m0.161s
user    0m0.015s
sys     0m0.000s
---------------------
```

#### Asynchronous 10,000 hashes

```
$ time python hash.py -c 10000 --small --async

About to do 10000 thing(s).
async
Done with 10000 thing(s).


real    0m0.326s
user    0m0.000s
sys     0m0.000s

----

$ time python hash.py -c 10000 --small --async

About to do 10000 thing(s).
async
Done with 10000 thing(s).


real    0m0.315s
user    0m0.000s
sys     0m0.000s
---------------------
```

#### Synchronous 1,000,000 hashes
```
$ time python hash.py -c 1000000 --small

About to do 1000000 thing(s).
sync
Done with 1000000 thing(s).


real    0m0.901s
user    0m0.000s
sys     0m0.000s

---------------------

$ time python hash.py -c 1000000 --small

About to do 1000000 thing(s).
sync
Done with 1000000 thing(s).


real    0m0.892s
user    0m0.000s
sys     0m0.015s
---------------------
```

#### Asynchronous 1,000,000 hashes
```
$ time python hash.py -c 1000000 --small --async

About to do 1000000 thing(s).
async
Done with 1000000 thing(s).


real    0m21.017s
user    0m0.000s
sys     0m0.016s
---------------------
$ time python hash.py -c 1000000 --small --async

About to do 1000000 thing(s).
async

Do you want to quit? (y/N): n

Done with 1000000 thing(s).


real    0m23.824s
user    0m0.000s
sys     0m0.000s
---------------------
```


### Synchronous Average

```
1000000 / 0.9 = 1111111 hash/s
1000000 / 0.9 = 1111111 hash/s
------------------------------
average = 1,111,111 hash/s
```

### Asynchronous Average

```
1000000 / 21 = 47619 hash/s
1000000 / 23.8 =  42016 hash/s
------------------------------
average = 44,817 hash/s
```

Looks like synchronous is the winner, so we'll go with that.

SHA256 does not seem to fare well with async with my CPU, seems to be limited by the CPU.

CUDA processing would have been cool.

#### Specs For This Test

i5-3570k @ 4.16 GHz (29% usage)
8 GB RAM (29 MB usage)