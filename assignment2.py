import string
from thefuzz import fuzz
import random
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

def organize_function():
    """
    This function cleans the original sms dataset and divide all the messages into two lists based on their class/category (spam list and ham list)
    """
    f = open('sms_data.txt') 
    spam_list=[]
    ham_list=[]
    for line in f:
        word = line.strip().lower()
        if "spam" in word:
            spam_list.append(word[5:])
        else:
            ham_list.append(word[5:])
    return spam_list,ham_list

def create_dict(list):
    """
    This function turns the list to a dictionary: the keys are words that appear in the list and the values are the frequencies of the words in the list.
    """
    hist = {}

    strippables = string.punctuation + string.whitespace

    for line in list:
        for word in line.split():
            word = word.strip(strippables)
            hist[word] = hist.get(word, 0) + 1
    return hist

def most_common(hist,num):
    """
    This function prints the keys and the corresponding values in a dictionary with x number of words with highest frequencies.
    """
    t=list()
    hist=dict(hist)
    for key, values in hist.items():
        t.append((values,key))
    t.sort(reverse=True)
    for values, key in t[0:num]:
        print(key,values)
    return

def words_in_spam_only(hist1, hist2,num):
    """
    This function produces the x number of words that appear most in hist1(dictionary1), but do not appear in hist2(dictionary2)
    """
    t=list()
    hist1=dict(hist1)
    hist2=dict(hist2)
    for key in hist1:
        if key not in hist2:
            t.append((hist1[key],key))
    t.sort(reverse=True)
    for values, key in t[0:num]:
        print(key,values)
    return

def sensitivity_analysis(text):
    text=str(text)
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    return score

def text_similarity(text1,number):
    """
    This function randomly chooses two strings in the list and compares the similarity between them.
    """
    value=0
    for i in range(number):
        value+=fuzz.token_sort_ratio(text1[random.randint(0,len(text1)-1)],text1[random.randint(0,len(text1)-1)])
    return value/number

def text_similarities(text1,text2,number):
    """
    This function randomly chooses one string from each list and compares the similarity between the two selected strings.
    """
    value=0
    for i in range(number):
        value+=fuzz.token_sort_ratio(text1[random.randint(0,len(text1)-1)],text2[random.randint(0,len(text2)-1)])
    return value/number

def main():
    spam_list,ham_list=organize_function() # create two lists: spam_list and ham_list
    spam_dict=create_dict(spam_list) # create one dictionary: spam_dict
    ham_dict=create_dict(ham_list) # create one dictionary: ham_list
    print(f'The number of spam messages is {len(spam_list)}.') 
    print(f'The number of ham messages is {len(ham_list)}.')
    print(f'The number of different words used in spam messages is {len(spam_dict)}.') 
    print(f'The number of different words used in ham messages is {len(ham_dict)}.')
    print(f'The top 20 words with highest frequency in spam messages are:')
    most_common(spam_dict,20)
    print(f'The top 20 words with highest frequency in ham messages are:')
    most_common(ham_dict,20)
    print(f'The top 20 most frequent words that are in spam messages, but not in ham messages are:')
    words_in_spam_only(spam_dict,ham_dict,20)
    print(f'The top 20 most frequent words that are in ham messages, but not in spam messages are:')
    words_in_spam_only(ham_dict,spam_dict,20)
    print(f'The text similarity within the strings of the spam list is {text_similarity(spam_list,10000)}.')
    print(f'The text similarity within the strings of the ham list is {text_similarity(ham_list,10000)}.')
    print(f'The text similarity between the strings of the spam list and the strings of the ham list is {text_similarities(ham_list,spam_list,10000)}.') 
    print('The sensitivity analysis for spam messages:')
    print(sensitivity_analysis(spam_list))
    print('The sensitivity analysis for ham messages:')
    print(sensitivity_analysis(ham_list))


if __name__ == '__main__':
    main()