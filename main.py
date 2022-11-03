def say_hello(index):
    print(index, 'Hello, World')

x = 1
for i in range(10):
    say_hello(x)
    x = x + 1
    
print('done!')