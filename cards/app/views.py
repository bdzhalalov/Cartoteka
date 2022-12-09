import json
from datetime import datetime

from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse

from .models import Card
from .forms import IncreaseAmountForm


def index(request):
    cards = Card.objects.all()
    context = {
        'cards': cards
    }
    return render(request, 'main.html', context)


def get_card_detail(request, id):
    card = get_object_or_404(Card, pk=id)
    form = IncreaseAmountForm()

    amount_data = []

    for line in open('amount.log'):
        amount_data.append(json.loads(line))

    data = []
    for el in amount_data:
        if el['card_id'] == id:
            data.append(el)
    print(data)

    context = {
        'card': card,
        'form': form,
        'data': reversed(data),
    }
    return render(request, 'card.html', context)


def activate_card(request, id):
    Card.objects.filter(pk=id).update(status='active')

    # TODO: add more variants for activate card, like: activate with phone, or mail

    return redirect('main')


def increase_amount(request, id):

    # TODO: create a real payment with some API like StripeAPI

    data = request.POST
    amount = dict(IncreaseAmountForm.CHOICES).get(data['choice'])

    card = Card.objects.get(pk=id)
    card_amount = card.amount

    total_amount = card_amount + amount

    card.amount = total_amount
    card.save()

    log_data = {
        'time': datetime.now().strftime('%d %B %Y | %H:%M'),
        'card_id': card.pk,
        'amount': f'+{amount}',
        'total_amount': total_amount,
    }

    with open('amount.log', 'a') as a:
        a.write(json.dumps(log_data) + '\n')

    return redirect(reverse('card', kwargs={'id': id}))


def delete_card(request, id):

    # TODO: make card deletion with user's confirmation

    Card.objects.get(pk=id).delete()

    return redirect('main')


def buy_something(request, id):

    # TODO: create products with different cost and write off the balance according product's cost. Now it's 1000

    card = Card.objects.get(pk=id)
    card_amount = card.amount

    if card_amount >= 1000:
        total_amount = card_amount - 1000
    else:
        return HttpResponse('Balance less than purchase amount!')

    card.amount = total_amount
    card.save()

    log_data = {
        'time': datetime.now().strftime('%d %B %Y | %H:%M'),
        'card_id': card.pk,
        'amount': f'-1000',
        'total_amount': total_amount,
    }

    with open('amount.log', 'a') as a:
        a.write(json.dumps(log_data) + '\n')

    return redirect(reverse('card', kwargs={'id': id}))
