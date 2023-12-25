#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 15 avr. 2015

Program with keyboard shortcuts to read and display easily an images sequence.

@author: fabien
'''
import sys
import os.path as osp
import cv2

path = "snake_color/"
prefix = "snake_"
digitNbr = 4
ext = ".png"

initIndex = 0

if __name__ == '__main__':
    if len(sys.argv) == 2:
        initIndex = int(sys.argv[1])
    waitTime = 10
    i = initIndex

    fullPath = osp.join(path, prefix + str(i).zfill(digitNbr) + ext)
    if osp.exists(fullPath):
        loop = True
    else:
        loop = False
        print("image Index does not exist.")

    nextKey = 1048686
    previousKey = 1048688
    quitKey = 113
    runKey = 114

    while(loop):
        fullPath = osp.join(path, prefix + str(i).zfill(digitNbr) + ext)
        if osp.exists(fullPath):
            currentImage = cv2.imread(fullPath, 1)
            cv2.putText(currentImage,
                        prefix + str(i).zfill(digitNbr) + ext,
                        (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.70,
                        (0, 0, 255),
                        2)
            cv2.imshow("Image", currentImage)
        else:
            i -= 1
            waitTime = 0
        retValue = cv2.waitKeyEx(waitTime)
        if waitTime == 0:
            if retValue == nextKey:
                i += 1
            if retValue == previousKey:
                i -= 1
            if retValue == runKey:
                waitTime = 5
            if retValue == quitKey:
                loop = False
        else:
            if retValue == runKey:
                waitTime = 0
            else:
                i += 1
        i %= 1000


    cv2.destroyAllWindows()
