# views.py is the mini app that handles all of your webpages and it's rendering.

from django.http import HttpResponse
from django.shortcuts import render
"""
render()¶
    render(request, template_name, context=None, content_type=None, status=None, using=None)

    [Context here in this project is the {} or will be name 'my_context'.
     Basically the third param is a dictionary to send to the HTML pages.]
    
    Source: https://docs.djangoproject.com/en/2.2/_modules/django/shortcuts/#render

    Combines a given template with a given context dictionary and returns an
     HttpResponse object with that rendered text.

    Django does not provide a shortcut function which returns a TemplateResponse
     because the constructor of TemplateResponse offers the same level of convenience as render().
"""

"""
This site provide a best explantion and example of *args and **kwargs: https://www.geeksforgeeks.org/args-kwargs-python/ check it out for the actual examples.

*args
    The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list.
        The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.

        What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined. With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).

        For example : we want to make a multiply function that takes any number of arguments and able to multiply them all together. It can be done using *args.

        Using the *, the variable that we associate with the * becomes an iterable meaning you can do things like iterate over it, run some higher order functions such as map and filter, etc.

**kwargs
    The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).
        A keyword argument is where you provide a name to the variable as you pass it into the function.

        One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
"""

# Create your views here. Register your view into urls.py
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs) # Using return HttpResponse the two values printed out are WSGI Request and GET method.
    print(request.user) # Tells what user (like guest, admin, or anonymous) made the request. Try display this page in incogito mode to see output.
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "home.html", {})

"""
From: https://www.fullstackpython.com/wsgi-servers.html

A Web Server Gateway Interface (WSGI) server implements the web server side of the WSGI interface for running Python web applications.

Why use WSGI and not just point a web server directly at an application?
    WSGI gives you flexibility. Application developers can swap out web stack components for others. For example, a developer can switch from Green Unicorn to uWSGI without modifying the application or framework that implements WSGI. From http://www.python.org/dev/peps/pep-3333/

    WSGI servers promote scaling. Serving thousands of requests for dynamic content at once is the domain of WSGI servers, not frameworks. WSGI servers handle processing requests from the web server and deciding how to communicate those requests to an application framework's process. The segregation of responsibilities is important for efficiently scaling web traffic.

WSGI is by design a simple standard interface for running Python code. As a web developer you won't need to know much more than:
    what WSGI stands for (Web Server Gateway Inteface)

    that a WSGI container is a separate running process that runs on a different port than your web server [like in Django the page run in this virualenv is on port 8000 by default. http://127.0.0.1].

    your web server is configured to pass requests to the WSGI container which runs your web application, then pass the response (in the form of HTML) back to the requester

If you're using a standard web framework such as Django, Flask, or Bottle, or almost any other current Python framework, you don't need to worry about how frameworks implement the application side of the WSGI standard. Likewise, if you're using a standard WSGI container such as Green Unicorn, uWSGI, mod_wsgi, or gevent, you can get them running without worrying about how they implement the WSGI standard.

However, knowing the WSGI standard and how these frameworks and containers implement WSGI should be on your learning checklist though as you become a more experienced Python web developer.
"""

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "title": "abc this is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [1313, 4231, 312, "Abc"],
        "my_html": "<h1>Hello World</h1>"

    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Socail Page</h1>")