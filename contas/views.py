from django.shortcuts import render
# import datetime
# from django.http import HttpResponse

def home(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, "contas/home.html")