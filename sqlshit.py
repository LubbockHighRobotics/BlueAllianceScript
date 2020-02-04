import mysql.connector
cnx = mysql.connector.connect( host=hostname, user=username, password=pass1, db=database )
cnxCursor = cnx.cursor()
def clear():
	sql="DELETE FROM `First` WHERE Zero = 0"
	cnxCursor.execute(sql)
	cnx.commit()
def insert(num, name):
	query = "INSERT INTO `First`(`Team Number`, `Team Names`) VALUES (%s, %s)"
	values = (num, name)
	cnxCursor.execute(query, values)
	cnx.commit()
fo = open("results.txt", "r")
file_txt = open("results.txt")
names = open("nicknames.txt", "r")
text = file_txt.read()
line =1
lines = ""
y =1
queryNum = 0
counter = 0
allLines = fo.readlines()
teamLines = names.readlines()
#print(allLines)
for i in text:
	if(i == "\n"):
		line += 1
lines = str(line)
teamArray = [0]*(line-1)
team2Array = [0]*(line-1)
nameArray = [0]*(line-1)
#print(teamArray)
#print("There are " + lines + " lines.")
while counter < line-1:
	nameArray[counter] = teamLines[counter]
	teamArray[counter] = int(allLines[counter])
	team2Array[counter]= int(allLines[counter])
	counter += 1
teamArray.sort()
#print(teamArray)
#print(nameArray)
clear() 
while queryNum < line-1:
	# print(teamArray)
	# print(nameArray)
	insert(num=teamArray[queryNum], name=nameArray[team2Array.index(teamArray[queryNum])])
	queryNum += 1
