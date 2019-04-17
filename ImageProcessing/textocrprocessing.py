# Importing the necessary packagess:

import numpy as np
import argparse
import cv2



def main():
    image = cv2.imread("C:\\Users\\SachinVardhan\\Desktop\\ModeF-1.jpg")
    # define the list of boundaries
    boundaries = [
        ([0, 0, 0], [115, 115, 115]),
        ([237, 237, 237], [255, 255, 255])
    ]

    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)

        # show the images
        cv2.imshow("images", np.hstack([image, output]))
        cv2.waitKey(0)

if __name__ == '__main__':
    main()