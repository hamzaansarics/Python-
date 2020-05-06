from csv import reader
from csv import writer
with open("G:\kha.csv",'r') as parentfile:
  with open("G:\pak.csv",'w',newline="") as childfile:
      aa=reader(parentfile)
      oo=writer(childfile)
      for i in aa:
          oo.writerow(i)

