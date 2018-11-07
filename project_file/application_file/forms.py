from django.forms import ModelForm
from application_file.models import Customer, Vehicle, Manufacturer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer        # Refer to the chosen Class model
        exclude = []            # Set a variable to exclude any field we wish to not have


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        exclude = []


class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        exclude = []
