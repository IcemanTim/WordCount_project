from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request) :
    return  render(request, 'home.html', {'hithere' : 'This is me'})

def count(request) :
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    wordcount_dictionary = {}
    
    for word in wordlist :
        if word in wordcount_dictionary :
            wordcount_dictionary[word] += 1
        else :
            wordcount_dictionary[word] = 1
    sortedWords = sorted(wordcount_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count' : len(wordlist), 'sortedWords' : sortedWords})