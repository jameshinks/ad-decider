import pandas as pd
import random as rand

workbook = pd.read_excel('C:/Users/james/Desktop/School Files/Semesters/2023-Spring/CSCI 428/Assignments/Assignment6/Adolescent-Loot-Box-Data-for-OSF.xlsx')
workbook.head() 
constTraining = 1154 #The constant value of how many lines are in the Excel file
n = 30 #The number of reruns desired for the test
#Global variables for the final output
adsChanceNo = []
adsChanceLow = []
adsChanceHigh = []
adsChance = []
purchaseChanceAds = []
purchaseChanceNo = []
purchaseChance = []
purchaseChanceReceived = []
testSample = []
def fillTestSample():
    global testSample
    i = 0
    while i < 100:
        random = rand.choice(range(1,constTraining))
        if random not in testSample:
            testSample.append(random)
            i += 1
#Global variables storing differences
genderDiff = [0,0,0]
ageDiff = [0,0,0]
countryDiff = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#Lists containing the various responses on the Excel sheet for each category
maleSynonyms = ['male', 'Male', 'm', 'M', 'Boy', 'Man', 'man', 'Man (male)', 'MALE', 'Dude', ' Male', 'Make', 'Masculine', 'Hombre', 'male penis']
femaleSynonyms = ['female', 'Female', 'f', 'F', 'Female(She/Her)']
other = ['other', 'Other', 'genderfluid', 'Genderfluid', 'Non-Binary', 'Non-binary', 'Non Binary', 'Non binary', 'Non gender', 'Fluid', 'zhi', 'Mies', 'Agender /trans boy']
ignore = ['Apache helicopter', 'Rather now say', 'Dragon']
#Original readthrough of the Excel Sheet: Stores $ Spent on Lootboxes/Microtransactions, and calculates a mean spent as a baseline
readLB = []
totalLB = 0
numLB = 0
numLBSpent = 0
readMicro = []
totalMicro = 0
numMicro = 0
numMicroSpent = 0
for i in range(constTraining):
    if i not in testSample:
        lootboxSpent = workbook['LootBoxSpendDollars'].iloc[i]
        microSpent = workbook['MicrotransactionSpendDollars'].iloc[i]
        readLB.append(lootboxSpent)
        numLB += 1
        if(workbook['HaveBoughtLB'].iloc[i] == 1):
            totalLB += lootboxSpent
            numLBSpent += 1
        readMicro.append(microSpent)
        numMicro += 1
        if(microSpent != 0):
            totalMicro += microSpent
            numMicroSpent += 1
    else:
        readLB.append(-1)
        readMicro.append(-1)
probLB = numLBSpent/numLB
meanLB = totalLB/numLB
probMicro = numMicroSpent/numMicro
meanMicro = totalMicro/numMicro
print(numLBSpent, "(", probLB, ") spent a total of", totalLB, "on Lootboxes for an average of", meanLB, "each.")
print(numMicroSpent, "(", probMicro, ") spent a total of", totalMicro, "on Microtransactions for an average of", meanMicro, "each.")
percentSpentLB = numLBSpent/numLB
percentSpentMicro = numMicroSpent/numMicro
print("The percent spent on LB/Microtransactions are", percentSpentLB, percentSpentMicro)
#Array Cleanup
for i in range(constTraining):
    if i not in testSample:
        if(pd.isna(readLB[i])):
            readLB[i] = 0
#Standard deviation has been shown to not be an effective measure for this sample, code to checck it left in
# #Reads through the lists of $ spent after having the means calculated to determine standard deviation
# stdNumeratorLB = 0
# stdNumearatorMicro = 0
# for i in range(constTraining):
#     stdNumeratorLB += (readLB[i]-meanLB)*(readLB[i]-meanLB)
#     stdNumearatorMicro += (readMicro[i]-meanMicro)*(readMicro[i]-meanMicro)
# stdLB = math.sqrt(stdNumeratorLB/1153)
# stdMicro = math.sqrt(stdNumearatorMicro/1153)
# print(stdLB, stdMicro)
#Calculates the individual means for LB spending for those with no, low, and high vulnerability to problem gambling
numNoProb = 0 
numLowProb = 0
numHighProb = 0
def gamblingvulnStats():
    global numNoProb
    zeroNoProb = 0
    totalNoProb = 0
    global numLowProb 
    zeroLowProb = 0
    totalLowProb = 0
    global numHighProb 
    zeroHighProb = 0
    totalHighProb = 0
    for i in range(constTraining):
        if i not in testSample:
            sent = workbook['ProblemGamblingCategories'].iloc[i]
            if(sent == 0):
                numNoProb += 1
                if readLB[i] != 0:
                    totalNoProb += readLB[i]
                else:
                    zeroNoProb += 1
            if(sent == 1):
                numLowProb += 1
                if readLB[i] != 0:
                    totalLowProb += readLB[i]
                else:
                    zeroLowProb += 1
            if(sent == 2):
                numHighProb += 1
                if readLB[i] != 0:
                    totalHighProb += readLB[i]
                else:
                    zeroHighProb += 1
    probNoProb = (numNoProb-zeroNoProb)/(numNoProb)
    probLowProb = (numLowProb-zeroLowProb)/(numLowProb)
    probHighProb = (numHighProb-zeroHighProb)/(numHighProb)
    meanNoProb = totalLowProb/(numNoProb-zeroNoProb)
    meanLowProb = totalLowProb/(numLowProb-zeroLowProb)
    meanHighProb = totalHighProb/(numHighProb-zeroHighProb)
    print("Number of subjects in each range:", numNoProb, numLowProb, numHighProb)
    print("Probability a subject in each range purchases a LB:", probNoProb, probLowProb, probHighProb)
    print("Total spent on LB in the range:", totalNoProb, totalLowProb, totalHighProb)
    print("Mean spent of those in the range that purchased a LB:", meanNoProb, meanLowProb, meanHighProb)
    percentSpentNo = (numNoProb-zeroNoProb)/numNoProb
    percentSpentLow = (numLowProb-zeroLowProb)/numLowProb
    percentSpentHigh = (numHighProb-zeroHighProb)/numHighProb
    print("Percent of subjects that spent money on LB:", percentSpentNo, percentSpentLow, percentSpentHigh)

    #Standard deviation has been shown to not be an effective measure for this sample, code to checck it left in
    # #Calculates standard deviation for those with no, low, and high vulnerability to problem gambling
    # stdNumeratorNo = 0
    # stdNumeratorLow = 0
    # stdNumeratorHigh = 0
    # for i in range(constTraining):
    #     sent = workbook['ProblemGamblingCategories'].iloc[i]
    #     if(sent == 0):
    #         if readLB[i] != 0:
    #             stdNumeratorNo += (readLB[i]-meanNoProb)*(readLB[i]-meanNoProb)
    #     if(sent == 1):
    #         if readLB[i] != 0:
    #             stdNumeratorLow += (readLB[i]-meanLowProb)*(readLB[i]-meanLowProb)
    #     if(sent == 2):
    #         if readLB[i] != 0:
    #             stdNumeratorHigh += (readLB[i]-meanHighProb)*(readLB[i]-meanHighProb)
    # stdNo = math.sqrt(stdNumeratorNo/1153)
    # stdLow = math.sqrt(stdNumeratorLow/1153)
    # stdHigh = math.sqrt(stdNumeratorHigh/1153)
    # print("Standard deviations:", stdNo, stdLow, stdHigh)

#Calculates the mean spent and percent of subjects who did purchase LB based on gender (Male, Female, Other)
def genderStats():
    maleCount = 0
    maleNumSpent = 0
    maleTotalSpent = 0
    femaleCount = 0
    femaleNumSpent = 0
    femaleTotalSpent = 0
    otherCount = 0
    otherNumSpent = 0
    otherTotalSpent = 0
    ignoreCount = 0
    for i in range(constTraining):
        if i not in testSample:
            gender = workbook['Gender'].iloc[i]
            if gender in maleSynonyms:
                maleCount += 1
                if readLB[i] != 0:
                    maleNumSpent += 1
                    maleTotalSpent += readLB[i]
            elif gender in femaleSynonyms:
                femaleCount += 1
                if readLB[i] != 0:
                    femaleNumSpent += 1
                    femaleTotalSpent += readLB[i]
            elif gender in other:
                otherCount += 1
                if readLB[i] != 0:
                    otherNumSpent += 1
                    otherTotalSpent += readLB[i]
            elif gender in ignore or pd.isna(gender):
                ignoreCount += 1
            else: #Checks for any entry in the data that has not been covered by gender lists
                print(gender)
    maleProb = (maleNumSpent/maleCount)
    maleMean = maleTotalSpent/maleNumSpent
    femaleProb = (femaleNumSpent/femaleCount)
    femaleMean = femaleTotalSpent/femaleNumSpent
    otherProb = (otherNumSpent/otherCount)
    otherMean = otherTotalSpent/otherNumSpent
    if ignoreCount != 0:
        print("Had to throw out", ignoreCount, "subjects due to invalid/no entry for Gender")
    print("Out of", maleCount, "male subjects,", maleNumSpent, "(", maleProb, ") have purchased LB at a total of", maleTotalSpent, "or a mean of", maleMean, "each.")
    print("Out of", femaleCount, "female subjects,", femaleNumSpent, "(", femaleProb, ") have purchased LB at a total of", femaleTotalSpent, "or a mean of", femaleMean, "each.")
    print("Out of", otherCount, "subjects of other genders,", otherNumSpent, "(", otherProb, ") have purchased LB at a total of", otherTotalSpent, "or a mean of", otherMean, "each.")
    extremeMaleSpenders = 0
    extremeFemaleSpenders = 0
    extremeOtherSpenders = 0
    for i in range(constTraining):
        if i not in testSample:
            gender = workbook['Gender'].iloc[i]
            if gender in maleSynonyms:
                if readLB[i] > maleMean*3:
                    extremeMaleSpenders += 1
            elif gender in femaleSynonyms:
                if readLB[i] > femaleMean*3:
                    extremeFemaleSpenders += 1
            elif gender in other:
                if readLB[i] > otherMean*3:
                    extremeOtherSpenders += 1
    percentExtremeMale = extremeMaleSpenders/maleNumSpent
    percentExtremeFemale = extremeFemaleSpenders/femaleNumSpent
    percentExtremeOther = extremeOtherSpenders/otherNumSpent
    #print("Percentage of subjects who have purchased LBs worth at least 3 times the mean for their group:", percentExtremeMale, percentExtremeFemale, percentExtremeOther)
    global genderDiff
    genderDiff[0] = (maleProb-probLB)
    genderDiff[1] = femaleProb-probLB
    genderDiff[2] = otherProb-probLB
    print("The difference in percent chance to buy a LB based on gender:", genderDiff[0], genderDiff[1], genderDiff[2])
def ageStats():
    eighteenCount = 0
    eighteenSpentCount = 0
    eighteenTotal = 0
    seventeenCount = 0
    seventeenSpentCount = 0
    seventeenTotal = 0
    sixteenCount = 0
    sixteenSpentCount = 0
    sixteenTotal = 0
    for i in range(constTraining):
        if i not in testSample:
            age = workbook['Age'].iloc[i]
            if age == 18:
                eighteenCount += 1
                if readLB[i] != 0:
                    eighteenSpentCount += 1
                    eighteenTotal += readLB[i]
            if age == 17:
                seventeenCount += 1
                if readLB[i] != 0:
                    seventeenSpentCount += 1
                    seventeenTotal += readLB[i]
            if age == 16:
                sixteenCount += 1
                if readLB[i] != 0:
                    sixteenSpentCount += 1
                    sixteenTotal += readLB[i]
    eighteenProb = eighteenSpentCount/eighteenCount
    eighteenMean = eighteenTotal/eighteenSpentCount
    seventeenProb = seventeenSpentCount/seventeenCount
    seventeenMean = seventeenTotal/seventeenSpentCount
    sixteenProb = sixteenSpentCount/sixteenCount
    sixteenMean = sixteenSpentCount/sixteenCount
    global ageDiff
    ageDiff[2] = eighteenProb-probLB
    ageDiff[1] = seventeenProb-probLB
    ageDiff[0] = sixteenProb-probLB
    print("Percentage of students in each age group that purchased a LB:", eighteenProb, seventeenProb, sixteenProb)
    print("Difference in percent per age group from percent of whole population:", ageDiff[2], ageDiff[1], ageDiff[0])
def countryStats():
    countryNum = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    countrySpentNum = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    countryTotal = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(constTraining):
        if i not in testSample:
            country = workbook['Country'].iloc[i] - 1
            countryNum[country] += 1
            if readLB[i] != 0:
                countrySpentNum[country] += 1
                countryTotal[country] += readLB[i]
    countryProb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    countryMean = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    global countryDiff
    for i in range(24):
        if countryNum[i] != 0:
            countryProb[i] = countrySpentNum[i]/countryNum[i]
            if countrySpentNum[i] != 0:
                countryMean[i] = countryTotal[i]/countrySpentNum[i]
        countryDiff[i] = countryProb[i]-probLB
        #print(countryDiff[i])

def testData():
    adsGiven = [0,0,0,0,0]
    noAdsGiven = [0,0,0,0,0]
    for i in testSample:
        offset = i
        gender = workbook['Gender'].iloc[offset]
        age = workbook['Age'].iloc[offset]
        country = workbook['Country'].iloc[offset] - 1
        global genderDiff
        global ageDiff
        global countryDiff
        genD = 0
        if gender in maleSynonyms:
            genD = genderDiff[0]
        elif gender in femaleSynonyms:
            genD = genderDiff[1]
        elif gender in other   : 
            genD = genderDiff[2]
        ageD = ageDiff[age-16]
        if country < len(countryDiff) + 1:
            countryD = countryDiff[country]
        ads = False
        if abs(genD) > abs(ageD) and abs(genD) > abs(countryD):
            #print("The trait with the most difference from the population mean for subject", offset, "is their gender,", gender, ", which has a probability", genD, "different from the population.")
            if genD > 0:
                ads = True
        elif abs(ageD) > abs(genD) and abs(ageD) > abs(countryD):
            #print("The trait with the most difference from the population mean for subject", offset, "is their age,", age, ", which has a probability", ageD, "different from the population.")
            if ageD > 0:
                ads = True
        elif abs(countryD) > abs(genD) and abs(countryD) > abs(ageD):
            #print("The trait with the most difference from the population mean for subject", offset, "is their country,", country, ", which has a probability", countryD, "different from the population.")
            if countryD > 0:
                ads = True
        else:
            print("Troubleshoot:", genD, ageD, countryD) #Troubleshoots in case of equal probabilities for now
        ##Only considers those differences that have a > 5% impact for making the precition
        # if genD < .1:
        #     genD = 0
        # if countryD < .1:
        #     countryD = 0
        # if ageD < .1:
        #     ageD = 0
        # if(genD+countryD+ageD > 0):
        #     ads = True
        if ads:
            chance = int(workbook['ProblemGamblingCategories'].iloc[offset])
            adsGiven[chance] += 1
            if workbook['HaveBoughtLB'].iloc[offset] == 1:
                adsGiven[3] += 1
            else:
                adsGiven[4] += 1
        elif not ads:
            chance = int(workbook['ProblemGamblingCategories'].iloc[offset])
            noAdsGiven[chance] += 1
            if workbook['HaveBoughtLB'].iloc[offset] == 1:
                noAdsGiven[3] += 1
            else:
                noAdsGiven[4] += 1
    percentGivenAds = []
    percentGivenAds.append(adsGiven[0]/(adsGiven[0]+noAdsGiven[0]))
    percentGivenAds.append(adsGiven[1]/(adsGiven[1]+noAdsGiven[1]))
    percentGivenAds.append(adsGiven[2]/(adsGiven[2]+noAdsGiven[2]))
    overallPercentGivenAds = (adsGiven[0] + adsGiven[1] + adsGiven[2])/(adsGiven[0] + adsGiven[1] + adsGiven[2] + noAdsGiven[0] + noAdsGiven[1] + noAdsGiven[2])
    percentAdsSpent = (adsGiven[3])/(adsGiven[3]+adsGiven[4])
    percentNoAdsSpent = (noAdsGiven[3])/(noAdsGiven[3]+noAdsGiven[4])
    percentSpentReceive = (adsGiven[3])/(adsGiven[3]+noAdsGiven[3])
    percentSpent = (adsGiven[3]+noAdsGiven[3])/(adsGiven[3]+adsGiven[4]+noAdsGiven[3]+noAdsGiven[4])
    global adsChanceNo
    global adsChanceLow
    global adsChanceHigh
    global adsChance
    global purchaseChance
    global purchaseChanceAds
    global purchaseChanceNo
    global purchaseChanceReceived
    print("Chances to see ads:")
    print("No Risk:", percentGivenAds[0])
    adsChanceNo.append(percentGivenAds[0])
    print("Low Risk:", percentGivenAds[1])
    adsChanceLow.append(percentGivenAds[1])
    print("Med-High Risk:", percentGivenAds[2])
    adsChanceHigh.append(percentGivenAds[2])
    print("Overall:", overallPercentGivenAds)
    adsChance.append(overallPercentGivenAds)
    print("Percent of those who were given ads that purchased a LB:", percentAdsSpent)
    purchaseChanceAds.append(percentAdsSpent)
    print("Percent of those who did not receive an ad that purchased a LB:", percentNoAdsSpent)
    purchaseChanceNo.append(percentNoAdsSpent)
    print("Percent of those who purchased a LB that received an ad", percentSpentReceive)
    purchaseChanceReceived.append(percentSpentReceive)
    print("Percent that purchased lootboxes:", percentSpent)
    purchaseChance.append(percentSpent)
def resetTests():
    global genderDiff
    global ageDiff
    global countryDiff
    global numNoProb
    global numLowProb
    global numHighProb
    global testSample
    genderDiff = [0,0,0]
    ageDiff = [0,0,0]
    countryDiff = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  
    numNoProb = 0 
    numLowProb = 0
    numHighProb = 0
    testSample = []
def runTests():
    fillTestSample()
    gamblingvulnStats()
    genderStats()
    ageStats()
    countryStats()
    testData()

def main():
    for i in range(n):
        runTests()
        resetTests()
    finChanceNo = 0
    finChanceLow = 0
    finChanceHigh = 0
    finChance = 0
    finPurchaseAds = 0
    finPurchaseNo = 0
    finAdsPurchase = 0
    finPurchaseChance = 0
    for i in range(n):
        offset = i-1
        finChanceNo += (adsChanceNo[offset]/n)
        finChanceLow += (adsChanceLow[offset]/n)
        finChanceHigh += (adsChanceHigh[offset]/n)
        finChance += (adsChance[offset]/n)
        finPurchaseAds += (purchaseChanceAds[offset]/n)
        finPurchaseNo += (purchaseChanceNo[offset]/n)
        finAdsPurchase += (purchaseChanceReceived[offset]/n)
        finPurchaseChance += (purchaseChance[offset]/n)
    print("Overall Output:")
    print("Overall Chance to See Advertisements:", finChance)
    print("Chance to See Advertisements Given Risk of Gambling Addiction:")
    print("No Risk:", finChanceNo)
    print("Low Risk:", finChanceLow)
    print("Medium-High Risk:", finChanceHigh)
    print("Overall percent of subjects that purchased a LB:", finPurchaseChance)
    print("Percent of those who would be shown ads that purchased a LB:", finPurchaseAds)
    print("Percent of those who would not be shown ads that purchased a LB:", finPurchaseNo)
    print("Percent of those that purchased a LB that would have been shown an ad:", finAdsPurchase)
    
main()