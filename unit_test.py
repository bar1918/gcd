# Unit test for greatest_common_divisor.py
# import greatest_common_divisor

from greatest_common_divisor import compute_gcd
import time

# Unit test for greatest_common_divisor.py

 
def simple_test_compute_gcd(input_a, input_b) :
    
    print "Inputs:     ", input_a, input_b
    print "GCD output: ", compute_gcd(input_a, input_b)
    print




current_time = time.time()
start_time = current_time


simple_test_compute_gcd(0,0)
simple_test_compute_gcd(1,1)
simple_test_compute_gcd(3,0)
simple_test_compute_gcd(0,4)
simple_test_compute_gcd(4,1)
simple_test_compute_gcd(3,4)
simple_test_compute_gcd(111,111)
simple_test_compute_gcd(-3,-4)
simple_test_compute_gcd(40902,24140)
simple_test_compute_gcd(-1024,4096)
simple_test_compute_gcd(-1024.4343,4096.34343)



end_time = time.time() 
elapse_time = end_time - start_time 
print elapse_time



