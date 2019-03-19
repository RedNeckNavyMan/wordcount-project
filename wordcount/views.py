from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def mypic(request):
#     return HttpResponse('Hello, my name is Thomas')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
            #increase
        else:
            #add to the dictionary
            worddictionary[word] = 1



    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddictionary':worddictionary.items()})






























