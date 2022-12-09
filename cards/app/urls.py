from django.urls import path

from .views import index, activate_card, get_card_detail, increase_amount, delete_card

urlpatterns = [
    path('', index, name='main'),
    path('card/<int:id>/', get_card_detail, name='card'),
    path('card/activate/<int:id>/', activate_card, name='activate'),
    path('card/charge/<int:id>/', increase_amount, name='charge'),
    path('card/delete/<int:id>/', delete_card, name='delete')
]