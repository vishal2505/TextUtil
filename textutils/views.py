from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')

    #Get the checkbox
    removepunchuation = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    removenewline = request.POST.get('removenewline', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    purpose_text = ""
    #check for checkbox on
    if removepunchuation == 'on':
        analyzed_text = ""
        puns = '''/,;:'[]{}!@#$%^&*()'''
        for char in djtext:
            if char not in puns:
                analyzed_text = analyzed_text + char
        djtext = analyzed_text
        purpose_text = purpose_text + "Removing Punctuations" + " AND "

        #params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed_text}
        #return render(request, 'analyze.html', params)

    if capitalize == 'on':
        analyzed_text = ""
        for char in djtext:
            analyzed_text = analyzed_text + char.upper()
        djtext = analyzed_text
        purpose_text = purpose_text + "Capitalized characters" + " AND "

        #params = {'purpose': "Capitalized characters", 'analyzed_text': analyzed_text}
        #return render(request, 'analyze.html', params)

    if removenewline == 'on':
        analyzed_text = ""
        for char in djtext:
            if char != "\n":
                analyzed_text = analyzed_text + char
        djtext = analyzed_text
        purpose_text = purpose_text + "Removed new line" + " AND "

        #params = {'purpose': "Removed New Line", 'analyzed_text': analyzed_text}
        #return render(request, 'analyze.html', params)

    if extraspaceremover == 'on':
        analyzed_text = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed_text = analyzed_text + char
        djtext = analyzed_text
        purpose_text = purpose_text + "Removed extra spaces" + " AND "

        #params = {'purpose': "Removed Extra spaces", 'analyzed_text': analyzed_text}
        #return render(request, 'analyze.html', params)

    if removepunchuation == 'on' or capitalize == 'on' or removenewline == 'on' or extraspaceremover == 'on':
        params = {'purpose': purpose_text, 'analyzed_text': djtext}
        return render(request, 'analyze.html', params)

    elif charcount == 'on':
        count=len(djtext)
        analyzed_text = f"No of characters in the text are {count}"

        params = {'purpose': "Counting no of characters", 'analyzed_text': analyzed_text}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('ERROR !!!')
