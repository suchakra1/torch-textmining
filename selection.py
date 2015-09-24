import csv
import sys

#python program  to select and clean data

#Text Classification using Deep Learning Approach
#Subhendu Chakrabarti

#input Train.csv, stack exchange data
#output train and test data .csv 

inputFile = "Train.csv"
outputFile = "train_se.csv"
testFile = "test_se.csv"

#pure sample 14 regular programming langaages
#llist=['c++','html','php','java','perl','javascript','python','xml','asp','c#','ruby','.net','jQuery','sql']

#noise sample with last three common keywords
llist=['c++','html','php','java','perl','javascript','python','xml','asp','c#','ruby','user','how','what']

sample = 200001

indexlist = []


if __name__ == "__main__":
#
#   Training data from Train.csv
#   Id, Title, Body, Tag
   
    f = open(outputFile, 'wb')
    out = csv.writer(f, delimiter=',')
    f1 = open(testFile, 'wb')
    tout = csv.writer(f1, delimiter=',')

    i = 0

    with open(inputFile) as csvfile:
        csvfile.readline() # removes header

        for row in csv.reader(csvfile, delimiter=',', quotechar='"'):
 
            #print row[1]
            for lng in llist:
                if row[1].find(lng) != -1:
                    i += 1
                    row[0] = str(llist.index(lng)+1)
                    if i < sample:
                        tout.writerow([" ".join(part.split()) for part in row])
                    else:    
                        out.writerow([" ".join(part.split()) for part in row])

                   #                    print row[0]
                    
            if i > sample*6: break
            
            


    f.close()
    f1.close()
