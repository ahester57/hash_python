## Hash Rates at Various File Sizes

Way faster to hash a single 't' than 10k of them.

### Synchronous hashing 10,000 of the letter 't'

#### 1,000,000 times
```
$ time python hash.py -c 1000000 --large

About to do 1000000 thing(s).
sync
Done with 1000000 thing(s).


real    0m57.409s
user    0m0.000s
sys     0m0.015s

------------------------------

$ time python hash.py -c 1000000 --large

About to do 1000000 thing(s).
sync
Done with 1000000 thing(s).


real    0m57.964s
user    0m0.000s
sys     0m0.000s
------------------------------
```

#### 10,000,000 times
```
$ time python hash.py -c 10000000 --large

About to do 10000000 thing(s).
sync
Done with 10000000 thing(s).


real    10m14.585s
user    0m0.000s
sys     0m0.000s

------------------------------

$ time python hash.py -c 10000000 --large

About to do 10000000 thing(s).
sync
Done with 10000000 thing(s).


real    9m57.213s
user    0m0.015s
sys     0m0.000s
```

### Synchronous hashing the letter 't'

#### 1,000,000 times
```
$ time python hash.py -c 1000000 --small

About to do 1000000 thing(s).
sync
Done with 1000000 thing(s).


real    0m0.905s
user    0m0.000s
sys     0m0.015s

------------------------------

$ time python hash.py -c 1000000 --small

About to do 1000000 thing(s).
sync
Done with 1000000 thing(s).


real    0m0.907s
user    0m0.000s
sys     0m0.000s
------------------------------
```

#### 10,000,000 times
```
$ time python hash.py -c 10000000 --small

About to do 10000000 thing(s).
sync
Done with 10000000 thing(s).


real    0m7.801s
user    0m0.015s
sys     0m0.000s

------------------------------

$ time python hash.py -c 10000000 --small

About to do 10000000 thing(s).
sync
Done with 10000000 thing(s).


real    0m7.600s
user    0m0.000s
sys     0m0.000s
------------------------------
```

#### 100,000,000 times
```
$ time python hash.py -c 100000000 --small

About to do 100000000 thing(s).
sync
Done with 100000000 thing(s).


real    1m16.866s
user    0m0.000s
sys     0m0.000s

------------------------------

$ time python hash.py -c 100000000 --small

About to do 100000000 thing(s).
sync
Done with 100000000 thing(s).


real    1m14.037s
user    0m0.015s
sys     0m0.000s
------------------------------
```

#### 1,000,000,000 times
```
$ time python hash.py -c 1000000000 --small

About to do 1000000000 thing(s).
sync
Done with 1000000000 thing(s).


real    13m8.912s
user    0m0.000s
sys     0m0.015s
------------------------------
```

### Flops

1 hash/s requires the equivalent of 12,700 flop/s. [1]


>1 integer operation = 2 floating point operations
>
>1 hash = 6.35K integer operations
>
>1 hash = 12.7K floating point operations


[1] PetaFLOPS and how it relates to Bitcoin


#### Specs For This Test

i5-3570k @ 4.16 GHz (29% usage)
8 GB RAM (29 MB usage)
