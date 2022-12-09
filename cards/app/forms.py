from django import forms


class IncreaseAmountForm(forms.Form):

    CHOICES = (
        ('1', 1000),
        ('2', 2000),
        ('3', 5000),
    )

    choice = forms.ChoiceField(choices=CHOICES, label='Please, choose amount of increasing: ')
