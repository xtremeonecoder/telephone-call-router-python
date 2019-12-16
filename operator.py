##
## Telephone Call Router - Python Application
##
## @category   Python_Application
## @package    telephone-call-router
## @author     Suman Barua
## @developer  Suman Barua <sumanbarua576@gmail.com>
##

#!/usr/bin/env python3
from array import *
import re

## Prepare price-list according to operators
## @return available operators and their price lists
def getTelephoneOperators():
    operators = {
        "Operator-A" : {
            "1" : 0.9,
            "268" : 5.1,
            "46" : 0.17,
            "4620" : 0.0,
            "468" : 0.15,
            "4631" : 0.15,
            "4673" : 0.9,
            "46732" : 1.1
        },
        "Operator-B" : {
            "1" : 0.92,
            "44" : 0.5,
            "46" : 0.2,
            "467" : 1.0,
            "48" : 1.2
        },
        ## Uncomment Operator-C and Operator-D if you want to check with more operators
        # "Operator-C" : {
        #     "1" : 2.0,
        #     "44" : 1.0,
        #     "46" : 3.0,
        #     "46725" : 4.0,
        #     "467" : 1.2,
        #     "4672" : 2.0
        # },
        # "Operator-D" : {
        #     "46" : 4.0,
        #     "467" : 2.0,
        #     "46725" : 3.0,
        #     "4672" : 1.0,
        #     "48" : 3.0
        # }
    }

    return operators


## Calculate the cheapest operator
## @param matchedItems
## @return array
def calculateCheapestCallRate(matchedItems):
    ## Necessary variables initialization
    result = {}
    cheapestOperator = ""
    cheapestPrice = 999999.0

    ## Iterate throgh the mapped items and find the cheapest price
    for item in matchedItems:
        if matchedItems[item] < cheapestPrice:
            cheapestOperator = item
            cheapestPrice = matchedItems[item]

    ## Return result
    result[0] = cheapestOperator
    result[1] = cheapestPrice
    return result


############################### Main Program Starts Here #####################################

## Program Execution Starts From Here
phoneNumber = input("\nEnter Telephone Number: ")
phoneNumber = re.sub(r"\D", "", phoneNumber)

# Prepare price-list according to operators
operators = getTelephoneOperators()

## Iterate all the existing price-lists according to operators
## Explore all the price items, and calculate the cheapest one
matchedItems = {}
for operator in operators:
    ## Necessary variables initialization
    maxPrefixLength = 0;
    leastPrice = 0.0;
    leastPrefix = "null";

    ## Iterate through the available operators and explore their price-list
    for prefix in operators[operator]:
        ## Check if the prefix matches the number or not.
        ## Check if the previously matched prefix length
        ## is smaller than the currently matched prefix length
        ## We will consider the maximum-length matched prefix
        if re.search("^" + prefix + "(.*)", phoneNumber) and (maxPrefixLength < len(prefix)):
            leastPrefix = prefix
            leastPrice = operators[operator][prefix]
            maxPrefixLength = len(prefix)

    ## Prepare least-price object as per operator
    if leastPrefix != "null":
        matchedItems[operator] = leastPrice


## List down the found least-price operators
if len(matchedItems) > 0:
    print("\n------------------------------------------------------------------------\n")
    print("Total {0} operator(s) found for the number \"{1}\"".format(len(matchedItems), phoneNumber))
    for item in matchedItems:
        print("=> {0} offers ${1}/minute".format(item, matchedItems[item]))


## Calculate the cheapest operator among the cheaps
print("\n------------------------------------------------------------------------\n")

## Get cheapest call rate
result = calculateCheapestCallRate(matchedItems)
if result[0] != "":
    print("Cheapest operator is \"{0}\", which offers ${1}/minute\n".format(result[0], result[1]))
else:
    print("Sorry, no operator found!\n")
