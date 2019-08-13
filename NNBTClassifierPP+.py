#Nearest neighbour approach to classification of breast tissue after pre-processing data and removing bad fields from the dataset(NNBTClassifier+)

import datetime
print(datetime.datetime.now())

def dist(l1, l2):
    temp = 0
    for x in [2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,29]:
        temp += (float(l1[x]) - float(l2[x])) ** 2
    distance = temp ** 0.5
    return distance

f = open("wbtdPP.txt", "r")

data = []
record = []
dList = []
nnList = []
diagnosis = []

for line in f:
    sTemp = str(line) 
    record = list(sTemp.split(","))
    data.append(record)

f.close()

print("Total size of dataset: ", len(data), " records found.")

#Building a prediction list

for i in range(0, len(data)):
    dList = []
    for j in range(0, len(data)):
        if i != j:
            d = dist(data[i], data[j])
            dList.append(d)
    for z in range(0, len(dList)):
        if dList[z] == min(dList):
            nnList.append(z)
    print(".", end = "")
print()
correctpred = 0

for q in range(0, len(data)):
    if data[q][1] == data[nnList[q]][1]:
        correctpred += 1
accuracy = (correctpred / int(len(data))) * 100

print("Accuracy of NNBTPP+ Classifier =", accuracy, "%")
print("No. of correct predictions =", correctpred)
print(datetime.datetime.now())
input()
