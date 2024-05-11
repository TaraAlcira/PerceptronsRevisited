import cv2
import numpy as np

def generate_2double_spiral(side_length, buffer):
    white = [255, 255, 255]
    black = [0, 0, 0]

    canvas = np.zeros((side_length + buffer, side_length + buffer, 3), dtype="uint8")

    x1, y1 = (side_length + buffer) // 2 + 1, (side_length + buffer) // 2 + 1
    x2, y2 = x1, y1

    x3, y3 = (side_length + buffer) // 2 - 1, (side_length + buffer) // 2 - 1 
    x4, y4 = x3, y3

    canvas[x1, y1] = white
    canvas[x3, y3] = white

    stepsSpiral1 = 2
    stepsSpiral2 = 2
    directionsSpiral1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    directionsSpiral2 = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    increase_interval = 8

    legSpiral1 = 0 # current leg of spiral 1
    legSpiral2 = 0 # current leg of spiral 2

    while True:
        # Update first spiral
        dx, dy = directionsSpiral1[legSpiral1 % 4]
        for _ in range(stepsSpiral1):
            x1, y1 = x1 + dx, y1 + dy
            if 0 <= x1 < (side_length + buffer) and 0 <= y1 < (side_length + buffer):
                canvas[x1, y1] = white
            else:
                break

        for _ in range(stepsSpiral1 - int(0.5 * increase_interval)):
            x2, y2 = x2 + dx, y2 + dy
            if 0 <= x2 < (side_length + buffer) and 0 <= y2 < (side_length + buffer):
                canvas[x2, y2] = white
            else:
                break

        legSpiral1 += 1
        if legSpiral1 % 2 == 0:
            stepsSpiral1 += increase_interval

        # Update second spiral
        dx2, dy2 = directionsSpiral2[legSpiral2 % 4]
        for _ in range(stepsSpiral2):
            x3, y3 = x3 + dx2, y3 + dy2
            if 0 <= x3 < (side_length + buffer) and 0 <= y3 < (side_length + buffer):
                canvas[x3, y3] = white
            else:
                break

        for _ in range(stepsSpiral2 - int(0.5 * increase_interval)):
            x4, y4 = x4 + dx2, y4 + dy2
            if 0 <= x4 < (side_length + buffer) and 0 <= y4 < (side_length + buffer):
                canvas[x4, y4] = white
            else:
                break

        legSpiral2 += 1
        if legSpiral2 % 2 == 0:
            stepsSpiral2 += increase_interval

        # Break if out of bounds
        if (
            not (0 <= x1 < side_length and 0 <= y1 < side_length)
            or not (0 <= x2 < side_length and 0 <= y2 < side_length)
            or not (0 <= x3 < side_length and 0 <= y3 < side_length)
            or not (0 <= x4 < side_length and 0 <= y4 < side_length)
        ):
            break

    x1, y1 = x1 + dx, y1 + dy
    x3, y3 = x3 + dx2, y3 + dy2

    x1, y1 = x1, y1 - 1
    x3, y3 = x3, y3 + 1
    x2, y2 = x2, y2 - 1
    x4, y4 = x4, y4 + 1

    dx_1 = abs(x2 - x1)
    dx_2 = abs(x4 - x3)

    if x1 > x2:
        if y1 > y2:
            canvas[x2:x1+1, y2 + 1 : y1 + 1] = black
        else:
            canvas[x2:x1+1, y1 + 1 : y2 + 2] = black
        x1, y1 = x1, y1 + dx_1 + 3
        x2, y2 = x2, y2 + 2
    else:
        if y1 > y2:
            canvas[x1 : x2 + 1, y2 + 1 : y1 + 1] = black
        else:
            canvas[x1 : x2 + 1, y1 + 1 : y2 + 1] = black
        x1, y1 = x1, y1 - dx_1 - 1

    if x3 > x4:
        if y3 > y4:
            canvas[x4 : x3 + 1, y4 : y3 + 2] = black
        else:
            canvas[x4 : x3 + 1, y3 : y4 + 1] = black
        x3, y3 = x3, y3 + dx_2 + 1
    else:
        if y3 > y4:
            canvas[x3 : x4 + 1, y4 - 1 : y3 + 2] = black
        else:
            canvas[x3 : x4 + 1, y3 + 1 : y4 + 2] = black
        x3, y3 = x3, y3 - dx_2 - 3
        x4, y4 = x4, y4 - 2

    if x1 > x2:
        canvas[x2:x1+1, y2] = white
    else:
        canvas[x1:x2+1, y1] = white

    if y1 > y2:
        canvas[x1, y2:y1] = white
    else:
        canvas[x2, y1:y2] = white

    if x3 > x4:
        canvas[x4:x3+1, y4] = white
    else:
        canvas[x3:x4+1, y3] = white

    if y3 > y4:
        canvas[x3, y4:y3] = white
    else:
        canvas[x4, y3:y4] = white

    return canvas

# side_length = 100
# buffer = 10

# canvas = generate_2double_spiral(side_length, buffer)
# cv2.imwrite("double_spiral.png", canvas)









