import pyautogui as pg

print(f"Your computer screen: {pg.size()}")

lx = None
ly = None

def controlCursor(cx, cy):
    global lx, ly
    lx, ly = pg.position()

    print(f"Face position in frame: {cx} {cy} | Cursor position: {lx}, {ly}")

    # nx, ny = pg.position()
    # if nx != lx and ny != ly:
    #     lx, ly = pg.position()
    #     print(f"Face position in frame: {cx} {cy} | Cursor position: {lx}, {ly}",end='\r')

