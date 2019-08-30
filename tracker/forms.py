from django.forms import ModelForm, TextInput, DateInput as DI

from tracker.models import Accreditation


class DateInput(DI):
    input_type = "date"


class AccreditationForm(ModelForm):
    class Meta:
        model = Accreditation
        fields = [
            "name",
            "email",
            "type",
            "date",
            "uc_username",
            "wfdf_userid",
        ]
        widgets = {
            "name": TextInput(attrs={"readonly": "readonly"}),
            "email": TextInput(attrs={"readonly": "readonly"}),
            "uc_username": TextInput(attrs={"readonly": "readonly"}),
            "date": DateInput(),
        }