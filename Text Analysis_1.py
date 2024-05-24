#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import string


# In[2]:


nltk.download('punkt')
nltk.download('stopwords')


# In[3]:


stop_words = set(stopwords.words('english'))


# In[4]:


# Define paths to your positive and negative word files
positive_words_file = "C:\\Users\\pooja\\Downloads\\positive-words.txt"
negative_words_file = "C:\\Users\\pooja\\Downloads\\negative-words.txt"

# Initialize dictionaries to store positive and negative words
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


# In[7]:


import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Load stop words
stop_words = set(stopwords.words('english'))

# Function to clean text
def clean_text(text):
    tokens = word_tokenize(text)
    cleaned_tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]
    return cleaned_tokens

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
        print(f"File: {filename}")
        print(f"Positive Score: {positive_score}")
        print(f"Negative Score: {negative_score}")
        print(f"Polarity Score: {polarity_score}")
        print(f"Subjectivity Score: {subjectivity_score}")
        print("------------------------------------------------------")


# In[ ]:




