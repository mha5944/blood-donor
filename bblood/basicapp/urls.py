from django.urls import path
from basicapp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('register/', views.register,name='register'),
    path('accounts/<slug:slug>/',views.detail_view,name='detail_view'),
    path('blood-donation-method/',views.donation_method, name='donation_method'),
    path('can-i-donate',views.can_i_donate,name='can-i-donate'),
    path('about/',views.about,name='about'),
]