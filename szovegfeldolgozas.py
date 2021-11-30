import csv

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
print(bow)

unique_words=len(set(bow))
all_words=len(bow)
print("ratio=",unique_words/all_words)


