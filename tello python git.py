#!/usr/bin/env python
 
import socket
import time

i = 0
 
#Create a UDP socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1' , 8889)
 
#command-mode : 'command'
socket.sendto('command'.encode('utf-8'),tello_address)
print ('start')
 
socket.sendto('takeoff'.encode('utf-8'),tello_address)
print ('takeoff')
 
time.sleep(6)

socket.sendto('land'.encode('utf-8'),tello_address)
print ('land')
