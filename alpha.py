import requests
from bs4 import BeautifulSoup
import nltk

links=['https://en.wikipedia.org/wiki/']
tokenizer = nltk.RegexpTokenizer(r"\w+")

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

def bagofwords(file,linktext):
    file = file.split('\n')
    tokenized_paralist=[]
    for x in range(len(file)):
        if file[x]!=[]:
            para=file[x]
            para=tokenizer.tokenize(para)
            if para != []:
                tokenized_paralist.append(para)
    print(tokenized_paralist)



def topic_cp(flag):
    topic=input('Enter the topic: ')
    for link in links:
        link+=topic
        r = requests.get(link)
        soup = BeautifulSoup(r.content,features="html.parser")
        content = soup.get_text().split('.')
        for x in range(len(content)-1,-1,-1):
            if content[x]=='' or content[x].count(' ') < 4:
                content.pop(x)
        f = open('dragons.txt',encoding="utf8")
        file = f.read()
        bagofwords(file,content)

menu()
