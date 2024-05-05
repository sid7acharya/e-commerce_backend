from django.urls import path
from .views import ProductCreateView,ProductListView,ProductDestroyView,ProductUpdateView,ProductRetrieveView

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('', ProductListView.as_view(), name='product-list'),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name='product-update'),
    path("<int:pk>/delete/", ProductDestroyView.as_view(), name='product-delete'),
    path("<int:pk>/retrieve/", ProductRetrieveView.as_view(), name='product-retrieve')
]
