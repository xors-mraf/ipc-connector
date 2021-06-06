# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import hashlib
import random
import math
RAND_TABLE_SIZE=1024
def merkle_tree(li):
 for l in li:
    l=(hashlib.sha256(l.encode('utf-8')).hexdigest())
 for i in range(int(math.log(RAND_TABLE_SIZE,2))):
     j=0
     while j<(RAND_TABLE_SIZE/math.pow(2,i)):
       print(i)
       if(j+2<=RAND_TABLE_SIZE/math.pow(2,i)):
        temp=li[j]+li[j+1]
        li[int(j/2)] =hashlib.sha256(temp.encode('utf-8')).hexdigest()
        j+=2

 return li[0]


li=[]
if __name__=="__main__":
   for i in range(RAND_TABLE_SIZE):
       li.append(bin(random.randint(100,999)))

   print(merkle_tree(li))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
