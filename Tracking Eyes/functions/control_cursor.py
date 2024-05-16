import pyautogui as pg

pg.FAILSAFE = False

position_x = 0
position_y = 0

speed = 1.3

limit_horizontal, limit_vertical = pg.size()

print(f"Your computer screen: Size(width={limit_horizontal}, height={limit_vertical})")

def controlCursor(cx, cy, sx, sy):
    global position_x, position_y, speed

    # calculate movment cursor position
    # get standard center screen position delete with currently screen position
    position_x += cx - sx
    position_y += cy - sy

    cursor_x = position_x * speed
    cursor_y = position_y * speed

    if cursor_x < 0:
        cursor_x = 0
        position_x = 0
        speed = 1
    elif cursor_x > limit_horizontal:
        cursor_x = limit_horizontal
        position_x = limit_horizontal
        speed = 1
    if cursor_y < 0:
        cursor_y = 0
        position_y = 0
        speed = 1
    elif cursor_y > limit_vertical:
        cursor_y = limit_vertical
        position_y = limit_vertical
        speed = 1

    # print(f"Face: {cx} {cy} | Cursor: {cursor_x} {cursor_y} | inc_x={position_x}, inc_y={position_y}")

    pg.moveTo(cursor_x, cursor_y)
