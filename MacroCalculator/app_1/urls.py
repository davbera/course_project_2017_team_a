from django.conf.urls import url

from . import views

app_name = 'app_1'

urlpatterns = [
    # es: /
    url(r'^$', views.home, name='home'),
    # es: /register/
    url(r'^register/$', views.register, name='register'),
    # ex: /profile/
    url(r'^profile/$', views.index, name='index'),
    # ex: /profile/5/
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    # ex: /profile/5/history/
    url(r'^profile/(?P<user_id>[0-9]+)/history/$', views.history, name='history'),
    # ex: /profile/5/add_food
    url(r'^profile/(?P<user_id>[0-9]+)/add_food/$', views.add_food, name='add_food'),
    # ex: /profile/5/add_food/4/add_ingredient
    url(r'^profile/(?P<user_id>[0-9]+)/add_food/(?P<item_id>[0-9]+)/add_ingredient$', views.add_ingredient,
        name='add_ingredient'),

]
