from django.forms import ModelForm
from .models import Accessories

class AccessoriesForm(ModelForm):
    class Meta:
        model = Accessories
        fields = ['title','description','price','gender','condition','category','image1','image2','image3','image4']