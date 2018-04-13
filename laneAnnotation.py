import os
import time
import cv2
import math
# from Tkinter import *
# import tkMessageBox
# import tkSimpleDialog
# from graphClass import Application


drawing = False
ix, iy = -1, -1
currentPointsLists = []
grid_line = ''
lane_class = []
rectNum = 0

def writeFile(gridline):
    # use to write out the grids along with the line drawn, when user press key 'n',
    # the rectangles need to be written down
    with open('labels3.txt', 'a+') as f:
        f.write(gridline + '\n')
        # f.write('\n')


def draw_line(event, x, y, flags, param):

    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
        drawing = True
        ix, iy = x, y
        currentPointsLists.append((ix, iy))
        #print ix, iy

    # elif event == cv2.EVENT_MOUSEMOVE:
        # if drawing == True:
        #     cv2.line(img, (ix, iy), (x, y), (0, 255, 0), 1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        ixd, iyd = x, y
        #print ixd, iyd
        clane = input('class index is:')
        # print clane
        lane_class.append(clane)
        if lane_class[len(lane_class) - 1] == 1:
            cv2.line(img, (ix, iy), (ixd, iyd), (0, 255, 0), 2)
        if lane_class[len(lane_class) - 1] == 2:
            cv2.line(img, (ix, iy), (ixd, iyd), (255, 0, 0), 2)
        # app = Application()
        # app.master.title('input class index')
        # app.mainloop()
        # clane = app.clane
        # app.quit()
        # clane = tkSimpleDialog.askinteger('input class index', '1,2,3')


        generateRect(ix, iy, ixd, iyd, clane)    # it will draw some rect according to the drawn line
        currentPointsLists.append((ixd, iyd))


def generateRect(x0, y0, x1, y1, clane):
    # need to add parameter "class label" after this, don't forget
    size = 8
    global rectNum
    global grid_line
    k = (float(y1) - float(y0)) / (float(x1) - float(x0))
    #print k
    #print round((y1-y0)/size)
    for i in range(1, int(abs((y1 - y0) / size)) + 1):
        y = y1 + (i - 1) * size + 1 + 4  #(x1, y1) is the below point, from the below point to up point, select a point per 8 pixel
        x = (float(y) - float(y1)) / k + float(x1)
        #print x, y

        if x >= 100 and y >= 360:
            if x <= 1180 and y >= 540:
                grid_line += str(int(math.ceil(x)) - 3) + ' ' + str(int(math.ceil(y)) - 4) + ' ' + str(
                    int(math.ceil(x)) + 4) + ' ' + str(int(math.ceil(y)) + 3) + ' ' + str(clane) + ' '
                grid_line += str(int(math.ceil(x)) - 11) + ' ' + str(int(math.ceil(y)) - 4) + ' ' + str(
                    int(math.ceil(x)) - 4) + ' ' + str(int(math.ceil(y)) + 3) + ' ' + str(clane) + ' '
                grid_line += str(int(math.ceil(x)) + 5) + ' ' + str(int(math.ceil(y)) - 4) + ' ' + str(
                    int(math.ceil(x)) + 12) + ' ' + str(int(math.ceil(y)) + 3) + ' ' + str(clane) + ' '
                rectNum += 3
                # grid_size = 8
                # cv2.rectangle(img, (int(math.ceil(x)) - 3, int(math.ceil(y)) - 4),
                #               (int(math.ceil(x)) + 4, int(math.ceil(y)) + 3), (255, 0, 0), 1)
                # cv2.rectangle(img, (int(math.ceil(x)) - 11, int(math.ceil(y)) - 4),
                #               (int(math.ceil(x)) - 4, int(math.ceil(y)) + 3), (0, 255, 0), 1)
                # cv2.rectangle(img, (int(math.ceil(x)) + 5, int(math.ceil(y)) - 4),
                #               (int(math.ceil(x)) + 12, int(math.ceil(y)) + 3), (0, 0, 255), 1)
                # grid_size = 16
                # cv2.rectangle(img, (int(math.ceil(x)) - 7, int(math.ceil(y)) - 8),
                #               (int(math.ceil(x)) + 8, int(math.ceil(y)) + 7), (255, 0, 0), 1)
                # cv2.rectangle(img, (int(math.ceil(x)) - 23, int(math.ceil(y)) - 8),
                #               (int(math.ceil(x)) - 8, int(math.ceil(y)) + 7), (0, 255, 0), 1)
                # cv2.rectangle(img, (int(math.ceil(x)) + 9, int(math.ceil(y)) - 8),
                #               (int(math.ceil(x)) + 24, int(math.ceil(y)) + 7), (0, 0, 255), 1)
            else:
                grid_line += str(int(math.ceil(x)) - 7) + ' ' + str(int(math.ceil(y)) - 4) + ' ' + str(
                    int(math.ceil(x))) + ' ' + str(int(math.ceil(y)) + 3) + ' ' + str(clane) + ' '
                grid_line += str(int(math.ceil(x)) + 1) + ' ' + str(int(math.ceil(y)) - 4) + ' ' + str(
                    int(math.ceil(x)) + 8) + ' ' + str(int(math.ceil(y)) + 3) + ' ' + str(clane) + ' '
                rectNum += 2
                # grid_size = 8
                # cv2.rectangle(img, (int(math.ceil(x)) - 7, int(math.ceil(y)) - 4),
                #               (int(math.ceil(x)), int(math.ceil(y)) + 3), (255, 0, 0), 1)
                # cv2.rectangle(img, (int(math.ceil(x)) + 1, int(math.ceil(y)) - 4),
                #               (int(math.ceil(x)) + 8, int(math.ceil(y)) + 3), (255, 0, 0), 1)
                # grid_size = 16
                # cv2.rectangle(img, (int(math.ceil(x)) - 15, int(math.ceil(y)) - 8),
                #               (int(math.ceil(x)), int(math.ceil(y)) + 7), (255, 0, 0), 1)
                # cv2.rectangle(img, (int(math.ceil(x)) + 1, int(math.ceil(y)) - 8),
                #               (int(math.ceil(x)) + 16, int(math.ceil(y)) + 7), (255, 0, 0), 1)
        if x < 100 and y >= 360:
            grid_line += str(int(math.ceil(x)) - 7) + ' ' + str(int(math.ceil(y)) - 4) + ' ' + str(
                int(math.ceil(x))) + ' ' + str(int(math.ceil(y)) + 3) + ' ' + str(clane) + ' '
            grid_line += str(int(math.ceil(x)) + 1) + ' ' + str(int(math.ceil(y)) - 4) + ' ' + str(
                int(math.ceil(x)) + 8) + ' ' + str(int(math.ceil(y)) + 3) + ' ' + str(clane) + ' '
            rectNum += 2
            # cv2.rectangle(img, (int(math.ceil(x)) - 7, int(math.ceil(y)) - 4),
            #               (int(math.ceil(x)), int(math.ceil(y)) + 3), (255, 0, 0), 1)
            # cv2.rectangle(img, (int(math.ceil(x)) + 1, int(math.ceil(y)) - 4),
            #               (int(math.ceil(x)) + 8, int(math.ceil(y)) + 3), (255, 0, 0), 1)
        # cv2.circle(img, (x, y), 2, 1)
        else:
            rectNum += 0
    # writeFile(grid_line)


file_dir = '/home/fangzz-cvman/data/lanes/beijing3'   #CLIP9784/
# listdir = []
imageList = []
# for root, dirs, files in os.walk(file_dir):
#     listdir.append(dirs)
# for i in range(len(listdir[0])):
#     filedir = file_dir + str(listdir[0][i])
for root, dirs, files in os.walk(file_dir):
    for file in files:
        # imageList.append(file_dir + str(listdir[0][i]) + '/' + file)
        imageList.append(file_dir + '/' + file)
        imageList.sort()

# imgDir = '/home/fangzz-cvman/data/beijing'
# img = cv2.imread('/home/fangzz-cvman/data/beijing/CLIP9784/0.png')
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_line)
# print img.shape
index = input("next annotation image index:")
# index = tkSimpleDialog.askinteger('input next image index', 'input integer')
print imageList[index]
img = cv2.imread(imageList[index])
while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1)
    if (k & 0xFF) == 27:
        break
    if chr(k) == 'n':
        print 'next image'
        for i in range(len(currentPointsLists) / 2):
            cx0, cy0, cx1, cy1 = currentPointsLists[2*i][0], currentPointsLists[2*i][1], currentPointsLists[2*i + 1][0], \
                             currentPointsLists[2*i + 1][1]
            generateRect(cx0, cy0, cx1, cy1, lane_class[i])
            print lane_class[i]
        #grid_line = '/laneimage/' + imageList[index].split('/')[-1] + ' ' + str(rectNum) + ' ' + grid_line
        grid_line = '/' + imageList[index].split('/')[-2] + '/' + imageList[index].split('/')[-1] + ' ' + str(rectNum) + ' ' + grid_line
        # print grid_line
        writeFile(grid_line)
        grid_line = ''
        rectNum = 0
        lane_class = []
        index += 1
        if index <= len(imageList) - 1:
            print imageList[index]
            img = cv2.imread(imageList[index])
            print 'index of the labeled images is: ', index
            currentPointsLists = []  # current points list is set free when press key 'n'

    if chr(k) == 'z':
        print 'concel operation'
        if len(currentPointsLists) is not 0:
            currentPointsLists.pop(len(currentPointsLists) - 1)
            currentPointsLists.pop(len(currentPointsLists) - 1)  # consecutively remove the last two elements
            lane_class.pop(len(lane_class) - 1)
            print lane_class

        img = cv2.imread(imageList[index])
        for i in range(len(currentPointsLists) / 2):
            # cv2.line(img, currentPointsLists[2*i], currentPointsLists[2*i + 1], (0, 255, 0), 2)
            print lane_class[i]
            if lane_class[i] == 1:
                cv2.line(img, currentPointsLists[2*i], currentPointsLists[2*i + 1], (0, 255, 0), 2)
            if lane_class[i] == 2:
                cv2.line(img, currentPointsLists[2*i], currentPointsLists[2*i + 1], (255, 0, 0), 2)

        # undo the last operation that a line is drawn
    if chr(k) == 'c':
        print 'clear all the lines'
        currentPointsLists = []
        lane_class = []
        img = cv2.imread(imageList[index])
cv2.destroyAllWindows()
