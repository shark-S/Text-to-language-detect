import sys
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords

def cal():
    text = sys.stdin.read()
    languages_ratios = {}
    toekns = wordpunct_tokenize(text)
    words = [word.lower() for word in toekns]
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)
        languages_ratios[language] = len(common_elements)
        
    ratios = languages_ratios
    most = max(ratios, key=ratios.get)
    print (most)
    """if most == "english":
        print ("English")
    if most == "german":
        print ("German")
    if most == "french":
        print ("French")
    if most == "spanish":
        print ("Spanish")"""
cal()
