from django import forms
from .models import Feedback

# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Имя:', max_length=13,
#                            min_length=4, error_messages={
#             'max_length': 'Слишком много символов',
#             'min_length': 'Слишком мало символов',
#             'requered': 'Укажите хотя бы один символ'
#         })
#     surname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
#     rating = forms.IntegerField(label='Рейтинг',min_value=0, max_value=5)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ['name', 'rating', 'surname', 'feedback']
        # exclude = ['rating']
        fields = '__all__'

        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рэйтинг',
        }
        error_messages = {
            'name': {
                'max_length': '* ой как много символов',
                'min_length': '* ой как мало символов',
                'required': '* поле не должно быть пустым',
            },
            'rating': {
                'max_value': '* Значение должно быть меньше 6',
            }
        }
