import time

inicio = time.time()
if True:
	for i in range(10000):
		for j in range(100):
			pass
fin = time.time()
print(round(fin-inicio,3))