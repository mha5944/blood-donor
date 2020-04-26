from django.urls import path
from basicapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='index'),
    path('register/', views.register,name='register'),
    path('accounts/<slug:slug>/',views.detail_view,name='detail_view'),
    path('blood-donation-method/',views.donation_method, name='donation_method'),
    path('can-i-donate',views.can_i_donate,name='can-i-donate'),
    path('about/',views.about,name='about'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]