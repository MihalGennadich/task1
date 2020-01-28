import numpy as np
import sys
q = sys.argv[1]
w = open(q)
e = w.readlines()
r = list(map(int, e))
t = np.array(r)
y = sum(r) / 2
per90 = np.percentile(t, 90)   #Perc calc
mediana = np.percentile(t, 50)  #Mediana

print('%.2f' % per90, '\n%.2f' % mediana, '\n%.2f' % min(r), '\n%.2f' % max(r), '\n%.2f' % y)

