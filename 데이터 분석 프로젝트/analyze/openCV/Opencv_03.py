import cv2
import numpy as np

image = cv2.imread('result1.png',cv2.IMREAD_COLOR)
#image_re = cv2.cvtColor(cv2.COLOR_BGR2GRAY)
cv2.imshow('Image Basic', image)
cv2.waitKey(0)
# 이미지 사이즈 조절
expand = cv2.resize(image, None, fx=1.5, fy=1.5 , interpolation= cv2.INTER_CUBIC)
cv2.imshow('Image Basic', expand)
cv2.waitKey(0)

shrink = cv2.resize(image, None, fx=0.5, fy=0.5 , interpolation= cv2.INTER_AREA)
cv2.imshow('Image Basic', shrink)
cv2.waitKey(0)

# # 이미지 이동 (행과 열 정보만 저장)
# height, width = image.shape[:2]
#
# M= np.float32([1, 0, 50], [0, 1, 10])
# dst = cv2.warpAffine(image, M, width, height)
# cv2.imshow('Image Basic', dst)
# cv2.waitKey(0)



