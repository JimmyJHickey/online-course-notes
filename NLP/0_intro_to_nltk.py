###
# Jimmy Hickey
# 2019-08-17
# Intro to nltk
####

from nltk.corpus import stopwords
import pandas as pd

# First 10 words of stop words
stopwords_10 = stopwords.words('english')[0:10]
# print(stopwords_10)

# Read as long string, i.e. assume no formatting/ tsv
raw_data = open("data/SMSSpamCollection.tsv").read()
# print(rawData[0:500])

# replace tabs with \n to split
parsed_data = raw_data.replace('\t', '\n').split('\n')
# print(parsed_data[0:5])

# Split out labels and text
label_list = parsed_data[0::2]
text_list = parsed_data[1::2]

# print(label_list[0:5])
# print(text_list[0:5])

# remove extra element from label_list
del label_list[-1]

# Make pandas dataframe
fullCorpus = pd.DataFrame({
        'label': label_list,
        'body_list': text_list
    })

print(fullCorpus.head())


# Try reading in as tsv
data_tsv = pd.read_csv("data/SMSSpamCollection.tsv", sep='\t', header = None)
print(data_tsv.head())
