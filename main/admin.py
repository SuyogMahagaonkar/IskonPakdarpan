from django.contrib import admin
from django_object_actions import DjangoObjectActions
from .models import UserDetail, Slider, Contact, Cart
from saler.models import Product, ProductSize, SalerDetail, category,Color, dow, SellerSlider, MyCart, WholeSaleProduct,\
    Orders, trend, WholeSaleProductOrders,ProductReview

admin.site.site_header = 'TasteBuddies'



class UserAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'user', 'dob', 'mobile', 'alternate_mobile', 'sex', 'address']
    list_filter = ('mobile', 'sex')


# class CartAdmin(admin.ModelAdmin):
#     list_display = ['user', 'product_id', 'product_size', 'number']
#     list_filter = ('user', 'number', 'product_id', 'product_size')


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']
    list_filter = ('name', 'email')
    search_fields = ['name', 'email', 'subject', 'message']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'name', 'url']
    list_filter = ('name',)
    search_fields = ['name']


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'sub_Categories']
#     list_filter = ('name',)
#     search_fields = ['name', 'sub_Categories']


# class MyCartAdmin(admin.ModelAdmin):
#     list_display = ['user', 'product_id', 'number']
#     list_filter = ('user', 'number', 'product_id',)


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['order_id', 'saler', 'user', 'products', 'size', 'status']
#     list_filter = ('status',)
#     search_fields = ['order_id', 'products', 'size', 'status']


# class ProductSizeAdmin(admin.ModelAdmin):
#     list_display = ['product', 'size', 'quantity']


class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'product_name', 'product_id2', 'category', 'subcategory','TotalCal']
    list_filter = ('category', 'subcategory')
    search_fields = ['product_name', 'product_id2','category']


# class SellerDAdmin(admin.ModelAdmin):
#     list_display = ['image_tag', 'user','mobile','gst_Number','shop_Name','account_Holder_Name','account_Number','ifsc_Code']

# class SelerSliderAdmin(admin.ModelAdmin):
#     list_display = ['image_tag', 'name', 'url']
#     list_filter = ('name',)
#     search_fields = ['name']

class TrendsAdmin(admin.ModelAdmin):
    list_display = ['product', 'number']

# class WholeSaleProductOrdersAdmin(admin.ModelAdmin):
#     list_display = ['order_id', 'user', 'products', 'status']
#     list_filter = ('status',)
#     search_fields = ['order_id', 'products', 'status']
#
# class WholeSaleProductAdmin(admin.ModelAdmin):
#     list_display = ['image_tag', 'product_name','product_id', 'category', 'subcategory', 'price','pub_date','size','color']
#     list_filter = ('category', 'subcategory')
#     search_fields = ['product_name','product_id']
#
# class ColorAdmin(admin.ModelAdmin):
# 	list_display=('title','color_bg')
#
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ['user', 'product','review', 'time']


admin.site.register(UserDetail, UserAdmin)
# admin.site.register(Color,ColorAdmin)
# admin.site.register(ProductReview,ReviewAdmin)
admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductSize, ProductSizeAdmin)
# admin.site.register(SalerDetail,SellerDAdmin)
admin.site.register(Slider, SliderAdmin)
# admin.site.register(category, CategoryAdmin)
#admin.site.register(dow)
admin.site.register(Contact, ContactAdmin)
# admin.site.register(SellerSlider,SelerSliderAdmin)
# admin.site.register(MyCart, MyCartAdmin)
# admin.site.register(WholeSaleProduct,WholeSaleProductAdmin)
# admin.site.register(WholeSaleProductOrders,WholeSaleProductOrdersAdmin)
# admin.site.register(Cart, CartAdmin)
#admin.site.register(Orders, OrderAdmin)
admin.site.register(trend,TrendsAdmin)
