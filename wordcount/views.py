from django.http import HttpResponse
from django.shortcuts import render 
import operator

def homepage(request):
    return render(request, 'home.html') #Dictionary in {{}} AFTER COMA

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1
    sortedWords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedWords})

def about(request):
    return render(request, 'about.html')

"""def eggs(request):
    return HttpResponse('<h1>EGGS</h1>') #Must be HTTP request
    """