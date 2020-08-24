from django  import forms 
from recipe_box_app.models import Recipe, Author



class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ( "title", "author", "description", "time_required", "instructions",)

class AddAuthorForm(forms.ModelForm):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Author
        fields = ('name', 'bio')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
    firstname = forms.CharField(max_length=240)
    lastname = forms.CharField(max_length=240)
    bio = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    password = forms.CharField(widget=forms.PasswordInput)