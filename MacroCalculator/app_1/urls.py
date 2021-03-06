from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'app_1'

urlpatterns = [
    # ex: /
    url(r'^$', views.home, name='home'),
    # ex: /register/
    url(r'^register/$', views.register, name='register'),
    # ex: /profile/
    url(r'^profile/$', views.index, name='index'),
    # ex: /profile/5/
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    # ex: /profile/5/history/
    url(r'^profile/(?P<user_id>[0-9]+)/history/$', views.history, name='history'),
    # ex: /profile/5/add_food
    url(r'^profile/(?P<user_id>[0-9]+)/add_food/$', views.add_food, name='add_food'),
    # ex: /profile/5/add_food/3/delete
    url(r'^profile/(?P<user_id>[0-9]+)/item/(?P<item_id>[0-9]+)/delete$', views.delete_food, name='delete_food'),
    # ex: /profile/5/add_food/4/add_ingredient
    url(r'^profile/(?P<user_id>[0-9]+)/add_food/(?P<item_id>[0-9]+)/add_ingredient$', views.add_ingredient,
        name='add_ingredient'),
    url(r'^profile/(?P<user_id>[0-9]+)/remove_user$', views.remove_user, name='remove_user'),

    url(r'^profile/(?P<user_id>[0-9]+)/objective/$', views.objective, name='objective'),

    url(r'^profile/(?P<user_id>[0-9]+)/modify_profile/$', views.edit_profile, name='edit_profile'),


    # ex: /login
    url(r'^login/$', auth_views.login, {'template_name': 'app_1/login.html'}, name='login'),
    # ex: /logout
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout')



]
