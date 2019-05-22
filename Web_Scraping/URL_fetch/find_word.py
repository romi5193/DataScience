import urllib3
test = raw_input("What word do you want to know the frequency of?...")
#url=raw_input("What is the url of the html text?...")
instance=urllib3.PoolManager()
responce=instance.request('GET', 'http://www.gutenberg.org/files/135/135-h/135-h.htm')
html=str(responce.data)

known_word=0
list_of_words= html.split(' ')
#print(list_of_words)

for word in list_of_words:
    if word==str(test):
        known_word += 1
print('The word %s occurs %d times' %(test, known_word))
#print(known_word)