from django.urls import path
from .views import CartCreateView,CartListView,CartDeleteView,CartUpdateView,CartRetrieveView

urlpatterns=[
    path('create/', CartCreateView.as_view(), name='cart-create'),
    path('list/', CartListView.as_view(), name='cart-list'),
    path("<int:pk>/update/", CartUpdateView.as_view(), name='cart-update'),
    path("<int:pk>/delete/", CartDeleteView.as_view(), name='cart-delete'),
    path("<int:pk>/retrieve/", CartRetrieveView.as_view(), name='cart-retrieve')
]

