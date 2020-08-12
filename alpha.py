import requests
from bs4 import BeautifulSoup
import nltk
import os
from file_selection import fileSelector

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

        print('\n1. Enter file path')
        print('2. Browse file')

        selection = int(input('\nChoose option to upload file: '))

        filename = ""

        if selection == 1:
            filename = input('Enter absolute path of local file to be checked')
        elif selection == 2:
            filename = fileSelector()

        if os.path.isfile(filename):
            f = open(filename,encoding="utf8")
            file = f.read()
            file = file.split('\n')
            tokenized_file = tokenizeText(file)

            print(bag_of_words(tokenized_file,tokenized_source))
        else:
            print('File not found.')

def bag_of_words(file,source):

    #Creating lists to store count of words for each paragraph
    dict_file = list()
    dict_source = list()

    for para in file:
        dict_file.append({word: para.count(word) for word in set(para)})
    
    for para in source:
        dict_source.append({word: para.count(word) for word in set(para)})

    score_list = list()

    for p1_dict in dict_file:
        max_score = 0
        for p2_dict in dict_source:
            total_words = sum(p2_dict.values())
            words_matched = 0

            for word in p1_dict.keys():
                if word in p2_dict.keys():
                    words_matched = words_matched+p1_dict[word] if p1_dict[word] <= p2_dict[word] else words_matched+p2_dict[word] 
            
            score = words_matched/total_words

            if score > max_score:
                max_score = words_matched/total_words
        score_list.append(max_score)

    plagiarism_score = (sum(score_list)/len(score_list)) * 100
    #Deleted some text from the last paragraph of dragons.txt to check for change in plagiarsim score
    
    return round(plagiarism_score,3)


if __name__ == '__main__':
    menu()