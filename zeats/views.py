from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from restaurant.models import Restaurant,Review,MenuItem,Order,OrderItem,MenuOption,MenuOptionValue,OrderOption, OrderExtra,MenuExtra
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib import auth
from userprofile.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from settings import COMMISSION
from referral.models import Referral

def home(request):

    args={}
    return render_to_response('frontpage.html',args)

def places(request):

    if request.GET.get('restaurant') is not None:
        restaurant_id=request.GET.get('restaurant')
        restaurant = Restaurant.objects.get(id=restaurant_id)
        latest_review = Review.objects.filter(restaurant=restaurant).order_by('-date')

        args={}
        args.update(csrf(request))
        args['restaurant'] = restaurant
        args['menu']=restaurant.menu_items.all().order_by('id')
        try:
            args['latest_review']=latest_review[0]
        except:
            pass
        return render_to_response('proto-menu2.html',args)
    else:
        city = request.GET.get('town')

        restaurants = Restaurant.objects.filter(city=city).order_by('-id')

        args={}

        args['city']=city

        args['restaurants']=restaurants
        
        return render_to_response('proto-places2.html',args)

def menu_dashboard(request):

    restaurant_id = request.GET.get('restaurant')
    restaurant = Restaurant.objects.get(id=restaurant_id)
    args={}
    args.update(csrf(request))
    args['restaurant']=restaurant
    args['menu'] = restaurant.menu_items.all().order_by('id')
    return render_to_response('create-menu-item.html',args)

def create_menu_item(request):


    if request.POST:       
        restaurant_id = request.GET.get('restaurant')
        restaurant = Restaurant.objects.get(id=restaurant_id)
        itemName = request.POST['itemName']
        itemDescription = request.POST['itemDescription']
        category = request.POST['category']
        minimumPrice = request.POST['minimumPrice']
        price_adjusted = float(minimumPrice) * COMMISSION

        MenuItem.objects.create(name=itemName,description=itemDescription,
                                category=category,restaurant=restaurant,price=minimumPrice,price_adjusted=price_adjusted)        

    return HttpResponse('success')

def delete_menu_item(request):

    item_id = request.GET.get('item')
    item = MenuItem.objects.get(id=item_id)

    item.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def create_menu_variation(request):

    item_id = request.GET.get('item')
    item = MenuItem.objects.get(id=item_id)

    if request.POST:
        
        propertyName = request.POST['propertyName']

        menuOption = MenuOption.objects.create(code=propertyName,item=item)
        
    return HttpResponse('success')

def add_menu_variation(request):

    from django.db.models import Min

    item_id = request.GET.get('item_id')
    option = MenuOption.objects.get(id=item_id)

    if request.POST:
        
        propertyValue = request.POST['propertyValue']
        propertyPrice = request.POST['propertyPrice']
        price_adjusted = float(propertyPrice) * COMMISSION

        menuOption = MenuOptionValue.objects.create(option=option,description=propertyValue,
                                                    price=propertyPrice,price_adjusted=price_adjusted)
             

    return HttpResponse('success')

def create_menu_extra(request):

    item_id = request.GET.get('item')
    item = MenuItem.objects.get(id=item_id)

    if request.POST:

        extraName = request.POST['extraName']
        extraPrice = request.POST['extraPrice']
        price_adjusted = float(extraPrice) * COMMISSION

        extra = MenuExtra.objects.create(code=extraName,price=extraPrice,item=item,price_adjusted=price_adjusted)
        

        return HttpResponse('success')
    else:
        return HttpResponse('Something went wrong :(')

def load_menu_items(request):

    restaurant_id=request.GET.get('restaurant')

    args={}
    restaurant = Restaurant.objects.get(id=restaurant_id)
    args.update(csrf(request))
    args['restaurant']=restaurant
    args['menu']=restaurant.menu_items.all().order_by('id')
    return render_to_response('menu-feed.html',args)

def load_property_feed(request):

    args={}
    args.update(csrf(request))
    item_id = request.GET.get('item_id')
    args['item'] = MenuItem.objects.get(id=item_id)
    
    return render_to_response('property-feed.html',args)

def load_extras_feed(request):

    args={}
    args.update(csrf(request))
    item_id=request.GET.get('item')
    args['item'] = MenuItem.objects.get(id=item_id)

    return render_to_response('extra_feed.html',args)

def add_order_item(request):

    if request.POST:

        menu_item_id = request.POST['menuItemId']
        menuItem = MenuItem.objects.get(id=menu_item_id)
        restaurant = menuItem.restaurant
        totalItemPrice = float(request.POST['totalItemPrice'])
        orderQuantity = int(request.POST['orderQuantity'])

        selected_options=request.POST.getlist('values[]')
        selected_extras = request.POST.getlist('extras[]')
        
        try:
            order = Order.objects.get(user=request.user,restaurant=restaurant,completed=False,placed=False)
            order.total=order.total+totalItemPrice
            order.save()
            
        except:
            order = Order.objects.create(user=request.user,restaurant=restaurant)
            order.total=order.total+totalItemPrice+order.restaurant.delivery_fee
            order.save()

        
##      orderItem = OrderItem.objects.get(item=menuItem,order=order)
##      orderItem.price = orderItem.price+totalItemPrice
##      orderItem.quantity = orderItem.quantity + orderQuantity
##      orderItem.save()
        
        order_item=OrderItem.objects.create(price=totalItemPrice,quantity=orderQuantity,
                                 order=order,item=menuItem,name=menuItem.name)

        for index in selected_options:
            optionValue = MenuOptionValue.objects.get(id=int(index))
            OrderOption.objects.create(code=optionValue.option.code,description=optionValue.description,
                                    order_item=order_item)
            
        for index in selected_extras:
            extra = MenuExtra.objects.get(id=int(index))
            OrderExtra.objects.create(code=extra.code,price=extra.price_adjusted,order_item=order_item)
            
            
        

        return HttpResponse('success')
    
    else:

        return HttpResponse('failure')


def update_necessary(request):

    try:

        print("\n Commission Value: %s \n"%COMMISSION)

        for option in MenuOptionValue.objects.all():
            
            price_adjusted = option.price * COMMISSION
            
            option.price_adjusted = price_adjusted
            option.save()

        for extra in MenuExtra.objects.all():

            price_adjusted = extra.price * COMMISSION
            
            extra.price_adjusted = price_adjusted
            extra.save()

        for item in MenuItem.objects.all():

            price_adjusted = item.price * COMMISSION
            
            item.price_adjusted = price_adjusted
            item.save()

        return HttpResponse('Success')
    
    except:
        raise
        return HttpResponse('Something went wrong')
        

    

def remove_order_item(request):

    if request.GET.get('order_item_id')is not None:

        order_item_id = request.GET.get('order_item_id')
        orderItem = OrderItem.objects.get(id=order_item_id)
        order = orderItem.order

        # A bit of security to prevent deleting other peoples orders
        if order.user == request.user:
            order.total = order.total - orderItem.price
            order.save()

            orderItem.delete()

            return HttpResponse('success')
        else:
            return HttpResponse('You\'re no allowed to do this!')

    else:

        return HttpResponse('failure')


def place_order(request):
    
    from django.utils import timezone
    from datetime import datetime
    
    if request.POST:
        order_id = request.GET.get('order')
        order = Order.objects.get(id=order_id)

        if request.POST['latitude']=='null' or request.POST['longitude']=='null':
            order.gps=False
        else:
            latitude = float(request.POST['latitude'])
            longitude = float(request.POST['longitude'])
            order.latitude=latitude
            order.longitude = longitude
            
        instructions = request.POST['deliveryInstructions']


        order.placed=True
        order.delivery_instructions=instructions
        order.date=timezone.now()

        order.save()

        return HttpResponseRedirect('/order/thanks/?order=%s'%order.id)

    return HttpResponse('success')

def complete_order(request):

    if request.user.profile.driver == False:
        return HttpResponse('You are not allowed to do this.')
    

    order_id = request.GET.get('order')
    order = Order.objects.get(id=order_id)

    if order.driver != request.user:
        return HttpResponse('You aren\'t allowed to do this!')

    order.completed=True
    order.save()

    profile = order.user.profile
    if profile.first_purchase == False:
        profile.first_purchase = True
        profile.save()

        if Referral.objects.filter(user2=profile.user).count()>0:
            referral = Referral.objects.get(user2=profile.user)
            user1Profile = referral.user1.profile
            user1Profile.referral_points+=1
            user1Profile.save()
            user2Profile = referral.user2.profile
            user2Profile.referral_points+=1
            user2Profile.save()
        
    return HttpResponse('success')

def driver_accept_order(request):

    order_id=request.GET.get('order')
    order = Order.objects.get(id=order_id)

    order.driver_accepted=True
    order.driver=request.user

    order.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def driver_order_list(request):

    args={}
    args['orders'] = request.user.deliveries.all()
    return render_to_response('proto-driver-order-list.html',args)

def thanks_order(request):
    import pytz
    from datetime import timedelta
    
    order_id = int(request.GET.get('order'))
    order = Order.objects.get(id=order_id)

    local_tz=pytz.timezone('Africa/Lusaka')
    earliest = order.date+timedelta(hours=1)
    earliest = earliest.astimezone(local_tz)
                                   
    latest = order.date+timedelta(hours=2)
    latest = latest.astimezone(local_tz)

    args={}
    args['order']=order
    args['earliest']=earliest
    args['latest']=latest
    return render_to_response('proto-thanks2.html',args)



def driver_order_queue(request):

    args={}
    orders = Order.objects.filter(completed=False,placed=True,driver_accepted=False).order_by('date')
    args['orders']=orders

    return render_to_response('proto-driver-order-queue.html',args)

def add_review(request):

    from django.db.models import Avg
    
    if request.POST:
        
        order_id = request.POST['orderId']
        order = Order.objects.get(id=order_id)
        rating = int(request.POST['rating'])
        description = request.POST['description']
        restaurant = order.restaurant

        review = Review.objects.create(rating=rating,description=description,
                              user=request.user,order=order,restaurant=restaurant)
        
        restaurant = review.restaurant
        averageRating = restaurant.reviews.aggregate(Avg('rating'))
        
        restaurant.rating = averageRating['rating__avg']
        restaurant.save()
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse('Something went wrong')

def reviews(request):

    if request.GET.get('restaurant') is not None:
        restaurant_id = request.GET.get('restaurant')
        restaurant = Restaurant.objects.get(id=restaurant_id)
        args={}
        args['restaurant']=restaurant
        args['reviews']=restaurant.reviews.all().order_by('-date')
        return render_to_response('proto-menu-reviews2.html',args)
    else:
        return HttpResponse('Something went wrong... :(')

@login_required
def cart(request):

    args={}
    args.update(csrf(request))
    args['loggedUser']=request.user
    try:
        
        restaurant_id = request.GET.get('restaurant')
        restaurant = Restaurant.objects.get(id=restaurant_id)
        cart = Order.objects.get(user=request.user,restaurant=restaurant,completed=False,placed=False)

        args['restaurant']=restaurant
        args['cart'] = cart
        
        
    except:

        try:
            restaurant_id = request.GET.get('restaurant')
            restaurant = Restaurant.objects.get(id=restaurant_id)
            args['restaurant']=restaurant
        except:
            return HttpResponse('Something went wrong.')

    return render_to_response('proto-cart2.html',args)

def settings(request):

    args={}
    args['loggedUser']=request.user
    return render_to_response('proto-settings2.html',args)


@login_required
def account_settings(request):

    args={}
    args.update(csrf(request))
    args['loggedUser'] = request.user
    return render_to_response('proto-settings-account2.html',args)

def edit_account_settings(request):

    if request.POST:

        oldPassword = request.POST['oldPassword']
        newPassword = request.POST['newPassword']

        user = auth.authenticate(username=request.user.username,password=oldPassword)

        if user is not None:
            user.set_password(newPassword)
            user.save()
            update_session_auth_hash(request,user)

            return HttpResponse('success')
        else:
            return HttpResponse('failure')
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse('Something went wrong')

@login_required
def delivery_settings(request):

    args={}
    args.update(csrf(request))
    args['loggedUser'] = request.user
    return render_to_response('proto-settings-delivery2.html',args)

def edit_delivery_settings(request):

    if request.POST:

        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        phone = request.POST['phone']
        addressl1 = request.POST['addressl1']
        addressl2 = request.POST['addressl2']

        profile = request.user.profile
        profile.firstName = firstName
        profile.lastName = lastName
        profile.phone = phone
        profile.addressl1 = addressl1
        profile.addressl2 = addressl2

        profile.save()

        user = request.user
        user.email = email
        user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse('Something went wrong. :(')

@login_required
def order_history(request):

    args={}
    args.update(csrf(request))
    
    orders = Order.objects.filter(user=request.user,completed=True).order_by('-id')

    args['orders']=orders

    return render_to_response('proto-order-history2.html',args)

def about(request):

    args={}

    return render_to_response('proto-settings-about2.html',args)

def terms(request):

    args={}

    return render_to_response('proto-terms2.html',args)

def register(request):

    if request.POST:
        
        username = request.POST['username']
        username = username.lower()
        password = request.POST['password']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        phone = request.POST['phone']
        addressl1 = request.POST['addressl1']
        addressl2 = request.POST['addressl2']
        city = request.POST['city']     

        try:
            User.objects.get(username=username)
            return HttpResponse('username')
        except:
            pass

        user = User.objects.create_user(username=username,password=password,email=email)
        profile = Profile.objects.create(firstName=firstName,lastName=lastName,phone=phone,addressl1=addressl1,
                               addressl2=addressl2,city=city,user=user)

        if request.POST.get('referral') is not None:
            referred_by=request.POST.get('referral')

            print "\n Referer = %s \n"%referred_by
            try:
                referring_user = User.objects.get(username=referred_by)
                profile.referred_by = referred_by
                profile.save()
                Referral.objects.create(user1=referring_user,user2=user)
            except:
                pass
            

        user = auth.authenticate(username=username,password=password)
        auth.login(request,user)

        return HttpResponse('/places/?town=%s'%city)

    else:

        args={}
        args.update(csrf(request))
        
        if request.GET.get('next') is not None:
            args['next_url'] = request.GET.get('next')

        if request.GET.get('ref') is not None:
            print"%s"%request.GET.get('ref')
            args['referral'] = request.GET.get('ref')
            
        return render_to_response('proto-register-account2.html',args)


def promo(request):

    args={}

    try:
        User.objects.get(username=request.user.username)
        args['loggedUser']=request.user
    except:
        pass
    
    return render_to_response('proto-incentive.html',args)

def login(request):

    if request.POST:

        username = request.POST['username']
        username=username.lower()
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            
            if request.POST.get('next_url') is not None:
                next_url = request.POST['next_url']
                return HttpResponse('%s'%next_url)
            
            return HttpResponse('/')
        else:
            return HttpResponse('error')

    else:
        return HttpResponse('fatal')

def logout(request):

    args={}

    auth.logout(request)

    return HttpResponseRedirect('/')
