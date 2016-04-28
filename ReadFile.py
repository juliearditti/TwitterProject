'''
Created on Apr 28, 2016

@author: juliearditti
'''
from operator import itemgetter

def filetolist(file):
    listinfo = []
    f = open(file)
    for line in f:
        line = line.strip().split()
        listinfo.append(line)
    f.close()
    return listinfo
    
def sumVolumes(file):
    tweetinfo = []
    totalVol = []
    for i in range(0, len(file), 2):
        tup = (file[i], file[i+1])
        tweetinfo.append(tup)
        sum = 0
        for num in file[i+1]:
            sum += float(num)
        totalVol.append(sum)
        
    return tweetinfo, totalVol
    
def findGreatestVol(tweetinfo, totalVol):
    least20 = []
    most20= []
    volIndicies = [(totalVol[i], i) for i in range(len(totalVol))]
    volIndicies = sorted(volIndicies, key=itemgetter(0))
    for i in range(0, 20):
        index = volIndicies[i][1]
        #print tweetinfo[index]
        tweet1 = [str(i) for i in tweetinfo[index][0]]
        tweet2 = [str(i) for i in tweetinfo[index][1]]
        least20.append((tweet1, tweet2))
    for i in range(len(totalVol)-20, len(totalVol)):
        index = volIndicies[i][1]
        tweet1 = [str(i) for i in tweetinfo[index][0]]
        tweet2 = [str(i) for i in tweetinfo[index][1]]
        most20.append((tweet1, tweet2))
    return least20, most20 
    
def createFile(least, most):
    file1 = open("least.txt", "w")
    file2 = open("most.txt", "w")
    for tup in least:
        
        file1.write(tup[0][1]+"\t")
        for i in tup[1]:
            file1.write(i+"\t")
        file1.write("\n")    
    for tup in most:
        file2.write(tup[0][1]+"\t")
        for i in tup[1]:
            file2.write(i+"\t")
        file2.write("\n")  

    file1.close()
    file2.close()

    return file1, file2
    
    
    
if __name__ == '__main__':
    file = filetolist("TwtHtag.txt")
    #print file
    lists = sumVolumes(file)
    tweetinfo = lists[0] 
    
    vol = lists[1]
    rankVol = findGreatestVol(tweetinfo, vol)
    least = rankVol[0]
    most = rankVol[1]
    file1, file2 = createFile(least, most)
    