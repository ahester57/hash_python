### Asynchronous vs. Synchronous Decision

[Asynchronous vs. Synchronous Decision](sync_or_async.md)
Little noticable difference in smaller task pools.

#### Synchronous 10000 hashes
```
$ time python hash.py -c 10000 --async false

About to do 10000 thing(s).
sync
Done with 10000 thing(s).


real    0m1.254s
user    0m0.015s
sys     0m0.109s
---------------------
$ time python hash.py -c 10000 --async false

About to do 10000 thing(s).
sync
Done with 10000 thing(s).
 
 
real    0m1.029s
user    0m0.000s
sys     0m0.062s
---------------------
```

#### Asynchronous 1000 hashes

```
$ time python hash.py -c 10000 --async true

About to do 10000 thing(s).
async
Done with 10000 thing(s).


real    0m1.143s
user    0m0.015s
sys     0m0.015s
---------------------
$ time python hash.py -c 10000 --async true

About to do 10000 thing(s).
async
hi
Done with 10000 thing(s).


real    0m1.381s
user    0m0.000s
sys     0m0.031s
---------------------
```

#### Synchronous 1000000 hashes
```
$ time python hash.py -c 1000000 --async false

About to do 1000000 thing(s).
sync
Done with 1000000 thing(s).


real    0m56.287s
user    0m0.000s
sys     0m0.031s
---------------------
$ time python hash.py -c 1000000 --async false

About to do 1000000 thing(s).
sync
Done with 1000000 thing(s).


real    1m3.361s
user    0m0.000s
sys     0m0.061s
---------------------
```

#### Asynchronous 1000000 hashes
```
$ time python hash.py -c 1000000 --async true

About to do 1000000 thing(s).
async
Done with 1000000 thing(s).


real    1m12.524s
user    0m0.000s
sys     0m0.077s
---------------------
$ time python hash.py -c 1000000 --async true

About to do 1000000 thing(s).
async
Done with 1000000 thing(s).


real    1m17.502s
user    0m0.000s
sys     0m0.047s
---------------------
```

Looks like synchronous is the winner, so we'll go with that.
