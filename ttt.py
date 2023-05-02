ttt = ' 7 | 8 | 9\n--- --- ---\n 4 | 5 | 6\n--- --- ---\n 1 | 2 | 3'
d = {1:47, 2:51, 3:55, 4:24, 5:28, 6:32, 7:1, 8:5, 9:9}
print(ttt,'\n')

def victory():
    return ttt[47]==ttt[51]==ttt[55] or ttt[24]==ttt[28]==ttt[32] or ttt[1]==ttt[5]==ttt[9] or ttt[47]==ttt[24]==ttt[1] or ttt[51]==ttt[28]==ttt[5] or ttt[55]==ttt[32]==ttt[9] or ttt[47]==ttt[28]==ttt[9] or ttt[55]==ttt[28]==ttt[1]
    
def playX():
    global ttt
    x = int(input('enter X at: '))
    if(ttt[d[x]]=='X' or ttt[d[x]]=='o'):
        print("\toccupied!")
        playX()
    else:
        left = ttt[:d[x]]
        right = ttt[d[x]+1:]
        ttt = left + 'X' + right
        print(ttt,'\n')
        
def playO():
    global ttt
    o = int(input('enter o at: '))
    if(ttt[d[o]]=='X' or ttt[d[o]]=='o'):
        print("\toccupied!")
        playO()
    else:
        left = ttt[:d[o]]
        right = ttt[d[o]+1:]
        ttt = left + 'o' + right
        print(ttt,'\n')
        
while True:
    playX()
    if victory():
        print('\n\t X player won!!') 
        break  
        
    playO()
    if victory():
        print('\n\t o player won!!') 
        break  
    
