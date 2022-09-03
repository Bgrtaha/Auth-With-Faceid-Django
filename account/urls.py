from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_request, name="login"),
    path("S-Scanner", views.s_scanner_request, name="s_scanner"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("models/<slug:slug>/", views.loadjson, name='loadjson')
#   path("account/models/<name:slug>/",views.deneme_request)
#   path("deneme",views.deneme_request, name="deneme")
]