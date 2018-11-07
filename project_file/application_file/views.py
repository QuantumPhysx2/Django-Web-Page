from django.shortcuts import render, redirect
from application_file.models import Customer, Vehicle, Manufacturer
from application_file.forms import CustomerForm, VehicleForm, ManufacturerForm


def index(request):
    page_content = {
        "title": "Home Page",
        "std_name": "Phu Gia Tran",
        "std_num": "S280030",
        "std_topic": "Car Rental Database Company",
        "std_reason": "My principal topic is based on a startup car rental business database because I wanted to try and get a "
                      "better understanding of how small company businesses lay out their databases, while at the same time, being "
                      "able to develop the database. The associated tables I have are: Customer, Vehicle and Manufacturer. "
                      "These three tables are all linked in a way in that many Customers may rent one or more Vehicles, and "
                      "each Vehicle may be rented by many Customers. In addition, every Vehicle has only one Manufacturer, and "
                      "every Manufacturer owns many Vehicles.",
    }
    return render(request, "Index.html", page_content)


def help_me(request):
    page_content = {
        "title": "User Guide",
        "add_guide": "To ADD a record to the database, simply fill out the asked details as provided. Once you get to the ‘Vehicle id:’ section, you must select one of the "
                     "available vehicles to choose from (if there is one which you are looking for but isn’t there, simply go to the ‘Vehicles’ database and fill out "
                     "the details as provided). When adding a Vehicle record, the ‘Manufacturer id:’ is simply the organization’s name of which the car was produced by. If "
                     "there is not a company that suits the Vehicle, you must go the Manufacturer database and fill out the provided details. When adding a Manufacturer record, "
                     "it is simply filling out the name and location of the Manufacturer. Once all the details are correct, you can now Add records for every table.",
        "update_guide": "To UPDATE a record, you simply click the ‘Update’ option underneath the Actions column. Bare in mind that if you do update a record, you may need to "
                        "consider the Vehicle ID or Manufacturer ID if they are going to be changed. In the event of doing so however, it is simply a matter of following the instructions.",
        "delete_guide": "To DELETE a record, you simply click the ‘Delete’ option under the Actions column. This will prompt you to confirm your deletion option. "
                        "Once you press Yes, that record will be deleted. If you press No, that record will remain. Note that once you delete a record, it cannot be recovered."
    }
    return render(request, "HelpUser.html", page_content)


def search(request):
    error = False               # Set a variable to detect whether the User has correctly inputted a valid query

    if 'q' in request.GET:      # If we retrieve a query (regardless of it being empty)...
        q = request.GET['q']    # ...Define the query (using a variable)
        if not q:               # ...At the same time, if there is no query (a Null input)...
            error = True        # ...Set the error detector to True to display an alternate result
        # Otherwise if there is a valid query...
        else:
            # ...Set a variable to initialize our class model
            found_customer = Customer.objects.filter(firstname__icontains=q)            # ...Set a variable so that the query finds only the 'firstname' attribute of Customer
            found_vehicle = Vehicle.objects.filter(name__icontains=q)                   # ...Set so that query finds only the 'name' attribute of Vehicle
            found_manufacturer = Manufacturer.objects.filter(location__icontains=q)     # ...Set so that query finds only the 'location' attribute of Manufacturer

            # Set our context in case of successful query
            page_context = {
                "found_customers": found_customer,
                "found_vehicles": found_vehicle,
                "found_manufacturers": found_manufacturer,
                "query": q,
                "failed_query": "Your search result did not match any of the entities stored in our database. Try again"
                                "but remembering to search using Customer's/Vehicle's NAME or Manufacturer's LOCATION."
                                "Your query does not have to be absolute"
            }

            # ...Return User to a new form (separate from the searching form) which will display the matching results in the query
            return render(request, "SearchResult.html", page_context)
    return render(request, "SearchForm.html", {"error": error})                         # After the if-block, if there is no query, show the error


# Read
def view_database(request):
    # Create separate variables which lists each database's attributes and entities
    customers = Customer.objects.all()
    vehicles = Vehicle.objects.all()
    manufacturers = Manufacturer.objects.all()

    page_context = {
        "customer_DB": customers,
        "vehicle_DB": vehicles,
        "manufacturer_DB": manufacturers,
        "customer_db_desc": "This is the list of all currently enlisted customers who are renting a vehicle within our database.",
        "vehicle_db_desc": "This database lists all of the vehicles that the customers can choose from to rent.",
        "manufacturer_db_desc": "This database lists all of the manufacturers that our vehicles have been produced by."
    }

    # Return the HTML file with a dictionary for context flexibility
    return render(request, "Database.html", page_context)


# Create (Note: we need to create SEPARATE Create, Update, Delete functions, otherwise we are creating/manipulating incorrect forms)
def create_customer(request):
    customer_form = CustomerForm(request.POST or None)          # Create an instance of the respective form (if there is one)

    # Form validation
    if customer_form.is_valid():                                # If the respective form is valid and existent...
        customer_form.save()                                    # ...Save the information that the User has inputted
        return redirect("create_customer_url")                  # ...Redirect User to same page if they wish to add more records

    # Set our context to use the instantiated form model
    page_context = {
        "title": "Entering Customer Record",
        "customer_form": customer_form
    }

    # After if-block, return User to the respective HTML form which will list the current/updated database for respective form
    # Repeat same logic with the other Create functions (only using different form models)
    return render(request, "CreateForm.html", page_context)


def create_vehicle(request):
    vehicle_form = VehicleForm(request.POST or None)

    if vehicle_form.is_valid():
        vehicle_form.save()
        return redirect("create_vehicle_url")

    page_context = {
        "title": "Entering Vehicle Record",
        "vehicle_form": vehicle_form
    }

    return render(request, "CreateForm.html", page_context)


def create_manufacturer(request):
    manufacturer_form = ManufacturerForm(request.POST or None)

    if manufacturer_form.is_valid():
        manufacturer_form.save()
        return redirect("create_manufacturer_url")

    page_context = {
        "title": "Entering Manufacturer Record",
        "manufacturer_form": manufacturer_form
    }

    return render(request, "CreateForm.html", page_context)


# Update
def update_customer(request, identifier):
    # Instantiate variable to retrieve the object ID
    entity = Customer.objects.get(customer_id=identifier)                  # <Class>.objects.get(<primary_key_name>=<variable_name>)
    customer_form = CustomerForm(request.POST or None, instance=entity)

    if customer_form.is_valid():
        customer_form.save()
        return redirect("database_url")

    page_context = {
        "title": "Updating Customer",
        "customer_form": customer_form,
        "entity": entity
    }

    return render(request, "UpdateForm.html", page_context)


def update_vehicle(request, identifier):
    entity = Vehicle.objects.get(vehicle_id=identifier)
    vehicle_form = VehicleForm(request.POST or None, instance=entity)

    if vehicle_form.is_valid():
        vehicle_form.save()
        return redirect("database_url")

    page_context = {
        "title": "Updating Vehicle",
        "vehicle_form": vehicle_form,
        "entity": entity
    }

    return render(request, "UpdateForm.html", page_context)


def update_manufacturer(request, identifier):
    entity = Manufacturer.objects.get(manufacturer_id=identifier)
    manufacturer_form = ManufacturerForm(request.POST or None, instance=entity)

    if manufacturer_form.is_valid():
        manufacturer_form.save()
        return redirect("database_url")

    page_context = {
        "title": "Updating Manufacturer",
        "manufacturer_form": manufacturer_form,
        "entity": entity
    }

    return render(request, "UpdateForm.html", page_context)


# Delete
def delete_customer(request, identifier):
    entity = Customer.objects.get(customer_id=identifier)                  # <Class>.objects.get(<primary_key_name>=<variable_name>)

    if request.method == "POST":                # If form method is POST...
        entity.delete()                         # ...Delete all saved entries associated with that entity's details
        return redirect("database_url")         # ...Return User to page with database

    page_context = {
        "title": "Confirm Deletion",
        "entity": entity
    }

    # Re-direct User to page with confirmation of deletion page
    return render(request, "DeleteForm.html", page_context)


def delete_vehicle(request, identifier):
    entity = Vehicle.objects.get(vehicle_id=identifier)

    if request.method == "POST":
        entity.delete()
        return redirect("database_url")

    page_context = {
        "title": "Confirm Deletion",
        "entity": entity
    }

    return render(request, "DeleteForm.html", page_context)


def delete_manufacturer(request, identifier):
    entity = Manufacturer.objects.get(manufacturer_id=identifier)

    if request.method == "POST":
        entity.delete()
        return redirect("database_url")

    page_context = {
        "title": "Confirm Deletion",
        "entity": entity,
        "warning_message": "WARNING: Deleting one record from this table will delete all associated records that are assigned with this foreign "
                           "key (i.e. certain Customers may be deleted as well if they are renting a car from this particular manufacturer)."
    }

    return render(request, "DeleteForm.html", page_context)
