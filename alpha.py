import requests
from bs4 import BeautifulSoup
import nltk

links=['https://en.wikipedia.org/wiki/']
tokenizer = nltk.RegexpTokenizer(r"\w+")

def tokenizeText(paralist):
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

def bagofwords(file,source):
    print(file[:2],'\n\n',source[:3])

def topic_cp(flag):
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
        print(tokenized_source[:2])
        f = open('dragons.txt',encoding="utf8")
        file = f.read()
        file = file.split('\n')
        tokenized_file = tokenizeText(file)
        bagofwords(tokenized_file,tokenized_source)

menu()
