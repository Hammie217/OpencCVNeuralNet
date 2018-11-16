import numpy as np
import cv2 as cv
from random import randint
import threading

NumberofNets = 20

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
global nets
nets = []

def createRandomNets():
    i=0
    while(i<NumberofNets):
        nets.append(neuralNet(randint(-100,100),randint(-100,100),randint(-100,100),randint(-100,100),randint(-100,100),randint(-100,100),randint(-100,100),randint(-100,100),randint(-100,100)))
        i=i+1
    return

def createNeuralMaps(i):
    i=int(i)
    for y in range(0, h):
        for x in range(0, w):
            nets[i].saliencyMap[y, x] = imgDepth[y,x]*nets[i].neuron1Strength/100 + imgDifference[y,x]*nets[i].neuron2Strength/100 + StrongCanny[y,x]*nets[i].neuron3Strength/100 + MedCanny[y,x]*nets[i].neuron4Strength/100 + WeakCanny[y,x]*nets[i].neuron5Strength/100 + imgGrey[y,x]*nets[i].neuron6Strength/100 + red[y,x]*nets[i].neuron7Strength/100 + green[y,x]*nets[i].neuron8Strength/100 + blue[y,x]*nets[i].neuron9Strength/100
    print("NeuralMapMade")
    return 


fileNumber =1
global img
img = cv.imread('rgbd_dataset_freiburg1_xyz/rgb/rgb'+str(fileNumber) + ".png")
createRandomNets()
i=0
while(i<NumberofNets):
    print("Neuron" +str(i) +" " +str(nets[i].neuron1Strength/100) +" " + str(nets[i].neuron2Strength/100) +" " + str(nets[i].neuron3Strength/100) +" " + str(nets[i].neuron4Strength/100) +" " + str(nets[i].neuron5Strength/100) +" " + str(nets[i].neuron6Strength/100) +" " + str(nets[i].neuron7Strength/100) +" " + str(nets[i].neuron8Strength/100) +" " + str(nets[i].neuron9Strength/100))
    i=i+1
while (True):
    img = cv.imread('rgbd_dataset_freiburg1_xyz/rgb/rgb'+str(fileNumber) + ".png")
    global imgGrey
    imgGrey = cv.imread('rgbd_dataset_freiburg1_xyz/rgb/rgb'+str(fileNumber) + ".png",0)
    global imgDepth
    imgDepth = cv.imread('rgbd_dataset_freiburg1_xyz/depth/depth'+str(fileNumber) + ".png",0)
    global imgNext
    imgNext = cv.imread('rgbd_dataset_freiburg1_xyz/rgb/rgb'+str(fileNumber+1) + ".png",0)
    global imgDifference
    imgDifference = cv.subtract(imgGrey,imgNext)
    global GaussianBlur
    GaussianBlur = cv.GaussianBlur(img,(3,3),0)
    global StrongCanny
    StrongCanny = cv.Canny(GaussianBlur,600,700)
    global MedCanny
    MedCanny = cv.Canny(GaussianBlur,400,500)
    global WeakCanny
    WeakCanny = cv.Canny(GaussianBlur,100,200)
    global red
    red = img.copy();
    red[:,:,0]=0
    red[:,:,1]=0
    global green
    green = img.copy();
    green[:,:,0]=0
    green[:,:,2]=0
    global blue
    blue = img.copy();
    blue[:,:,1]=0
    blue[:,:,2]=0
    red = cv.cvtColor(red, cv.COLOR_BGR2GRAY)
    green = cv.cvtColor(green, cv.COLOR_BGR2GRAY)
    blue = cv.cvtColor(blue, cv.COLOR_BGR2GRAY)

    global h
    h=img.shape[0]
    global w
    w=img.shape[1]

    
    threads = [ ]
    for i in range(NumberofNets):
        t = threading.Thread(target=createNeuralMaps, args=(i,))
        threads.append(t)
        t.start()
        
    for one_thread in threads:
        one_thread.join()
   
    
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
