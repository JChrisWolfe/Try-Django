# Here we are going to render the contents of the products database in these pages.
# This is a good case of dedicating each app to specific roles.
# This views.py has it's own template folder 'products/templates/'.
# Also checkout pages/views.py to see some comments that can help you understand some
#  things on this page, 
#  and checkout the logic in the context(s) are here. Very modular.

from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm # Checkout forms.py
from .models import Product


# From: https://www.w3schools.com/tags/ref_httpmethods.asp

#     GET is used to request data from a specified resource.

#     GET is one of the most common HTTP methods.

#     Note that the query string (name/value pairs) is sent in the URL of a GET request:
#         /test/demo_form.php?name1=value1&name2=value2

#     Some other notes on GET requests:

#         GET requests can be cached
#         GET requests remain in the browser history
#         GET requests can be bookmarked
#         GET requests should never be used when dealing with sensitive data
#         GET requests have length restrictions
#         GET requests is only used to request data (not modify)



# From: https://www.w3schools.com/tags/ref_httpmethods.asp

#     POST is used to send data to a server to create/update a resource.

#     The data sent to the server with POST is stored in the request body of the HTTP request:
#         POST /test/demo_form.php HTTP/1.1
#         Host: w3schools.com
#         name1=value1&name2=value2
#     POST is one of the most common HTTP methods.

#     Some other notes on POST requests:
#         POST requests are never cached
#         POST requests do not remain in the browser history
#         POST requests cannot be bookmarked
#         POST requests have no restrictions on data length


# This is how you will create a record to DB though webpage.
def product_create_view(request):
    form = ProductForm(request.POST or None) #Default param is request.GET
    if form.is_valid(): # Has to follow logic from forms.py
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id) # This one line is how you handle a page not found or 404. You could also do it this way: https://docs.djangoproject.com/en/2.2/topics/http/views/#django.http.Http404 check comment below this function. Needs to be imported.
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context) #http://127.0.0.1:8000/product/<int:id>/update

# Example of another 404 handling:

# from django.http import Http404

# try:
#   obj = Product.objects.get(id=1)
# except Product.DoesNotExist:
#   raise Http404


def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context) # Checkout http://127.0.0.1:8000/products/

def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST": # Make sure it's a POST request!
        obj.delete() # This one line is how you delete the specific Object QuerySet called by 'obj = get_object_or_404(Product, id=id)'
        return redirect('../../') # Go back to the '/product/<int:someID>' page. Needs to be imported.
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context) #http://127.0.0.1:8000/product/<int:id>/delete
