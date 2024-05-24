#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from textstat import flesch_reading_ease, flesch_kincaid_grade

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('cmudict')

# Load stop words
stop_words = set(stopwords.words('english'))

# Function to clean text
def clean_text(text):
    tokens = word_tokenize(text)
    cleaned_tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]
    return cleaned_tokens

# Function to count syllables in a word
def syllable_count(word):
    d = nltk.corpus.cmudict.dict()
    if word.lower() in d:
        return max([len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]])
    else:
        # Simple fallback for words not found in CMU Pronouncing Dictionary
        return max(1, len(word) // 3)

# Function to calculate sentiment scores
def calculate_sentiment_scores(tokens, positive_words, negative_words):
    positive_score = sum(1 for word in tokens if word in positive_words)
    negative_score = sum(1 for word in tokens if word in negative_words)
    polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(tokens) + 0.000001)
    return positive_score, negative_score, polarity_score, subjectivity_score

# Load positive and negative words
positive_words_file = "C:\\Users\\pooja\\Downloads\\positive-words.txt"
negative_words_file = "C:\\Users\\pooja\\Downloads\\negative-words.txt"

positive_words = set()
negative_words = set()

# Read positive words from file
with open(positive_words_file, 'r') as file:
    for line in file:
        word = line.strip()
        positive_words.add(word)

# Read negative words from file
with open(negative_words_file, 'r') as file:
    for line in file:
        word = line.strip()
        negative_words.add(word)

# Replace "extracted_articles" with the path to your directory containing extracted articles
directory_path = "C:\\Users\\pooja\\Downloads\\extracted_articles"

# Process each text file
for filename in os.listdir(directory_path):
    with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as file:
        text = file.read()
        cleaned_tokens = clean_text(text)
        positive_score, negative_score, polarity_score, subjectivity_score = calculate_sentiment_scores(cleaned_tokens, positive_words, negative_words)
        
        # Additional features
        sentences = sent_tokenize(text)
        word_count = len(cleaned_tokens)
        avg_sentence_length = word_count / len(sentences)
        complex_word_count = sum(1 for word in cleaned_tokens if len(word) > 2)  # Considering words with more than 2 characters as complex
        percentage_complex_words = (complex_word_count / word_count) * 100
        
        # Calculate FOG Index
        fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
        
        print(f"File: {filename}")
        print(f"Average Sentence Length: {avg_sentence_length}")
        print(f"FOG Index: {fog_index}")
        print(f"Word Count: {word_count}")
        print("------------------")


# In[2]:


import os
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('cmudict')

# Load stop words
stop_words = set(stopwords.words('english'))

# Function to clean text
def clean_text(text):
    tokens = word_tokenize(text)
    cleaned_tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]
    return cleaned_tokens

# Function to count syllables in a word
def syllable_count(word):
    d = nltk.corpus.cmudict.dict()
    if word.lower() in d:
        return max([len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]])
    else:
        # Simple fallback for words not found in CMU Pronouncing Dictionary
        return max(1, len(word) // 3)

# Replace "extracted_articles" with the path to your directory containing extracted articles
directory_path = "C:\\Users\\pooja\\Downloads\\extracted_articles"

# Process each text file
for filename in os.listdir(directory_path):
    with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as file:
        text = file.read()
        cleaned_tokens = clean_text(text)
        
        # Additional features
        sentences = sent_tokenize(text)
        word_count = len(cleaned_tokens)
        avg_sentence_length = word_count / len(sentences)
        complex_word_count = sum(1 for word in cleaned_tokens if len(word) > 2)  # Considering words with more than 2 characters as complex
        percentage_complex_words = (complex_word_count / word_count) * 100
        
        print(f"File: {filename}")
        print(f"Percentage of Complex Words: {percentage_complex_words}")
        print(f"Avg Number of Words per Sentence: {avg_sentence_length}")
        print(f"Complex Word Count: {complex_word_count}")
        print("------------------")


# In[ ]:




