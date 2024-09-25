from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    peoples = [
        {'name': 'Abhi jeet', 'age': 25},
        {'name': 'Rohan sharma', 'age': 23},
        {'name': 'akash', 'age': 25},
        {'name':'viaansh', 'age':5}
    ]


    text = """Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nisi quam alias aperiam facilis culpa autem dicta voluptatibus et, aut debitis mollitia temporibus sint dignissimos error aliquam minus dolor. At, eum.
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis consequatur, inventore modi tempore dolorum repudiandae. Nesciunt rerum provident delectus a, sint rem, et sed est laborum numquam tempore autem modi!
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Facilis est laboriosam ipsa, enim quia quo cum vero incidunt accusantium commodi rem impedit necessitatibus obcaecati animi magni eos, id hic explicabo!
    """
    return render(request, "home/index.html", context = {'page': 'Django 2024','peoples' : peoples, 'text' : text})

def about(request):
    context = {'page':'About'}
    return render(request, "home/about.html", context)

def contact(request):
    context = {'page':'Contact'}
    return render(request, "home/contact.html" , context)


def success_page(request):
    return HttpResponse("<h1>success page!</h1>")