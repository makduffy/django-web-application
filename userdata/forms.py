from django.forms import ModelForm
from .models import UserData


class UserDataModelForm(ModelForm):
    class Meta:
        model = UserData
        fields = ['name', 'email', 'phoneNo', 'fruit_selection']

    def validation(self):

        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        phone_no = cleaned_data.get("phoneNo")
        fruit_selection = cleaned_data.get("fruit_selection")





