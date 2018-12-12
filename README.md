# Virality+

## 1) Preprocessing
Comments and Captions are enhanced by removing digits, punctuation, lemmatization, stop words,...

-> be aware to check the correct path of the file in input and output.

#### 1_clean_caption.py -> clean all the caption generated during through NeuralTalk.

Execution:
	
```
python3 1_clean_caption.py filename.json
```

Output: .json file saved under the folder path: /caption_cleaned/

#### 1_clean_comment.py -> cleans all the comment that are present in .json file crawled from Google+.

Execution:

```
python3 1_clean_comment.py filename.json
```

Output: .json file saved under the folder path: /comment_cleaned/

## 2) Compare 
For every post/image, check if there is an overlap between comments and captions

Execution:
	
```
python3 2_compare.py caption_filename.json comment_filename.json
```
```
for file in /text_process/comment_cleaned/*; do
    name=${file##*/}
    if [[ -f /text_process/caption_cleaned/$name ]]; then
        echo "$name exists in both directories"
        python3 2_compare.py /text_process/comment_cleaned/$name /text_process/caption_cleaned/$name
    fi
done
```
Ooutput: .json file saved under the folder path: /text_compared/

## 3) Clustering
For every post, cluster all the comments and get the most significant words: top 5 words for every cluster k, where k=(sqrt(length_comment/2))

Execution:
	
```
python3 3_clustering.py /text_compared/filename.json
```

Ooutput: .json file saved under the folder path: /text_clustered/

## 4) Dictionary
Collect all the worda clustered in the previous step, create a list of them and save in a all_word.csv file.
Cluster again all the words in the all_word.csv in order to have just the 1000 most significative words.

Execution:
```
for f in /text_clustered/*.json; 
do
  python3 4_dictionary.py "$f"
done

```
Output: .csv file containing all the words

## 5) Evaluation
For every post all the values of virality score, number of likes, reshares, comments.

Execution:
```
for f in /text_clustered/*.json; 
do
  python3 5_virscore.py "$f"
done

```
Output: .csv file containing all the values
