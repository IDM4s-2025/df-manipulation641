import time
import numpy as np

start=time.time()

total=0
for i in np.arange(10000000):
    total = i+total
print(total)
end =time.time()
print(end -start)

start= time.time()
print(np.sum(np.arange(10000000)))

end=time.time()
print(end-start)