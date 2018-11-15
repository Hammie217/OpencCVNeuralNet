import numpy as np
import cv2 as cv
from random import randint

NumberofNets = 40

class neuralNet:
    def __init__(self, first, second, third, fourth, fivth, sixth, seventh, eighth, nineth):
        self.neuron1Strength = first
        self.neuron2Strength = second
        self.neuron3Strength = third
        self.neuron4Strength = fourth
        self.neuron5Strength = fivth
        self.neuron6Strength = sixth
        self.neuron7Strength = seventh
        self.neuron8Strength = eighth
        self.neuron9Strength = nineth
        self.saliencyMap = img.copy()
    pass
nets = []
def createRandomNets():
 
    for i in range(NumberofNets):
        nets.append(neuralNet(randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100)))
    return

fileNumber =1
img = cv.imread('rgbd_dataset_freiburg1_xyz/rgb/rgb'+str(fileNumber) + ".png")
createRandomNets()

for i in range(NumberofNets):
    print("Neuron" +str(i) +" " +str(nets[i].neuron1Strength/100) +" " + str(nets[i].neuron2Strength/100) +" " + str(nets[i].neuron3Strength/100) +" " + str(nets[i].neuron4Strength/100) +" " + str(nets[i].neuron5Strength/100) +" " + str(nets[i].neuron6Strength/100) +" " + str(nets[i].neuron7Strength/100) +" " + str(nets[i].neuron8Strength/100) +" " + str(nets[i].neuron9Strength/100))

while (True):
    img = cv.imread('rgbd_dataset_freiburg1_xyz/rgb/rgb'+str(fileNumber) + ".png")
    imgGrey = cv.imread('rgbd_dataset_freiburg1_xyz/rgb/rgb'+str(fileNumber) + ".png",0)
    imgDepth = cv.imread('rgbd_dataset_freiburg1_xyz/depth/depth'+str(fileNumber) + ".png",0)
    imgNext = cv.imread('rgbd_dataset_freiburg1_xyz/rgb/rgb'+str(fileNumber+1) + ".png",0)
    imgDifference = cv.subtract(imgGrey,imgNext)
    GaussianBlur = cv.GaussianBlur(img,(3,3),0)
    StrongCanny = cv.Canny(GaussianBlur,600,700)
    MedCanny = cv.Canny(GaussianBlur,400,500)
    WeakCanny = cv.Canny(GaussianBlur,100,200)
    red = img.copy();
    red[:,:,0]=0
    red[:,:,1]=0
    green = img.copy();
    green[:,:,0]=0
    green[:,:,2]=0
    blue = img.copy();
    blue[:,:,1]=0
    blue[:,:,2]=0
    red = cv.cvtColor(red, cv.COLOR_BGR2GRAY)
    green = cv.cvtColor(green, cv.COLOR_BGR2GRAY)
    blue = cv.cvtColor(blue, cv.COLOR_BGR2GRAY)
    
    h=img.shape[0]
    w=img.shape[1]
    for i in range(NumberofNets):
        for y in range(0, h):
            for x in range(0, w):
                nets[i].saliencyMap[y, x] = imgDepth[y,x]*nets[i].neuron1Strength/100 + imgDifference[y,x]*nets[i].neuron2Strength/100 + StrongCanny[y,x]*nets[i].neuron3Strength/100 + MedCanny[y,x]*nets[i].neuron4Strength/100 + WeakCanny[y,x]*nets[i].neuron5Strength/100 + imgGrey[y,x]*nets[i].neuron6Strength/100 + red[y,x]*nets[i].neuron7Strength/100 + green[y,x]*nets[i].neuron8Strength/100 + blue[y,x]*nets[i].neuron9Strength/100

    #Show Images
    #cv.imshow('image',img)
    #cv.imshow('depth',imgDepth)
    #cv.imshow('differance',imgDifference)
    #cv.imshow('StrongCanny',StrongCanny)
    #cv.imshow('MedCanny',MedCanny)
    #cv.imshow('WeakCanny',WeakCanny)
    #cv.imshow('grayScale',imgGrey)
    #cv.imshow('Red',red)
    #cv.imshow('Green',green)
    #cv.imshow('Blue',blue)
    cv.imshow('SalencyMap0',nets[0].saliencyMap)

    fileNumber=fileNumber +1;
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
