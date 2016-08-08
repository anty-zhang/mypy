# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *
import os


def openImage():
    # 读取图像
    pil_img = Image.open("../image/normal.jpg")
    # pil_img.convert('L')
    pil_img.rotate(45).show()
    # pil_img.show()
    # print pil_img  # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=869x432 at 0x9B6D04C>


def convertFormat():
    filelist = ["/home/andy/Documents/documents/python/computer_vision/image/chuangyelaji.gif"]
    # filelist = ["/home/andy/Documents/documents/python/computer_vision/image/cyblaji.png"]

    for infile in filelist:
        outputfile = os.path.splitext(infile)[0] + ".jpg"
        print 'infile:', infile
        print 'outputfile:', outputfile

        if infile != outputfile:
            try:
                im = Image.open(infile).convert('RGB').save(outputfile)

                """
                不能分开写
                im = Image.open(infile)
                im.convert('RGB')
                im.save(outputfile)
                """
            except IOError:
                print 'cannot convert', infile


def matplotTest():
    file = "/home/andy/Documents/documents/python/computer_vision/image/chuangyelaji.jpg"
    # read image to array
    im = array(Image.open(file))
    # plot the image
    imshow(im)

    # some points
    x = [100, 100, 400, 400]
    y = [200, 500, 200, 500]

    # plot the points with red star-markets
    plot(x, y, "r*")

    # line plot connecting the first two points
    plot(x[:2], y[:2])

    # add title and show the plot
    title("plotting: empire.jpg")

    axis("on")
    show()


if __name__ == '__main__':
    # openImage()
    # convertFormat()
    matplotTest()
