from django import forms

SIZES = {"xs": "XS", "s": "SM", "m": "MD", "l": "LG", "xl": "XL"}
COLORS = {"white": "White", "black" : "Black"}
class AddToCartForm(forms.Form):
    size_choice = forms.ChoiceField(widget=forms.Select, choices=SIZES)
    color_choice = forms.ChoiceField(widget=forms.Select, choices=COLORS)
    quantity = forms.IntegerField(min_value=1, initial=1)