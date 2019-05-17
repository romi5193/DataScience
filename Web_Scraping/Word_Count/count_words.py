'''
count how many times an author uses a word in a html book 
'''
import urllib2
test = raw_input("What word do you want to know the frequency of?...")
url=raw_input("What is the url of the html text?...")
responce= urllib2.urlopen(str(url))
html= responce.read()

known_word=0
list_of_words= html.split(' ')
#print(list_of_words)

for word in list_of_words:
    if word==str(test):
        known_word += 1
print(known_word)
#print("There are %d number of the word 'the' in the book", %d(the))