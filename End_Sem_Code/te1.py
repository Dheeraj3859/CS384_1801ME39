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

def extract_number(st):
    x=st.split('_')
    x1=x[1].split('.')
    re=x1[0][1:]
    return re
s="Group_G01.csv"
x=int(extract_number(s))
if x==1:
	print("ok")