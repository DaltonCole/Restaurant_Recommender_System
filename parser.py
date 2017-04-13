

#with ('./RCdata/rating_final.csv') as f:


import csv

def rating():
	with open('./RCdata/rating_final.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		next(csvfile)

		with open('./Parsed/rating.csv', 'w', newline='') as f:
			spamwriter = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

			for row in spamreader:
				spamwriter.writerow([row[0], row[1], row[2]])

def food_rating():
	with open('./RCdata/rating_final.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		next(csvfile)

		with open('./Parsed/food_rating.csv', 'w', newline='') as f:
			spamwriter = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

			for row in spamreader:
				spamwriter.writerow([row[0], row[1], row[3]])

def service_rating():
	with open('./RCdata/rating_final.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		next(csvfile)

		with open('./Parsed/service_rating.csv', 'w', newline='') as f:
			spamwriter = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

			for row in spamreader:
				spamwriter.writerow([row[0], row[1], row[4]])

rating()
food_rating()
service_rating()