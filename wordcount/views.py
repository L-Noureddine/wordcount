from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    #Url looking for, cockies, parametered .. etc
    return render(request, "home.html", {'love':'FATOMA'})

def aboutpage(request):
    #Url looking for, cockies, parametered .. etc
    return render(request, "about.html")

def count(request):
    #Url looking for, cockies, parametered .. etc

    #print(request.GET['fulltext'])
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict.keys():
            worddict[word] +=1
        else:
            worddict[word] = 1

    s = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    #s = [(k, worddict[k]) for k in sorted(worddict, key=worddict.get, reverse=True)]

    return render(request, "count.html", {'fulltext':fulltext, 'wordscount':len(wordlist), 'worddict':s})