#!/usr/bin/env python3

"""
    Display animation on Vector's face
"""


import os
import sys
import time

try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import anki_vector
from anki_vector.util import degrees

args = anki_vector.util.parse_command_args()
    
def face_animation():
    image_settings = []
    face_images = []
    current_directory = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(current_directory, "face_animation")

    for i in range(1, 24):
        image_settings.append(image_path + '/face' + str(i) + '.png')

    for image_name in image_settings:
        image = Image.open(image_name)

        pixel_bytes = anki_vector.screen.convert_image_to_screen_data(image)

        face_images.append(pixel_bytes)

    num_loops = 20
    duration_s = 0.1

    print("Press CTRL-C to quit (or wait %s seconds to complete)" % int(num_loops*duration_s*len(face_images)))

    for _ in range(num_loops):
        for i in range(0, len(face_images)):
            robot.screen.set_screen_with_image_data(face_images[i], duration_s)
            time.sleep(duration_s)

with anki_vector.robot.Robot() as robot:
    robot.behavior.set_head_angle(degrees(45.0))
    robot.behavior.set_lift_height(0.0)
    robot.conn.release_control()
    time.sleep(1)
    robot.conn.request_control()
    face_animation()

