
from django.urls import path
from .views import LoginView,LogoutView,Signup,UserListView,UserDeleteView,UserUpdateView,UserRetrieveView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", Signup.as_view(), name="signup"),
    path("",UserListView.as_view(), name="user-view"),
    path("<int:pk>/update/",UserUpdateView.as_view(), name="user-update"),
    path("<int:pk>/delete/",UserDeleteView.as_view(), name="user-delete"),
    path("<int:pk>/retrieve/",UserRetrieveView.as_view(), name="user-retrieve")
    ]
    