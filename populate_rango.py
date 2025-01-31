import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango_with_django_project.settings")

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages=[{"title": "Official Python Tutorial", "url":"https://docs.python.org/3/tutorial/", "views":1},
                  {"title": "How to Think like a Computer Scientist", "url":'https://www.greenteapress.com/thinkpython/', "views":2},
                  {"title": "Learn Python in 10 Minutes", "url":'https://www.korokithakis.net/tutorials/python/', "views":4}]
    
    django_pages=[{'title':'Official Django Tutorial', 'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', "views":8},
                  {'title':'Django Rocks', 'url':'http://www.djangorocks.com/', "views":16},
                  {'title':'How to Tango with Django', 'url':'http://www.tangowithdjango.com/', "views":32}]
    
    other_pages=[{'title':'Bottle', 'url':'http://bottlepy.org/docs/dev/', "views":64},
                  {'title':'Flask', 'url':'http://flask.pocoo.org', "views":128}]
    
    categories={'Python': {'pages': python_pages, "views":128, "likes":64},
                'Django': {'pages': django_pages, "views":64, "likes":32},
                'Other Frameworks': {'pages': other_pages, "views":32, "likes":16}}
    
    for category, category_data in categories.items():
        c = add_category(category, category_data["views"], category_data["likes"])
        for p in category_data['pages']:
            add_page(c, p['title'], p['url'], p["views"])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(category, title, url, views=0):
    p = Page.objects.get_or_create(category=category, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_category(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c
    
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()