# Unit test for greatest_common_divisor.py
# import greatest_common_divisor

from greatest_common_divisor import compute_gcd
import time
import random


# Unit test for greatest_common_divisor.py

 
def simple_test_compute_gcd() :
# Returns -1 if any errors occur
# Add more test inputs
# Test vectors are setup as:
#     [expected output, first_int, second_int]

    test_vector = [[0,0,0]]
    test_vector.append([1,1,1])
    test_vector.append([0,0,0])
    test_vector.append([1,1,1])
    test_vector.append([3,3,0])
    test_vector.append([4,0,4])
    test_vector.append([1,4,1])
    test_vector.append([1,3,4])
    test_vector.append([111,111,111])
    test_vector.append([1,-3,-4])
    test_vector.append([34,40902,24140])
    test_vector.append([1024,-1024,4096])
    test_vector.append([-1,-1024.4343,4096.34343])
    test_vector.append([2147483647,2 ** 31 - 1,2 ** 31 - 1])
    test_vector.append([2147483648,2 ** 31,2 ** 31])
    test_vector.append([2147483649,2 ** 31 + 1,2 ** 31 + 1])
    test_vector.append([2**62,2 ** 62,2 ** 62])
    test_vector.append([-1,2 ** 63 - 1,2 ** 63 - 1])
    test_vector.append([-1,2 ** 63,2 ** 63])
    error_num = 0
    
    for test_index in range(len(test_vector)) :
        current_test_value = test_vector[test_index]
        if current_test_value[0] != compute_gcd(current_test_value[1], current_test_value[2]) :
            print  "Error occured with following values"
            print "Inputs:         ", current_test_value[1], current_test_value[2]
            print "GCD output:     ", compute_gcd(current_test_value[1], current_test_value[2])
            print "Correct output: ", current_test_value[0]
            print
            error_num = -1

    return error_num

def loop_test_compute_gcd(iterations) :
    for i in range(iterations) :
        compute_gcd(int(random.randrange(0,2^31)), int(random.randrange(0,2^31)))


# Run some the test 
# No profiling has been done.

current_time = time.time()
start_time = current_time

if (simple_test_compute_gcd() == -1) :
    print "Error occured"
else :
    print "No errors"
    
# Need to perform more performance testing
loop_test_compute_gcd(100000)

end_time = time.time() 
elapse_time = end_time - start_time 
print elapse_time



