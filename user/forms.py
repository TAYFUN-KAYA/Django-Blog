from django import forms


class LoginForm(forms.Form):
    username=forms.CharField(max_length=30,label="Username")
    password=forms.CharField(max_length=25,label="Password ",widget=forms.PasswordInput)



class RegisterForms(forms.Form):
    username=forms.CharField(max_length=30,label="Kullanıcı adını giriniz")
    password=forms.CharField(max_length=25,label="Şifrenizi giriniz",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=25,label="Şifrenizi doğrulayınız",widget=forms.PasswordInput)
    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")

        if password and confirm and password!=confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor")
        values={
            "username":username,
            "password":password
        }
        return values