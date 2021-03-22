from time import time
import math


def full_decorator(function):
    def nested_function(begin, exit):
        if begin < 0 or exit <= 0:
            raise ValueError("time is not negative nor zero")
        if isinstance(begin, str) or isinstance(exit, bool):
            raise ValueError(
                "this field requires numbers decluding (0, negatives)")
        start = time()
        function(begin, exit)
        end = time()
        print(f"Required Time to complete: {end - start} seconds")
    return nested_function


@full_decorator
def numbers_range(start, end):
    for number in range(start, end):
        print(number)


numbers_range(1, 100000)
