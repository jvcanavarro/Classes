import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print("width:", image.shape[1])
print("height:", image.shape[0])
print("channels:", image.shape[2])


(b, g, r) = image[0, 0]
print('Pixel at (0,0) - Red: {}, Green: {}, Blue: {}'.format(r, g, b))
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print('Pixel at (0,0) - Red: {}, Green: {}, Blue: {}'.format(r, g, b))


corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)
cv2.waitKey(0)
image[0:100 ,0:100] = (0, 0, 255)

cv2.imshow("Updated", image)
cv2.waitKey(0)