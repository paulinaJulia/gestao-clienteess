from django.forms import ModelForm
from .models import person

class personForm(ModelForm):
    class Meta:
        model = person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
