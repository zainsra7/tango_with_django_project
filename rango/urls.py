from django.conf.urls import url

from rango import views

urlpatterns =[
    url(r'^$', views.index, name='index'),

    # Adding the rango/about url mapping
    url(r'about/', views.about, name='about'),
    url(r'^category/(?P<category_name_url>[\w\-]+)/$',
        views.show_category, name='show_category')
]