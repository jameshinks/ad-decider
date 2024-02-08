import pandas as pd
import random as rand

workbook = pd.read_excel('C:/Users/james/Desktop/School Files/Semesters/2023-Spring/CSCI 428/Assignments/Assignment6/Adolescent-Loot-Box-Data-for-OSF.xlsx')
workbook.head() 
constTraining = 1154 #The constant value of how many lines are in the Excel file
n = 30 #The number of reruns desired for the test
testSample = []
readLB = []
readMicro = []
meanLBNo = 0
meanMicroNo = 0
meanLBLow = 0
meanMicroLow = 0
meanLBHigh = 0
meanMicroHigh = 0
predictedGroup = []
actualGroup = []
#Global Variables for final output
noSample = []
lowSample = []
highSample = []
correctSample = []
estimateSample = []

def fillTestSample():
    global testSample
    i = 0
    while i < 100:
        random = rand.choice(range(1,constTraining))
        if random not in testSample:
            testSample.append(random)
            i += 1
def runTraining():
    global readLB
    global readMicro
    for i in range(constTraining):
        if pd.isna(workbook['LootBoxSpendDollars'].iloc[i]):
            readLB.append(0)
        else:
            readLB.append(workbook['LootBoxSpendDollars'].iloc[i])
        if pd.isna(workbook['MicrotransactionSpendDollars'].iloc[i]):
            readMicro.append(0)
        else:
            readMicro.append(workbook['MicrotransactionSpendDollars'].iloc[i])
    numNo = 0
    totalLBNo = 0
    totalMicroNo = 0
    numLow = 0
    totalLBLow = 0
    totalMicroLow = 0
    numHigh = 0
    totalLBHigh = 0
    totalMicroHigh = 0
    for i in range(constTraining):
        if i not in testSample:
            check = workbook['ProblemGamblingCategories'].iloc[i]
            if check == 0:
                numNo += 1
                totalLBNo += readLB[i]
                totalMicroNo += readMicro[i]
            elif check == 1:
                numLow += 1
                totalLBLow += readLB[i]
                totalMicroLow += readMicro[i]
            elif check == 2:
                numHigh += 1
                totalLBHigh += readLB[i]
                totalMicroHigh += readMicro[i]
    global meanLBNo
    global meanLBLow
    global meanLBHigh
    global meanMicroNo
    global meanMicroLow
    global meanMicroHigh
    meanLBNo = (totalLBNo)/(numNo)
    meanMicroNo = (totalMicroNo)/(numNo)
    meanLBLow = (totalLBLow)/(numLow)
    meanMicroLow = (totalMicroLow)/(numLow)
    meanLBHigh = (totalLBHigh)/(numHigh)
    meanMicroHigh = (totalMicroHigh)/(numHigh)
    print("Mean spent on Loot Boxes for those with No/Low/Med-High Probability of problem gambling:", meanLBNo, meanLBLow, meanLBHigh)
    print("Mean spent on Microtransactions for those with No/Low/Med-High Probability of problem gambling:", meanMicroNo, meanMicroLow, meanMicroHigh)
def runTesting():
    for i in testSample:
        lb = readLB[i]
        micro = readMicro[i]
        if abs(lb-meanLBNo) < abs(lb-meanLBLow) and abs(lb-meanLBNo) < abs(lb-meanLBHigh):
            lbDiff = lb-meanLBNo
            targetLB = 0
        elif abs(lb-meanLBLow) < abs(lb-meanLBNo) and abs(lb-meanLBLow) < abs(lb-meanLBHigh):
            lbDiff = lb-meanLBLow
            targetLB = 1
        else:
            lbDiff = lb-meanLBHigh
            targetLB = 2
        if abs(micro-meanMicroNo) < abs(micro-meanMicroLow) and abs(micro-meanMicroNo) < abs(micro-meanMicroHigh):
            microDiff = micro-meanMicroNo
            targetMicro = 0
        elif abs(micro-meanMicroLow) < abs(micro-meanMicroNo) and abs(micro-meanMicroLow) < abs(micro-meanMicroHigh):
            microDiff = micro-meanMicroLow
            targetMicro = 1
        else:
            microDiff = micro-meanMicroHigh
            targetMicro = 2
        if lbDiff > microDiff:
            target = targetLB
        else:
            target = targetMicro
        #print(lb, micro, meanLBNo, meanLBLow, meanLBHigh, meanMicroNo, meanMicroLow, meanMicroHigh) #Code for Troubleshooting
        #print("This subject is most closely related to the group", target)
        global predictedGroup
        predictedGroup.append(target)

def checkTesting():
    correctNo = 0
    incorrectNo = 0
    correctLow = 0
    incorrectLow = 0
    correctHigh = 0
    incorrectHigh = 0
    global actualGroup
    for i in testSample:
        actualGroup.append(workbook['ProblemGamblingCategories'].iloc[i]) #Stored in case future implementation will require
    for i in range(100):
        offset = i-1
        if predictedGroup[offset] == actualGroup[offset]:
            if predictedGroup[offset] == 0:
                correctNo += 1
            elif predictedGroup[offset] == 1:
                correctLow += 1
            else:
                correctHigh += 1
        else:
            if predictedGroup[offset] == 0:
                incorrectNo += 1
            elif predictedGroup[offset] == 1:
                incorrectLow += 1
            else:
                incorrectHigh += 1
    correctTotal = correctNo + correctLow + correctHigh
    incorrectTotal = incorrectNo + incorrectLow + incorrectHigh
    correctPercent = correctTotal/(correctTotal+incorrectTotal)
    global noSample
    global lowSample
    global highPercent
    global correctSample
    global estimateSample
    noPercent = (correctNo)/(correctNo+incorrectNo)
    noSample.append(noPercent)
    lowPercent = (correctLow)/(correctLow+incorrectLow)
    lowSample.append(lowPercent)
    highPercent = (correctHigh)/(correctHigh+incorrectHigh)
    highSample.append(highPercent)
    print("Percent correctly identified as No/Low/Med-High Probability Groups:", correctPercent)
    correctSample.append(correctPercent)
    estimateCorrect = 0
    estimateIncorrect = 0
    for i in range(100):
        offset = i-1
        if(predictedGroup[offset] == 0):
            if(actualGroup[offset] == 0):
                estimateCorrect += 1
            else:
                estimateIncorrect += 1
        else:
            if(actualGroup[offset] == 0):
                estimateIncorrect += 1
            else:
                estimateCorrect += 1
    estimatePercent = estimateCorrect/(estimateCorrect+estimateIncorrect)
    print("Percent correctly identifies as No/Any Probability Groups:", estimatePercent)
    estimateSample.append(estimatePercent)

def resetTests():
    global testSample
    global readLB
    global readMicro
    global meanLBNo
    global meanLBLow
    global meanLBHigh
    global meanMicroNo
    global meanMicroLow
    global meanMicroHigh
    global predictedGroup
    global actualGroup
    testSample = []
    readLB = []
    readMicro = []
    meanLBNo = 0
    meanMicroNo = 0
    meanLBLow = 0
    meanMicroLow = 0
    meanLBHigh = 0
    meanMicroHigh = 0
    predictedGroup = []
    actualGroup = []


def runTests():
    fillTestSample()
    runTraining()
    runTesting()
    checkTesting()

def main():
    for i in range(n):
        runTests()
        resetTests()
    finNoPercent = 0
    finLowPercent = 0
    finHighPercent = 0
    finCorrectPercent = 0
    finEstimatePercent = 0
    for i in range(n):
        offset = i-1
        finNoPercent += (noSample[offset]/n)
        finLowPercent += (lowSample[offset]/n)
        finHighPercent += (highSample[offset]/n)
        finCorrectPercent += (correctSample[offset]/n)
        finEstimatePercent += (estimateSample[offset]/n)
    print("Overall Output:")
    print("Percent Correctly identified as having No Risk of Problem Gambling:", finNoPercent)
    print("Percent Correctly identified as having Low Risk of Problem Gambling:", finLowPercent)
    print("Percent Correctly identified as having Med/High Risk of Problem Gambling:", finHighPercent)
    print("Percent Correctly identified into their group of No, Low, or Med/High Risk of Problem Gambling:", finCorrectPercent)
    print("Percent Correctly identified as either having No or Some Risk of Problem Gambling:", finEstimatePercent)
main()