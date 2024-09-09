import cv2

img_file = "./img/girl.jpg"
img = cv2.imread(img_file)
cv2.imshow('IMG', img)
cv2.waitKey()
cv2.destroyAllWindows()

from PIL import Image
img = Image.open("./img/girl.jpg")
img.show()

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow('IMG', img)
cv2.waitKey()
cv2.destroyAllWindows()