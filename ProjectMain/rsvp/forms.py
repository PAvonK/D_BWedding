from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Snippet
from django.core.validators import RegexValidator

class NameWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        super().__init__([
            forms.TextInput(),
            forms.TextInput()
        ], attrs)

    def decompress(self, value):
        if value:
            return value.split(' ')
        return ['', '']

class NameField(forms.MultiValueField):
    widget = NameWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(),
            forms.CharField()
        )

        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        #takes value of both forms.CharField() and put into list
        return f'{data_list[0]} {data_list[1]}'


class RsvpForm(forms.Form):
    name = NameField()
    #name_first = forms.CharField()
    #name_last = forms.CharField()
    email = forms.EmailField(label='e-mail', required=False)
    attending = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], required=False)
    number_guests = forms.CharField(required=False)
    couple_message = forms.CharField(widget=forms.Textarea, required=False)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            #'name_first',
            #'name_last',
            'email',
            'attending',
            'number_guests',
            'couple_message',
            Submit('submit', 'Submit')
        )

    print('name_first', 'name_last', 'email')
    

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('name', 'body')