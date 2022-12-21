from django import forms

from my_plant.plants_app.models import Plant


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class EditPlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class DeletePlantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Plant
        fields = '__all__'