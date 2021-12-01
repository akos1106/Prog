import csv
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


# def remove_tag(s,tag):                #egy karakterre
#     idx=s.find(tag)
#     while idx!=-1:
#         s=s[:idx]+s[idx+1:]
#         idx=s.find(tag)
#     return s
import string


def remove_tags(s,tags_to_remove):      #tobb karakterre is
    for tag in tags_to_remove:
        idx=s.find(tag)
        while idx!=-1:
            s=s[:idx]+s[idx+len(tag):]
            idx=s.find(tag)
    return s


def remove_punctuations(s):
    new_s=""
    for c in s:
        if c not in string.punctuation:
            new_s+=c
    return new_s


def count_words_and_letters(message):
    word_list=[]
    letter_count=0
    tmp=message.split(' ')
    for word in tmp:
        if word!="":
            word_list.append(word)
            letter_count+=len(word)
    return (word_list,len(word_list),letter_count)

def calc_bow(twitter_count):
    new_bow=[]
    for tweet in twitter_count:
        word_list,_,_=tweet
        for word in word_list:
            new_bow.append(word)
    return new_bow


def remove_stopwords(all_words):
    new_all_words= []
    all_stop_words=stopwords.words('english')
    for word in all_words:
        if word not in all_stop_words:
            new_all_words.append(word)
    return new_all_words

#3.f
def plot_top_n_words(all_words,n):
    word_count={}
    for word in all_words:
        if not word in word_count:
            word_count[word]=1
        else:
            word_count[word]+=1

    word_count=sorted(word_count.items(),key=lambda x: x[1],reverse=True)

    top_words=word_count[:n]
    top_words=top_words[::-1]

    x_lista=[]
    for tuple in top_words:
        x_lista.append(tuple[0])

    y_lista=[]
    for tuple in top_words:
        y_lista.append(tuple[1])


    # plt.barh(x_lista,y_lista)
    # plt.show()

    return top_words

def plot_word_distribution(top_words,all_words):

    word_list = [word_tuple[0] for word_tuple in top_words]

    count=0
    for selected_word in word_list:
        distibution_list=[]

        for word in all_words:
            if word==selected_word:
                distibution_list.append(count+1)
            else:
                distibution_list.append(0)
        count+=2
        plt.scatter(range(len(distibution_list)),distibution_list,marker='|')
        plt.ylim(0.1,count)       #y tengelyen mettől meddig

    plt.show()

def plot_word_sentiment(all_words):
    sia=SentimentIntensityAnalyzer()

    # egyben=""
    # for s in all_words:
    #     egyben+=s+" "

    text=" ".join(all_words)
    scores=sia.polarity_scores(text)
    print(scores)


    scores_list=list(scores.values())
    scores_list=scores_list[:-1]

    label_list=list(scores.keys())
    label_list=label_list[:-1]

    plt.pie(scores_list,labels=label_list,shadow=True,startangle=90,colors=['red','gray','green'])
    plt.title("SIA")
    plt.show()



####################################################################################
#MAIN

csv_file = csv.reader(open("TrumpTweets.csv","r",encoding='utf-8') , delimiter=";")

tags_to_remove=["http","pic.","#","@","…","–","’","”","“","\xa0"]

twitterMessages=[]
twitter_counts=[]

for line in csv_file:
    tmp=line[4].lower()
    tmp=remove_tags(tmp,tags_to_remove)
    tmp=remove_punctuations(tmp)
    twitterMessages.append(tmp)
    twitter_counts.append((count_words_and_letters(tmp)))

bow=calc_bow(twitter_counts)


unique_words=len(set(bow))
all_words=len(bow)
print("ratio=",unique_words/all_words)


# print(stopwords.words('english'))
bow=remove_stopwords(bow)
unique_words=len(set(bow))
all_words=len(bow)
print("ratio=",unique_words/all_words)


top_words=plot_top_n_words(bow,5)
plot_word_distribution(top_words,bow)

plot_word_sentiment(bow)


