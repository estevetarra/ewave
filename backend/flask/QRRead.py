#!/usr/bin/python
from sys import argv
import numpy as np
import zbar
import cv2
from PIL import Image


def getQRPosition (path):
    # create a reader
    scanner = zbar.ImageScanner()

    # configure the reader
    scanner.parse_config('enable')

    # obtain image data
    img = cv2.imread(path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    pil = Image.open(path).convert('L')
    width, height = pil.size
    raw = pil.tobytes()

    # wrap image data
    image = zbar.Image(width, height, 'Y800', raw)

    # scan the image for barcodes
    scanner.scan(image)

    res=False
    # extract results
    for symbol in image:
        # do something useful with results
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
        QRData=symbol.data
        topLeftCorners, bottomLeftCorners, bottomRightCorners, topRightCorners = [item for item in symbol.location]
        topLeftCorner=[[topLeftCorners[0],topLeftCorners[1]]]
        bottomLeftCorner=[[bottomLeftCorners[0],bottomLeftCorners[1]]]
        topRightCorner=[[topRightCorners[0],topRightCorners[1]]]
        bottomRightCorner=[[bottomRightCorners[0],bottomRightCorners[1]]]
        corners = np.asarray([bottomLeftCorner,bottomRightCorner,topLeftCorner,topRightCorner],dtype=np.float32)
        res=True

    if (res==False):
        print 'Not able to scan QR'
        return 0,0,0
        exit(1)
    objp = np.zeros((2*2,3), np.float32)
    objp[:,:2] = np.mgrid[0:2,0:2].T.reshape(-1,2)


    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    objpoints.append(objp)
    imgpoints.append(corners)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
    retval,rvec,tvec = cv2.solvePnP(objp, corners, mtx, dist)

    a=np.zeros((4,4),np.float32)
    a[0:3,0:3],_ = cv2.Rodrigues(np.asarray(rvecs))
    a[0:3,3]= np.transpose(np.asarray(tvecs)[0])[0]
    a[3,3]=1
    ai = np.linalg.inv(a)

    return 1, QRData, ai[0:3,3]


    #axis = np.float32([[1,0,0], [0,1,0], [0,0,-1]]).reshape(-1,3)

    #def draw(img, corners, imgpts):
    #    corner = tuple(corners[0].ravel())
    #    img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255,0,0), 5)
    #    img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0,255,0), 5)
    #    img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
    #    return img

    #imgpts, jac = cv2.projectPoints(axis, rvec, tvec, mtx, dist)
    #img = draw(img,corners,imgpts)
    #cv2.imwrite('res.jpg', img)

    # cv2.imwrite('res.jpg',img)
    # clean up
    del(image)