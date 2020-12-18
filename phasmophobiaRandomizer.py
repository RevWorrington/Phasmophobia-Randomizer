import random
import math
import os

def Main():

    
    #Player Count Request
    def getPlayerTotal():
        playerNumber = int(input("Enter the number of players (1-4): "))
        if playerNumber > 4 or playerNumber < 1:
            print("Invalid number of players, number must 1-4")
            getPlayerTotal()
        return playerNumber
    
    playerTotal = getPlayerTotal()

    #Duplicate Request
    def getDuplicateRequest():
        duplicateRequest = str(input("Do you want to allow item duplicates between players? (Y/N): "))
        duplicateRequest = duplicateRequest.upper()
        if duplicateRequest != str("Y") and duplicateRequest != str("N"):
            print("Invalid answer, must be either 'Y' or 'N'")
            getDuplicateRequest()
        if duplicateRequest == "Y":
            return True
        return False
    
    duplicateAllowed = getDuplicateRequest()
    
    #Master List for Storing Pulls
    itemAvailable = ["Candle","Crucifix","EMF","Weak Flashlight","Ghost Writing Book","Glow Stick","Infrared Light Sensor","Lighter","Motion Sensor","Parabolic Microphone","Photo Camera","Salt","Smudge Sticks","Sound Sensor","Spirit Box","Strong Flashlight","Thermometer","UV Flashlight","Video Camera"]
    itemAmount = [4,2,2,4,2,2,4,2,4,2,3,2,4,4,4,2,4,3,2,6]
    tempArray = []

    #Helper functions
    def itemRemove(removedItem):
        return itemAvailable.remove(removedItem)

    def checkAmount(item):
        #Check performed if duplicates are allowed
        itemName = itemAvailable[item]
        itemAmount[item] -= 1
        if itemAmount[item] == 0:
            itemRemove(itemName)
        return itemName

    def checkAmountDuplicate(item):
        #Check performed if duplicates are not allowed
        itemName = itemAvailable[item]
        itemAvailable.remove(itemName)
        return itemName

    def getItem(itemList):
        itemValue = random.randint(0,len(itemList)-1)
        if duplicateAllowed == False:
            return checkAmountDuplicate(itemValue)
        return checkAmount(itemValue)

    def getItemList(itemList2):
        tempArray = itemList2
        itemOne = getItem(tempArray)
        if itemOne in tempArray:
            tempArray.remove(itemOne)
        itemTwo = getItem(tempArray)
        if itemTwo in tempArray:
            tempArray.remove(itemTwo)
        itemThree = getItem(tempArray)
        newList = [itemOne,itemTwo,itemThree]
        return newList

    #Randomizer Output
    playerOn = 1
    for player in range(0,playerTotal):
        listPlayer = getItemList(itemAvailable)
        print("-----------------------------------------")
        print("Items for Player " + str(playerOn))
        print("Item 1: " + listPlayer[0])
        print("Item 2: " + listPlayer[1])
        print("Item 3: " + listPlayer[2])
        player += 1
        playerOn += 1

Main()
holdOpen = input("Good Hunting! Press any key to close.")   

