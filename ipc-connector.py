# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import socket
import threading
import time
import sys
import os
import queue
import logging

#///////////////////////////////
def send_socket(clientsocket,addr,timeout,q,x):
  time_out_counter = 0
  while (True):
    seconds = time.time()
    time.sleep(0.000001)
    if not q.empty():
        n = clientsocket.send(q.queue[0])
        if (n == len(q.queue[0])):
            q.get()
            x = False
        if (n == 0):
         if (x == False):
            time_out_counter = int(seconds)
            x = True
         if (time_out_counter + timeout == int(seconds)):
            print(f'connection by address:{addr} timedout')
            return
    elif (q.empty()):
        if (x == False):
            time_out_counter = int(seconds)
            x = True
        if (time_out_counter + timeout == int(seconds)):
            print(f'connection by address:{addr}timedout.')
            return
#//////////////////////////////////
def recv_socket(clientsocket,addr,timeout,buffer_size,q,x):
    time_out_counter=0
    #x is timeout checking varible thath is
    while True:
      seconds=time.time()
      data = clientsocket.recv(buffer_size)
      if (data != b''):
              q.put(data)
              x = False

      if (data == b''):
              if (x == False):
                  time_out_counter = int(seconds)
                  x = True
              if (time_out_counter + timeout == int(seconds)):
                  print(f'connection by address:{addr} timedout')
                  return




      #print(int(seconds))



#///////////////////////////////////

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print(f'ipc connection by *M.R.A.F*\n')
host=str(input('welcome to ipc communication configuration please enter host for listening:'))
port=int(input('hello please enter port for listening:'))
timeout=int(input('enter timeout for connection in seconds:'))
buffer_size=int(input('enter buffer size for recieving(in byte):'))


s.bind((host,port))
s.listen(5)

print('*listening on:'+host+':'+str(port))
tokens1={}
tokens2={}
while (True):
  conn, addr = s.accept()
  print('#connection*'+str(addr)+'*accepted.')
  data=conn.recv(39)
  token=data.decode('ascii')
  if (token not in tokens1 and token not in tokens2):
    q = queue.Queue()
    tokens1[token]=q
    del q
    qq= queue.Queue()
    tokens2[token] = qq
    del qq
  else:
      tokens1[token],tokens2[token]=tokens2[token],tokens1[token]

  timeout_check=False
  t1 = threading.Thread(target=recv_socket, args=(conn, addr, timeout,buffer_size,tokens1[token],timeout_check))
  t2=  threading.Thread(target=send_socket,args=(conn,addr,timeout,tokens2[token],timeout_check))
  t1.start()
  t2.start()





s.close()







