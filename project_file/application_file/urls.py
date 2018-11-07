from django.conf.urls import url
from application_file import views

# URL file for our searching database function
urlpatterns = [
    url(r'^$', views.index, name="index_url"),
    url(r'^modifying_database_guide/$', views.help_me, name="help_me_url"),

    # Searching Database
    url(r'^search-database/result/$', views.search, name="search_url"),

    # Read
    url(r'^database/$', views.view_database, name="database_url"),

    # Create
    url(r'^database/create_customer/$', views.create_customer, name="create_customer_url"),
    url(r'^database/create_vehicle/$', views.create_vehicle, name="create_vehicle_url"),
    url(r'^database/create_manufacturer/$', views.create_manufacturer, name="create_manufacturer_url"),

    # Update (we are retrieving the IDs of each record using RegEx)
    url(r'^database/update_customer/(\d{1,9})/?$', views.update_customer, name="update_customer_url"),
    url(r'^database/update_vehicle/(\d{1,9})/?$', views.update_vehicle, name="update_vehicle_url"),
    url(r'^database/update_manufacturer/(\d{1,9})/?$', views.update_manufacturer, name="update_manufacturer_url"),

    # Delete (using same ID catcher method to delete specific record)
    url(r'^database/delete_customer/(\d{1,9})/?$', views.delete_customer, name="delete_customer_url"),
    url(r'^database/delete_vehicle/(\d{1,9})/?$', views.delete_vehicle, name="delete_vehicle_url"),
    url(r'^database/delete_manufacturer/(\d{1,9})/?$', views.delete_manufacturer, name="delete_manufacturer_url"),
]
