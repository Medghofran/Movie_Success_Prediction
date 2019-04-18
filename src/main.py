import pandas as pd
import csv
from sklearn.preprocessing import StandardScaler
from pca import run_pca
from knn import run_knn
from random_forest import run_random_forest
from logistic import run_logistic_regression
from server import run, _classifier
import numpy as np

def fill_nan(df_movie, col):
    df_movie[col] = df_movie[col].fillna(df_movie[col].median())

def data_prepocessing():
    df = pd.read_csv('../data/imdb.csv', error_bad_lines= False , quoting=csv.QUOTE_MINIMAL)
    #df = df[df['year'] > 2000]
    df_movie = df
    cols = list(df_movie.columns)
    fill_nan(df_movie,cols)
    # delete columns using the columns parameter of drop
    df_movie = df_movie.drop(columns="type")
    df_movie = df_movie.drop(columns="fn")
    df_movie = df_movie.drop(columns="tid")
    df_movie = df_movie.drop(columns="url")

    # col = list(df_movie.columns)
    # col.remove('type')
    # col.remove('fn')
    # col.remove('tid')
    # col.remove('url')

    # sc = StandardScaler()
    # temp = sc.fit_transform(df_movie[col])
    # df_movie[col] = temp
 
    df_standard = df_movie[list(df_movie.describe().columns)]
    return (df_movie, df_standard)

def classify(row):
    if row['imdbRating'] >= 0 and row['imdbRating'] < 4:
        return 0
    elif row['imdbRating'] >= 4 and row['imdbRating'] < 8:
        return 1
    elif row['imdbRating'] >= 8 and row['imdbRating'] <= 10:
        return 2

if __name__ == '__main__':
    df_movie, df_standard = data_prepocessing()
    df_knn = df_movie

    df_knn["class"] = df_knn.apply(classify, axis=1)
    df_knn = df_knn.drop(columns="imdbRating")
    #run_knn(df_knn)
    run_logistic_regression(df_knn)
    classifier = run_random_forest(df_knn)
    run(classifier)

