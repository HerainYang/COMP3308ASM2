import csv
import numpy
import math
class dataManager:
    def __init__(self):
        self.attrList_yes = []
        for index in range(0, 8):
            self.attrList_yes.append([])
        self.attrList_no = []
        for index in range(0, 8):
            self.attrList_no.append([])
        self.stdList_yes = []
        self.stdList_no = []
        self.meanList_yes = []
        self.meanList_no = []


    def updateData(self, line: list):
        if line[8] == 'yes':
            for index in range(0, 8):
                self.attrList_yes[index].append(float(line[index]))
        else:
            for index in range(0, 8):
                self.attrList_no[index].append(float(line[index]))


def readCSV(csvFile, manager: dataManager):
    csvReader = csv.reader(csvFile)
    for line in csvReader:
        if len(line) != 9:
            print("format error")
            return -1
        manager.updateData(line)

    for index in range(0, 8):
        manager.stdList_yes.append(numpy.std(manager.attrList_yes[index], ddof=1))
        manager.stdList_no.append(numpy.std(manager.attrList_no[index], ddof=1))
        manager.meanList_yes.append(numpy.mean(manager.attrList_yes[index]))
        manager.meanList_no.append(numpy.mean(manager.attrList_no[index]))

    return 0

def calculateND(x_input, mean, std):
    part1 = 1/(std * math.sqrt(2*math.pi))
    #print("part1 is ", part1)
    part2 = math.pow(math.e, -(pow(x_input-mean, 2)/(2*pow(std, 2))))
    #print("part2 is", part2)
    return part1*part2

def run_NB(trainingFileName, testingFileName):
    manager = dataManager()
    trainingData = open(trainingFileName)
    testingData = open(testingFileName)
    readCSV(trainingData, manager)
    trainingData.close()

    csvReader = csv.reader(testingData)
    for line in csvReader:
        if len(line) != 8:
            print("format error")
            return -1
        pro_Yes = 1
        pro_No = 1
        for index in range(0, 8):
            #print("x", float(line[index]), "mean", manager.meanList_yes[index], "std", manager.stdList_yes[index], "-->", calculateND(float(line[index]), manager.meanList_yes[index], manager.stdList_yes[index]))
            pro_Yes *= calculateND(float(line[index]), manager.meanList_yes[index], manager.stdList_yes[index])
            pro_No *= calculateND(float(line[index]), manager.meanList_no[index], manager.stdList_no[index])
        pro_Yes *= (len(manager.attrList_yes[0]) / (len(manager.attrList_yes[0])+len(manager.attrList_no[0])))
        pro_No *= (len(manager.attrList_no[0]) / (len(manager.attrList_yes[0]) + len(manager.attrList_no[0])))
        #print("pro of yes is ", pro_Yes, ",pro of no is ", pro_No)
        if(pro_Yes >= pro_No):
            print("Yes")
        else:
            print("No")



    testingData.close()

    # for index in range(0, len(manager.attrList_no[0])):
    #     print("index", index, "with:",end=' ')
    #     for i in range(0, 8):
    #         print(manager.attrList_no[i][index], end=' ')
    #     print()
    #
    # for i in range(0, 8):
    #     print("index", i, "class yes, mean:", manager.meanList_yes[i], "std:", manager.stdList_yes[i])
    #     print("index", i, "class no, mean:", manager.meanList_no[i], "std:", manager.stdList_no[i])
    #
    # print(calculateND(60, 74.6, 8))
    # print(math.e)