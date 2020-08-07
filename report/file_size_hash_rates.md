## Hash Rates at Various File Sizes

### Synchronous hashing the letter 't'

#### 1,000,000 times
```
$ time python hash.py -c 1000000 --small                                                                    

About to do 1000000 thing(s).
sync
Done with 1000000 thing(s).


real    0m2.363s
user    0m0.000s
sys     0m0.047s
```


#### 10,000,000 times
```
$ time python hash.py -c 10000000 --small

About to do 10000000 thing(s).
sync
Done with 10000000 thing(s).


real    0m19.277s
user    0m0.015s
sys     0m0.031s
```

#### 100,000,000 times
```
crashed: MemoryError
```
I tried making some adjustments to avoid this memory error, but my entire PC crashed doing so.



### Flops

1 hash/s requires the equivalent of 12,700 flop/s. [1]


>1 integer operation = 2 floating point operations
>
>1 hash = 6.35K integer operations
>
>1 hash = 12.7K floating point operations


[1] PetaFLOPS and how it relates to Bitcoin