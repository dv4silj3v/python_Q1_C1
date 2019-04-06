import time

begin = time.time()

for i in range(10000000):
    pass

end = time.time()

print(end - begin)