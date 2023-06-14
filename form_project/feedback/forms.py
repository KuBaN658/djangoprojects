from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя:', max_length=13,
                           min_length=4, error_messages={
            'max_length': 'Слишком много символов',
            'min_length': 'Слишком мало символов',
            'requered': 'Укажите хотя бы один символ'
        })
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
    rating = forms.IntegerField(label='Рейтинг',min_value=0, max_value=5)