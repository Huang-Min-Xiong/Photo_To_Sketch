import cv2

img_src = './img.jpg'
img = cv2.imread(img_src)
resize_img = cv2.resize(img, (800,600), interpolation=cv2.INTER_CUBIC) #縮放圖片
gray_img = cv2.cvtColor(resize_img,cv2.COLOR_BGR2GRAY) #灰階處理
inverted_gray_img = 255 - gray_img
blurred_img = cv2.GaussianBlur(inverted_gray_img,(21,21),0) #高斯模糊處理
inverted_blurred_img = 255 - blurred_img
sketch_img = cv2.divide(gray_img,inverted_blurred_img,scale=256.0) #影象運算處理

cv2.imshow('resize_img',resize_img) #縮放後的圖
cv2.imshow('sketch_img',sketch_img) #素描圖
cv2.waitKey(0)