# Created app. This is the BackEnd Products python code that allows you to add
#  Products to the DB though form. This dictates how the forms behave on a POST request.
from django import forms

from .models import Product

# This is pure Django form of setting up how the webpage's form checking logic. Do NOT do it the pure HTML way. It's bad practice.
class ProductForm(forms.ModelForm):
    # Check what a widget is in the function below. 
    # Reference: https://docs.djangoproject.com/en/2.2/ref/forms/widgets/
    title       = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    price       = forms.DecimalField(initial=199.99)
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


# A widget is Django’s representation of an HTML input element. The widget handles the
#  rendering of
#  the HTML, and the extraction of data from a GET/POST dictionary that corresponds to the widget.

# The HTML generated by the built-in widgets uses HTML5 syntax, targeting <!DOCTYPE html>. For
#  example, it uses boolean attributes such as checked rather than the XHTML style of
#   checked='checked'.

# Tip

#     Widgets should not be confused with the form fields 
#     (https://docs.djangoproject.com/en/2.2/ref/forms/fields/). 
#      Form fields deal with the logic of input
#       validation and are used directly in templates. Widgets deal with rendering of HTML form
#        input elements on the web page and extraction of raw submitted data. However, widgets do
#         need to be assigned (https://docs.djangoproject.com/en/2.2/ref/forms/widgets/#widget-to-field) to form fields.


class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    price       = forms.DecimalField(initial=199.99)