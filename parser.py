

#with ('./RCdata/rating_final.csv') as f:


import csv
import pprint

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
	restaurant = [['placeID', 'cash','VISA','MasterCard-Eurocard','American_Express','bank_debit_cards','checks','Discover','Carte_Blanche','Diners_Club','Visa','Japan_Credit_Bureau','gift_certificates']]

	# A list of list of the following format: [[placeID, payment_method], ...]
	payment_method = []

	with open('./RCdata/chefmozaccepts.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		next(csvfile)

		for row in spamreader:
			payment_method.append(row)

	restaurant_data = {}

	for i in payment_method:
		if i[0] not in restaurant_data:
			restaurant_data[i[0]] = {'payment_methods' : [], 'cuisine_type' : [], 'hours' : {}, 'parking' : [], 'location' : {}}
		restaurant_data[i[0]]['payment_methods'].append(i[1])

	# A list of list of the following format: [[placeID, cuisine], ...]
	cuisine = []

	with open('./RCdata/chefmozcuisine.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		next(csvfile)

		for row in spamreader:
			cuisine.append(row)

	for i in cuisine:
		if i[0] not in restaurant_data:
			restaurant_data[i[0]] = {'payment_methods' : [], 'cuisine_type' : [], 'hours' : {}, 'parking' : [], 'location' : {}}
		restaurant_data[i[0]]['cuisine_type'].append(i[1])


	# A list of list of the following format: [[placeID, hours, days], ...]
	# NEED TO FORMAT THIS MORE BECAUSE OF WEIRD ; FORMATING
	hours = []

	with open('./RCdata/chefmozhours4.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		next(csvfile)

		for row in spamreader:
			hours.append(row)

	days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	for i in hours:
		if i[0] not in restaurant_data:
			restaurant_data[i[0]] = {'payment_methods' : [], 'cuisine_type' : [], 'hours' : {}, 'parking' : [], 'location' : {}}

		for day in days:
			if day in i[2]:
				if day not in restaurant_data[i[0]]['hours']:
					restaurant_data[i[0]]['hours'][day] = []
				temp = i[1].split(';')
				for j in temp:
					if j != '':
						restaurant_data[i[0]]['hours'][day].append(j)

		#restaurant_data[i[0]]['hours'].append([i[1], i[2]])
	

	# A list of list of the following format: [[placeID, parking_lot], ...]
	parking = []

	with open('./RCdata/chefmozparking.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		next(csvfile)

		for row in spamreader:
			parking.append(row)

	for i in parking:
		if i[0] not in restaurant_data:
			restaurant_data[i[0]] = {'payment_methods' : [], 'cuisine_type' : [], 'hours' : {}, 'parking' : [], 'location' : {}}
		restaurant_data[i[0]]['parking'].append(i[1])

	# NEED TO DO SPECIAL STUFF FOR THIS ONE TOO
	# A list of list of the following format: [[placeID, parking_lot], ...]
	location = []

	with open('./RCdata/geoplaces2.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		next(csvfile)

		for row in spamreader:
			location.append(row)

	for i in location:
		if i[0] not in restaurant_data:
			restaurant_data[i[0]] = {'payment_methods' : [], 'cuisine_type' : [], 'hours' : {}, 'parking' : [], 'location' : {}}
		restaurant_data[i[0]]['location']['latitude'] = i[1]
		restaurant_data[i[0]]['location']['longitude'] = i[2]
		restaurant_data[i[0]]['location']['the_geom_meter'] = i[3]
		restaurant_data[i[0]]['location']['name'] = i[4]
		restaurant_data[i[0]]['location']['address'] = i[5]
		restaurant_data[i[0]]['location']['city'] = i[6]
		restaurant_data[i[0]]['location']['state'] = i[7]
		restaurant_data[i[0]]['location']['country'] = i[8]
		restaurant_data[i[0]]['location']['fax'] = i[9]
		restaurant_data[i[0]]['location']['zip'] = i[10]
		restaurant_data[i[0]]['location']['alcohol'] = i[11]
		restaurant_data[i[0]]['location']['smoking_area'] = i[12]
		restaurant_data[i[0]]['location']['dress_code'] = i[13]
		restaurant_data[i[0]]['location']['accessibility'] = i[14]
		restaurant_data[i[0]]['location']['price'] = i[15]
		restaurant_data[i[0]]['location']['url'] = i[16]
		restaurant_data[i[0]]['location']['Rambience'] = i[17]
		restaurant_data[i[0]]['location']['franchise'] = i[18]
		restaurant_data[i[0]]['location']['area'] = i[19]
		restaurant_data[i[0]]['location']['other_services'] = i[20]

	return restaurant_data


#print(item())
#item()
k = item()
pp = pprint.PrettyPrinter(indent=4)

print(len(k))
pp.pprint(item())









































