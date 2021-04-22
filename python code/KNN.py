import math
import csv

class patient:
    def __init__(self, a0, a1, a2, a3, a4, a5, a6, a7):
        self.attrList = []
        self.classVal = None
        self.attrList.append(a0)
        self.attrList.append(a1)
        self.attrList.append(a2)
        self.attrList.append(a3)
        self.attrList.append(a4)
        self.attrList.append(a5)
        self.attrList.append(a6)
        self.attrList.append(a7)
        self.distance = 0


def readCSV(csvFile, training: bool):
    if training:
        numOfAttr = 9
    else:
        numOfAttr = 8
    csvReader = csv.reader(csvFile)
    patientList = []
    for line in csvReader:
        if len(line) != numOfAttr:
            print("format error")
            return None
        patientList.append(
            patient(float(line[0]), float(line[1]), float(line[2]), float(line[3]), float(line[4]), float(line[5]),
                    float(line[6]), float(line[7])))
        if training:
            patientList[-1].classVal = line[8]
    return patientList

def sortKey(target: patient):
    return target.distance

def findKNeighbor(targetPatient: patient, trainingList: list, ruleK):
    neighbours = []
    for candidate in trainingList:
        euclideanDistance(targetPatient, candidate) # will update distance for all neighbor
        if len(neighbours) < ruleK:
            neighbours.append(candidate)
            neighbours.sort(key=sortKey, reverse=True)
        else:
            if candidate.distance < neighbours[0].distance:
                neighbours.pop(0)
                neighbours.append(candidate)
                neighbours.sort(key=sortKey, reverse=True)
    return neighbours

def euclideanDistance(targetPatient: patient, trainingPatient: patient):
    sumBeforeSqrt = 0
    for index in range(0, len(targetPatient.attrList)):
        sumBeforeSqrt += math.pow((targetPatient.attrList[index] - trainingPatient.attrList[index]), 2)
    trainingPatient.distance = math.sqrt(sumBeforeSqrt)

def run_KNN(trainingFileName, testingFileName, K):
    trainingData = open(trainingFileName)
    testingData = open(testingFileName)
    training_patientList = readCSV(trainingData, True)
    testing_patientList = readCSV(testingData, False)
    trainingData.close()
    testingData.close()

    testing_patientList.sort(key=sortKey)

    for element in testing_patientList:
        countingYes = 0
        countingNo = 0
        #print("*************testing*************", element.attrList)
        neighbours = findKNeighbor(element, training_patientList, K)
        for neighbor in neighbours:
            #print(neighbor.attrList, "with distance", neighbor.distance, ", and it say[", neighbor.classVal, "]")
            if neighbor.classVal == 'yes':
                countingYes += 1
            else:
                countingNo += 1
        if countingYes >= countingNo:
            print('yes')
        else:
            print('no')
