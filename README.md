# A Textual Analysis of Agatha Christie Novel's as Proof of Cognitive Decline

[Data Visualization](https://dylan-mack.herokuapp.com/)


Agatha Christie (1890 - 1976) was an English writer known as the best-selling fiction writer of all time, having sold more than 
two billion copies of her detective mystery novels.

Towards the end of her life, Christie's health began to decline which can be seen in some of her poorly received later works. Some
critics referred to "Elephants Can Remember" as one of her 'execrable last novels', in which Christie "loses her grip altogether". 
Computer analysis of Christie's writing has reveal that she might have developed a form of dementia, possibly Alzheimer's disease, at this time.

 
I conducted a textual analysis on Agatha Christie's novels to further determine if her writing style changed in any significant way during 
her active writing years (1920 - 1975) which may be indicative of cognitive decline. 
 
 
All 67 of Christie's novels written under her name were compiled as pdf documents and converted to text documents. 
Word and sentence tokenization through python's Natural Language Toolkit (NLTK) library was used to create json files representing 
word and sentence tokenized versions of each book. 

Concordances were created of each book, containing each unique word occurrence written and the number of times it appears. 
NLTK part of speech (POS) tagging was also used to create tagged concordance dictionaries, which match each unique word occurence to its POS. 
Tagged concordance dictionaries were then used to make unique word concordances without stop words and proper noun (NNP) concordances. 

**The following Features were created:**

Average POS per sentence

Ordered Concordance 

Stop word free Concordance

NNP Concordance 

Average Word Length

Average Sentence Length (by characters and words)

Total Number of Pronouns

Number of Unique Words Used

Number of Unique Stop words Used

Number of Unique NNPs used 

Frequency of Words


# Probabilistic Validation


The Null Hypothesis is that data on Agatha Christie novels published after 1960 follow the same writing patterns as novels published before 1960. 
Three probability measures are used to substantiate the claims on the data: T Test, Z Score, and the use of Chebyshev's Inequality


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $Pr(\left|X-\mu  \right|\geq k\sigma )\leq \frac{1}{k^{2}}$


Observations on frequency of indefinite pronouns and unique vocabularly in Agatha Christie novels are taken to be independent observations. 
This is because general writing style is involved in the overall null hypothesis and the occurence of word frequency and unique 
vocabularly do not impact  the probability of occurence in another book past the influence writing style.

The primary sample is taken to be Agatha Christie novels *written* after 1960 with a sample size of 14, and random variable X that takes 
on continuous values [0,100], representing the % of total words in a novel that satisfy the metric.


Average p-value for all metrics over 100 random samples are between .48 to .52, while p-values for all metrics are between .0002 to .0257
and Z-scores for all metrics are between 2.6 to 5.1 .

Chebyshev inequality bounds the likelihood of selecting the maximum value from the data set between 5% to 15% for all metrics. 









