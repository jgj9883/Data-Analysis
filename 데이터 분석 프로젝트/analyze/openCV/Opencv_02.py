import cv2
import time
image = cv2.imread('result1.png')
# # 픽셀 수 및 이미지 크기 확인
# print(image.shape)
# print(image.size)
#
# # 이미지 Numpy 객체의 특정 픽셀을 가리킴
# px = image[100, 100]
#
# # B, G, R 순서로 출력
# # Gray Scale : B, G, R로 구분되지 않는다.
# print(px)
#
# # R 값만 출력하기
# print(px[2])

# 특정 픽셀만 바꾸기
start_time = time.time()
# 1번째 방법
for i in range(0,100):
    for j in range(0,100):
        image[i,j] = [255, 255, 255]
    # print("--- %s seconds ---" % (time.time() - start_time))
cv2.imshow('Image Basic', image)
cv2.waitKey(0)

# 2번째 방법
start_time = time.time()
image[0:100, 0:100] = [0,0,0]
# print("--- %s seconds ---" % (time.time() - start_time))
cv2.imshow('Image Basic', image)
cv2.waitKey(0)


# # 특정 부분만 추출해서 출력
# # Numpy Slicing : ROI 처리 기능
# roi = image[200:350, 50:200]
# # ROI 단위로 이미지 복사하기
# image[0:150, 0:150] = roi
# cv2.imshow('Image Basic', image)
# cv2.waitKey(0)
#
