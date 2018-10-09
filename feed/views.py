from django.shortcuts import render
#from django.http import HttpResponse
from feed.models import Article, Comment, HashTag


# def index(request):
#     return HttpResponse("Hello, world. You're at the feed index.")


# def index(request):
#     name = "Sherlock"
#     num = [1,2,3,4,5]

#     return render(request, "index.html", {"name":name, "num":num})


def index(request):
    category = request.GET.get("category")
    hashtag = request.GET.get("hashtag")
    
    if not category and not hashtag:
        article_list = Article.objects.all()
    elif category:
        article_list = Article.objects.filter(category=category)
    elif hashtag:
        article_list = Article.objects.filter(hashtag__name=hashtag)

    hashtag_list = HashTag.objects.all()
    category_list = sorted(set([(article.category, article.get_category_display()) for article in article_list]))

    ctx = {
        "article_list" : article_list,
        "hashtag_list" : hashtag_list,
        "category_list" : category_list,
    }
    return render(request, "index.html", ctx)


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    hashtag_list = HashTag.objects.all()
    ctx = {
        "article" : article,
        "hashtag_list" : hashtag_list,
    }

    return render(request, "detail.html", ctx)