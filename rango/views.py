from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

from rango.forms import CategoryForm, PageForm
from rango.models import Category
from rango.models import Page


def index(request):

    # Chapter 5
    # Previously -> return HttpResponse("Rango says hey there partner! | <b><a href='rango/about'>About</a></b>")
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    # context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    # return render(request, 'rango/index.html', context=context_dict)

    # Chapter 6
    # Query the database for a list of ALL categories currently stored
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5] # Order_by('-') returns descending order because of '-' and then [:5] is slicing list for first 5 elements from 0 - 4

    # Chapter 6 Exercise
    pages_list = Page.objects.order_by('-views')[:5]
    # context_dict = {'categories': category_list, 'pages': pages_list}

    # Chapter 7 Exercise (Get all categories)
    all_categories = Category.objects.all()
    context_dict = {'all_categories': all_categories, 'categories': category_list, 'pages': pages_list}

    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)


def about(request):
    # Previously -> return HttpResponse("Rango says here is the about page. | <b><a href='/rango/'>Main</a></b>")
    # Sending my name in context dictionary
    context_dict= {'name' : "Muhammad Zain Ul Islam"}

    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_url):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_url)

        # Retrieve all of the associated pages
        # Note that filter() will return a list of page objects or an empty list
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages
        context_dict['pages'] = pages

        # We also add the category objects from
        # the database to the context dictionary
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category
        # Don't do anything - the template will display "no category" message for us
        context_dict['category'] = None
        context_dict['pages'] = None

    # Go render the response and return it to the client
    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    form = CategoryForm()

    # A HTTP Post
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided a valid form?
        if form.is_valid():
            # Save the new category to the database
            cat = form.save(commit=True)
            # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added is on the index page
            # Then we can direct the user back to the index page
            print(cat, cat.slug)
            return index(request)
        else:
            # The supplied form contained errors
            # just print them to the terminal
            print(form.errors)

    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any)
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_url):
    try:
        category = Category.objects.get(slug=category_name_url)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_url)
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)