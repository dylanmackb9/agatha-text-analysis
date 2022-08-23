
from main import *


# CREATING FREQ CSV

header = ["Title", "Publish Year", "Frequency1", "Frequency2", "Frequency3", "Frequency4" "Word1", "Word2", "Word3", "Word4"]
wordtest1 = "something"
wordtest2 = "someone"
wordtest3 = "anything"
wordtest4 = "they"
frequency1 = np.divide(frequencyFinder(wordtest1, concordance), total_words) * 100
frequency2 = np.divide(frequencyFinder(wordtest2, concordance), total_words) * 100
frequency3 = np.divide(frequencyFinder(wordtest3, concordance), total_words) * 100
frequency4 = np.divide(frequencyFinder(wordtest4, concordance), total_words) * 100

final = [header]

for i, book in enumerate(labels):
  temp = [labels[i][:-6], years[i], frequency1[i], frequency2[i], frequency3[i], frequency4[i], wordtest1, wordtest2, wordtest3, wordtest4]
  final.append(temp)


with open(os.path.expanduser('~/Dev/gitreps/AgathaWeb-DViz/services/data/')+"freq.csv", 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(final)


# CREATING UNIQUE WORD CSV

header = ["Title", "Publish Year", "Unique Words", "Total Words", "Percent Unique"]

final = [header]

for i, book in enumerate(labels):
  temp = [labels[i][:-6], years[i], unique_words[i], total_words[i], np.divide(unique_words, total_words)[i] * 100]
  final.append(temp)


with open(os.path.expanduser('~/Dev/gitreps/AgathaWeb-DViz/services/data/') + "unique.csv", 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(final)