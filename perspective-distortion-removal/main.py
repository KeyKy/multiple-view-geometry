import numpy as np
import argparse
import cv2
import sys

def select_points(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print (x,y)
        cv2.circle(image, (x,y), 2, (255,0,0))
        cv2.imshow('image', image)


def parse_args():
    parser = argparse.ArgumentParser(description='4 point method')
    parser.add_argument('--image', help='input image')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()

def main(args):
    global image
    image = cv2.imread(args.image)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', select_points)

    while True:
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("c"):
            break


    cv2.destroyAllWindows()
    height, width, _ = image.shape
    print height, width
    corners = np.float32(([50,56], [128,22], [215,113], [121,175]))
    destination = np.float32([[0, 0], [width, 0],  [width, height], [0, height]])
    transformationMatrix = cv2.getPerspectiveTransform(corners, destination)
    warpedImage = cv2.warpPerspective(image, transformationMatrix, (width, height))

    cv2.namedWindow("image2", 0)
    cv2.imshow("image2", warpedImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    args = parse_args()
    main(args)

