from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Count, F, Value # https://docs.djangoproject.com/en/2.2/ref/models/expressions/
from django.db.models.functions import Length, Upper

# the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    response = redirect('/first_app/')
    return response

def show(request, number):
    response = "placeholder to display blog " + str(number)
    return HttpResponse(response)


def edit(requet, number):
    response = "placeholder to edit blog " + str(number)
    return HttpResponse(response)

def destroy(request, number):
    response = redirect('/first_app/')
    return response

def create_again(request):

    if request.method == "POST":
        print("*"*50)
        # print(request.POST)
        # print(request.POST['name'])
        # print(request.POST['desc'])
        # print(request.session)
        # request.session['name'] = "test"  # more on session below
        # print(request.session['name'])
        # print("*"*50)
        # del request.session['key']
        # {{request.session.name}} in the html
        return redirect("/first_app/")
    else:
        return redirect("/first_app/")

def html(request):

    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }

    return render(request, './first_app/index.html', context)


    # if request.method == "GET":
    #     print("a GET request is being made to this route")
    #     return render(request, "some_app/some_template.html")
    # if request.method == "POST":
    #     print("a POST request is being made to this route")
    #     return redirect("/")



    #  <h1>All Movies</h1>
    # <ul>
    # {% for movie in all_the_movies %}
    #     <li>{{ movie.title }}</li>
    # {% endfor %}
    # </ul>