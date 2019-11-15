from .models import Post
from .models import Transpost
from .models import Serverlist
#from .models import Selecttest
#from .models import Radiotest
from django import forms
from .models import Login

class RegForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('email','name','password')


class TransForm(forms.ModelForm):
    class Meta:
        model = Transpost
        fields = ('document','language')


class ServerlistForm(forms.ModelForm):
    class Meta:
        model = Serverlist
        fields = ('name','team','server_count','model_name','code','use_case')


#class RadiotestForm(forms.ModelForm):
#    class Meta:
#        model = Radiotest
#        fields = ('choice_field')


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('email','password')




#AREA_SELECT=[('jeju','jeju'),
#             ('pusan','pusan'),
#             ('gimpo','gimpo')]

#class RadiotestForm(forms.Form):
#    option = forms.ChoiceField(widget=forms.RadioSelect,choices=AREA_SELECT)    