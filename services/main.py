import numpy as np
import matplotlib.pyplot as plt
import string
import os
import json
import csv

import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag

from scipy import stats



from features import *
from services import *


nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# labels: list[strings]
# words: list[list[strings]]
# sentences: list[list[strings]]


number_of_books = len(labels)
years = createYears(labels)  # list[strings]
mystops = set(stopwords.words("english"))  # Stop words 
pronouns = ["I", "he", "him", "his", "she", "her", "hers", "it"]
pos = ['JJ', 'JJR', "JJS", 'RB', 'RBR', 'RBS']


concordance = createConcordance(labels, words)  # list[dictionaries{string Word; int occurances}]
nostop_concordance = concordanceNoStops(concordance, mystops)

unique_words, total_words = uniqueWords(number_of_books, labels, concordance, words)  # int,int

total_stops = totalNumStop(number_of_books, mystops, words)
total_unique_stops = totalUniqueStop(number_of_books, mystops, concordance)

avg_sentence_len_c, avg_sentence_len_w = sentenceLength(number_of_books, sentences)
avg_word_length = np.divide(avg_sentence_len_c, avg_sentence_len_w)

num_pronouns = numPronoun(number_of_books, pronouns, concordance)


# PART OF SPEECH FEATURES
tagdicts = postagDict(concordance)  # list of dictionaries with all words and their tags
avgpos_sentence = avgposPerSentence(number_of_books, concordance, pos, sentences, tagdicts)


nnp_concordance = concordanceNNP(nostop_concordance, mystops) # concordance of nnps
#total_nnps = totalNNP(number_of_books, nnp_concordance, words)
total_unique_nnps = totalUniqueNNP(number_of_books, nnp_concordance)


# AVG NUM VERBS PER SENTENCE

plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(years, avgpos_sentence)
plt.title("Average number of verbs per sentence used in Agatha Christie Novels 1920-1973")
plt.show()


# ORDERED CONCORDANCE

# concordance is now ordered 

#print(concordance[0])

for conc in concordance:
  print(max(conc, key=conc.get))



# STOP WORD REMOVED CONCORDANCE


print(total_stops)


plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(years, np.divide(total_stops, total_words))
plt.title("Total Number of 'Stopwords' used in Agatha Christie Novels 1920-1973")
plt.show()


# PROPER NOUN CONCORDANCE

print(total_nnps)

plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(years, np.divide(total_nnps, total_words))
plt.title("Total Number of 'Proper Nouns' used in Agatha Christie Novels 1920-1973")
plt.show()


# AVERAGE WORD LENGTH

plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(years, avg_word_length)
plt.title("Average Word Length in Agatha Christie Novels 1920-1973")

plt.show()



# AVERAGE SENTENCE LENGTH
print(avg_sentence_len_c)
print(avg_sentence_len_w)

plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(years, avg_sentence_len_c)
plt.title("Average Sentence Length in Agatha Christie Novels 1920-1973")
plt.show()




# TOTAL NUMBER OF PRONOUNS USED IN EACH BOOK

plt.figure(figsize=(8, 6), dpi=80)
#plt.scatter(years, num_pronouns+total_nnps)
plt.scatter(years, np.divide(total_nnps, num_pronouns) / total_words)
plt.title("Total Number of Pronouns Used in Agatha Christie Novels 1920-1973")
plt.show()



# NUMBER OF UNIQUE/TOTAL WORDS IN EACH BOOK


print(unique_words)
print(total_words)
print(years)
print(labels)

plt.figure(figsize=(8, 6), dpi=80)
#plt.scatter(years, unique_words)
plt.scatter(years, unique_words / total_words)
plt.title("Number of Unique Words Used in Agatha Christie Novels 1920-1973")
plt.show()


# TOTAL NUMBER OF UNIQUE STOP WORDS USED

plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(years, np.divide(total_unique_stops, total_words))
plt.title("Total Number of Unique 'Stopwords' used in Agatha Christie Novels 1920-1973")
plt.show()



# TOTAL NUMBER OF UNIQUE NNP USED

plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(years, np.divide(total_unique_nnps, total_words))
plt.title("Total Number of Unique Proper Nouns used in Agatha Christie Novels 1920-1973")
plt.show()




# FREQUENCY OF INDEFINITE WORD 

wordtest1 = "someone"
wordtest2 = "anything"
wordtest3 = "something"
wordtest4 = "they"
frequency1 = frequencyFinder(wordtest1, concordance)
frequency2 = frequencyFinder(wordtest2, concordance)
frequency3 = frequencyFinder(wordtest3, concordance)
frequency4 = frequencyFinder(wordtest4, concordance)
# print(frequency1)
# print(book_names)
# print(years)
print(((frequency2 / total_words)*100)[-1])

plt.figure(figsize=(8, 6), dpi=80)
plt.scatter(years, np.divide(frequency2, total_words)*100)
#plt.scatter(years, frequency2)
#plt.scatter(years, frequency3)
plt.title("Frequency of word '"+wordtest1+"' in Agatha Christie novels published 1920-1973")
plt.show()









