""""
Name of Script: Webscraper
Author: Lindsay Coudert
Date: Friday 23rd August 2024.
"""
import nltk
from bs4 import BeautifulSoup
import urllib.request
from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt

response = urllib.request.urlopen('http://192.168.52.146/tafe_cyber/public/staff/index.php')
#response = urllib.request.urlopen('http://192.168.52.146/tafe_cyber/public/language.php')

html = response.read()
soup = BeautifulSoup(html, "html5lib")
text = soup.get_text(strip=True)

print(text)


tokens = [t for t in text.split()]
tokens = [token.lower() for token in tokens]

print (tokens)

freq = nltk.FreqDist(tokens)

df = pd.DataFrame.from_dict(freq, orient='index')
df = df.rename(columns={0:'freq'})
result = df.sort_values(['freq'], ascending=False)

result.head(10)

plt.figure(figsize=(15,8))
freq.plot(20, cumulative=False)
plt.show()

clean_tokens = tokens.copy()
clean_tokens = [token.lower() for token in clean_tokens]

for token in tokens:
    if token in stopwords.words('is'):
        clean_tokens.remove(token)

clean_freq = nltk.FreqDist(clean_tokens)

clean_df = pd.DataFrame.from_dict(clean_freq, orient='index')
clean_df = clean_df.rename(columns={0:'freq'})
clean_result = clean_df.sort_values(['freq'], ascending=False)

clean_result.head(10)

plt.figure(figsize=(15,8))
clean_freq.plot(20, cumulative=False)
plt.show()
