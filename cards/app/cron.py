from datetime import datetime

from .models import Card


def check_card_status():
    cards = Card.objects.filter(status='active')

    for card in cards:
        if datetime.now() > card.expiration_date:
            card.status = 'overdue'
            card.save()
