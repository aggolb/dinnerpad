from django.contrib import admin
from models import Restaurant, Review, MenuItem,OrderItem,Order,MenuExtra,OrderExtra,MenuOption,MenuOptionValue
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(MenuItem)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(MenuExtra)
admin.site.register(OrderExtra)
admin.site.register(MenuOption)
admin.site.register(MenuOptionValue)
