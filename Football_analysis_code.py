import csv
import numpy as np

def result(team1, team2):
	
	file1=' '
	file2=' '

	
	if(team1=='1'):
		file1='ManUtd.csv'
	elif(team1=='2'):
		file1='ManCity.csv'
	elif(team1=='3'):
		file1='Chelsea.csv'
	elif(team1=='4'):
		file1='WestHam.csv'
	elif(team1=='5'):
		file1='Southampton.csv'
	elif(team1=='6'):
		file1='Everton.csv'
	elif(team1=='7'):
		file1='Leicester.csv'
	elif(team1=='8'):
		file1='Liverpool.csv'
	elif(team1=='9'):
		file1='Arsenal.csv'
	elif(team1=='10'):
		file1='Tottenham.csv'
	elif(team1=='11'):
		file1='Newcastle.csv'
	elif(team1=='12'):
		file1='Fulham.csv'
	elif(team1=='13'):
		file1='Wolves.csv'
	elif(team1=='14'):
		file1='Crystal.csv'
	elif(team1=='15'):
		file1='Watford.csv'
	elif(team1=='16'):
		file1='Burnley.csv'
	elif(team1=='17'):
		file1='Bournemouth.csv'
	elif(team1=='18'):
		file1='Brighton.csv'
	elif(team1=='19'):
		file1='Huddersfield.csv'
	elif(team1=='20'):
		file1='Cardiff.csv'

	

	if(team2=='1'):
		file2='ManUtd.csv'
	elif(team2=='2'):
		file2='ManCity.csv'
	elif(team2=='3'):
		file2='Chelsea.csv'
	elif(team2=='4'):
		file2='WestHam.csv'
	elif(team2=='5'):
		file2='Southampton.csv'
	elif(team2=='6'):
		file2='Everton.csv'
	elif(team2=='7'):
		file2='Leicester.csv'
	elif(team2=='8'):
		file2='Liverpool.csv'
	elif(team2=='9'):
		file2='Arsenal.csv'
	elif(team2=='10'):
		file2='Tottenham.csv'
	elif(team2=='11'):
		file2='Newcastle.csv'
	elif(team2=='12'):
		file2='Fulham.csv'
	elif(team2=='13'):
		file2='Wolves.csv'
	elif(team2=='14'):
		file2='Crystal.csv'
	elif(team2=='15'):
		file2='Watford.csv'
	elif(team2=='16'):
		file2='Burnley.csv'
	elif(team2=='17'):
		file2='Bournemouth.csv'
	elif(team2=='18'):
		file2='Brighton.csv'
	elif(team2=='19'):
		file2='Huddersfield.csv'
	elif(team2=='20'):
		file2='Cardiff.csv'

if (file1==file2):
	print("Error! you chose same team!")
	break

	first = 0
	all_data1 = []

	with open(file1, 'rU') as csvfile:
		spamreader1 = csv.reader(csvfile, delimiter= ',', quotechar='|')
		for row1 in spamreader1:

			if(first == 0):
				first = 1
				continue
			else:
				all_data1.append(row1)

	finalForm1=0
	for i in range(len(all_data1)):
		form1=0
		for j in range(5):
			parameter1=all_data1[i][j+1]
			form1 = int(form1) + int(parameter1)
		form1_per_match= form1/5.0
		finalForm1= float(finalForm1) + float(form1_per_match)

	#print(finalForm1/len(all_data1))	


	second = 0
	all_data2 = []

	with open(file2, 'rU') as csvfile:
		spamreader2 = csv.reader(csvfile, delimiter= ',', quotechar='|')
		for row2 in spamreader2:

			if(second == 0):
				second = 1
				continue
			else:
				all_data2.append(row2)

	finalForm2=0
	for i in range(len(all_data2)):
		form2=0
		for j in range(5):
			parameter2=all_data2[i][j+1]
			form2 = int(form2) + int(parameter2)
		form2_per_match= form2/5.0
		finalForm2= float(finalForm2) + float(form2_per_match)

	#print(finalForm2/len(all_data2))

  
	if (int(finalForm1)==int(finalForm2)):
		return "Draw"

	elif (finalForm1>finalForm2):
		return all_data1[0][0]

	elif (finalForm1<finalForm2):
		return all_data2[0][0]



def main():
	print("1. Manchester United 2. Manchester City 3. Chelsea 4. West Ham 5. Southampton") 
	print("6. Everton 7. Leicester 8. Liverpool 9. Arsenal 10. Tottenham 11. Newcastle ")
	print("12. Fulham 13. Wolves 14. Crystal Palace 15. Watford 16. Burnley 17. Bournemouth")
	print("18. Brighton 19. Huddersfield 20. Cardiff")
	
	ch='Y'
	while ch=='Y' or ch=='y':
		
		team1= input("Enter team1 index from list")
		team2= input("Enter team2 index from list")

		output= result(team1, team2)

		print(output)
		ch=input("Do you want to continue: Y/N?")




if __name__ == "__main__":
    main()