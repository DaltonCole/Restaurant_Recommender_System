

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

#rating()
#food_rating()
#service_rating()

def user():
	# A list of list of the following format: [[userID, cuisine], ...]
	cuisine = []

	with open('./RCdata/usercuisine.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')

		for row in spamreader:
			cuisine.append(row)

	# A list of list of the following format: [[userID, payment_method], ...]
	payment_method = []

	with open('./RCdata/userpayment.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')

		for row in spamreader:
			payment_method.append(row)

	# userID,latitude,longitude,smoker,drink_level,dress_preference,ambience,transport,marital_status,hijos,birth_year,interest,personality,religion,activity,color,weight,budget,height
	# NEED TO DO MORE WITH DATA
	# A list of list of the following format: [[userID, ...], ...]
	profile = []

	with open('./RCdata/userprofile.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')

		for row in spamreader:
			profile.append(row)

	return [cuisine, payment_method, profile]


def item():
	# A list of list of the following format: [[placeID, payment_method], ...]
	payment_method = []

	with open('./RCdata/chefmozaccepts.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')

		for row in spamreader:
			payment_method.append(row)

	# A list of list of the following format: [[placeID, cuisine], ...]
	cuisine = []

	with open('./RCdata/chefmozcuisine.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')

		for row in spamreader:
			cuisine.append(row)

	# A list of list of the following format: [[placeID, hours, days], ...]
	# NEED TO FORMAT THIS MORE BECAUSE OF WEIRD ; FORMATING
	hours = []

	with open('./RCdata/chefmozhours4.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')

		for row in spamreader:
			hours.append(row)

	# A list of list of the following format: [[placeID, parking_lot], ...]
	parking = []

	with open('./RCdata/chefmozparking.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')

		for row in spamreader:
			parking.append(row)

	# placeID,latitude,longitude,the_geom_meter,name,address,city,state,country,fax,zip,alcohol,smoking_area,dress_code,accessibility,price,url,Rambience,franchise,area,other_services
	# NEED TO DO SPECIAL STUFF FOR THIS ONE TOO
	# A list of list of the following format: [[placeID, parking_lot], ...]
	location = []

	with open('./RCdata/geoplaces2.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')

		for row in spamreader:
			location.append(row)

	return [payment_method, cuisine, hours, parking, location]

print(item())










































