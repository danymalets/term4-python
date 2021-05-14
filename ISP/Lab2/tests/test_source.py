glob = 100


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def func(x):
    return glob - x


class A:
    a = 123

    def sqr(self, x):
        return self.a + x * x


