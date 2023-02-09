# Rudzeris
import os
import keyboard
import time

Moves=('up','down','left','right')
defaultmaps =  """
||||||||||||||||
O     ||||| ||||
||||| |      |||
|     || ||| |||
|| ||    | | |||
||   | ||| | |||
|||||| ||| |  ||
|          || ||
|| ||| |||    ||
|||||| ||||||X||
||||||||||||||||
"""

"""
      ||
        
     | |
|||||| |||| |
|     i      |
|||||| |||
     | |
     |||
"""

def showMap(maps):
    for a in maps:
        for b in a:
            print(b,end='')
        print()

def showPlayer(maps,x,y):
    if x<0 or y<0:
        return
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            print(maps[i][j],end='')
        print()

def Play(a):
    a=a.replace('X','i')
    b=a.split('\n')
    for i in range(0,len(b)):
        b[i]=list(b[i])
    x=-1
    y=-1
    for i in range(0,len(b)):
        for j in range(0,len(b[i])):
            if b[i][j]=='i':
                x=i
                y=j
    return b,x,y

def Clear():
    os.system('cls')

def move(maps, nx,ny,x,y):
    if nx:
        if(maps[x+nx][y]!='|'):
            if(maps[x+nx][y]=='O'):
                return maps,-2,-2
            q=maps[x]
            q[y]=' '
            maps[x]=q
            x=nx+x
            maps[x][y]='i'
    elif ny:
        if maps[x][y+ny]!='|':
            if(maps[x][y+ny]=='O'):
                return maps,-2,-2
            q=maps[x]
            q[y]=' '
            maps[x]=q
            y=ny+y
            maps[x][y]='i'
    return maps,x,y

def menu():
    maps=""
    px=-1
    py=-1
    while True:
        Clear()
        print('1 - Начать игру\t2 - Выйти из игры')
        showPlayer(maps,px,py)
        time.sleep(0.2)
        x=keyboard.read_key()
        if x=='1' or x=='2':
            if x=='1':
                maps,px,py=Play(defaultmaps)
            else:
                break
        elif x in Moves and maps!="":
            if(px==-2 and py==-2):
                print("Вы победили")
                break
            elif x==Moves[0]:
                maps,px,py=move(maps,-1,0,px,py)
            elif x==Moves[1]:
                maps,px,py=move(maps,1,0,px,py)
            elif x==Moves[2]:
                maps,px,py=move(maps,0,-1,px,py)
            elif x==Moves[3]:
                maps,px,py=move(maps,0,1,px,py)
    qa=input("Хотите повторить? >> ")
    if(qa=='да' or qa=='Да'):
        menu()
menu()
