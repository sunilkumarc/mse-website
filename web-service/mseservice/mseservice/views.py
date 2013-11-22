from django.http import HttpResponse

def  getArticle(request):
    with open("articles.json", "r") as f:
        response = HttpResponse(f.read())
    return response
