#oarimah_Assign3.py
#################################################
##############Import tools#######################
from graphics import GraphicsWindow
import happy_histogram
import sys

################################################
#############Main Function######################
################################################

def main():
    tweets = input("Please input the twitter file name: ")  #read file name
    keywordFile = input("Please input the keyword file name: ")
    try: #try the following code
        tweets = open(tweets,'r',encoding="utf-8")    #read the tweets from the input file name
        p1 = [49.189787, -67.444574] #coordiante for point 1
        p2 = [24.660845, -67.444574] #coordiante for point 2
        p3 = [49.189787, -87.518395] #coordiante for point 3
        p4 = [24.660845, -87.518395] #coordiante for point 4
        p5 = [49.189787, -101.998892] #coordiante for point 5
        p6 = [24.660845, -101.998892] #coordiante for point 6
        p7 = [49.189787, -115.236428] #coordiante for point 7
        p8 = [24.660845, -115.236428] #coordiante for point 8
        p9 = [49.189787, -125.242264] #coordiante for point 9
        p10 = [24.660845, -125.242264] #coordiante for point 10

        ############################################################
        ##############Calculating area for zones#####################
        eastern = area(p1,p2,p3,p4)  #Calculating Eastern Area Zone
        central = area(p3,p4,p5,p6)  #Calculating Central Area Zone
        mountain = area(p5,p6,p7,p8) #Calculating Mountian Area Zone
        pacific = area(p7,p8,p9,p10) #Calculating Pacific Area Zone

        output = open("outEx.txt",'w')
        keywordsList = [] #creating a list to save keywords and their sentinal value
        keywords = open(keywordFile,"r",encoding="utf-8")  #Importing keywords from keywords.txt file
        kw = keywords.readline()    #Reading the first line of the keywords.txt

        #############################################################
        #######################Accessing and modifiying the keyword file############
        while kw !="":  #going through the keyword file
        #for kw in keywords:
            kw = cleanKeys(kw) #cleaing the kyword line using cleanKeys() funcction
            kw[1] = int(kw[1]) #converting kw[1] into intger for calcuation pourposes

            keywordsList.append(kw)  #appending kw to keywordsList list
            kw = keywords.readline() #reading the next line fo the file


        #############################################################
        #########################Creating area zone tweet storage list
        pacificCol=[]       #creating a pacific zone tweet list
        mountinCol = []     #creating a Mountain zone tweet list
        centralCol = []     #creating a central zone tweet list
        easternCol = []     #creating a Eastern zone tweet list
        outLocCol = []     #creating a Out of zone zone tweet list

        ###############################################################3
        ################saving the scors for each tweet to a list
        scorePacific = []                   #creating a list to save tweet score for Pacific
        scoreMountin = []           #creating a list to save tweet score for Mountain
        scoreCentral = []           #creating a list to save tweet score for Central
        scoreEastern = []           #creating a list to save tweet score for Eastern


        #tweet = tweets.readline()

        #################################################################
        ####################Accessing modifiying the tweet file along with score and tweet list
        for tweet in tweets:
            tweet = cleanKeywords(tweet)   #cleaning the tweet line
            #using the returnArea function to pin point the location of the tweet
            tweetLoc = returnArea([tweet[0],tweet[1]],eastern,"Eastern", pacific,"Pacific", mountain,"Mountin",central,"Central")
            if tweetLoc[1] == "Eastern": #if tht tweet was from Eastern reagon
                easternCol.append(tweet[5].split()) #add the tweet to Eastern list and split them
                #print(tweet[5])
                score(keywordsList,tweet[5].split(),scoreEastern)#using the score method to calcualte the score
            elif tweetLoc[1] == "Mountin":  #same description as in line 74
                mountinCol.append(tweet[5].split()) #same description as in line 75
                score(keywordsList,tweet[5].split(),scoreMountin) ##same description as in line 77
            elif tweetLoc[1] == "Central": #same description as in line 74
                centralCol.append(tweet[5].split()) #same description as in line 75
                score(keywordsList,tweet[5].split(),scoreCentral)#same description as in line 77
            elif tweetLoc[1] == "Pacific": #same description as in line 74
                pacificCol.append(tweet[5].split()) #same description as in line 75
                score(keywordsList,tweet[5].split(),scorePacific)#same description as in line 77
            else:
                outLocCol.append(tweet[5].split())

        meanEastern = mean(scoreEastern)  #find the mean of Eastern area
        meanCenteral = mean(scoreCentral)  #find the mean of Centeral area
        meanMountain = mean(scoreMountin)  #find the mean of Mountain area
        meanPacific = mean(scorePacific)  #find the mean of Pacific area

        print("number of tweets in Eastern zone is: ",len(easternCol)," Happiness score is: ",round(meanEastern,2))
        print("number of tweets in Centeral zone is: ",len(centralCol)," Happiness score is: ",round(meanCenteral,2))
        print("number of tweets in Mountain zone is: ",len(mountinCol)," Happiness score is: ",round(meanMountain,2))
        print("number of tweets in Pacific zone is: ",len(pacificCol)," Happiness score is: ",round(meanPacific,2))

        hhist = happy_histogram  #instanticating the happy_histogram Class
        #win= GraphicsWindow(640, 480) #defining a window size
        #canvas = win.canvas() #
        hhist.drawSimpleHistogram(meanEastern,meanCenteral,meanMountain,meanPacific) #invoking the drawSimpleHistogram() method for visual porpuses
        #win.wait() #to keep the canvas open
        tweets.close()  #to close the tweet file
        keywords.close() #to close the keyword file
    except IOError : #creat an exception incase the user input the wrong file name
        print("Error: file was not found.")
        sys.exit() #it exit the program

    except ValueError :#create an aexcpetion incase the user ad unreadable file
        print("Error: invalid file.")
        sys.exit() #it exits the program
    except RuntimeError as error :
        print("Error:", str(error))
        sys.exit() #it exits the program


##################################################################
#########################functions################################
##################################################################
##################################################################


############################################
#################Average functions
########The following function will calcualte the mean of a given list
def mean(numbers):
    return float(sum(numbers)) / len(numbers)  #return the sum of the numbers divded by the length of the list


############################################
##################Clean Keywords function
#it will take a string
def cleanKeywords(keywords):
    #will clean th string of words first from punctuation and then split them into a list
    keywords = keywords.replace("[","").replace("!","").replace("\n","").replace("]","").split(" ",5)
    #it removes comma from the first item on the list
    keywords[0] = keywords[0].replace(",", "")
    #convering the first 3 items on the list to float
    for i in range(3):
        keywords[i] = float(keywords[i])
    #it return the keywords into as a list
    return keywords

#####################################################
###############Clean keys function
#basic string cleaning function that ment for keywords.txt file
#you have to pass a string once you call the function
def cleanKeys(keywords):
    #it cleans the keywords form commas and then split them into a list
    keywords = keywords.replace(","," ").split()
    #it return the opperation as a list
    return keywords

##############################################
#########Find the min and max of the area
#it will take in coordinate as floats
def area(p1,p2,p3,p4):
    #it organises the coordinates into x and y
    x = [p1[0],p2[0],p3[0],p4[0]]
    y = [p1[1],p2[1],p3[1],p4[1]]
    #it finds the max and min of x and y
    xMin = min(x)
    xMax = max(x)
    yMin = min(y)
    yMax = max(y)
    #it returns the area the would help find zone for each coordinate in a list table format
    return[[xMin,xMax],[yMin,yMax]]

##############################################
#################Checks area function########
#Find if coordinate falls with in an area
#it will only return a boolean based on the coordinates that is given
def checkArea(cords,area):
    #it checks if the cordinates falls with in a given area
    if cords[0]> area[0][0] and cords[0]<area[0][1]:
        if cords[1]> area[1][0] and cords[1]<area[1][1]:
            #if true, it will retun true
            return True
        else:
            #else it will return false
            return False
    else:
        #if the first condition was false, it will return false
        return False

##########################################################
#################returns area for giving coordinates
################it will take in cooriante, area, and area name for each zone
def returnArea(cords,area1,areaName1,area2,areaName2,area3,areaName3,area4,areaName4):
    #it checks if the coordinate falles within the area using the checkArea function
    #the same proccess will apply for all givin coordinate for all zone
    #it will return cords and areaname of for each tweets
    if checkArea([cords[0],cords[1]],area1) == True:
        return(cords,areaName1)
    elif checkArea([cords[0],cords[1]],area2) == True:
        return(cords,areaName2)
    elif checkArea([cords[0],cords[1]],area3) == True:
        return(cords,areaName3)
    elif checkArea([cords[0],cords[1]],area4) == True:
        return(cords,areaName4)
    else:
        #if it is outside of specfied zone, it will return that the area is not with in our zone
        return(cords,"no area in our database")



######################################################3
#score function
#it takes in keywords, the tweets and the area
#it will return by appending total to the area score list

def score(keywords,tweets,area):

    total=0 #variable total is set to zero. It will keep a track of the total
    count = 0 #it will counting occorances
    for key in keywords: #it loop through each keywords
        for tweet in tweets: #it will loop throug all the tweets
            if key[0].lower() == tweet.lower(): #it checks if there is a match between a tweet word and keyword and it convert them to all small caps
                count = count+1 #it add counts
                total = total+key[1] #it sum up the total
    if total != 0: #if total does not equal zero
        total = total/count #it averages out
        return area.append(total) #it append the area list with the tweet score
    else:
        total = 0 #else it will return and append zero to the list
        return area.append(total)



main()
