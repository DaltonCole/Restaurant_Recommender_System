from surprise import SVD
from surprise import NMF
from surprise import KNNBasic
from surprise import Dataset, Reader
from surprise import evaluate, print_perf

import numpy as np
import matplotlib.pyplot as plt

import os

import parser

import random

random.seed(0)

'''
####################################################################################
# Load the movielens-100k dataset (download it if needed),
# and split it into 3 folds for cross-validation.
data = Dataset.load_builtin('ml-100k')
data.split(n_folds=3)

# We'll use the famous SVD algorithm.
algo = SVD()

# Evaluate performances of our algorithm on the dataset.
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])

print_perf(perf)
####################################################################################
'''

print("############################################## Rating ##############################################")
# path to dataset file
#file_path = os.path.expanduser('~/Desktop/CS6001/Project/RCdata/rating_final.csv')
file_path = os.path.expanduser('~/Desktop/CS6001/Project/Parsed/rating.csv')

# As we're loading a custom dataset, we need to define a reader.
reader = Reader(line_format='user item rating', sep=',', rating_scale=(0, 2), skip_lines=1)

data = Dataset.load_from_file(file_path, reader=reader)
data.split(n_folds=5)

################################## SVD ##################################
print("################################## SVD ##################################")

# We'll use the famous SVD algorithm.
algo = SVD()

# Evaluate performances of our algorithm on the dataset.
perf_svd = evaluate(algo, data, measures=['RMSE', 'MAE'])

print_perf(perf_svd)

################################## PMF ##################################
print("################################## PMF ##################################")

# We'll use the famous SVD algorithm.
algo = SVD(biased=False)

# Evaluate performances of our algorithm on the dataset.
perf_pmf = evaluate(algo, data, measures=['RMSE', 'MAE'])

print_perf(perf_pmf)

################################## NMF ##################################
print("################################## NMF ##################################")

# We'll use the famous SVD algorithm.
algo = NMF()

# Evaluate performances of our algorithm on the dataset.
perf_nmf = evaluate(algo, data, measures=['RMSE', 'MAE'])

print_perf(perf_nmf)

print("############################# User based Collaborative Filtering #############################")
algo = KNNBasic(sim_options = {'user_based': True})
perf_user_based = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_user_based)
print()

print("############################# Item based Collaborative Filtering #############################")
algo = KNNBasic(sim_options = {'user_based': False})
perf_item_based = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_item_based)
print()

print("Question: 13")
print("############################ User based Collaborative Filtering MSD ###########################")
algo = KNNBasic(sim_options = {'name':'MSD','user_based': True})
perf_user_based_msd = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_user_based_msd)
print()

print("########################## User based Collaborative Filtering Cosine ##########################")
algo = KNNBasic(sim_options = {'name':'cosine','user_based': True})
perf_user_based_cosine = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_user_based_cosine)
print()

print("########################## User based Collaborative Filtering Pearson #########################")
algo = KNNBasic(sim_options = {'name':'pearson','user_based': True})
perf_user_based_pearson = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_user_based_pearson)
print()

print("############################ Item based Collaborative Filtering MSD ###########################")
algo = KNNBasic(sim_options = {'name':'MSD','user_based': False})
perf_item_based_msd = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_item_based_msd)
print()

print("########################## Item based Collaborative Filtering Cosine ##########################")
algo = KNNBasic(sim_options = {'name':'cosine','user_based': False})
perf_item_based_cosine = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_item_based_cosine)
print()

print("########################## Item based Collaborative Filtering Pearson #########################")
algo = KNNBasic(sim_options = {'name':'pearson','user_based': False})
perf_item_based_pearson = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_item_based_pearson)

print(perf_svd)

'''
# Graph
N = 11
means = [perf_svd['rmse'][-1], perf_pmf['rmse'][-1], perf_nmf['rmse'][-1], perf_user_based['rmse'][-1], perf_item_based['rmse'][-1], perf_user_based_msd['rmse'][-1], perf_user_based_cosine['rmse'][-1], perf_user_based_pearson['rmse'][-1], perf_item_based_msd['rmse'][-1], perf_item_based_cosine['rmse'][-1], perf_item_based_pearson['rmse'][-1]]
for i in range(len(means)):
	means[i] = round(means[i], 2)
means = tuple(means)

labels = ('SVD', 'PMF', 'NFM', 'User Based', 'Item Based', 'U-B-MSD' , 'U-B-Cosine', 'U-B-Pearson', 'I-B-MSD' , 'I-B-Cosine', 'I-B-Pearson')

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, means, width, color='r')

ax.set_xlabel('Method')
ax.set_ylabel('RMSE')
ax.set_title('Method vs RMSE')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(labels)

ax.legend((rects1[0],), ('Rating',))
ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=45)


print(means)
for i,j in zip(range(0,11) , means):
	ax.annotate(str(j),xy=(i,j))

#plt.savefig("image.png")

plt.show()
'''

print("\n############################################## Food Rating ##############################################")
# path to dataset file
#file_path = os.path.expanduser('~/Desktop/CS6001/Project/RCdata/rating_final.csv')
file_path = os.path.expanduser('~/Desktop/CS6001/Project/Parsed/food_rating.csv')

# As we're loading a custom dataset, we need to define a reader.
reader = Reader(line_format='user item rating', sep=',', rating_scale=(0, 2), skip_lines=1)

data = Dataset.load_from_file(file_path, reader=reader)
data.split(n_folds=5)

################################## SVD ##################################
print("################################## SVD ##################################")

# We'll use the famous SVD algorithm.
algo = SVD()

# Evaluate performances of our algorithm on the dataset.
perf_svd_food = evaluate(algo, data, measures=['RMSE', 'MAE'])

print_perf(perf_svd_food)

################################## PMF ##################################
print("################################## PMF ##################################")

# We'll use the famous SVD algorithm.
algo = SVD(biased=False)

# Evaluate performances of our algorithm on the dataset.
perf_pmf_food = evaluate(algo, data, measures=['RMSE', 'MAE'])

print_perf(perf_pmf_food)

################################## NMF ##################################
print("################################## NMF ##################################")

# We'll use the famous SVD algorithm.
algo = NMF()

# Evaluate performances of our algorithm on the dataset.
perf_nmf_food = evaluate(algo, data, measures=['RMSE', 'MAE'])

print_perf(perf_nmf_food)

print("############################# User based Collaborative Filtering #############################")
algo = KNNBasic(sim_options = {'user_based': True})
perf_user_based_food = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_user_based_food)
print()

print("############################# Item based Collaborative Filtering #############################")
algo = KNNBasic(sim_options = {'user_based': False})
perf_item_based_food = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_item_based_food)
print()

print("Question: 13")
print("############################ User based Collaborative Filtering MSD ###########################")
algo = KNNBasic(sim_options = {'name':'MSD','user_based': True})
perf_user_based_msd_food = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_user_based_msd_food)
print()

print("########################## User based Collaborative Filtering Cosine ##########################")
algo = KNNBasic(sim_options = {'name':'cosine','user_based': True})
perf_user_based_cosine_food = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_user_based_cosine_food)
print()

print("########################## User based Collaborative Filtering Pearson #########################")
algo = KNNBasic(sim_options = {'name':'pearson','user_based': True})
perf_user_based_pearson_food = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_user_based_pearson_food)
print()

print("############################ Item based Collaborative Filtering MSD ###########################")
algo = KNNBasic(sim_options = {'name':'MSD','user_based': False})
perf_item_based_msd_food = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_item_based_msd_food)
print()

print("########################## Item based Collaborative Filtering Cosine ##########################")
algo = KNNBasic(sim_options = {'name':'cosine','user_based': False})
perf_item_based_cosine_food = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_item_based_cosine_food)
print()

print("########################## Item based Collaborative Filtering Pearson #########################")
algo = KNNBasic(sim_options = {'name':'pearson','user_based': False})
perf_item_based_pearson_food = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_item_based_pearson_food)


print("\n############################################## Service Rating ##############################################")
# path to dataset file
#file_path = os.path.expanduser('~/Desktop/CS6001/Project/RCdata/rating_final.csv')
file_path = os.path.expanduser('~/Desktop/CS6001/Project/Parsed/service_rating.csv')

# As we're loading a custom dataset, we need to define a reader.
reader = Reader(line_format='user item rating', sep=',', rating_scale=(0, 2), skip_lines=1)

data = Dataset.load_from_file(file_path, reader=reader)
data.split(n_folds=5)

################################## SVD ##################################
print("################################## SVD ##################################")

# We'll use the famous SVD algorithm.
algo = SVD()

# Evaluate performances of our algorithm on the dataset.
perf_svd_service = evaluate(algo, data, measures=['RMSE', 'MAE'])

print_perf(perf_svd_service)

################################## PMF ##################################
print("################################## PMF ##################################")

# We'll use the famous SVD algorithm.
algo = SVD(biased=False)

# Evaluate performances of our algorithm on the dataset.
perf_pmf_service = evaluate(algo, data, measures=['RMSE', 'MAE'])

print_perf(perf_pmf_service)

################################## NMF ##################################
print("################################## NMF ##################################")

# We'll use the famous SVD algorithm.
algo = NMF()

# Evaluate performances of our algorithm on the dataset.
perf_nmf_service = evaluate(algo, data, measures=['RMSE', 'MAE'])

print_perf(perf_nmf_service)

print("############################# User based Collaborative Filtering #############################")
algo = KNNBasic(sim_options = {'user_based': True})
perf_user_based_service = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_user_based_service)
print()

print("############################# Item based Collaborative Filtering #############################")
algo = KNNBasic(sim_options = {'user_based': False})
perf_item_based_service = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_item_based_service)
print()

print("Question: 13")
print("############################ User based Collaborative Filtering MSD ###########################")
algo = KNNBasic(sim_options = {'name':'MSD','user_based': True})
perf_user_based_msd_service = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_user_based_msd_service)
print()

print("########################## User based Collaborative Filtering Cosine ##########################")
algo = KNNBasic(sim_options = {'name':'cosine','user_based': True})
perf_user_based_cosine_service = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_user_based_cosine_service)
print()

print("########################## User based Collaborative Filtering Pearson #########################")
algo = KNNBasic(sim_options = {'name':'pearson','user_based': True})
perf_user_based_pearson_service = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_user_based_pearson_service)
print()

print("############################ Item based Collaborative Filtering MSD ###########################")
algo = KNNBasic(sim_options = {'name':'MSD','user_based': False})
perf_item_based_msd_service = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_item_based_msd_service)
print()

print("########################## Item based Collaborative Filtering Cosine ##########################")
algo = KNNBasic(sim_options = {'name':'cosine','user_based': False})
perf_item_based_cosine_service = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_item_based_cosine_service)
print()

print("########################## Item based Collaborative Filtering Pearson #########################")
algo = KNNBasic(sim_options = {'name':'pearson','user_based': False})
perf_item_based_pearson_service = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf_item_based_pearson_service)



####### Combined Graph #######
N = 11
ind = np.arange(N)  # the x locations for the groups
width = 0.30       # the width of the bars
labels = ('SVD', 'PMF', 'NFM', 'User Based', 'Item Based', 'U-B-MSD' , 'U-B-Cosine', 'U-B-Pearson', 'I-B-MSD' , 'I-B-Cosine', 'I-B-Pearson')
fig, ax = plt.subplots()

# Rating
means = [perf_svd['rmse'][-1], perf_pmf['rmse'][-1], perf_nmf['rmse'][-1], perf_user_based['rmse'][-1], perf_item_based['rmse'][-1], perf_user_based_msd['rmse'][-1], perf_user_based_cosine['rmse'][-1], perf_user_based_pearson['rmse'][-1], perf_item_based_msd['rmse'][-1], perf_item_based_cosine['rmse'][-1], perf_item_based_pearson['rmse'][-1]]
for i in range(len(means)):
	means[i] = round(means[i], 2)
means = tuple(means)

rects1 = ax.bar(ind, means, width, color='r')

# Food rating
food_means = [perf_svd_food['rmse'][-1], perf_pmf_food['rmse'][-1], perf_nmf_food['rmse'][-1], perf_user_based_food['rmse'][-1], perf_item_based_food['rmse'][-1], perf_user_based_msd_food['rmse'][-1], perf_user_based_cosine_food['rmse'][-1], perf_user_based_pearson_food['rmse'][-1], perf_item_based_msd_food['rmse'][-1], perf_item_based_cosine_food['rmse'][-1], perf_item_based_pearson_food['rmse'][-1]]
for i in range(len(food_means)):
	food_means[i] = round(food_means[i], 2)
food_means = tuple(food_means)

rects2 = ax.bar(ind + width, food_means, width, color='y')

# Service rating
service_means = [perf_svd_service['rmse'][-1], perf_pmf_service['rmse'][-1], perf_nmf_service['rmse'][-1], perf_user_based_service['rmse'][-1], perf_item_based_service['rmse'][-1], perf_user_based_msd_service['rmse'][-1], perf_user_based_cosine_service['rmse'][-1], perf_user_based_pearson_service['rmse'][-1], perf_item_based_msd_service['rmse'][-1], perf_item_based_cosine_service['rmse'][-1], perf_item_based_pearson_service['rmse'][-1]]
for i in range(len(service_means)):
	service_means[i] = round(service_means[i], 2)
service_means = tuple(service_means)

rects3 = ax.bar(ind + width + width, service_means, width, color='b')

fig.subplots_adjust(bottom=0.2)

ax.set_xlabel('Method')
ax.set_ylabel('RMSE')
ax.set_ylim([0,1])
ax.set_title('Method vs RMSE')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(labels)

ax.legend((rects1[0], rects2[0], rects3[0]), ('Rating', 'Food', 'Service'))
ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=45)

'''
print(means)
for i,j in zip(range(0,11) , means):
	ax.annotate(str(j),xy=(i,j))
for i,j in zip(range(11,22) , food_means):
	ax.annotate(str(j),xy=(i,j))
for i,j in zip(range(0,11) , service_means):
	ax.annotate(str(j),xy=(i,j))
'''

#plt.savefig("image.png")

plt.show()


####### Rating Graph #######
N = 11
ind = np.arange(N)  # the x locations for the groups
width = 0.30       # the width of the bars
labels = ('SVD', 'PMF', 'NFM', 'User Based', 'Item Based', 'U-B-MSD' , 'U-B-Cosine', 'U-B-Pearson', 'I-B-MSD' , 'I-B-Cosine', 'I-B-Pearson')
fig, ax = plt.subplots()

# Rating
means = [perf_svd['rmse'][-1], perf_pmf['rmse'][-1], perf_nmf['rmse'][-1], perf_user_based['rmse'][-1], perf_item_based['rmse'][-1], perf_user_based_msd['rmse'][-1], perf_user_based_cosine['rmse'][-1], perf_user_based_pearson['rmse'][-1], perf_item_based_msd['rmse'][-1], perf_item_based_cosine['rmse'][-1], perf_item_based_pearson['rmse'][-1]]
for i in range(len(means)):
	means[i] = round(means[i], 2)
means = tuple(means)

rects1 = ax.bar(ind, means, width, color='r')

fig.subplots_adjust(bottom=0.2)

ax.set_xlabel('Method')
ax.set_ylabel('RMSE')
ax.set_ylim([0,1])
ax.set_title('Method vs RMSE')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(labels)

ax.legend((rects1[0],), ('Rating',))
ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=45)


for i,j in zip(range(0,11) , means):
	ax.annotate(str(j),xy=(i,j))

#plt.savefig("image.png")

plt.show()


####### Food Graph #######
N = 11
ind = np.arange(N)  # the x locations for the groups
width = 0.30       # the width of the bars
labels = ('SVD', 'PMF', 'NFM', 'User Based', 'Item Based', 'U-B-MSD' , 'U-B-Cosine', 'U-B-Pearson', 'I-B-MSD' , 'I-B-Cosine', 'I-B-Pearson')
fig, ax = plt.subplots()

# Food rating
food_means = [perf_svd_food['rmse'][-1], perf_pmf_food['rmse'][-1], perf_nmf_food['rmse'][-1], perf_user_based_food['rmse'][-1], perf_item_based_food['rmse'][-1], perf_user_based_msd_food['rmse'][-1], perf_user_based_cosine_food['rmse'][-1], perf_user_based_pearson_food['rmse'][-1], perf_item_based_msd_food['rmse'][-1], perf_item_based_cosine_food['rmse'][-1], perf_item_based_pearson_food['rmse'][-1]]
for i in range(len(food_means)):
	food_means[i] = round(food_means[i], 2)
food_means = tuple(food_means)

rects2 = ax.bar(ind, food_means, width, color='y')

fig.subplots_adjust(bottom=0.2)

ax.set_xlabel('Method')
ax.set_ylabel('RMSE')
ax.set_ylim([0,1])
ax.set_title('Method vs RMSE')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(labels)

ax.legend((rects2[0],), ('Rating',))
ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=45)

for i,j in zip(range(0,11) , food_means):
	ax.annotate(str(j),xy=(i,j))


#plt.savefig("image.png")

plt.show()

####### Service Graph #######
N = 11
ind = np.arange(N)  # the x locations for the groups
width = 0.30       # the width of the bars
labels = ('SVD', 'PMF', 'NFM', 'User Based', 'Item Based', 'U-B-MSD' , 'U-B-Cosine', 'U-B-Pearson', 'I-B-MSD' , 'I-B-Cosine', 'I-B-Pearson')
fig, ax = plt.subplots()

# Service rating
service_means = [perf_svd_service['rmse'][-1], perf_pmf_service['rmse'][-1], perf_nmf_service['rmse'][-1], perf_user_based_service['rmse'][-1], perf_item_based_service['rmse'][-1], perf_user_based_msd_service['rmse'][-1], perf_user_based_cosine_service['rmse'][-1], perf_user_based_pearson_service['rmse'][-1], perf_item_based_msd_service['rmse'][-1], perf_item_based_cosine_service['rmse'][-1], perf_item_based_pearson_service['rmse'][-1]]
for i in range(len(service_means)):
	service_means[i] = round(service_means[i], 2)
service_means = tuple(service_means)

rects3 = ax.bar(ind, service_means, width, color='b')

fig.subplots_adjust(bottom=0.2)

ax.set_xlabel('Method')
ax.set_ylabel('RMSE')
ax.set_ylim([0,1])
ax.set_title('Method vs RMSE')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(labels)

ax.legend((rects3[0],), ('Rating',))
ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=45)

for i,j in zip(range(0,11) , service_means):
	ax.annotate(str(j),xy=(i,j+0.05))

plt.savefig("image.png")

plt.show()




