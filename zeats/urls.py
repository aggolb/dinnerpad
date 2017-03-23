"""zeats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #User Specific
    url(r'^register/$','zeats.views.register'),
    url(r'^login/$','zeats.views.login'),
    url(r'^logout/$','zeats.views.logout'),
    url(r'^profile/edit/$','zeats.views.edit_delivery_settings'),
    url(r'^account/edit/$','zeats.views.edit_account_settings'),
    #Order Specific
    url(r'^order/add-item/$','zeats.views.add_order_item'),
    url(r'^order/remove-item/$','zeats.views.remove_order_item'),
    url(r'^order/add-review/$','zeats.views.add_review'),
    url(r'^order/place/$','zeats.views.place_order'),
    url(r'^order/complete/$','zeats.views.complete_order'),
    url(r'^order/thanks/$','zeats.views.thanks_order'),
    url(r'^order/driver-accept-order/','zeats.views.driver_accept_order'),
    #Driver Specific
    url(r'^driver/order-queue/$','zeats.views.driver_order_queue'),
    url(r'^driver/order-list/$','zeats.views.driver_order_list'),
    #Menu Specific
    url(r'^menu/dashboard/$','zeats.views.menu_dashboard'),
    url(r'^menu/create-item/$','zeats.views.create_menu_item'),
    url(r'^menu/create-variation/$','zeats.views.create_menu_variation'),
    url(r'^menu/add-variation/$','zeats.views.add_menu_variation'),
    url(r'^menu/load-menu-items/$','zeats.views.load_menu_items'),
    url(r'^menu/load-property-feed/$','zeats.views.load_property_feed'),
    url(r'^menu/delete-menu-item/$','zeats.views.delete_menu_item'),
    url(r'^menu/create-extra/$','zeats.views.create_menu_extra'),
    url(r'^menu/load-extras-feed/$','zeats.views.load_extras_feed'),
    #Aministrative Tasks
    url(r'^update_necessary/$','zeats.views.update_necessary'),
    #Site Specific
    url(r'^places/$','zeats.views.places'),
    url(r'^reviews/$','zeats.views.reviews'),
    url(r'^settings/account/$','zeats.views.account_settings'),
    url(r'^settings/delivery/$','zeats.views.delivery_settings'),
    url(r'^order-history/$','zeats.views.order_history'),
    url(r'^about/$','zeats.views.about'),
    url(r'^terms/$','zeats.views.terms'),
    url(r'^settings/$','zeats.views.settings'),
    url(r'^cart/$','zeats.views.cart'),
    url(r'^promo/$','zeats.views.promo'),
    url(r'^$','zeats.views.home'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
