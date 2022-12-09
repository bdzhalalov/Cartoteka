from django.urls import path

from .views import index, activate_card, get_card_detail

urlpatterns = [
    path('', index, name='main'),
    path('card/<int:id>/', get_card_detail, name='card'),
    path('card/activate/<int:id>/', activate_card, name='activate'),
]