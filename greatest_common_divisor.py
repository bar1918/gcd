# -----------------------------------------------------------------------------
# Name:           greatest_common_divisor.py
#
# Description:    Computes greatest_common_divisor of two input integers
#
# Author:         Robbie Armitano
#
# Cobntributors:  <none>
#
# Copyright:      Robbie Armitano
# -----------------------------------------------------------------------------


def compute_gcd(int_a, int_b):
    #
    # Returns the greatest common divisor (gcd) of two integers:
    # int_a and int_b
    #
    # The algorithm is based on Euclid's Algorithm described in Knuth's
    # Art Art of Computer Programming Vol 2 (pages 316 Section 4.5.2)
    # This is algorithm B.
    # This implementation uses bit-wise evaluation of the even/oddness
    # and then uses division. No appreciable improvement was found when
    # division and multiplication by two was substituded with bit-wise shift
    # operations. Knuth's algorithm leveraged shift since it was
    # computationally more efficient in some computer architectures. The
    # original algorithm only required: addition and shift to compute the gcd.
    # I used multiplication and division for clarity.
    #
    # Returns:
    #       gcd if int_a and int_b are positive integer
    #       -1 if errors are found  (if int_a or int_b are not integers)
    #

    error_return_value = -1

    # Simple error checking.
    # Checks for int
    # ???? Need to check for long ????
    # ???? Need to check for float.is_integer(int_a) ????
    if ((type(int_a) != int) or (type(int_b) != int)):
        return error_return_value

    int_a = abs(int_a)
    int_b = abs(int_b)

    # End cases for recursion
    if (int_a == 0):
        return int_b

    if (int_b == 0):
        return int_a

    if (int_a == int_b):
        return int_a

    # Take each input and remove all factors of 2
    # If both are even factor out a 2
    if not ((int_a & 0x1) or (int_b & 0x1)):
        # Both int_a and int_b are even
        # Recursively call with int_a and int_b reduced by a factor of 2
        # At this point neither int_a or int_b can be zero
        # gcd value is multiplied by a factor of 2
            return 2 * compute_gcd(int_a / 2, int_b / 2)

    # Case of int_a is even and int_b is odd
    if not (int_a & 0x1):
        # recursively call with int_a factored by 2
        # At this point int_b will never have another factor of 2 and we
        # eliminate factors of two from future gcd computations
            return compute_gcd(int_a / 2, int_b)

    # Case of int_a is odd and int_b even
    if not (int_b & 0x1):
        # Recursively call with inb_b factored by 2
        # At this point int_a will never have another factor of 2 and we
        # eliminate factors of two from future gcd computations
        return compute_gcd(int_a, int_b / 2)

    # Neither of the integers have factors of two, both are odd.
    # (NOTE: both are odd so their difference is even and can be evenly
    # divided by 2.)
    # Reduce the larger integer
    if (int_a > int_b):
        return compute_gcd((int_a - int_b) / 2, int_b)
    else:
        return compute_gcd(int_a, (int_b - int_a) / 2)
