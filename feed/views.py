from django.shortcuts import render
#from django.http import HttpResponse
from feed.models import Article, Comment



# def index(request):
#     return HttpResponse("Hello, world. You're at the feed index.")


# def index(request):
#     name = "Sherlock"
#     num = [1,2,3,4,5]

#     return render(request, "index.html", {"name":name, "num":num})


def index(request):
    article_list = Article.objects.all()
    ctx = {
        "article_list" : article_list
    }
    return render(request, "index.html", ctx)