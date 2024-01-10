# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
X,Y=list(map(float,input().split()))
if X == 1:
    c= Y*4.00
    print('Total: R$ ''%.2f'%c)
if X == 2:
    c= Y*4.5
    print('Total: R$ ''%.2f'%c)
if X == 3:
    c= Y*5
    print('Total: R$ ''%.2f'%c)
if X == 4:
    c= Y*2
    print('Total: R$ ''%.2f'%c)
if X == 5:
    c= Y*1.50
    print('Total: R$ ''%.2f'%c)