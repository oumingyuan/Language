import cv2

img = cv2.imread('loginLog.jpg', 0)

# cv2.WINDOW_NORMAL参数指示可以调整大小,缺省的参数是cv2.WINDOW_AUTOSIZE,即根据图片的大小来显示
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# 显示图片
cv2.imshow('image', img)

# 等待键盘,0代表无限等待,10代表10ms
cv2.waitKey(0)

# 保存图片的操作,保存到当前目录下的save.png
cv2.imwrite('save.png', img)

# 销毁窗口
cv2.destroyAllWindows()
