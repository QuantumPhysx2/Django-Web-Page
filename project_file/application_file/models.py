from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=75)
    lastname = models.CharField(max_length=75)
    age = models.IntegerField(help_text="Must be above 18 to Register", validators=[MaxValueValidator(100), MinValueValidator(18)])
    gender = models.CharField(max_length=6, help_text="Male/Female/Other")
    email = models.EmailField(blank=True, help_text="Customer Email")
    # Using RegEx for getting contact number
    contact_number_regex = RegexValidator(regex=r'^(\d{1,9})/?', message="Up to 12 Digits")
    # Set a field which has a required validator of regex
    contact_number = models.CharField(validators=[contact_number_regex], max_length=12, blank=False)
    rental_plan = models.CharField(max_length=7, help_text="Weekly/Monthly/Yearly")
    # Set up Foreign Key to link to the 'Vehicle' table (opens up a selection box of existing IDs to choose from)
    # models.ForeignKey("<TableName>")
    vehicle_id = models.ForeignKey("Vehicle", help_text="Assigned Vehicle")     # This is our One-to-Many cardinality

    def __str__(self):
        return str("%s %s" % (self.firstname, self.lastname))       # Using string manipulation for returning readable information


class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text="Name of Vehicle")
    model = models.CharField(max_length=50, help_text="Name of Company Maker")
    year = models.CharField(max_length=4, help_text="Year when Vehicle was Produced")
    manufacturer_id = models.ForeignKey("Manufacturer")
    drivetrain = models.CharField(max_length=3, help_text="FWD/RWD/AWD/2WD/4WD")
    passenger_capacity = models.IntegerField(help_text="How Many Seatable Passengers", validators=[MaxValueValidator(100), MinValueValidator(1)])
    type = models.CharField(max_length=50, help_text="Offroad/Truck/Lightweight/Family Car etc")
    description = models.TextField(help_text="Description about Vehicle's Condition", blank=True)

    def __str__(self):
        return str("%s / %s" % (self.name, self.drivetrain))


class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return str("%s" % self.name)
