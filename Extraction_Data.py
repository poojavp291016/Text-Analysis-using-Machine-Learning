#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import os


# In[2]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
# Read the input Excel file
df = pd.read_excel("C:\\Users\\pooja\\Downloads\\Input.xlsx")

# Function to extract article text from a URL
def extract_article_text(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find and extract the article title
        article_title = soup.find('title').text.strip()

        # Find and extract the article text
        article_text = ""
        article_body = soup.find('body')
        for paragraph in article_body.find_all('p'):
            article_text += paragraph.text.strip() + "\n"

        return article_title, article_text
    except Exception as e:
        print(f"Error occurred while extracting text from {url}: {e}")
        return None, None

# Create a directory to save the text files
if not os.path.exists("extracted_articles"):
    os.makedirs("extracted_articles")

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']

    # Extract article text
    article_title, article_text = extract_article_text(url)
    # Save the extracted text to a text file
    if article_title and article_text:
        filename = f"extracted_articles/{url_id}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(article_title + "\n\n")
            file.write(article_text)

print("Extraction complete. Text files saved in 'extracted_articles' directory.")


# In[ ]:




