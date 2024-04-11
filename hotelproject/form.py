from django import forms
from .models import Details

class HotelForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = [
            "title",
            "price",
            "number_of_bathroom",
            "address",
            "image",
        ]