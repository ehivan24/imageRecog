'''
Created on Jan 4, 2015

@author: edwingsantos
'''
from __builtin__ import len, str

if __name__ == '__main__':
    pass

from PIL import Image
import numpy as np  
import matplotlib.pyplot as plt   
import time
from collections import Counter 


def createExamples():
    numberArrayExamples = open('numberArEx.txt','a')
    numbersWeHave = range(0,10)
    versionsWeHabe = range(1,10)
    
    for eachNum in numbersWeHave:
        for eachVer in versionsWeHabe:
            #print str(eachNum) + '.' + str(eachVer) 
            imgFilePath = 'images/numbers/' + str(eachNum) + '.' + str(eachVer) + '.png'
            ie = Image.open(imgFilePath)
            eiar = np.array(ie)
            eiar1 = str(eiar.tolist())
            
            lineToWrite = str(eachNum) + '::' + eiar1 + '\n'
            numberArrayExamples.write(lineToWrite)  
            
            

def threshold(imgArray):
    balanceArray = []
    newArray = imgArray
    
    for eachRow in imgArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x + y, eachPix[:3])/len(eachPix[:3])
            balanceArray.append(avgNum)
            
    balanceArray = reduce(lambda x, y: x + y, balanceArray)/len(balanceArray)        
 
    for eachRow in newArray:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:3])/len(eachPix[:3]) > balanceArray:
                eachPix[0] = 255 
                eachPix[1] = 255 
                eachPix[2] = 255
                eachPix[3] = 255 
             
            else:
                eachPix[0] = 0
                eachPix[1] = 0 
                eachPix[2] = 0
                eachPix[3] = 255
                
                
    return newArray 

def whatNumIsThis(filePath):
    matchArray = []
    loadExamples = open('numberArEx.txt', 'r').read()
    loadExamples = loadExamples.split('\n')
    
    i = Image.open(filePath)
    
    iar = np.array(i)
    iarl = iar.tolist()
    
    inQuestion = str(iarl)
    
    for eachExample in loadExamples:
        if len(eachExample ) > 3:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentArr = splitEx[1]
            
            eachPixExample = currentArr.split('],') 
            
            eachPixInQ = inQuestion.split('],') 
            
            x = 0
            
            while x < len(eachPixExample):
                if eachPixExample[x] == eachPixInQ[x]:
                    matchArray.append(int(currentNum))
                 
                x += 1   
                
                
    #print   matchArray
    x = Counter(matchArray) 
    print x   
    
    
    graphX = []
    graphY = []
    
    for eachThing in x:
        #print eachThing
        graphX.append(eachThing)
        #print x[eachThing]
        graphY.append(x[eachThing])
        
    fig = plt.figure()
    ax1 = plt.subplot2grid((4,4), (0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4), (1,0), rowspan=3, colspan=4)
    
    ax1.imshow(iar)
    
    ax2.bar(graphX, graphY, align='center')
    plt.ylim(400)
    
    xloc = plt.MaxNLocator(12)
    
    ax2.xaxis.set_major_locator(xloc)
    plt.show()
    
    

        

#createExamples()
                



#whatNumIsThis('images/numbers/8.7.png'))



""" 
i =  Image.open("images/numbers/0.1.png")
iar = np.array(i)
 
i2 =  Image.open("images/numbers/y0.4.png")
iar2 = np.array(i2)

i3 =  Image.open("images/numbers/y0.5.png")
iar3 = np.array(i3)

i4 =  Image.open("images/sentdex.png")
iar4 = np.array(i4)



threshold(iar)
threshold(iar2)
threshold(iar3)
threshold(iar4)


fig = plt.figure()
ax1 = plt.subplot2grid((8,6), (0,0), rowspan = 4 , colspan = 3)
ax2 = plt.subplot2grid((8,6), (4,0), rowspan = 4 , colspan = 3)
ax3 = plt.subplot2grid((8,6), (0,3), rowspan = 4 , colspan = 3)
ax4 = plt.subplot2grid((8,6), (4,3), rowspan = 4 , colspan = 3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()


    
#i = Image.open("images/dotndot.png", )
i = Image.open("images/numbers/y0.5.png")
iar = np.array(i)
print(iar) 

plt.imshow(iar)

plt.show()

"""
