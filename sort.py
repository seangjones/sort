#!C:\Users\1000c_000\AppData\Local\Programs\Python\Python36\python.exe
import os
from random import *

fileDir = os.path.dirname(os.path.realpath('__file__'))
#print('fileDir = '+fileDir)
relPath = 'data\\numbers.txt'
data_file_path = os.path.join(fileDir, relPath)

def sort():
    print("sort: start")

    #open data file for reading
    data_file = open(data_file_path, 'r')

    myList = []

    for line in data_file:
        myList.append(line.rstrip())

    print('Unsorted list:\n')
    print (myList)

    myList.sort()

    print('Sorted list:\n')
    print (myList)

    #close the data file
    data_file.close()


    #print("sort: end")

def create_data_file():
    print("create_data_file: start")

    #print("Creating data file of numbers at " + data_file_path)
    data_file = open(data_file_path, 'w')
    #print(data_file_path + " opened for writing")

    #number of values to put into file
    numberOfValues = randint(1,100)
    print('Generating %d random numbers...' % numberOfValues)
    for i in range(numberOfValues):
        randomNumber = randint(10,99)
        data_file.write('%d\n' % randomNumber)
        #print('%d: %d' % (i, randomNumber))

    #close the data file
    data_file.close()

    #print("create_data_file: end")


if __name__ == '__main__':
    print("main: Start")
    create_data_file()
    sort()
    print ("main: End")
