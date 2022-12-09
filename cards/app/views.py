from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Card


def index(request):
    cards = Card.objects.all()
    context = {
        'cards': cards
    }
    return render(request, 'main.html', context)


def get_card_detail(request, id):
    card = get_object_or_404(Card, pk=id)
    context = {
        'card': card
    }
    return render(request, 'card.html', context)


def activate_card(request, id):
    Card.objects.filter(pk=id).update(status='active')

    return redirect('main')
