Returns the greatest common divisor (gcd) of two integers int_a and int_b

The algorithm is based on Euclid's Algorithm described in Knuth's 
Art of Computer Programming Vol. 2 (pages 316 Section 4.5.2)
This is algorithm "B" from the book.

This implementation uses bit-wise evaluation of the even/oddness
and then uses division. No appreciable improvement was found when division 
and multiplication was substituted with bit-wise shift operations.

Knuth's algorithm leveraged shift since it was computationally more efficient
in some computer architectures. The algorithm only required: Addition and shift
was required to compute the gcd.
