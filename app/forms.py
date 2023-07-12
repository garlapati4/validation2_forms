from django import forms
def Validate_for_a(Svalue):
    if Svalue[0]=='a':
        raise forms.ValidationError('First letter should not be a')
def Validate_for_len(Svalue):
    if len(Svalue)<=5:
        raise forms.ValidationError('Len is lessthan 5')
class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[Validate_for_a,Validate_for_len])
    Sage=forms.IntegerField()
    email=forms.EmailField()
    remail=forms.EmailField()
    url=forms.URLField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    
    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['remail']
        if e!=r:
            raise forms.ValidationError('emails do not matched')
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot')
