d = {}
i = 0
built_in = dir(__builtins__)
# print(built_in)
for item in built_in:
    d[i] = item
    i += 1


for k in d.keys():
    index = k
    v = d.get(k)
    if not (v.endswith('Error') or v.endswith('Exception') or v.endswith('Warning')):
        #pass
        print(f'{index}:{v}')
        # print(str(help(v)).find(':'))
#
# print(StopIteration.__mro__)
# print(StopIteration.__class__)
# print(int.__class__)
# print(int.__qualname__)
# print(int.__bases__)
# s = range(3)
# i = 4
# s = range(i)
# print(repr(i))
# print(repr('a'))
#print(pass)

s = 'abc'
print(s)
b = s[2::-1]
print(b)

def print_all(list):
    for i in list:
        print(i)

# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)