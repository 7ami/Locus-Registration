from django import forms


class OurForm(forms.Form):
    firt_name = forms.CharField(label="First Name", max_length=100, required=True)
    last_name = forms.CharField(label="Last Name ", max_length=100, required=True)
    Contact_No = forms.IntegerField(label_suffix="Contact Number", required=True)
    email = forms.CharField(label="E-mail", max_length=100)
    company = forms.CharField(label="College/Company", max_length=100)

