import os
from tkinter import filedialog
from tkinter import Tk
from tkinter.constants import TRUE
from numpy import dtype, true_divide, where
import pandas as pd
import numpy as np

def abs(a):
    if a>=0:
        return(a)
    else:
        return(-a)

def sort_num(x):
    return x

root=Tk()
root.withdraw()
file =  filedialog.askopenfilenames(initialdir ="C:/",title = "Select CSV")
memofile = filedialog.askopenfilenames(initialdir ="C:/",title = "Select txt")
memofileopne= open(memofile[0],'w')
pi1=57.29577951
file = tuple(sorted(file,key=sort_num))


for a in range(len(file)):
    wd = pd.read_csv(file[a],sep=';')
    for line in range(int(len(wd))):
        
        longitude=wd['Computer Timestamp']
        latitude=wd['Recording Name']

        if line % 2 == 1:
            latitude[line]=float(latitude[line])
            memo=[str(longitude[line]*pi1),str(latitude[line]*pi1)]
            memobreak=True
            try:
                if float(longitude[line])<0.1:
                    memobreak = False
                    break

                if abs((longitude[line])-(longitude[line+2])) >0.00005 and float(longitude[line+2]) != float(longitude[line]) and memobreak !=False:
                    print(longitude[line]-longitude[line+2])

                    #print(file[a])
                    #print(longitude[line])
                    #print("line-2  :",longitude[line-2])
                    #print("line+2 : ",longitude[line+2])
                    #memofileopne = open('1'+memofile[0],'w')
                    #print(memo,end='',file=memofileopne)
                    #print(file[a])
                    #print(longitude[line] * pi1)
                    #print(longitude[line])
                    #print('line-2 : ',longitude[line+2])
                    #print('line-2 - line', abs(longitude[line]-longitude[line+2]))
                    #print(abs((longitude[line]*pi1)-(longitude[line+2]*pi1)))



                elif memobreak!=False:
                    memo=','.join(memo)
                    print(memo,end=' ',file=memofileopne)


            except:
                continue

                
    '''
    longitude=wd['Computer Timestamp']
    latitude=wd['Recording Name']
    #sheet = wb.get_sheet_by_name('Sheet1')
    #sheet.delete_rows(1)
    print(longitude[1::2])
    print(latitude[1::2])
    '''

os.system("pause")





#57.29577951
 