from django import forms
import random


class IncreaseAmountForm(forms.Form):

    CHOICES = (
        ('1', 1000),
        ('2', 2000),
        ('3', 5000),
    )

    choice = forms.ChoiceField(choices=CHOICES, label='Please, choose amount of increasing: ')


class GenerateCardForm(forms.Form):

    CHOICES = (
        ('1', 30),
        ('2', 183),
        ('3', 365),
    )

    series = forms.IntegerField(min_value=1, max_value=9999, initial=random.randint(1, 9999), label='Input card series')
    count = forms.IntegerField(min_value=1, max_value=5, label='Count of cards')
    expiration_date = forms.ChoiceField(choices=CHOICES, label='Choose duration of card activity. Days: ')

