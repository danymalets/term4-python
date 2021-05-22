from serializer_lib.factory.factory import create_serializer

ser = create_serializer("json")
d = ser.load("my_tests/z1.json")
fib = ser.load("my_tests/z2.json")
func = ser.load("my_tests/z3.json")
A = ser.load("my_tests/z4.json")
a = ser.load("my_tests/z5.json")

print(d)
print(fib(5))
print(func(1))
print(A())
print(a.sqr(5))
