from django import forms
from .models import Author,Books

# from .models import  Post






class BookForm(forms.ModelForm):
    
    class Meta:
        model = Books
        fields = ('Author', 'headline', 'Withdrawn','Draft','published_date')
        
        
        
class AuthorForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'email')


