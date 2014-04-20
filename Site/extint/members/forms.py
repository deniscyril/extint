 # -*- coding: utf-8 -*-
 
from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(label=u'Prénom', max_length=50)
    last_name = forms.CharField(label=u'Nom de famille', max_length=50)
    username = forms.CharField(label=u'Nom d\'utilisateur', max_length=50)
    password = forms.CharField(
        label=u'Mot de passe', max_length=100, widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label=u'Confirmation', max_length=100, widget=forms.PasswordInput
    )
    email = forms.EmailField(label=u'Adresse email')
    date_of_birth = forms.DateField()
    #country = 
    phone1 = forms.CharField(label=u'Téléphone 1', max_length=50)
    phone2 = forms.CharField(label=u'Téléphone 2', max_length=50)
    phone3 = forms.CharField(label=u'Téléphone 3', max_length=50)
    
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        if not password_confirm== password:
            msg = u'Les mots de passe sont différents'
            self._errors['password'] = self.error_class([''])
            self._errors['password_confirm'] = self.error_class([msg])
            
            if 'password' in cleaned_data:
                del cleaned_data['password']
                
            if 'password_confirm' in cleaned_data:
                del cleaned_data['password_confirm']
                
        
        