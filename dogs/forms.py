from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField
from django.utils import timezone

from dogs.models import Dog, Parent


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class DogForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Dog
        exclude = ("view_counter", "owner")


class DogModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Dog
        fields = ("description", "bread")


class ParentForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Parent
        fields = "__all__"

    def clean_date_born(self):
        date_born = self.cleaned_data['date_born']
        current_year = timezone.now().year
        timedelta = current_year - date_born
        if timedelta > 100:
            raise ValidationError('Возраст собаки не может быть больше 100 лет')
        return date_born
