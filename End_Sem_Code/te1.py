import pandas as pd
import os
from queue import Queue
q=Queue()

def get_padded_string(num):
    st=str(num)
    if len(st)==2:
        return st
    else:
        return '0'+st

q.put(('varsha','1801cs69'))
q.put(('sunny','180ME45'))

while q.empty()==False:
	x=q.get()
	print(x)


	