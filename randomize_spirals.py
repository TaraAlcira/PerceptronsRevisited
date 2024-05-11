import random
import numpy as np
import cv2
import os
import json
# from scipy.ndimage import rotate

from one_spiral_function import generate_1double_spiral
from two_spirals_function import generate_2double_spiral

number_list = []
range_images = 20000

def generateRandomSpirals():
    side_length = random.randint(40, 70)
    buffer = random.randint(5, 20)
    random_number = random.choice([1, 2])
    random_angle = random.choice([0, 1, 2, 3])

    if random_number == 1:
        canvas = generate_1double_spiral(side_length, buffer)
    else:
        canvas = generate_2double_spiral(side_length, buffer)

    canvas = np.rot90(canvas, random_angle)

    return canvas, random_number


# create a folder
if not os.path.exists("random_spirals"):
    os.makedirs("random_spirals")
    print("Directory created")

# generate random spirals
for i in range(range_images):
    canvas, number = generateRandomSpirals()

    # canvas = cv2.imread(f"random_spirals/random_spiral_{i}.png", cv2.IMREAD_GRAYSCALE)
    # canvas = cv2.resize(canvas, (512, 512), interpolation=cv2.INTER_LINEAR)
    # canvas = cv2.resize(canvas, (256, 256), interpolation=cv2.INTER_NEAREST)
    # random_angle = random.randint(0, 360)
    # canvas = rotate(canvas, random_angle)

    # # move spiral to the right and down
    # move_right = random.randint(0, 20)
    # move_down = random.randint(0, 20)
    # canvas = np.roll(canvas, move_right, axis=1)
    # canvas = np.roll(canvas, move_down, axis=0)

    # make sure the images are binary
    canvas = cv2.threshold(canvas, 127, 255, cv2.THRESH_BINARY)[1]

    cv2.imwrite(f"random_spirals/random_spiral_{i}.png", canvas)

    number_list.append(number)

data = {}
for i in range(range_images):
    data[f"random_spiral_{i}"] = number_list[i]

with open("random_spirals.json", "w") as f:
    json.dump(data, f)

# canvas = generateRandomSpirals()
# cv2.imwrite("random_spirals.png", canvas)

# change to 512 x 512 and add a random angle of rotation
# for i in range(range_images):
#     canvas = cv2.imread(f"random_spirals/random_spiral_{i}.png", cv2.IMREAD_GRAYSCALE)
#     canvas = cv2.resize(canvas, (512, 512), interpolation=cv2.INTER_NEAREST)
#     random_angle = random.randint(0, 360)
#     canvas = rotate(canvas, random_angle)
    # canvas = cv2.resize(canvas, (128, 128), interpolation=cv2.INTER_NEAREST)
    # cv2.imwrite(f"random_spirals/random_spiral_{i}.png", canvas)


