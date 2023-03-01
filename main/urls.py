from django.urls import path
from . import views
from django.contrib import admin

admin.autodiscover()
admin.site.enable_nav_sidebar = False
urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name="signup"),
    path('account_settings/', views.account_settings, name="account_settings"),
    path("product/<int:prod_id>", views.productView, name="ProductView"),
    path('contact/', views.contact, name="contact"),
    path("products/<str:catg>", views.view_all, name="products_view_all"),
    path('plus_element_cart/', views.plus_element_cart),
    path('minus_element_cart/', views.minus_element_cart),
    path('add_to_cart/', views.add_to_cart),
    path('delete_from_cart/', views.delete_from_cart),
    path('dummy_cart/', views.dummy_cart),
    path('cart/', views.cart, name="main_cart"),
    path('checkout/', views.checkout, name="main_checkout"),
    path('order_now/', views.order_now, name="order_now"),
    path('myorders/', views.MyOrders, name="myorders"),
    path('search/', views.search, name="search"),
    path('MenuFilter/<str:querys>', views.MenuFilter, name="MenuFilter"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path("Team/", views.Team, name="Team"),
    path("Recommand/", views.Recommand, name="Recommand"),
    path("Recommand-result/", views.dropdown_recommand_result, name="dropdown_recommand_result"),
    path("random_recomandation/", views.random_recomandation, name="random_recomandation"),
    path("history_recomandation/", views.History_recommand_result, name="History_recommand_result"),
    path("save_history_recomandation/", views.save_history_recomandation, name="save_history_recomandation"),
    ]