hostname = 'mysql.lhsrobotics.net'
username = 'lhsrobo'
pass1 = 'DomSkyBlack4717'
database = 'lhs_scoutdb'

import mysql.connector
cnx = mysql.connector.connect( host=hostname, user=username, password=pass1, db=database )
cnxCursor = cnx.cursor()
def clear():
	sql="DELETE FROM `Schedule` WHERE Zero = 0"
	cnxCursor.execute(sql)
	cnx.commit()
def insert(matchNum, red1, red2, red3, blue1, blue2, blue3):
	query = "INSERT INTO `Schedule`(`Match Number`, `Red 1`, `Red 2`, `Red 3`, `Blue 1`, `Blue 2`, `Blue 3`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
	values = (matchNum, red1, red2, red3, blue1, blue2, blue3)
	cnxCursor.execute(query, values)
	cnx.commit()
fo = open("redteams.txt", "r")
fo2 = open("blueteams.txt", "r")
fo3 = open("matchnumbers.txt", "r")
readteams = open("redteams.txt")
blueteams = open("blueteams.txt", "r")
redtext = readteams.read()
bluetext = blueteams.read()
line =1
lines = ""
y =1
queryNum = 0
counter = 0
redlines = fo.readlines()
bluelines = fo2.readlines()
matchNumsString = fo3.readlines()
# print(matchNumsString)
matchNums = [0]*len(matchNumsString)
def clear():
	sql="DELETE FROM `Schedule` WHERE `Match Number` > 0"
	cnxCursor.execute(sql)
	cnx.commit()
while(counter<len(matchNumsString)):
    # print(matchNumsString[counter][:-1])
    matchNums[counter] = int(matchNumsString[counter][:-1])
    counter = counter + 1
counter = 0
while(counter<len(redlines)):
    redlines[counter] = redlines[counter][4:-2]
    counter = counter + 1
counter = 0
while (counter < len(bluelines)):
    bluelines[counter] = bluelines[counter][4:-2]
    counter = counter + 1
counter = 0
numOfMatches = len(bluelines)/3
clear()
# print(numOfMatches)
while(counter<numOfMatches):
    insert(counter + 1,redlines[matchNums.index(counter+1)*3],redlines[matchNums.index(counter+1)*3+1],redlines[matchNums.index(counter+1)*3+2],bluelines[matchNums.index(counter+1)*3],bluelines[matchNums.index(counter+1)*3+1],bluelines[matchNums.index(counter+1)*3+2])
    # print(counter)
    # print(counter+1, redlines[counter*3],redlines[(counter*3)+1],redlines[(counter*3)+2])#,bluelines[counter*3],bluelines[(counter*3)+1],bluelines[(counter*3)+2])
    counter = counter + 1
# print(matchNums)
# insert(12,11,12,13,14,15,16)
