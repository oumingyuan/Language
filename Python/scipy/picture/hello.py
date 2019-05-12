from scipy.misc import imread, imsave, imresize

'''
图片处理软件
'''
if __name__ == "__main__":
    img = imread("timg.jpg")
    img_type = img.dtype
    print(img_type)

    img_shape = img.shape
    print(img_shape)
    img_height = img_shape[0]
    print(img_height)

    print(img_shape[2])
