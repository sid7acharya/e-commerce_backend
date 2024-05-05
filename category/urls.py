from django.urls import path
from .views import CategoryCreateView, CategoryListView, CategoryUpdateView, CategoryDestroyView, CategoryRetrieveView

urlpatterns = [
    path('create/', CategoryCreateView.as_view(), name='category-create'),
    path('list/', CategoryListView.as_view(), name='category-list'),
    path("<int:pk>/update/", CategoryUpdateView.as_view(), name='category-update'),
    path("<int:pk>/delete/", CategoryDestroyView.as_view(), name='category-delete'),
    path("<int:pk>/retrieve/", CategoryRetrieveView.as_view(), name='category-retrieve')
]

