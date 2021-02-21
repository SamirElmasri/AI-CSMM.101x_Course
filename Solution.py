# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:55:24 2020

@author: Samir
"""
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
 
def split(final):
    x = []
    y = []
    for i in range(len(final)):
        x.append(final[i][0])
        y.append(final[i][1])
    return x , y


def count_vec(x, typegram , stop_list):
    if typegram == 'unigram':
        typed = (1,1)
    elif typegram == 'bigram':
        typed = (2,2)
    vectorizer = CountVectorizer(stop_words = stop_list , ngram_range = typed)
    X = vectorizer.fit_transform(x)
    features = vectorizer.get_feature_names()
    #labelcount = X.toarray()
    return features , X

def vec_countidf(x,typegram, stop_list, features):
    if typegram == 'unigram':
        typed = (1,1)
    elif typegram == 'bigram':
        typed = (1,2)
    pipe = Pipeline([('count',CountVectorizer(stop_words = stop_list , ngram_range = typed , vocabulary = features)), ('tfid', TfidfTransformer())]).fit(x)
    pipe['count'].transform(x)
    pipe['tfid'].idf_
    gram = pipe.transform(x)
    
    return gram

def count_vec_test(x, typegram , stop_list, features):
    if typegram == 'unigram':
        typed = (1,1)
    elif typegram == 'bigram':
        typed = (1,2)
    vectorizer = CountVectorizer(stop_words = stop_list , ngram_range = typed, vocabulary = features)
    X = vectorizer.fit_transform(x)
    features = vectorizer.get_feature_names()
    #labelcount = X.toarray()
    return X
    
def modeling(array , y , need_prdt, array_test, y_test, filename):
    model = SGDClassifier( loss = 'hinge' , penalty= 'l1')
    model.fit(array , y)
    score_train = model.score(array , y)
    score_test = model.score(array_test , y_test)
    
    prediction = model.predict(need_prdt)
    #for i in range(len(need_prdt)):
    #prediction.append(model.predict(need_prdt[i]))
    
    with open(filename, 'w') as filehandle:
        for listitem in prediction:
            filehandle.write('%s\n' % listitem)
    
    return score_train , score_test, prediction
        