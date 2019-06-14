#This script finds the number of times an author uses a word in an html book

import urllib3
target_word = input(str("What word do you want to know the frequency of?..."))
url=input(str("What is the url of the html text?..."))

instance = urllib3.PoolManager()
responce = instance.request('GET', url)
html = str(responce.data)

known_word = 0
list_of_words = html.split(' ')
for word in list_of_words:
    if word == str(target_word):
        known_word += 1
print('The word %s occurs %d times' %(target_word, known_word))
