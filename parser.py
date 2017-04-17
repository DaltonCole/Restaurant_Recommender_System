import csv
import pprint

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import f1_score
from sklearn.feature_selection import VarianceThreshold
from sklearn import preprocessing
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt
from random import sample # Random integer
import os
import sys

flatten = lambda l: [item for sublist in l for item in sublist]

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
	user_data = {}

	# A list of list of the following format: [[userID, cuisine], ...]
	cuisine = []

	with open('./RCdata/usercuisine.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		next(csvfile)

		for row in spamreader:
			cuisine.append(row)

	for i in cuisine:
		if i[0] not in user_data:
			user_data[i[0]] = {'cuisine' : [], 'payment_method' : [], 'profile' : {}}
		user_data[i[0]]['cuisine'].append(i[1])

	# A list of list of the following format: [[userID, payment_method], ...]
	payment_method = []

	with open('./RCdata/userpayment.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		next(csvfile)

		for row in spamreader:
			payment_method.append(row)

	for i in payment_method:
		if i[0] not in user_data:
			user_data[i[0]] = {'cuisine' : [], 'payment_method' : [], 'profile' : {}}
		user_data[i[0]]['payment_method'].append(i[1])

	#,,,,,,,,,,,,,,,,,
	# NEED TO DO MORE WITH DATA
	# A list of list of the following format: [[userID, ...], ...]
	profile = []

	with open('./RCdata/userprofile.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		next(csvfile)

		for row in spamreader:
			profile.append(row)

	for i in profile:
		if i[0] not in user_data:
			user_data[i[0]] = {'cuisine' : [], 'payment_method' : [], 'profile' : {}}
		user_data[i[0]]['profile']['latitude'] = i[1]
		user_data[i[0]]['profile']['longitude'] = i[2]
		user_data[i[0]]['profile']['the_geom_meter'] = i[3]
		user_data[i[0]]['profile']['smoker'] = i[4]
		user_data[i[0]]['profile']['drink_level'] = i[5]
		user_data[i[0]]['profile']['dress_preference'] = i[6]
		user_data[i[0]]['profile']['ambience'] = i[7]
		user_data[i[0]]['profile']['transport'] = i[8]
		user_data[i[0]]['profile']['marital_status'] = i[9]
		user_data[i[0]]['profile']['hijos'] = i[10]
		user_data[i[0]]['profile']['birth_year'] = i[11]
		user_data[i[0]]['profile']['interest'] = i[12]
		user_data[i[0]]['profile']['personality'] = i[13]
		user_data[i[0]]['profile']['activity'] = i[14]
		user_data[i[0]]['profile']['color'] = i[15]
		user_data[i[0]]['profile']['weight'] = i[16]
		user_data[i[0]]['profile']['budget'] = i[17]
		user_data[i[0]]['profile']['height'] = i[18]

	return user_data


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
			if(row not in hours):
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

def user_dect_to_matrix(user_dict):
	# Create a header for the matrix
	cuisine_header = ['Afghan', 'African', 'American', 'Armenian', 'Asian', 'Australian', 'Austrian', 'Bagels', 'Bakery', 'Bar', 'Bar_Pub_Brewery', 'Barbecue', 'Basque', 'Brazilian', 'Breakfast-Brunch', 'British', 'Burgers', 'Burmese', 'Cafe-Coffee_Shop', 'Cafeteria', 'Cajun-Creole', 'California', 'Cambodian', 'Canadian', 'Caribbean', 'Chilean', 'Chinese', 'Contemporary', 'Continental-European', 'Cuban', 'Deli-Sandwiches', 'Dessert-Ice_Cream', 'Dim_Sum', 'Diner', 'Doughnuts', 'Dutch-Belgian', 'Eastern_European', 'Eclectic', 'Ethiopian', 'Family', 'Fast_Food', 'Filipino', 'Fine_Dining', 'French', 'Fusion', 'Game', 'German', 'Greek', 'Hawaiian', 'Hot_Dogs', 'Hungarian', 'Indian-Pakistani', 'Indigenous', 'Indonesian', 'International', 'Irish', 'Israeli', 'Italian', 'Jamaican', 'Japanese', 'Juice', 'Korean', 'Kosher', 'Latin_American', 'Lebanese', 'Malaysian', 'Mediterranean', 'Mexican', 'Middle_Eastern', 'Mongolian', 'Moroccan', 'North_African', 'Organic-Healthy', 'Pacific_Northwest', 'Pacific_Rim', 'Persian', 'Peruvian', 'Pizzeria', 'Polish', 'Polynesian', 'Portuguese', 'Regional', 'Romanian', 'Russian-Ukrainian', 'Scandinavian', 'Seafood', 'Soup', 'Southeast_Asian', 'Southern', 'Southwestern', 'Spanish', 'Steaks', 'Sushi', 'Swiss', 'Tapas', 'Tea_House', 'Tex-Mex', 'Thai', 'Tibetan', 'Tunisian', 'Turkish', 'Vegetarian', 'Vietnamese']
	payment_header = ['cash', 'bank_debit_cards', 'MasterCard-Eurocard', 'VISA', 'American_Express']
	user_profile_header = ['latitude', 'longitude', 'the_geom_meter', 'smoker', 'drink_level', 'dress_preference', 'ambience', 'transport', 'marital_status', 'hijos', 'birth_year', 'interest', 'personality', 'religion', 'activity', 'color', 'weight', 'budget', 'height']

	header = ['userID'] + cuisine_header + payment_header + user_profile_header

	# Make it so each value represents a different index in the matrix
	name_to_position = {}

	for i, counter in zip(header, range(0, len(header))):
		name_to_position[i] = counter

	# Fill matrix
	user_matrix = []
	user_matrix.append(header)

	for user, values in user_dict.items():
		row = [0] * len(header)

		# Set user ID
		row[0] = user

		# Set cuisine
		for i in values['cuisine']:
			row[name_to_position[i]] += 1

		# Set payment method
		for i in values['payment_method']:
			row[name_to_position[i]] += 1

		# Set profile
		for i, j in values['profile'].items():
			row[name_to_position[i]] = j

		# Append row to user matrix
		user_matrix.append(row)

	return user_matrix

def user_dect_to_user_list(user_dict):
	# Create a header for the matrix
	cuisine_header = ['Afghan', 'African', 'American', 'Armenian', 'Asian', 'Australian', 'Austrian', 'Bagels', 'Bakery', 'Bar', 'Bar_Pub_Brewery', 'Barbecue', 'Basque', 'Brazilian', 'Breakfast-Brunch', 'British', 'Burgers', 'Burmese', 'Cafe-Coffee_Shop', 'Cafeteria', 'Cajun-Creole', 'California', 'Cambodian', 'Canadian', 'Caribbean', 'Chilean', 'Chinese', 'Contemporary', 'Continental-European', 'Cuban', 'Deli-Sandwiches', 'Dessert-Ice_Cream', 'Dim_Sum', 'Diner', 'Doughnuts', 'Dutch-Belgian', 'Eastern_European', 'Eclectic', 'Ethiopian', 'Family', 'Fast_Food', 'Filipino', 'Fine_Dining', 'French', 'Fusion', 'Game', 'German', 'Greek', 'Hawaiian', 'Hot_Dogs', 'Hungarian', 'Indian-Pakistani', 'Indigenous', 'Indonesian', 'International', 'Irish', 'Israeli', 'Italian', 'Jamaican', 'Japanese', 'Juice', 'Korean', 'Kosher', 'Latin_American', 'Lebanese', 'Malaysian', 'Mediterranean', 'Mexican', 'Middle_Eastern', 'Mongolian', 'Moroccan', 'North_African', 'Organic-Healthy', 'Pacific_Northwest', 'Pacific_Rim', 'Persian', 'Peruvian', 'Pizzeria', 'Polish', 'Polynesian', 'Portuguese', 'Regional', 'Romanian', 'Russian-Ukrainian', 'Scandinavian', 'Seafood', 'Soup', 'Southeast_Asian', 'Southern', 'Southwestern', 'Spanish', 'Steaks', 'Sushi', 'Swiss', 'Tapas', 'Tea_House', 'Tex-Mex', 'Thai', 'Tibetan', 'Tunisian', 'Turkish', 'Vegetarian', 'Vietnamese']
	payment_header = ['cash', 'bank_debit_cards', 'MasterCard-Eurocard', 'VISA', 'American_Express']
	user_profile_header = ['latitude', 'longitude', 'the_geom_meter', 'smoker', 'drink_level', 'dress_preference', 'ambience', 'transport', 'marital_status', 'hijos', 'birth_year', 'interest', 'personality', 'religion', 'activity', 'color', 'weight', 'budget', 'height']

	header = cuisine_header + payment_header + user_profile_header

	# Make it so each value represents a different index in the matrix
	name_to_position = {}

	for i, counter in zip(header, range(0, len(header))):
		name_to_position[i] = counter

	# Fill matrix
	user_matrix = {}
	user_matrix['header'] = header

	for user, values in user_dict.items():
		row = [0] * len(header)

		# Set cuisine
		for i in values['cuisine']:
			row[name_to_position[i]] += 1

		# Set payment method
		for i in values['payment_method']:
			row[name_to_position[i]] += 1

		# Set profile
		for i, j in values['profile'].items():
			row[name_to_position[i]] = j

		# Append row to user matrix
		le = preprocessing.LabelEncoder()
		le.fit(row)

		user_matrix[user] = le.transform(row)

	return user_matrix

def item_dect_to_matrix(item_dict):
	# Create a header for the matrix
	cuisine_header = ['Afghan', 'African', 'American', 'Armenian', 'Asian', 'Bagels', 'Bakery', 'Bar', 'Bar_Pub_Brewery', 'Barbecue', 'Brazilian', 'Breakfast-Brunch', 'Burgers', 'Cafe-Coffee_Shop', 'Cafeteria', 'California', 'Caribbean', 'Chinese', 'Contemporary', 'Continental-European', 'Deli-Sandwiches', 'Dessert-Ice_Cream', 'Diner', 'Dutch-Belgian', 'Eastern_European', 'Ethiopian', 'Family', 'Fast_Food', 'Fine_Dining', 'French', '', 'Game', 'German', 'Greek', 'Hot_Dogs', 'International', 'Italian', 'Japanese', 'Juice', 'Korean', 'Latin_American', 'Mediterranean', 'Mexican', 'Mongolian', 'Organic-Healthy', 'Persian', 'Pizzeria', 'Polish', 'Regional', 'Seafood', 'Soup', 'Southern', 'Southwestern', 'Spanish', 'Steaks', 'Sushi', 'Thai', 'Turkish', 'Vegetarian', 'Vietnamese']
	hours_header = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	parking_header = ['public', 'none', 'yes', 'valet parking', 'fee', 'street', 'validated parking'] # Note, fee probably means free
	geoplaces_header = ['latitude', 'longitude', 'the_geom_meter', 'name', 'address', 'city', 'state', 'country', 'fax', 'zip', 'alcohol', 'smoking_area', 'dress_code', 'accessibility', 'price', 'url', 'Rambience', 'franchise', 'area', 'other_services']
	payment_header = ['cash', 'VISA', 'MasterCard-Eurocard', 'American_Express', 'bank_debit_cards', 'checks', 'Discover', 'Carte_Blanche', 'Diners_Club', 'Visa', 'Japan_Credit_Bureau', 'gift_certificates']

	header = ['userID'] + cuisine_header + hours_header + parking_header + geoplaces_header + payment_header

	# Make it so each value represents a different index in the matrix
	name_to_position = {}

	for i, counter in zip(header, range(0, len(header))):
		name_to_position[i] = counter

	# Fill matrix
	item_matrix = []
	item_matrix.append(header)

	for item, values in item_dict.items():
		row = [0] * len(header)

		# Set item ID
		row[0] = item

		# Set cuisine
		for i in values['cuisine_type']:
			row[name_to_position[i]] += 1

		# Set payment method
		for i in values['payment_methods']:
			row[name_to_position[i]] += 1

		# Set parking method
		for i in values['parking']:
			row[name_to_position[i]] += 1

		# Hours
		for day, hours in values['hours'].items():
			row[name_to_position[day]] = hours # SHOULD DO SOMETHING WITH THIS

		# Set location data
		for i, j in values['location'].items():
			if j != '?':
				row[name_to_position[i]] = j

		# Append row to item matrix
		item_matrix.append(row)

	return item_matrix

def item_dect_to_item_list(item_dict):
	# Create a header for the matrix
	cuisine_header = ['Afghan', 'African', 'American', 'Armenian', 'Asian', 'Bagels', 'Bakery', 'Bar', 'Bar_Pub_Brewery', 'Barbecue', 'Brazilian', 'Breakfast-Brunch', 'Burgers', 'Cafe-Coffee_Shop', 'Cafeteria', 'California', 'Caribbean', 'Chinese', 'Contemporary', 'Continental-European', 'Deli-Sandwiches', 'Dessert-Ice_Cream', 'Diner', 'Dutch-Belgian', 'Eastern_European', 'Ethiopian', 'Family', 'Fast_Food', 'Fine_Dining', 'French', '', 'Game', 'German', 'Greek', 'Hot_Dogs', 'International', 'Italian', 'Japanese', 'Juice', 'Korean', 'Latin_American', 'Mediterranean', 'Mexican', 'Mongolian', 'Organic-Healthy', 'Persian', 'Pizzeria', 'Polish', 'Regional', 'Seafood', 'Soup', 'Southern', 'Southwestern', 'Spanish', 'Steaks', 'Sushi', 'Thai', 'Turkish', 'Vegetarian', 'Vietnamese']
	hours_header = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	parking_header = ['public', 'none', 'yes', 'valet parking', 'fee', 'street', 'validated parking'] # Note, fee probably means free
	geoplaces_header = ['latitude', 'longitude', 'the_geom_meter', 'name', 'address', 'city', 'state', 'country', 'fax', 'zip', 'alcohol', 'smoking_area', 'dress_code', 'accessibility', 'price', 'url', 'Rambience', 'franchise', 'area', 'other_services']
	payment_header = ['cash', 'VISA', 'MasterCard-Eurocard', 'American_Express', 'bank_debit_cards', 'checks', 'Discover', 'Carte_Blanche', 'Diners_Club', 'Visa', 'Japan_Credit_Bureau', 'gift_certificates']

	header = cuisine_header + hours_header + parking_header + geoplaces_header + payment_header

	# Make it so each value represents a different index in the matrix
	name_to_position = {}

	for i, counter in zip(header, range(0, len(header))):
		name_to_position[i] = counter

	# Fill matrix
	item_matrix = {}
	item_matrix['header'] = header

	for item, values in item_dict.items():
		row = [0] * len(header)

		# Set item ID
		row[0] = item

		# Set cuisine
		for i in values['cuisine_type']:
			row[name_to_position[i]] = int(row[name_to_position[i]]) + 1

		# Set payment method
		for i in values['payment_methods']:
			row[name_to_position[i]] += 1

		# Set parking method
		for i in values['parking']:
			row[name_to_position[i]] += 1

		# Hours
		for day, hours in values['hours'].items():
			row[name_to_position[day]] = ''.join(hours) # SHOULD DO SOMETHING WITH THIS

		# Set location data
		for i, j in values['location'].items():
			if j != '?':
				row[name_to_position[i]] = j

		# Append row to item matrix
		le = preprocessing.LabelEncoder()
		le.fit(row)

		item_matrix[item] = le.transform(row)

	return item_matrix

# returns pair of user_ratings and restaurant_ratings dict
def rating_dict():
	user_ratings = {}
	restaurant_ratings = {}

	with open('./RCdata/rating_final.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		next(csvfile)

		for row in spamreader:
			if row[0] not in user_ratings:
				user_ratings[row[0]] = []
			user_ratings[row[0]].append((row[1], row[2], row[3], row[4]))

			if row[1] not in restaurant_ratings:
				restaurant_ratings[row[1]] = []
			restaurant_ratings[row[1]].append((row[0], row[2], row[3], row[4]))

	return user_ratings, restaurant_ratings


def ratings_dict_to_matrix(user_dict, rest_dict):
	header = ['userID', 'placeID', 'rating', 'food_rating', 'service_rating']

	user_matrix = [header]

	for i, j in header.items():
		pass

	return

def restaurant_1_to_n_user(user_dict, rest_dict, rest_ratings_dict, classifier):
	# Dictionary of user features {userID: features}
	user_feaure_dict = user_dect_to_user_list(user_dict)

	# Average of how often the classifier was right
	average_correct_ratings = []
	average_correct_food_ratings = []
	average_correct_service_ratings = []

	# For each restaurant, seperate restID and user features
	for restaurant, rating in rest_ratings_dict.items():
		# Matrix of features
		rest_matrix = []
		# List of ratings
		ratings_list = []
		food_ratings_list = []
		service_ratings_list = []

		# For each user. User is in tuple format (userID, rating, food_rating, service_rating)
		for user in rating:
			rest_matrix.append(user_feaure_dict[user[0]])
			ratings_list.append(user[1])
			food_ratings_list.append(user[2])
			service_ratings_list.append(user[3])

		# Rows in matrix
		m_length = len(rest_matrix)

		# Perform decision tree classiciation for ratings
		for i in range(m_length):
			try:
				clf = classifier.fit((rest_matrix[0:i] + rest_matrix[i+1:m_length]), ((ratings_list[0:i] + ratings_list[i+1:m_length])))

				ratings_prediction = clf.predict([rest_matrix[i]])

				if ratings_prediction == ratings_list[i]:
					average_correct_ratings.append(1)
				else:
					average_correct_ratings.append(0)
			except:
				pass

		# Perform decision tree classiciation for food ratings
		for i in range(m_length):
			try:
				clf = classifier.fit((rest_matrix[0:i] + rest_matrix[i+1:m_length]), ((food_ratings_list[0:i] + food_ratings_list[i+1:m_length])))

				ratings_prediction = clf.predict([rest_matrix[i]])

				if ratings_prediction == food_ratings_list[i]:
					average_correct_food_ratings.append(1)
				else:
					average_correct_food_ratings.append(0)
			except:
				pass

		# Perform decision tree classiciation for service ratings
		for i in range(m_length):
			try:
				clf = classifier.fit((rest_matrix[0:i] + rest_matrix[i+1:m_length]), ((service_ratings_list[0:i] + service_ratings_list[i+1:m_length])))

				ratings_prediction = clf.predict([rest_matrix[i]])

				if ratings_prediction == service_ratings_list[i]:
					average_correct_service_ratings.append(1)
				else:
					average_correct_service_ratings.append(0)
			except:
				pass

	# Average correct
	return [np.mean(average_correct_ratings), np.mean(average_correct_food_ratings), np.mean(average_correct_service_ratings), len(average_correct_ratings)]

def user_1_to_n_restaurant(user_dict, rest_dict, user_ratings_dict, classifier):
	# Dictionary of user features {userID: features}
	item_feaure_dict = item_dect_to_item_list(rest_dict)

	# Average of how often the classifier was right
	average_correct_ratings = []
	average_correct_food_ratings = []
	average_correct_service_ratings = []

	# For each user, seperate restID and restaurant features
	for user, rating in user_ratings_dict.items():
		# Matrix of features
		user_matrix = []
		# List of ratings
		ratings_list = []
		food_ratings_list = []
		service_ratings_list = []

		# For each restaurant. Rest is in tuple format (placeID, rating, food_rating, service_rating)
		for rest in rating:
			user_matrix.append(item_feaure_dict[rest[0]])
			ratings_list.append(rest[1])
			food_ratings_list.append(rest[2])
			service_ratings_list.append(rest[3])

		# Rows in matrix
		m_length = len(user_matrix)

		# Perform decision tree classiciation for ratings
		for i in range(m_length):
			try:
				clf = classifier.fit((user_matrix[0:i] + user_matrix[i+1:m_length]), ((ratings_list[0:i] + ratings_list[i+1:m_length])))

				ratings_prediction = clf.predict([user_matrix[i]])

				if ratings_prediction == ratings_list[i]:
					average_correct_ratings.append(1)
				else:
					average_correct_ratings.append(0)
			except:
				pass

		# Perform decision tree classiciation for food ratings
		for i in range(m_length):
			try:
				clf = classifier.fit((user_matrix[0:i] + user_matrix[i+1:m_length]), ((food_ratings_list[0:i] + food_ratings_list[i+1:m_length])))

				ratings_prediction = clf.predict([user_matrix[i]])

				if ratings_prediction == food_ratings_list[i]:
					average_correct_food_ratings.append(1)
				else:
					average_correct_food_ratings.append(0)
			except:
				pass

		# Perform decision tree classiciation for service ratings
		for i in range(m_length):
			try:
				clf = classifier.fit((user_matrix[0:i] + user_matrix[i+1:m_length]), ((service_ratings_list[0:i] + service_ratings_list[i+1:m_length])))

				ratings_prediction = clf.predict([user_matrix[i]])

				if ratings_prediction == service_ratings_list[i]:
					average_correct_service_ratings.append(1)
				else:
					average_correct_service_ratings.append(0)
			except:
				pass

	# Average correct
	return [np.mean(average_correct_ratings), np.mean(average_correct_food_ratings), np.mean(average_correct_service_ratings), len(average_correct_ratings)]

def restaurant_1_to_n_user_reduced(user_dict, rest_dict, rest_ratings_dict, classifier):
	# Dictionary of user features {userID: features}
	user_feaure_dict = user_dect_to_user_list(user_dict)

	# Average of how often the classifier was right
	average_correct_ratings = []
	average_correct_food_ratings = []
	average_correct_service_ratings = []

	# For each restaurant, seperate restID and user features
	for restaurant, rating in rest_ratings_dict.items():
		# Matrix of features
		rest_matrix = []
		# List of ratings
		ratings_list = []
		food_ratings_list = []
		service_ratings_list = []

		# For each user. User is in tuple format (userID, rating, food_rating, service_rating)
		for user in rating:
			rest_matrix.append(user_feaure_dict[user[0]])
			ratings_list.append(user[1])
			food_ratings_list.append(user[2])
			service_ratings_list.append(user[3])

		sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
		rest_matrix = sel.fit_transform(rest_matrix)

		# Rows in matrix
		m_length = len(rest_matrix)

		# Perform decision tree classiciation for ratings
		for i in range(m_length):
			try:
				clf = classifier.fit((rest_matrix[0:i] + rest_matrix[i+1:m_length]), ((ratings_list[0:i] + ratings_list[i+1:m_length])))

				ratings_prediction = clf.predict([rest_matrix[i]])

				if ratings_prediction == ratings_list[i]:
					average_correct_ratings.append(1)
				else:
					average_correct_ratings.append(0)
			except:
				pass

		# Perform decision tree classiciation for food ratings
		for i in range(m_length):
			try:
				clf = classifier.fit((rest_matrix[0:i] + rest_matrix[i+1:m_length]), ((food_ratings_list[0:i] + food_ratings_list[i+1:m_length])))

				ratings_prediction = clf.predict([rest_matrix[i]])

				if ratings_prediction == food_ratings_list[i]:
					average_correct_food_ratings.append(1)
				else:
					average_correct_food_ratings.append(0)
			except:
				pass

		# Perform decision tree classiciation for service ratings
		for i in range(m_length):
			try:
				clf = classifier.fit((rest_matrix[0:i] + rest_matrix[i+1:m_length]), ((service_ratings_list[0:i] + service_ratings_list[i+1:m_length])))

				ratings_prediction = clf.predict([rest_matrix[i]])

				if ratings_prediction == service_ratings_list[i]:
					average_correct_service_ratings.append(1)
				else:
					average_correct_service_ratings.append(0)
			except:
				pass

	# Average correct
	a = sum(average_correct_ratings)
	if(a != 0):
		a /= len(average_correct_ratings)
	b = sum(average_correct_ratings)
	if(b != 0):
		b /= len(average_correct_food_ratings)
	c = sum(average_correct_ratings)
	if(c != 0):
		c /= len(average_correct_service_ratings)
	return [a,b,c, len(average_correct_ratings)]

def user_1_to_n_restaurant_reduced(user_dict, rest_dict, user_ratings_dict, classifier):
	# Dictionary of user features {userID: features}
	item_feaure_dict = item_dect_to_item_list(rest_dict)

	# Average of how often the classifier was right
	average_correct_ratings = []
	average_correct_food_ratings = []
	average_correct_service_ratings = []

	# For each user, seperate restID and restaurant features
	for user, rating in user_ratings_dict.items():
		# Matrix of features
		user_matrix = []
		# List of ratings
		ratings_list = []
		food_ratings_list = []
		service_ratings_list = []

		# For each restaurant. Rest is in tuple format (placeID, rating, food_rating, service_rating)
		for rest in rating:
			user_matrix.append(item_feaure_dict[rest[0]])
			ratings_list.append(rest[1])
			food_ratings_list.append(rest[2])
			service_ratings_list.append(rest[3])

		sel = VarianceThreshold(threshold=(.2 * (1 - .2)))
		user_matrix = sel.fit_transform(user_matrix, ratings_list)
		print(len(user_matrix))

		# Rows in matrix
		m_length = len(user_matrix)

		# Perform decision tree classiciation for ratings
		for i in range(m_length):
			try:
				clf = classifier.fit((user_matrix[0:i] + user_matrix[i+1:m_length]), ((ratings_list[0:i] + ratings_list[i+1:m_length])))

				ratings_prediction = clf.predict([user_matrix[i]])

				if ratings_prediction == ratings_list[i]:
					average_correct_ratings.append(1)
				else:
					average_correct_ratings.append(0)
			except Exception as e: print(e)

		# Perform decision tree classiciation for food ratings
		for i in range(m_length):
			try:
				clf = classifier.fit((user_matrix[0:i] + user_matrix[i+1:m_length]), ((food_ratings_list[0:i] + food_ratings_list[i+1:m_length])))

				ratings_prediction = clf.predict([user_matrix[i]])

				if ratings_prediction == food_ratings_list[i]:
					average_correct_food_ratings.append(1)
				else:
					average_correct_food_ratings.append(0)
			except:
				pass

		# Perform decision tree classiciation for service ratings
		for i in range(m_length):
			try:
				clf = classifier.fit((user_matrix[0:i] + user_matrix[i+1:m_length]), ((service_ratings_list[0:i] + service_ratings_list[i+1:m_length])))

				ratings_prediction = clf.predict([user_matrix[i]])

				if ratings_prediction == service_ratings_list[i]:
					average_correct_service_ratings.append(1)
				else:
					average_correct_service_ratings.append(0)
			except:
				pass

	# Average correct
	a = sum(average_correct_ratings)
	if(a != 0):
		a /= len(average_correct_ratings)
	b = sum(average_correct_ratings)
	if(b != 0):
		b /= len(average_correct_food_ratings)
	c = sum(average_correct_ratings)
	if(c != 0):
		c /= len(average_correct_service_ratings)
	return [a,b,c, len(average_correct_ratings)]


#print(item())
#item()
#k = item()
pp = pprint.PrettyPrinter(indent=4)

#print(len(k))
#pp.pprint(k)

#t = item_dect_to_matrix(k)

#for i in t:
#	print(i)


a = user()
b = item()
c, d = rating_dict();
#pp.pprint(d)
# DecisionTreeClassifier()
# KNeighborsClassifier(n_neighbors=1)
# SVC()

from sklearn.linear_model import SGDClassifier
# SGDClassifier(loss="hinge", penalty="l2")
# from sklearn.gaussian_process import GaussianProcess
# GaussianProcess(theta0=1e-2, thetaL=1e-4, thetaU=1e-1) NO
from sklearn.ensemble import RandomForestClassifier
# RandomForestClassifier(n_estimators=1)
# from sklearn.neural_network import MLPClassifier
# MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1) NO
from texttable import Texttable

t1 = Texttable()

print('Prediction Precision: User')
header = ['Classifier', 'Rating', 'Food Rating', 'Service Rating', 'Samples']

u_decision_tree = ['Decision Tree'] + user_1_to_n_restaurant(a,b,c, DecisionTreeClassifier())
u_knn = ['kNN, k=1'] + user_1_to_n_restaurant(a,b,c, KNeighborsClassifier(n_neighbors=1))
u_knn2 = ['kNN, k=2'] + user_1_to_n_restaurant(a,b,c, KNeighborsClassifier(n_neighbors=2))
u_knn3 = ['kNN, k=3'] + user_1_to_n_restaurant(a,b,c, KNeighborsClassifier(n_neighbors=3))
u_knn4 = ['kNN, k=4'] + user_1_to_n_restaurant(a,b,c, KNeighborsClassifier(n_neighbors=4))
u_knn5 = ['kNN, k=5'] + user_1_to_n_restaurant(a,b,c, KNeighborsClassifier(n_neighbors=5))
u_knn6 = ['kNN, k=6'] + user_1_to_n_restaurant(a,b,c, KNeighborsClassifier(n_neighbors=6))
u_svc = ['SVC'] + user_1_to_n_restaurant(a,b,c, SVC())

t1.add_rows([header, u_decision_tree, u_svc, u_knn, u_knn2, u_knn3, u_knn4, u_knn5, u_knn6])

print(t1.draw())
print()

t2 = Texttable()

print('Prediction Precision: Restaurant')
header = ['Classifier', 'Rating', 'Food Rating', 'Service Rating', 'Samples']

i_decision_tree = ['Decision Tree'] + restaurant_1_to_n_user(a,b,d, DecisionTreeClassifier())
i_knn = ['kNN, k=1'] + restaurant_1_to_n_user(a,b,d, KNeighborsClassifier(n_neighbors=1))
i_knn2 = ['kNN, k=2'] + restaurant_1_to_n_user(a,b,d, KNeighborsClassifier(n_neighbors=2))
i_knn3 = ['kNN, k=3'] + restaurant_1_to_n_user(a,b,d, KNeighborsClassifier(n_neighbors=3))
i_knn4 = ['kNN, k=4'] + restaurant_1_to_n_user(a,b,d, KNeighborsClassifier(n_neighbors=4))
i_knn5 = ['kNN, k=5'] + restaurant_1_to_n_user(a,b,d, KNeighborsClassifier(n_neighbors=5))
i_knn6 = ['kNN, k=6'] + restaurant_1_to_n_user(a,b,d, KNeighborsClassifier(n_neighbors=6))
i_svc = ['SVC'] + restaurant_1_to_n_user(a,b,d, SVC())

t2.add_rows([header, i_decision_tree, i_svc, i_knn, i_knn2, i_knn3, i_knn4, i_knn5, i_knn6])

print(t2.draw())
print()
'''

##########

t1 = Texttable()

print('Prediction Precision: User, reduced variance')
header = ['Classifier', 'Rating', 'Food Rating', 'Service Rating', 'Samples']

u_decision_tree = ['Decision Tree'] + user_1_to_n_restaurant_reduced(a,b,c, DecisionTreeClassifier())
u_knn = ['kNN, k=1'] + user_1_to_n_restaurant_reduced(a,b,c, KNeighborsClassifier(n_neighbors=1))
u_knn2 = ['kNN, k=2'] + user_1_to_n_restaurant_reduced(a,b,c, KNeighborsClassifier(n_neighbors=2))
u_knn3 = ['kNN, k=3'] + user_1_to_n_restaurant_reduced(a,b,c, KNeighborsClassifier(n_neighbors=3))
u_knn4 = ['kNN, k=4'] + user_1_to_n_restaurant_reduced(a,b,c, KNeighborsClassifier(n_neighbors=4))
u_knn5 = ['kNN, k=5'] + user_1_to_n_restaurant_reduced(a,b,c, KNeighborsClassifier(n_neighbors=5))
u_knn6 = ['kNN, k=6'] + user_1_to_n_restaurant_reduced(a,b,c, KNeighborsClassifier(n_neighbors=6))
u_svc = ['SVC'] + user_1_to_n_restaurant_reduced(a,b,c, SVC())

t1.add_rows([header, u_decision_tree, u_svc, u_knn, u_knn2, u_knn3, u_knn4, u_knn5, u_knn6])

print(t1.draw())
print()

t2 = Texttable()

print('Prediction Precision: Restaurant, reduced variance')
header = ['Classifier', 'Rating', 'Food Rating', 'Service Rating', 'Samples']

i_decision_tree = ['Decision Tree'] + restaurant_1_to_n_user_reduced(a,b,d, DecisionTreeClassifier())
i_knn = ['kNN, k=1'] + restaurant_1_to_n_user_reduced(a,b,d, KNeighborsClassifier(n_neighbors=1))
i_knn2 = ['kNN, k=2'] + restaurant_1_to_n_user_reduced(a,b,d, KNeighborsClassifier(n_neighbors=2))
i_knn3 = ['kNN, k=3'] + restaurant_1_to_n_user_reduced(a,b,d, KNeighborsClassifier(n_neighbors=3))
i_knn4 = ['kNN, k=4'] + restaurant_1_to_n_user_reduced(a,b,d, KNeighborsClassifier(n_neighbors=4))
i_knn5 = ['kNN, k=5'] + restaurant_1_to_n_user_reduced(a,b,d, KNeighborsClassifier(n_neighbors=5))
i_knn6 = ['kNN, k=6'] + restaurant_1_to_n_user_reduced(a,b,d, KNeighborsClassifier(n_neighbors=6))
i_svc = ['SVC'] + restaurant_1_to_n_user_reduced(a,b,d, SVC())

t2.add_rows([header, i_decision_tree, i_svc, i_knn, i_knn2, i_knn3, i_knn4, i_knn5, i_knn6])

print(t2.draw())
print()

#e = user_1_to_n_restaurant(a,b,c, DecisionTreeClassifier())
#pp.pprint(e)
'''





























