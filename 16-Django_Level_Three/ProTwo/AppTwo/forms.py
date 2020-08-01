from django.forms import ModelForm
from AppTwo.models import User

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
