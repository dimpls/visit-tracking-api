from django.urls import path
from .views import StoreListByPhoneNumber, CreateVisit

urlpatterns = [
    path('stores/<str:phone_number>/', StoreListByPhoneNumber.as_view(), name='store-list-by-phone'),
    path('visits/create/<int:id>/', CreateVisit.as_view(), name='create-visit'),

]