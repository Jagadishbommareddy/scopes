from django.db import models
from django.contrib import admin
# from django_scopes import ScopedManager
# # Create your models here.
# class Site(models.Model):
# 	name = models.CharField(max_length=255)
#
# class Post(models.Model):
# 	site = models.ForeignKey(Site,on_delete = models.CASCADE)
# 	title = models.CharField(max_length=255)
# objects = ScopedManager(site='site')
#
# class Comment(models.Model):
# 	post = models.ForeignKey(Post,on_delete = models.CASCADE)
# 	text = models.CharField(max_length=255)
# objects = ScopedManager(site='post__site')
#
# admin.site.register(Site)
# admin.site.register(Post)
# admin.site.register(Comment)
# class Order(models.Model):
#     number = models.CharField(max_length=30, unique=True)
#     created = models.DateTimeField(auto_now_add=True)
#     # reference to objects in a different domain
#     company_id = models.IntegerField()
#     operator_id = models.IntegerField()
#     customer_id = models.IntegerField()
#     objects = OrderManager()
# 	as_company = factory_manager_for_company
#
# class OrderManager(models.Manager):
#     def __init__(self, company_id=None, *args, **kwargs):
#         self._company_id = company_id
#         super().__init__(*args, **kwargs)
#     def get_queryset(self) -> OrderQuerySet:
#         queryset = OrderQuerySet(
#             model=self.model,
#             using=self._db,
#             hints=self._hints
#         )
#         if self._company_id is not None:
#             queryset = queryset.filter(company_id=self._company_id)
#         return queryset
#     @classmethod
#     def factory(cls, model, company_id=None):
#         manager = cls(company_id)
#         manager.model = model
#         return manager
# def factory_manager_for_company(company_id):
#     return OrderManager.factory(model=Order, company_id=company_id)
