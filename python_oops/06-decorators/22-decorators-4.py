#!/usr/bin/env python

def decorator(inner):
    def inner_decorator(*args, **kwargs):
        print(args, kwargs)

    return inner_decorator


@decorator
def decorated(string_args):
    print("This happened : " + string_args)


if __name__ == "__main__":
    decorated("Hello, how are you?")

# This prints :
# # python 22-decorators-4.py
# ('Hello, how are you?',)
