from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'), 						# /rewards_app/
    url(r'^friends/', views.add_friend, name='friend_name'), 	# /rewards_app/friends/
    url(r'^add_friend/', views.add_friend, name='add_friend'), 	# /rewards_app/add_friend/

]
