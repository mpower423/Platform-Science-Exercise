# Coding Exercise for Platform Science Interview
# Maria Power
# Dec. 19, 2023

# Caclulate the SS for each combination of drivers and destinations  and determine the best match using the following rules:
# If the length of the shipment's destination street name is even, the base suitability score (SS) is the number of vowels in the driver’s
# name multiplied by 1.5. (#note: I am assuming y as a consonant)
# If the length of the shipment's destination street name is odd, the base SS is the number of consonants in the driver’s name multiplied
# by 1.
# If the length of the shipment's destination street name shares any common factors (besides 1) with the length of the driver’s name, the
# SS is increased by 50% above the base SS.
#
#Note: I am assuming the street name is the characters after the address number up to the comma 
# Once a driver is matched, they are removed from the list
#

# Possible Optimizations/Improvements:
#
# 1) get factors function can be done more efficiently, eg. when finding first factor, do the division and recursively call the getFactors() for the result
# introduces recursion so that may not be more efficient in other ways
#
# 2) don't do calculations more than once and store the result for further use. Eg. calculate the driver's factors the first time but not after
#
# 3) Error handling/data exceptions (bad data)

# Run instructions:
# Based on Python 3.12
# can be invoked from the commandline with `python ps_excercise.py <destination list filename> <driver list filename>`
# where <destination list filename> is the filename (in the same directory of the prorgram file) and
#       <driver list filename> is the filename (in the same directory of the program file)
# if the filenames are not given, you will be prompted for them.


from collections import Counter
import re
import sys

# function to find the factors of a number (brute force) and skipping 1

def getFactors(x):
    factors = []
    for i in range(2, x + 1):
        if x % i == 0:
            factors.append (i)
    return (factors)


# program start
# Get the data first and strip out new lines: 

# Accept arguments on the commandline, if less than needed prompt:

args = sys.argv

# get shipment destination list
if len(args) > 1:
    shipmentFileName = args[1]
else:
    shipmentFileName = input('Enter Shipment Destinations filename: ')

shipmentFile = open(shipmentFileName, 'r')
shipments = shipmentFile.read().splitlines()

#get driver list
if len(args) > 2:
    driverFileName = args[2]
else:
    driverFileName = input('Enter Driver filename: ')

driverFile = open(driverFileName, 'r')
drivers = driverFile.read().splitlines()

# define vowel and consonant set. Note: y is treated as a consonant
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

for sIdx, s in enumerate(shipments):
    maxSS = 0
    maxSSIdx = 0
    streetName = re.findall(r'^\d+|\S+ +\S+$', s.split(',')[0])[1]
    # print (s, streetName)
    lenShipment = len(streetName)
    sFactors = getFactors(lenShipment)
    # print (streetName, lenShipment)
    for dIdx, d in enumerate(drivers):
        countOfChars = Counter(d.lower())
        numVowels = 0
        numConsonants = 0
        SS = 0

        for v in vowels: numVowels += countOfChars[v]
        for c in consonants: numConsonants += countOfChars[c]

        if lenShipment % 2 == 0: #even value
            SS = numVowels * 1.5
        else: #odd value
            SS = numConsonants

        for f in getFactors(len(d)):
            if f in sFactors:
                SS += SS * .5
                break # only need to confirm one factor match

        if SS > maxSS:
            maxSS = SS
            maxSSIdx = dIdx

    print ('For Shipment Destination #', sIdx, ":", s, 'the best driver is', ': ', drivers[maxSSIdx], 'with a score of ', maxSS)

    # Remove selected driver from list
    
    drivers.remove(drivers[maxSSIdx])


        

