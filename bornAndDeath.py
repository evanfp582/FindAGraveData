#! python3

import re, pyperclip
text=pyperclip.paste()
#Create a regex for removing unknowns and getting years
preString= re.sub(
"(18 Mar 1817 – 7 Oct)|(^\w+ \w+ \w+ – unknown)|(unknown – \w\w\w \w+)|(unknown – \w+ \w\w\w \w+)|(\w+ \w+ – unknown)|(unknown – \w \w+ \d\d\d\d)|((^\s\w\w\w\s[0-9][0-9][0-9][0-9]|([0-9][0-9][0-9][0-9]\s–)|(\s[0-9][0-9][0-9][0-9])$) – unknown)|unknown – \w+|(\w+ – unknown)|[1,3-9][0-5]\d\d+|(\d\d\d\d\d+)"
," ",text)

phoneRegex=re.compile(r'''
(
# get year from whole text #####
([0-9]+\s\w\w\w\s[0-9][0-9][0-9][0-9])|(\s[0-9][0-9][0-9][0-9])\s|([0-9][0-9][0-9][0-9]\s–)
)
''',re.VERBOSE)

#DONE: Extract the birth and death year from this text
text=preString
extractedPhone=phoneRegex.findall(text)
allPhoneNumbers= []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#DONE: Take extracted year number and put them all in a list
results = ' '.join(allPhoneNumbers)
##pyperclip.copy(results)
print(results)

yearRegex=re.compile(r'''
(
# Narrow the years#
([0-9][0-9][0-9][0-9])
)
''',re.VERBOSE)
extractedYear=yearRegex.findall(results)
allYear= []
for yearNumber in extractedYear:
    allYear.append(yearNumber[0])
yearResults=' '.join(allYear)
print(allYear)
print(len(allYear))
length=len(allYear)

#TODO: split two groups by death year
deathYear=input("What year do you want to split the age groups into: ")
halfLength=int(length/2)
#print(halfLength)
counter=0
preYear=[]
postYear=[]
skipYear=1
append=0
for counter in range (0,halfLength): 
    currentYear=(allYear[skipYear])
    #print(currentYear)
    counter=counter+1
    if int(currentYear) < int(deathYear):
        preYear.append(allYear[skipYear])
        preYear.append(int(allYear[skipYear-1]))
    if int(currentYear) >= int(deathYear):
        postYear.append(allYear[skipYear])
        postYear.append(int(allYear[skipYear-1]))
    skipYear=skipYear+2
print(postYear)
print(preYear)

#Subtract the Death by the Birth
counter=0
preAge=[]
postAge=[]
x=0
#Gets the ages of Pre and sets it to the list preAge
preYearLength=int(len(preYear)/2)
print(preYearLength)
for counter in range(0,preYearLength):
    #print("This is the counter "+str(x))
     preAge.append(int(preYear[x])-(int(preYear[x+1])))
     #print(preAge)
     x=x+2
x=0
#Gets the Ages of post and sets it to the list postAge
postYearLength=int(len(postYear)/2)
print(postYearLength)
for counter in range(0,postYearLength):
    #print("This is the counter "+str(x))
    postAge.append(int(postYear[x])-(int(postYear[x+1])))
    #print(postAge)
    x=x+2


#Results into a handy dandy string
preResults = ''.join(str(preAge))
preSampleSize=len(preAge)
postResults = ''.join(str(postAge))
postSampleSize=len(postAge)


#TODO: Split Each into age group and era
preDict={'0-4':0,'5-9':0,'10-14':0,'15-19':0,'20-24':0,'25-29':0,'30-34':0,'35-39':0,'40-44':0,'45-49':0,'50-54':0,'55-59':0,'60-64':0,'65-69':0,'70-74':0,'75-79':0,'80-84':0,'85-89':0,'90-94':0,'95-99':0,'100+':0}
postDict={'0-4':0,'5-9':0,'10-14':0,'15-19':0,'20-24':0,'25-29':0,'30-34':0,'35-39':0,'40-44':0,'45-49':0,'50-54':0,'55-59':0,'60-64':0,'65-69':0,'70-74':0,'75-79':0,'80-84':0,'85-89':0,'90-94':0,'95-99':0,'100+':0}
counter=0
for counter in range(0,preSampleSize):
    if int(preAge[counter])<=4:
        five=preDict.get('0-4')
        five=five+1
        preDict['0-4'] = five
    elif int(preAge[counter])<=9:
        nine=preDict.get('5-9')
        nine=nine+1
        preDict['5-9'] = nine
    elif int(preAge[counter])<=14:
        fourteen=preDict.get('10-14')
        fourteen=fourteen+1
        preDict['10-14'] = fourteen
    elif int(preAge[counter])<=19:
        nineteen=preDict.get('15-19')
        nineteen=nineteen+1
        preDict['15-19'] = nineteen
    elif int(preAge[counter])<=24:
        twentyfour=preDict.get('20-24')
        twentyfour=twentyfour+1
        preDict['20-24'] = twentyfour
    elif int(preAge[counter])<=29:
        twentynine=preDict.get('25-29')
        twentynine=twentynine+1
        preDict['25-29'] = twentynine
    elif int(preAge[counter])<=34:
        thirtyfour=preDict.get('30-34')
        thirtyfour=thirtyfour+1
        preDict['30-34'] = thirtyfour
    elif int(preAge[counter])<=39:
        thirtynine=preDict.get('35-39')
        thirtynine=thirtynine+1
        preDict['35-39'] = thirtynine
    elif int(preAge[counter])<=44:
        fourtyfour=preDict.get('40-44')
        fourtyfour=fourtyfour+1
        preDict['40-44'] = fourtyfour
    elif int(preAge[counter])<=49:
        fourtynine=preDict.get('45-49')
        fourtynine=fourtynine+1
        preDict['45-49'] = fourtynine
    elif int(preAge[counter])<=54:
        fiftyfour=preDict.get('50-54')
        fiftyfour=fiftyfour+1
        preDict['50-54'] = fiftyfour
    elif int(preAge[counter])<=59:
        fiftynine=preDict.get('55-59')
        fiftynine=fiftynine+1
        preDict['55-59'] = fiftynine
    elif int(preAge[counter])<=64:
        sixtyfour=preDict.get('60-64')
        sixtyfour=sixtyfour+1
        preDict['60-64'] = sixtyfour
    elif int(preAge[counter])<=69:
        sixtynine=preDict.get('65-69')
        sixtynine=sixtynine+1
        preDict['65-69'] = sixtynine
    elif int(preAge[counter])<=74:
        seventyfour=preDict.get('70-74')
        seventyfour=seventyfour+1
        preDict['70-74'] = seventyfour
    elif int(preAge[counter])<=79:
        seventynine=preDict.get('75-79')
        seventynine=seventynine+1
        preDict['75-79'] = seventynine
    elif int(preAge[counter])<=84:
        eightyfour=preDict.get('80-84')
        eightyfour=eightyfour+1
        preDict['80-84'] = eightyfour
    elif int(preAge[counter])<=89:
        eightynine=preDict.get('85-89')
        eightynine=eightynine+1
        preDict['85-89'] = eightynine
    elif int(preAge[counter])<=94:
        ninetyfour=preDict.get('90-94')
        ninetyfour=ninetyfour+1
        preDict['90-94'] = ninetyfour
    elif int(preAge[counter])<=99:
        ninetynine=preDict.get('95-99')
        ninetynine=ninetynine+1
        preDict['95-99'] = ninetynine
    elif int(preAge[counter])>=100:
        onehundred=preDict.get('100+')
        onehundred=onehundred+1
        preDict['100+'] = onehundred

##("Now POST X DATE")
for counter in range(0,postSampleSize):
    if int(postAge[counter])<=4:
        five=postDict.get('0-4')
        five=five+1
        postDict['0-4'] = five
    elif int(postAge[counter])<=9:
        nine=postDict.get('5-9')
        nine=nine+1
        postDict['5-9'] = nine
    elif int(postAge[counter])<=14:
        fourteen=postDict.get('10-14')
        fourteen=fourteen+1
        postDict['10-14'] = fourteen
    elif int(postAge[counter])<=19:
        nineteen=postDict.get('15-19')
        nineteen=nineteen+1
        postDict['15-19'] = nineteen
    elif int(postAge[counter])<=24:
        twentyfour=postDict.get('20-24')
        twentyfour=twentyfour+1
        postDict['20-24'] = twentyfour
    elif int(postAge[counter])<=29:
        twentynine=postDict.get('25-29')
        twentynine=twentynine+1
        postDict['25-29'] = twentynine
    elif int(postAge[counter])<=34:
        thirtyfour=postDict.get('30-34')
        thirtyfour=thirtyfour+1
        postDict['30-34'] = thirtyfour
    elif int(postAge[counter])<=39:
        thirtynine=postDict.get('35-39')
        thirtynine=thirtynine+1
        postDict['35-39'] = thirtynine
    elif int(postAge[counter])<=44:
        fourtyfour=postDict.get('40-44')
        fourtyfour=fourtyfour+1
        postDict['40-44'] = fourtyfour
    elif int(postAge[counter])<=49:
        fourtynine=postDict.get('45-49')
        fourtynine=fourtynine+1
        postDict['45-49'] = fourtynine
    elif int(postAge[counter])<=54:
        fiftyfour=postDict.get('50-54')
        fiftyfour=fiftyfour+1
        postDict['50-54'] = fiftyfour
    elif int(postAge[counter])<=59:
        fiftynine=postDict.get('55-59')
        fiftynine=fiftynine+1
        postDict['55-59'] = fiftynine
    elif int(postAge[counter])<=64:
        sixtyfour=postDict.get('60-64')
        sixtyfour=sixtyfour+1
        postDict['60-64'] = sixtyfour
    elif int(postAge[counter])<=69:
        sixtynine=postDict.get('65-69')
        sixtynine=sixtynine+1
        postDict['65-69'] = sixtynine
    elif int(postAge[counter])<=74:
        seventyfour=postDict.get('70-74')
        seventyfour=seventyfour+1
        postDict['70-74'] = seventyfour
    elif int(postAge[counter])<=79:
        seventynine=postDict.get('75-79')
        seventynine=seventynine+1
        postDict['75-79'] = seventynine
    elif int(postAge[counter])<=84:
        eightyfour=postDict.get('80-84')
        eightyfour=eightyfour+1
        postDict['80-84'] = eightyfour
    elif int(postAge[counter])<=89:
        eightynine=postDict.get('85-89')
        eightynine=eightynine+1
        postDict['85-89'] = eightynine
    elif int(postAge[counter])<=94:
        ninetyfour=postDict.get('90-94')
        ninetyfour=ninetyfour+1
        postDict['90-94'] = ninetyfour
    elif int(postAge[counter])<=99:
        ninetynine=postDict.get('95-99')
        ninetynine=ninetynine+1
        postDict['95-99'] = ninetynine
    elif int(postAge[counter])>=100:
        onehundred=postDict.get('100+')
        onehundred=onehundred+1
        postDict['100+'] = onehundred
print('This is the pre ' + str(deathYear)+" data, this has a sample size of "+ str(preSampleSize))
print(preDict)
print('This is the post ' + str(deathYear)+" data, this has a sample size of "+ str(postSampleSize))
print(postDict)
#TODO: Ask the user what list they would like to use
print("Press 0 if you want to have the pre-"+str(deathYear)+" on your clipboard, 1 for the post-"+str(deathYear)+" data" )
answer=input()
if int(answer)==0:
    pyperclip.copy(preFinal)
if int(answer)==1:
    pyperclip.copy(postFinal)






    
