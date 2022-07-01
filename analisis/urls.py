from django.urls import path
from django.contrib.auth import views as aut_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('editprofile/', views.editProfile, name="editprofile"),
    path('faq/', views.faq, name="faq"),
    path('set_analysis/', views.set_analaysis, name="set_analysis"),
    path('analysis_resume/', views.analysis_resume, name="analysis_resume"),
    path('test_view/', views.test_view, name="test_view"),


    path('reset_password/', aut_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', aut_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', aut_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', aut_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)