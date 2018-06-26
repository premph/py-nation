from django import forms
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from smallthings import models as m

class PostModelForm(forms.ModelForm):
    class Meta:
        model = m.Post
        fields = '__all__'
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
        
class UploadForm(forms.Form):
    title = forms.CharField(max_length=255,help_text="Enter a title")
    slug = forms.SlugField(max_length=255)
    

   # cat = forms.ChoiceField(widget=forms.RadioSelect(choices=m.NewPost.categories), help_text="Enter a category")
    cat = forms.ChoiceField(choices=m.NewPost.categories,initial=m.NewPost.categories[1], help_text="Enter a category")
    
    
    keywords = forms.CharField(max_length=40,help_text="Enter a keywords")
    author = forms.CharField(max_length=30,help_text="Enter author name")
    
    images = 'images'
    thumbs = 'thumbs'
    image = forms.ImageField()
    thumb = forms.ImageField()
    
    
    
    summary = forms.CharField(max_length = 300)
    content = forms.CharField(widget=forms.Textarea)
    published = forms.BooleanField(initial=True)
    created = forms.DateTimeField(initial=timezone.now)
    
    def process(self):
        #cd = self.cleaned_data
        cleaned_data = super(UploadForm, self).clean()
        title = cleaned_data.get('title')
        slug = cleaned_data.get('slug')
        
        if not title and not slug:
            raise forms.ValidationError('You have to write something!')
            
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        

class CommentForm(forms.ModelForm):
    '''
    author = forms.CharField(max_length=200)
    text = forms.CharField(widget=forms.Textarea)
    created = forms.DateTimeField(initial=timezone.now)
    approved = forms.BooleanField(initial=False)
    '''
    class Meta:
        model = m.Comments
        fields = ('name', 'email','body','post')
       
class RunQuery(forms.Form):
    query = forms.CharField(max_length=255,help_text="Enter search keyword")
    order = forms.CharField(max_length=255,help_text="Enter search order")
    num = forms.CharField(max_length=255,help_text="Enter number of output queries")
    

    
    def process(self):
        #cd = self.cleaned_data
        cleaned_data = super(UploadForm, self).clean()
        query = cleaned_data.get('query')
        order = cleaned_data.get('order')
        num = cleaned_data.get('num')
        
        if not query and not order and not num:
            raise forms.ValidationError('You have to write something!')