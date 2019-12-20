# -*- coding: utf-8 -*-

import json
import sys
import re
import random

### Calculate Jaccard Distance between tweets
def jaccard_distance(x,y):
    x = x.split(" ")
    y = y.split(" ")
    x_U_y = len(set(x).union(set(y)))
    x_I_y = len(set(x).intersection(set(y)))    
    d = 1 - (x_I_y/x_U_y)
    return d

### Calculate Error
def calculate_SSE(cluster):
    SSE = 0
    for id,tweets in cluster.items():
        for tweet in tweets:
            SSE_dist = jaccard_distance(id_tweet_dict[int(id)],id_tweet_dict[tweet])
            SSE = SSE + SSE_dist * SSE_dist 
    return SSE

### Pre-processing the text from the dataset
def preprocessText(s):
    s = s.split('|')[2].lower()
    s = " ".join(filter(lambda x:x[0]!='@', s.split()))
    s = s.replace("#", "")
    s = re.sub(r"http\S+", "", s)
    return s

### Pre-processing the ids from the dataset of various tweets
def preprocessId(s):
    return int(s.split('|', 1)[0])
    
### function to calculate the K_Means neighbors
def k_means(k, seed_list, id_tweet_dict, output):
    if k > len(seed_list):
        print("Number of clusters ", k ," is more than Numbers of Seeds",len(seed_list))
        return
    elif k < len(seed_list):
        print("Truncating seed list as k is less than number of seeds")
        seed_list = seed_list[0:k]
        

    cluster = {}
    
    for seed in seed_list:
        cluster[seed] = []
    
    #Creating Cluster by measuring each tweet with each seed and adding it in respective cluster
    for id,tweet in id_tweet_dict.items():
        min_dist = sys.maxsize
        min_seed = ''
        for seed in seed_list:
            dist = jaccard_distance(id_tweet_dict[int(seed)],tweet)
            if(dist < min_dist):
                min_dist = dist
                
                min_seed = seed
        cluster[min_seed].append(id)
        
    seed_list = []

    #Making new seed list from new clusters by taking mean
    for id,tweets in cluster.items():
        best_centroid_dist = 255
        best_centroid = ''
        for tweet in tweets:
            distance = 0
            for each_tweet in tweets:
                distance = distance + jaccard_distance(id_tweet_dict[int(tweet)],id_tweet_dict[int(each_tweet)])

            mean = distance/len(tweets)
            
            if(mean < best_centroid_dist):
                best_centroid_dist = distance
                best_centroid = tweet
        seed_list.append(best_centroid)    

    
    if output == str(cluster):
        print("Value of K: ",str(k))
        prevCount = 1
        count = 1
        file = open('./K_MEANS_OUTPUT.txt.','a+')
        file.write("Value of K: " + str(k) + '\n')
        file.write("SSE:" + str(calculate_SSE(cluster)) + '\n')
        print("SSE: ", str(calculate_SSE(cluster)))
        print("SEED_LIST: ", seed_list)
        i=1
        file.write("Size of each cluster" + '\n')
        for key,value in cluster.items():
            #file.write(str(i) + '     ' )
            for x in value:
                count += 1
                #file.write(str(x) +', ')
            #file.write('\n')
            file.write(str(i) + ' : ' + str(count - prevCount) + " tweets" + '\n')
            i+=1
            prevCount = count
        #file.write("SSE:" + str(calculate_SSE(cluster)))
        file.write('\n\n')
        file.close()
        return    
        
    output = str(cluster)
    k_means(k, seed_list,id_tweet_dict, output)
 


if __name__ == "__main__":
    nameOfDataset = sys.argv[1]
    startingValueOfK = int(sys.argv[2])
    finalValueOfK = int(sys.argv[3])
    rangeOfK = int(sys.argv[4])
    
    id_tweet_dict = {}
    
    #Fetching dataset and pre-processing it
    seed_list = []
    with open("./" + nameOfDataset, "r", encoding="utf8") as f: 
        for line in f:
            print("line ", line)
            text = preprocessText(line)
            id = preprocessId(line)
            seed_list.append(id)
            id_tweet_dict[id] = text
    
    #print("id_tweet_dict: ", id_tweet_dict)   
    for kValue in range(startingValueOfK, finalValueOfK, rangeOfK):
        k_means(kValue, random.choices(seed_list, k=kValue + 1), id_tweet_dict, output='')