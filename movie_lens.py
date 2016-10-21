# coding=utf-8
import pandas as pd
from termcolor import colored

u_names = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('data/ml-1m/users.dat', sep='::', header=None, names=u_names, engine='python')

r_names = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('data/ml-1m/ratings.dat', sep='::', names=r_names, engine='python')

m_names = ['movie_id', 'title', 'genres']
movies = pd.read_table('data/ml-1m/movies.dat', sep='::', names=m_names, engine='python')

data = pd.merge(pd.merge(ratings, users), movies)

mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
ratings_by_title = data.groupby('title').size()

active_titles = ratings_by_title.index[ratings_by_title >= 250]
mean_ratings = mean_ratings.ix[active_titles]

top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)

print colored('-------- Фильмы, оказавшиеся на первом месте у зрителей-женщин --------', 'blue')
print top_female_ratings[:10]
print colored('-----------------------------------------------------------------------', 'blue')

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='diff')

# TODO Makkinni_U__-_Python_i_analiz_dannykh_-_2015 стр 42
