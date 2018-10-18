import mystats as ms
import numpy as np
# File: my_stat_test.py

np.random.seed(0)    # make sure everyone gets the same answers

int_list1 = [ 3, 4, 5, 4, 5, 2, 2, 1, 2, 1, 7, 8, 9, 10, 4, 0 ]

int_list2 = [ np.random.randint(1000) for i in range(1000) ]

float_list1 = [ 1.1, 2.3, 4.3, 6.7, 9.8, 3.3, 1.4, 1.8, 9.1, 5.6, 5.0 ]

float_list2 = list(np.random.rand(1000))

int_tup1 = ( 3, 1, 5, 4, 9, 9, 4, 4, 7, 1, 0, 2, 3 )

int_tup2 = tuple(np.random.randint(1000) for i in range(1000))

int_set1 = { 5, 6, 7, 4, 5, 4, 9, 8, 0, 1, 5, 4, 4, 2 }

int_set2 = { np.random.randint(1000) for i in range(1000) }

print("mean of int_list1:", ms.mean(int_list1))
print("stddev of int_list1:", ms.stddev(int_list1))
print("median of int_list1:", ms.median(int_list1))
print("mode of int_list1:", ms.mode(int_list1))

print("mean of int_list2:", ms.mean(int_list2))
print("stddev of int_list2:", ms.stddev(int_list2))
print("median of int_list2:", ms.median(int_list2))
print("mode of int_list2:", ms.mode(int_list2))

print("mean of float_list1:", ms.mean(float_list1))
print("stddev of float_list1:", ms.stddev(float_list1))
print("median of float_list1:", ms.median(float_list1))

print("mean of float_list2:", ms.mean(float_list2))
print("stddev of float_list2:", ms.stddev(float_list2))
print("median of float_list2:", ms.median(float_list2))

print("mean of int_tup1:", ms.mean(int_tup1))
print("stddev of int_tup1:", ms.stddev(int_tup1))
print("median of int_tup1:", ms.median(int_tup1))
print("mode of int_tup1:", ms.mode(int_tup1))

print("mean of int_tup2:", ms.mean(int_tup2))
print("stddev of int_tup2:", ms.stddev(int_tup2))
print("median of int_tup2:", ms.median(int_tup2))
print("mode of int_tup2:", ms.mode(int_tup2))

print("mean of int_set1:", ms.mean(int_set1))
print("stddev of int_set1:", ms.stddev(int_set1))
print("median of int_set1:", ms.median(int_set1))
print("mode of int_set1:", ms.mode(int_set1))

print("mean of int_set2:", ms.mean(int_set2))
print("stddev of int_set2:", ms.stddev(int_set2))
print("median of int_set2:", ms.median(int_set2))
print("mode of int_set2:", ms.mode(int_set2))

