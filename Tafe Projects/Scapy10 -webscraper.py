#Author: Lindsay Coudert
#Date: Thursday the 7th of November


import nltk
import urllib.request

response = urllib.request.urlopen('http://127.0.0.1/dvwa/cyber_dvva_2024/login.php')
html = response.read()
print(html)