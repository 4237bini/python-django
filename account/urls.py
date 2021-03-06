from django.urls import path

from django.contrib.auth import views as auth_views

from . import views 

urlpatterns=[
    path("register", views.register, name="register"),
    path("loginPage", views.loginPage, name="loginPage"),
    path("logout", views.logout, name="logout"),
    path("reset_password", auth_views.PasswordResetView.as_view(template_name="changerequest.html"), name="reset_password"),
    path("reset_password_sent", auth_views.PasswordResetDoneView.as_view(template_name="done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name="changepassword.html"), name="password_reset_confirm"),
    path("reset_password_complete", auth_views.PasswordResetCompleteView.as_view(template_name="done1.html"), name="password_reset_complete"),
    path("adduserprofile/<int:id>", views.adduserprofile, name ="adduserprofile"),

    path("userprofilecreated/<int:id>", views.userprofilecreated, name ="userprofilecreated"),


]    