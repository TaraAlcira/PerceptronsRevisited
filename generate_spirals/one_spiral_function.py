import cv2
import numpy as np
import random

def generate_1double_spiral(side_length, buffer):
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

    side_length = (side_length + buffer)

    # remove last leg
    for _ in range(stepsSpiral1):
        x1, y1 = x1 - dx, y1 - dy
        if 0 <= x1 < side_length and 0 <= y1 < side_length:
            canvas[x1, y1] = black
        else:
            break

    # remove leg before last leg
    dx, dy = directionsSpiral1[(legSpiral1 - 2) % 4]
    for _ in range(stepsSpiral1 - int(0.5 * increase_interval)):
        x1, y1 = x1 - dx, y1 - dy
        if 0 <= x1 < side_length and 0 <= y1 < side_length:
            canvas[x1, y1] = black
        else:
            break

    # remove last leg
    for _ in range(stepsSpiral2):
        x3, y3 = x3 - dx2, y3 - dy2
        if 0 <= x3 < side_length and 0 <= y3 < side_length:
            canvas[x3, y3] = black
        else:
            break

    # remove leg before last leg
    dx2, dy2 = directionsSpiral2[(legSpiral2 - 2) % 4]
    for _ in range(stepsSpiral2 - int(0.5 * increase_interval)):
        x3, y3 = x3 - dx2, y3 - dy2
        if 0 <= x3 < side_length and 0 <= y3 < side_length:
            canvas[x3, y3] = black
        else:
            break


    # # remove any artifacts (white pixels with 4 black neighbors)
    # for i in range(1, side_length - 1):
    #     for j in range(1, side_length - 1):
    #         if np.all(canvas[i, j] == white):
    #             if (
    #                 np.all(canvas[i - 1, j] == [0, 0, 0])
    #                 and np.all(canvas[i + 1, j] == [0, 0, 0])
    #                 and np.all(canvas[i, j - 1] == [0, 0, 0])
    #                 and np.all(canvas[i, j + 1] == [0, 0, 0])
    #             ):
    #                 canvas[i, j] = [0, 0, 0]

    # remove any artifacts (white pixels with 4 black neighbors or in small clusters)
    for i in range(1, side_length - 1):
        for j in range(1, side_length - 1):
            if np.all(canvas[i, j] == white):
                # Check for 1x1 white pixel surrounded by black
                if (
                    np.all(canvas[i - 1, j] == [0, 0, 0]) and
                    np.all(canvas[i + 1, j] == [0, 0, 0]) and
                    np.all(canvas[i, j - 1] == [0, 0, 0]) and
                    np.all(canvas[i, j + 1] == [0, 0, 0])
                ):
                    canvas[i, j] = [0, 0, 0]
                # Check for vertical 2x1 cluster of white pixels
                elif i < side_length - 2 and np.all(canvas[i + 1, j] == white):
                    if (
                        np.all(canvas[i - 1, j] == [0, 0, 0]) and
                        np.all(canvas[i + 2, j] == [0, 0, 0]) and
                        np.all(canvas[i, j - 1] == [0, 0, 0]) and
                        np.all(canvas[i, j + 1] == [0, 0, 0]) and
                        np.all(canvas[i + 1, j - 1] == [0, 0, 0]) and
                        np.all(canvas[i + 1, j + 1] == [0, 0, 0])
                    ):
                        canvas[i, j] = [0, 0, 0]
                        canvas[i + 1, j] = [0, 0, 0]
                # Check for horizontal 2x1 cluster of white pixels
                elif j < side_length - 2 and np.all(canvas[i, j + 1] == white):
                    if (
                        np.all(canvas[i - 1, j] == [0, 0, 0]) and
                        np.all(canvas[i + 1, j] == [0, 0, 0]) and
                        np.all(canvas[i, j - 1] == [0, 0, 0]) and
                        np.all(canvas[i, j + 2] == [0, 0, 0]) and
                        np.all(canvas[i - 1, j + 1] == [0, 0, 0]) and
                        np.all(canvas[i + 1, j + 1] == [0, 0, 0])
                    ):
                        canvas[i, j] = [0, 0, 0]
                        canvas[i, j + 1] = [0, 0, 0]


    # find lowest left white pixel of spiral 1 and make it blue
    is_white = np.all(canvas == white, axis=-1)

    x1, y1 = np.where(is_white)
    x1_temp, y1_temp = x1[len(x1)-1], y1[0]-1
    canvas[x1_temp, y1_temp] = white
    canvas[x1_temp-1, y1_temp] = white
    canvas[x1_temp-2, y1_temp] = white

    x3, y3 = np.where(is_white)
    x3, y3 = x3[0], y3[len(y3)-1]+1
    canvas[x3, y3] = white
    canvas[x3+1, y3] = white
    canvas[x3+2, y3] = white

    return canvas

# side_length = random.randint(50, 100)
# buffer = 10

# canvas = generate_1double_spiral(side_length, buffer)
# cv2.imwrite("1double_spiral.png", canvas)


# start_x, start_y = (side_length + buffer) // 2 + 1, (side_length + buffer) // 2 + 1






