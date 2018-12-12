import json
import sys
import re
import time
import spacy
import collections
import numpy as np
from math import sqrt
from sklearn.cluster import KMeans
from spacy.lang.en import English

nlp = spacy.load('en_core_web_lg', disable=['tagger','ner', 'parser'])
nlp.add_pipe(nlp.create_pipe('sentencizer'))

filename_in = sys.argv[-1]
start_time = time.time()

def text_to_matrix(text):
	#word to vec by using spacy library and similarity function. 
	#similarity performed with GloVe which is "count-based" model
	doc = nlp(text)
	matrix=[]
	counter=0
	tok=None
	for token in doc:
		tok=token.vector
		#print(token.vector)
		counter+=1
		token_result =[]
		""" #how to get the similarity score between two values, not necessary during this phase
			for token2 in tokens:
			similarity=token1.similarity(token2)
			token_result.append(similarity)"""
		matrix.append(tok)
	#print matrix
	return matrix, counter

def clustering(matrix_comment, k):
    #create k means object and pass to it the number of clusters
	kmeans = KMeans(k,n_jobs=4)
	#pass the matrix to the fit method of kmeans to compute k-means clustering.
	kmeans.fit(matrix_comment)
	#y_kmeans = kmeans.predict(matrix_comment)
	#print "labels:", 
	kmeans.labels_
	clusters = collections.defaultdict(list)
	for i, label in enumerate(kmeans.labels_):
		clusters[label].append(i)
	
	centers = kmeans.cluster_centers_
	labels=kmeans.labels_	
	return dict(clusters),labels,centers

filename=re.sub(r'/Users/fatbardha/Desktop/text_process/text_compared/', "" , filename_in)
print("~> Clustering", filename)
obj={}
final_data=[]
with open(filename_in) as json_data:
	data = json.load(json_data)
	for d in data:
		image_id = d['id']
		comments = d['comments']
		print ("-------------------------------------------------------")
		print (image_id)
		print (comments)
		#print(comments)
		matrix_comment,len_comm=text_to_matrix(comments)
		k=int(sqrt(len_comm/2))
		if k>4:
			clusters, labels, centers=clustering(matrix_comment,k)
			for cluster in range(k):
				print("cluster: ", cluster)
				for i,sent in enumerate(clusters[cluster]):
					text=None
					counter=0
					for word in comments.split():
						text=word
						if (counter==sent):
							print("word", sent, ": ", text)
						counter+=1
			
			#comment word near to the centroid
			#order_centroids=centers.argsort()[:, ::-1]
			order_centroids=centers.argsort()[:, ::-1]
			keyword_list=[]
			for cluster in range(k):
				#print ("cluster: ", cluster)
				#5 most common word
				for ind in order_centroids[cluster, :5]:
					#print ("ind,",ind)
					text_comm=None
					counter=0
					for word in comments.split():
						#print("counter",counter, "word",word)
						text_comm=word
						if (counter==ind):
							#print ("ind: ",ind,"word: ", text_comm)
							if text_comm not in keyword_list:
								keyword_list.append(text_comm)
						counter+=1	
			
			d['keyword']=keyword_list
			print("keyword list ", keyword_list)
			
		else:
			print("Not enogth comments to cluster, k<4")
			d['keyword']=[""]
			#clustering

#Encode JSON data
with open('/Users/fatbardha/Desktop/'+ filename, 'w') as f:
	json.dump(data, f, indent=4)


end_time = time.time()
difference_time = end_time - start_time
print("~> Clustered", filename, "in: ", difference_time)


