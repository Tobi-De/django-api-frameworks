from django import forms

from car.models import Car


class ExtendedModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            for name in self.fields:
                if name not in self.initial and hasattr(self.instance, name):
                    value = getattr(self.instance, name)

                    # Format datetime values with microseconds to match other frameworks
                    if hasattr(value, "isoformat"):
                        iso_str = value.isoformat()[:-6] + "Z"
                        self.initial[name] = iso_str
                    else:
                        self.initial[name] = value


class CarForm(ExtendedModelForm):
    car_model_id = forms.IntegerField(required=False)
    car_model_name = forms.CharField(required=False)
    car_model_year = forms.IntegerField(required=False)
    color = forms.CharField(required=False)

    created_at = forms.DateTimeField(required=False, disabled=True)
    updated_at = forms.DateTimeField(required=False, disabled=True)

    class Meta:
        model = Car
        fields = ["id", "vin", "model", "owner"]
