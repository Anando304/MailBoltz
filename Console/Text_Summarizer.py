## @file Text_Summarizer.py
 # @author Anando Zaman
 # @brief Summarizes text and outputs N-best results
 # @date May 16, 2020
 # @details Extractive NLP text summarization

'''
libraries
pip install lxml
pip install beautifulsoup4
pip install nltk

The idea:
- Import data from a data source.
- Format the data to remove brackets and extra spaces and SAVE it TO the SAME VARIABLE.
- Format the data once more but now remove the numbers and punctuation. SAVE this TO a NEW VARIABLE.
- This new variable will be used to determine the frequency of the words later. This frequency will be a 'score'.
- The other older variable(first variable) will be used for calculating the scores for each sentence by adding
  the weighted frequencies of the words that occur in that particular sentence. This way, we can re-create
  the sentences based on relative score for a summary!
  
 - So basically, find the words in each sentence that occurred in the vocab/word_freq. The vocab/word_freq
   is the variable with our vocab and the relative weighting of each word. We sum the weights for the words
   found in each sentence that match the corresponding word in the vocab/word_freq. We then display the top n-sentences
   with the highest scores.
'''

import nltk
import re
from collections import Counter
# For extracting n-largest elements from a dictionary.
import heapq


''' @brief Method used for text summarization
 @details Extractive algorithm to summarize text and display N-best results
 @return Returns a string
'''
def summarizer(article_text,N):

    '''Pre-processing'''
    # String pre-processing
    # Removing Square Brackets and Extra Spaces
    # Don't remove punctuation here as this
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)

    # formatted_article_text for word-tokenization later. This is so that we can find the word freq/distribution
    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)


    '''Tokenization/Vocab'''
    # Tokenize the article_text sentences
    sentence_list = nltk.sent_tokenize(article_text)

    # Creating our Vocabulary AND frequency of each words in it
    # Tokenize the formatted_article_text for words.
    vocab = nltk.word_tokenize(formatted_article_text)
    # Find the number of occurences of each word
    word_freq = Counter(vocab)
    # Divide all by the max value to get weighted frequency score!
    max_freq = max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq
    #print(word_freq)


    '''Sentence Scoring'''
    # Will contain each sentence and its score
    sentence_scores = {}

    # Compute the score by summing each word score via word_freq. word_freq is the weighted freq score!
    for sentence in sentence_list:
        # To avoid very lengthy sentences
        if len(sentence.split(' ')) < 34:
            for word in nltk.word_tokenize(sentence):
                if word in word_freq.keys():
                    # if exists, then add to score
                    if sentence in sentence_scores.keys():
                        sentence_scores[sentence] += word_freq[word]
                    # Otherwise, create new key with word-score val
                    else:
                        sentence_scores[sentence] = word_freq[word]



    '''Create Summary'''
    # Create a summary
    summary_sentences = heapq.nlargest(N, sentence_scores, key=sentence_scores.get)
    summary = '\n'.join(summary_sentences)
    return summary