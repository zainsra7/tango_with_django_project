from django.conf.urls import url

from rango import views

# app_name = 'rango'  # Adding namespace if there are multiple apps

urlpatterns =[
    url(r'^$', views.index, name='index'),

    # Adding the rango/about url mapping
    url(r'about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_url>[\w\-]+)/$',
        views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_url>[\w\-]+)/add_page/$',
        views.add_page, name='add_page'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
]