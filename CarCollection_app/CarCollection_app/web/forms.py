from django import forms

from CarCollection_app.web.models import Profile, Car


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password', 'first_name', 'last_name','profile_picture')
        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
            'password': 'Password',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password', 'first_name', 'last_name','profile_picture')


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Car.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'model', 'year', 'image_url', 'price')


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'model', 'year', 'image_url', 'price')


class DeleteCarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Car
        fields = ('type', 'model', 'year', 'image_url', 'price')

