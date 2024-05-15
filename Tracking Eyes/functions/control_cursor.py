import pyautogui as pg

lx = 0
ly = 0

print(f"Your computer screen: {pg.size()}")

def controlCursor(cx, cy):
    global lx, ly
    lx, ly = pg.position()

    print(f"Face position in frame: {cx} {cy} | Cursor position: {lx} {ly}")

    # nx, ny = pg.position()
    # if nx != lx and ny != ly:
    #     lx, ly = pg.position()
    #     print(f"Face position in frame: {cx} {cy} | Cursor position: {lx}, {ly}",end='\r')

