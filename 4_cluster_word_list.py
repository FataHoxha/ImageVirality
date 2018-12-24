import json
import sys
import re
import csv
import time
import spacy
import collections
import numpy as np
from sklearn.cluster import KMeans
from spacy.lang.en import English
from sklearn.feature_extraction.text import TfidfVectorizer

filename = sys.argv[-1]
nlp = spacy.load('en_core_web_lg', disable=['tagger','ner', 'parser'])

def text_to_matrix(text):
        #word to vec by using spacy library and similarity function. 
        #similarity performed with GloVe which is "count-based" model
        #doc = nlp(text)
        matrix=[]
        for word in text:
                doc = nlp(word)
                for token in doc:
                        matrix.append(token.vector)
                #print matrix
        #oprint (matrix)
        return matrix

def clustering(word_list, n_clusters):
        token_matrix = text_to_matrix(word_list)
        kmeans = KMeans(n_clusters)
        kmeans.fit(token_matrix)
        clusters = collections.defaultdict(list)
        #centroids=kmeans.cluster_centers_
        for i, label in enumerate(kmeans.labels_):
                clusters[label].append(i)
        return dict(clusters)#,centroids

def compute_top_word(terms_in_cluster):
    #check if the list has just one element, if so return it without computing his similarity
    if len(terms_in_cluster)>1:
        text = ""
        for word in terms_in_cluster:
            print
            text=text+word+" "
        doc = nlp(text)
        word_list=[]
        for word1 in doc:
            for word2 in doc:
                if word1!=word2:
                    #we compute the similarity to get the most representative word of the dataset
                    word_list.append((word1.similarity(word2),word1.text, word2.text))
        #print(word_list)
        top=(max(word_list))
        return(top[1])
    else:
        return(terms_in_cluster[0])

def save_cluster_result(word,cluster):
    #print(word,cluster)
    with open('cluster_result_list.csv', 'a', newline='') as csv_out:
        writer = csv.writer(csv_out)
        writer.writerow((word,cluster)) 

def save_top_word(word,cluster):
    #print(word,cluster)
    with open('topword_result_list.csv', 'a', newline='') as csv_out:
        writer = csv.writer(csv_out)
        writer.writerow((word,cluster)) 
    pass
if __name__ == "__main__":
        word_list=[]
        with open(filename,'r') as csv_in:
            for d in csv_in:
                text=str(d)
                text=re.sub(r'\n', "" , text)
                word_list.append(text)
                
                #print (word_list)
            n_clusters= 1000
            #clusters,order_centroid = clustering(word_list, n_clusters)
            clusters = clustering(word_list, n_clusters)
            for cluster in range(n_clusters):
                print ("cluster ",cluster,":")
                terms_in_cluster=[]
                for i,word in enumerate(clusters[cluster]):
                    print ("word ",i,": ",word_list[word])
                    terms_in_cluster.append(word_list[word])
                    save_cluster_result(word_list[word],cluster)

                    #save csv with all the content
                top_word=compute_top_word(terms_in_cluster)
                print (top_word)
                save_top_word(top_word,cluster)
                #save csv with top words
            """   
            print("Top terms per cluster:")
            order_centroids = order_centroid.argsort()[:, ::-1]
            #print(order_centroids)

            print("Top terms")
            for i in range(n_clusters):
                print("Cluster %d:" % i),
                for ind in order_centroids[i, :1]:
                    print(' %s' % word_list[ind])
            """
               
