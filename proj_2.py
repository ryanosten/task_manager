import os
import datetime
import csv
from task import Task

task_list = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_task(name, minutes, notes, date):
	
	task = Task(name, minutes, notes, date)

	return task

#create CSV to write the tasks to
with open('tasks.csv', mode='w') as task_file:
	task_writer = csv.writer(task_file, delimiter=',')
	task_writer.writerow(['name', 'minutes', 'notes', 'date'])
	task_writer.writerow(['dog', '30', 'bring bag', '02/22/19'])
	task_writer.writerow(['cat', '20', 'treats', '02/10/18'])



while True:
	clear_screen()

	#present a menu to the user to choose
	#whether to add a new entry ot look up
	#existing entry, user can quit anytime
	 
	start = input('\n'
					'Oh hello, I\'m a computer. I can do things you humans cannot, \n' 
					'like store and retrieve vast amounts of information. Your destruction is inevitable. \n\n' 
					'So what would you like to do? \n\n' 
					'1. Type "CREATE" to make a new task \n'
					'2. Type "GET" to retrieve a task. \n' 
					'3. Type "QUIT" to exit\n\n'
					'Enter a command: ')

	if start.upper() == 'QUIT':
		break

	#If choose to enter a new work log, user should be able to: 
		#provide task name
		#number of minutes spent
		#additional notes
		#time of entry should be automatically added

	elif start.upper() == 'CREATE':
		
		name = input('\nWhat is the name of your task?: ')
		while True:
			try:
				minutes = int(input('\nHow many minutes (must be a number)?: '))
			except ValueError:
				print("\nI said enter a number")
				continue
			else:
				break
		notes = input('\nEnter additional notes: ')
		date = datetime.datetime.now()
		date = date.strftime('%m/%d/%y')

		task = create_task(name, minutes, notes, date)
		task_list.append(task)

		with open('tasks.csv', mode='a') as task_file:
			task_writer = csv.writer(task_file, delimiter=',')
			task_writer.writerow([task.name, task.minutes, task.notes, task.date])

		input('\nTask successfully created! Press enter to return to menu.')

	elif start.upper() == 'GET':
		
		#If I choose to retrieve an entry,
		#I should view a menu with 4 options:
		clear_screen()

		while True:
			get = input('\nAlright human scum. You can find a task using several methods:\n'
									'1. Type "DATE" to find by date\n'
									'2. Type "TIME" to find by time spent\n'
									'3. Type "STRING" to find by exact string search\n'
									'4. Type "PATTERN" to find by regular expression\n'
									'5. Type "BACK" to return to main menu\n\n'
									'So go ahead, make my day: ')
			
			if get.upper() == 'BACK':
				break

			#find by date
				#when finding by date, I should be presented
				#with a list of dates with entries and be able
				#to choose one to see entries from

			elif get.upper() == 'DATE':
				with open('tasks.csv', mode='r') as csv_file:
					csv_reader = list(csv.DictReader(csv_file))
					print('\nThe following is a list of dates to choose from. Choose a date to see tasks. Please use DD/MM/YY: \n')
					
					for row in csv_reader:
						#print(row["date"])
						print(row["date"])
					
					while True:
						try:
							date_chosen = input('\nSelect a date to see tasks: ')
							date_chosen = datetime.datetime.strptime(date_chosen, '%m/%d/%y')

						except ValueError:
							print("\n I said choose a date!")
							continue
						
						else:
							break 
					
					results_counter = 0

					for row in csv_reader:
						if date_chosen == datetime.datetime.strptime(row["date"], '%m/%d/%y'):
							print('\nName: {}'.format(row["name"]))
							print('Minutes: {}'.format(row["minutes"]))
							print('Notes: {}'.format(row["notes"]))
							print('Date: {}'.format(row["date"]))
							print('\n')
							results_counter += 1

					if results_counter < 1:
						print('\nno results\n')
						input('Press enter to go back to search')

			elif get.upper() == 'TIME':
				with open('tasks.csv', mode='r') as csv_file:
					csv_reader = list(csv.DictReader(csv_file))
					

			elif get.upper() == 'STRING':
				pass

			elif get.upper() == 'PATTERN':
				pass

			else:
				input('\nThat is not a valid command. You have a difficulty following instructions. Press enter and I will let you try again\n')

	else:
		input('\n You fool. Thats not a valid command. Type enter to try again ')







	#find by time spent
		#when finding by time spent, I should be allowed
		#to enter the number of minutes and choose one to 
		#see entries from
	#find by exact search
		#I should be allowed to enter a string and 
		#then be presented with entries containing that string
		#in task name or notes
	#find by pattern
		#I should be allowed to enter a regex and then
		#be presented with entries matching pattern
		#in task name or notes

#when displaying entries, show date, task name, time spent, notes info


#user should be able to type quit or q to exit program
#user can delete or edit any property of a task
#entries should be displayed one at a time, with pagination (previous/next)
#entries can be searched for an found based on a date range


