import requests
from bs4 import BeautifulSoup
import nltk
import os

links=['https://en.wikipedia.org/wiki/']
tokenizer = nltk.RegexpTokenizer(r"\w+")

def tokenizeText(paralist):
    '''Converts list of paragraphs/texts into list of tokenized paragraphs'''
    
    tokenized_text = list()
    for x in range(len(paralist)):
        if paralist[x]!=[]:
            para=paralist[x]
            para=tokenizer.tokenize(para)
            if para != []:
                tokenized_text.append(para)
    return tokenized_text

def menu():
    print('WELCOME TO PLAGIARISM DETECTOR\nChoose from the following options:')
    print('1.Topic (More lenient, only checks particular websites for C&P)')
    print('2.File (Submit a file to check for C&P as well as Disguised Plagiarism)')
    type=input()
    flag=input('Do you want a detailed analysis? (Enter Y/n): ')
    if type == '1' :
        topic_cp(flag)
    elif type == '2':
        pass

def topic_cp(flag):
    ''' Checks for copy&paste type of plagiarism for the given document
        by comparing with texts/data from the given sources/links''' 

    topic=input('Enter the topic: ')
    for link in links:
        link+=topic
        r = requests.get(link)
        soup = BeautifulSoup(r.content,features="html.parser")

        link_text = list()

        for para in soup.find_all('p'):
             link_text.append(para.get_text())

        for x in range(len(link_text)-1,-1,-1):
            if link_text[x] == '\n':
                link_text.pop(x)

        tokenized_source = tokenizeText(link_text)

        filename = input('Enter absolute path of local file to be checked')

        if os.path.isfile(filename):
            f = open(filename,encoding="utf8")
            file = f.read()
            file = file.split('\n')
            tokenized_file = tokenizeText(file)

            bagofwords(tokenized_file,tokenized_source)
        else:
            print('File not found.')

def bagofwords(file,source):
    pass

if __name__ == '__main__':
    menu()


'''
for key in dict.keys():

    if key in 2nd dict keys():
        negative score=|dict[key]-dict2[key]|

'''
