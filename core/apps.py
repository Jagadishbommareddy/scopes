from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'


## Common Classes

class ContactNumber(models.Model):
    contact_number = models.IntegerField(max_length=10)

class Media(models.Model):
    name = models.CharField(max_length=255)

class Country(models.Model):
    name = models.CharField(max_length=255)#Metadata
class State(models.Model):
    name = models.CharField(max_length=255) #Metadata

class Address(models.Model):
    plot_number = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    city  =  models.CharField(max_length=255)
    state = models.ForeignKey(State)
    pin_code =models.IntegerField()

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=255) #Metadata

class PriorityLevel(models.Model):
    name = models.CharField(max_length=255) #Metadata
class SLAComplaince(models.Model):
    name = models.IntegerField(max_length=255) #Metadata

#Super admin
class NewSubscription(models.Model):
    company_name = models.CharField(max_length=255)
    no_of_technicians = models.IntegerField()
    contact_details = models.ForeignKey(ContactNumber)
    upload_logo = models.ForeignKey(Media)
    no_service_desks = models.IntegerField()
    subscription_plan = models.ForeignKey(SubscriptionPlan)
    address = models.ForeignKey(Address)
    admin_info = models.ForeignKey(User)
    time_stamp = DateTimeField(default=datetime.now()
class ProductCategory(models.Model):
    company = models.ForeignKey(NewSubscription)
    product_category = models.CharField(max_length=255)
    model_number = models.CharField(max_length=255)
    description = models.TextField()
    upload_image = models.ForeignKey(Media)
    time_stamp = DateTimeField(default=datetime.now()
class SubCategory(models.Model):
    product_category = models.ForeignKey(ProductCategory)
    sub_category_name = models.CharField(max_length = 255)
    upload_image = models.ForeignKey(Media)
    time_stamp = DateTimeField(default=datetime.now()

class SLAMapping(models.Model):
    priority_level = models.ForeignKey(PriorityLevel)
    resolution_time = models.DataTimeField()
    response_time = models.DataTimeField()
    acceptance_time = models.DataTimeField()
    sla_complaince_target = models.ForeignKey(SLAComplaince)

class BuildingDetails(models.Model):
    company_name = models.ForeignKey(NewSubscription)
    priority_level = models.ForeignKey(PriorityLevel)
    product_category = models.ForeignKey(ProductCategory)
    sub_category = models.ForeignKey(SubCategory)
    per_cal_charges_within_sla = models.FloatField()
    per_cal_charges_for_elapsed_sla = models.FloatField()
